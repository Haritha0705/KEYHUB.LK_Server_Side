from __future__ import annotations

import uuid
from datetime import datetime, timezone
from typing import Optional

from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import JSONB
from sqlmodel import SQLModel, Field


class AuditLog(SQLModel, table=True):
    __tablename__ = "audit_log"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

    entity: str = Field(max_length=100, index=True)          # e.g. "Vehicle"
    entity_id: uuid.UUID = Field(index=True)
    operation_type: str = Field(max_length=20)               # ADD / UPDATE / DELETE

    before: dict = Field(default_factory=dict, sa_column=Column(JSONB))   # {} for ADD
    after: dict = Field(default_factory=dict, sa_column=Column(JSONB))

    user_id: uuid.UUID = Field(index=True)
    detail_header: Optional[str] = Field(default=None, max_length=255)

    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
