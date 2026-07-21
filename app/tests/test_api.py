from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_healthz():
    r = client.get("/healthz")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}


def test_shorten_returns_code():
    r = client.post("/shorten", json={"url": "https://example.com/page"})
    assert r.status_code == 201
    body = r.json()
    assert len(body["code"]) == 6
    assert body["target_url"] == "https://example.com/page"


def test_resolve_redirects():
    code = client.post(
        "/shorten", json={"url": "https://example.com/page"}
    ).json()["code"]
    r = client.get(f"/{code}", follow_redirects=False)
    assert r.status_code == 307
    assert r.headers["location"] == "https://example.com/page"


def test_resolve_missing_returns_404():
    r = client.get("/nonexistent", follow_redirects=False)
    assert r.status_code == 404
