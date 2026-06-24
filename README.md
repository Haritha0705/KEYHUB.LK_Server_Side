# KEYHUB.LK — Server Side

Backend REST API for **KEYHUB.LK**, a vehicle marketplace platform for Sri Lanka. The service powers vehicle listings — cars, SUVs, motorbikes, three-wheelers, lorries, heavy machinery and more — along with their specifications, pricing, documents, media and ownership history.

Built with **FastAPI**, **SQLModel** and **PostgreSQL**, following a layered architecture (router → service → repository → model) with database migrations managed by **Alembic**.

---

## Tech Stack

| Layer            | Technology                          |
| ---------------- | ----------------------------------- |
| Language         | Python 3.11                         |
| Web framework    | FastAPI                             |
| ORM / models     | SQLModel (SQLAlchemy + Pydantic)    |
| Database         | PostgreSQL 18                       |
| Migrations       | Alembic                             |
| Validation       | Pydantic v2                         |
| Server           | Uvicorn                             |
| Containerization | Docker / Docker Compose             |
| Monitoring       | Sentry                              |

---

## Architecture

The codebase uses a clean, layered design so that each concern lives in one place:

```
HTTP Request
   │
   ▼
routers/      ── API endpoints & request wiring
   │
   ▼
services/     ── business logic
   │
   ▼
repository/   ── database access (CRUD)
   │
   ▼
models/       ── SQLModel database tables
```

Supporting layers:

- **`schemas/`** — Pydantic request/response models (API contracts), separate from DB models.
- **`mapper/`** — translation between schemas and database models.
- **`core/`** — database engine, session dependency and settings.
- **`utils/`** — shared helpers (e.g. pagination).

### Project layout

```
src/app/
├── main.py                 # FastAPI app entrypoint
├── core/
│   ├── db.py               # Engine + session dependency
│   └── settings.py
├── models/                 # Database tables (SQLModel)
│   ├── common.py           # Base model, timestamps, shared enums
│   └── vehicle/            # Vehicle + specs, pricing, docs, media, history
├── schemas/                # API request/response models
├── repository/             # Data-access layer
├── services/               # Business logic
├── mapper/                 # Model ⇄ schema mapping
├── routers/                # API route definitions
└── utils/
alembic/                    # Database migrations
```

### Data model

A `Vehicle` is the central entity and is composed of several related records:

- **`vehicle`** — core listing (type, title, make, model, year, condition, status, location, featured/verified flags).
- **`vehicle_specs`** (1:1) — mileage, engine capacity, fuel type, transmission, body type, seats, etc.
- **`vehicle_pricing`** (1:1) — price, currency (default `LKR`), negotiable / leasing options.
- **`vehicle_documents`** (1:1) — registration and ownership documents.
- **`vehicle_history`** (1:1) — ownership / accident history.
- **`vehicle_media`** (1:N) — images and videos, ordered by position.

Shared enums (in `models/common.py`) include `VehicleType`, `VehicleCondition`, `VehicleStatus`, `FuelType`, `Transmission`, `MediaType` and `UserRole`.

---

## Getting Started

### Prerequisites

- Python 3.11+
- PostgreSQL 18 (or Docker)

### Environment variables

Create a `.env.dev` file in the project root:

```env
POSTGRES_USER=your_user
POSTGRES_PASSWORD=your_password
POSTGRES_DB=keyhub_main_db
DATABASE_URL=postgresql://your_user:your_password@db:5432/keyhub_main_db
```

> The application reads `DATABASE_URL` from the environment and falls back to a local Postgres connection if it is not set.

---

## Running with Docker (recommended)

This brings up the API and a PostgreSQL database, and runs migrations automatically on startup.

```bash
docker compose up --build
```

The API will be available at **http://localhost:8000**.

---

## Running locally

```bash
# 1. Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Apply database migrations
alembic upgrade head

# 4. Start the development server
fastapi dev src/app/main.py --port 8000
```

---

## API

Once running, interactive documentation is available at:

- **Swagger UI** — http://localhost:8000/docs
- **ReDoc** — http://localhost:8000/redoc

### Endpoints

All routes are versioned under `/api/v1`.

| Method | Path                  | Description           |
| ------ | --------------------- | --------------------- |
| GET    | `/`                   | Health check          |
| POST   | `/api/v1/vehicles/`   | Create a new vehicle  |

> The vehicle domain is the foundation of the platform; additional endpoints (listing, filtering, media, pricing, etc.) build on the same layered structure.

---

## Database Migrations

Migrations are managed with Alembic.

```bash
# Create a new migration from model changes
alembic revision --autogenerate -m "describe your change"

# Apply migrations
alembic upgrade head

# Roll back the last migration
alembic downgrade -1
```

---

## License

This project is licensed under the terms described in the [LICENSE](./LICENSE) file.
