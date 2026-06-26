import uuid

from sqlalchemy import String, UUID
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column

from src.app.models.common import BaseModel


class AuditLog(BaseModel):
    """Append-only audit trail of write operations on domain entities."""

    __tablename__ = "audit_log"

    entity: Mapped[str] = mapped_column(String(100), index=True)          # e.g. "Vehicle"
    entity_id: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True), index=True)
    operation_type: Mapped[str] = mapped_column(String(20))               # ADD / UPDATE / DELETE
    before: Mapped[dict | None] = mapped_column(JSONB)                     # {} for ADD
    after: Mapped[dict | None] = mapped_column(JSONB)                      # {} for DELETE
    user_id: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True), index=True)
    detail_header: Mapped[str | None] = mapped_column(String(255))
