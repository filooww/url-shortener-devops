# URL Shortener — DevOps Portfolio Project

Production-style сервис коротких ссылок (bit.ly-подобный), развёрнутый полным DevOps-циклом: IaC, config management, контейнеризация, оркестрация, CI/CD и observability.

> Статус: 🚧 в разработке

---

## Architecture

<!-- TODO: вставить диаграмму (docs/architecture.png) -->
_TODO: описание компонентов и схема._

Компоненты:
- **API** — FastAPI-сервис (создание/резолв коротких ссылок)
- **PostgreSQL** — хранение ссылок
- **Redis** — кэш горячих ссылок

---

## Tech stack

| Слой              | Технологии                          |
|-------------------|-------------------------------------|
| Приложение        | Python, FastAPI                     |
| Контейнеризация   | Docker, docker-compose              |
| IaC               | Terraform                           |
| Config management | Ansible                             |
| Оркестрация       | Kubernetes, Helm                    |
| CI/CD             | GitHub Actions                      |
| Observability     | Prometheus, Grafana, Loki           |
| Cloud             | AWS (dev — local kind/docker)       |

---

## Getting started (local)

_TODO: инструкция запуска через docker-compose._

```bash
# TODO
