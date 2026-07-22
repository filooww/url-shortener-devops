from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from app.cache import cache_get, cache_set
from app.config import settings
from app.database import Base, engine, get_db
from app.models import Link
from app.schemas import ShortenRequest, ShortenResponse
from app.shortener import generate_code

Base.metadata.create_all(bind=engine)

app = FastAPI(title="URL Shortener")


@app.get("/healthz")
def healthz():
    return {"status": "ok"}


@app.post("/shorten", response_model=ShortenResponse, status_code=201)
def shorten(payload: ShortenRequest, db: Session = Depends(get_db)):
    code = generate_code()
    while db.query(Link).filter(Link.code == code).first() is not None:
        code = generate_code()

    link = Link(code=code, target_url=str(payload.url))
    db.add(link)
    db.commit()

    return ShortenResponse(
        code=code,
        short_url=f"{settings.base_url}/{code}",
        target_url=str(payload.url),
    )


@app.get("/{code}")
def resolve(code: str, db: Session = Depends(get_db)):
    # сначала кэш — если попали, в БД не ходим вообще
    cached = cache_get(code)
    if cached is not None:
        return RedirectResponse(url=cached, status_code=307)

    link = db.query(Link).filter(Link.code == code).first()
    if link is None:
        raise HTTPException(status_code=404, detail="Not found")

    link.clicks += 1
    db.commit()
    cache_set(code, link.target_url)
    return RedirectResponse(url=link.target_url, status_code=307)
