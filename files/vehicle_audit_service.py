import logging
import uuid
from datetime import datetime, timezone

from sqlmodel import Session

# Adapt this import to your real audit table. A minimal reference model is
# shown at the bottom of this file in a comment so you can drop it into
# src/app/models/audit/audit_log.py and wire it up.
from src.app.models.audit.audit_log import AuditLog

logger = logging.getLogger(__name__)

# operation types (mirrors the company's ADD/UPDATE/DELETE constants)
ADD = "ADD"
UPDATE = "UPDATE"
DELETE = "DELETE"


class VehicleAuditService:
    """Writes an audit/history record describing who changed what.

    This is the equivalent of the company's PayrollHistoryService.add_history_record.
    It does NOT commit - it only stages the row in the same session, so the
    calling service can commit the vehicle + the audit row atomically.
    """

    def __init__(self, session: Session):
        self.session = session

    def record_create(self, vehicle, user_id: uuid.UUID) -> None:
        before: dict = {}
        after = {
            "title": vehicle.title,
            "make": vehicle.make,
            "model": vehicle.model,
            "status": str(vehicle.status),
            "condition": str(vehicle.condition),
        }
        self._add_record(
            entity_id=vehicle.id,
            operation_type=ADD,
            before=before,
            after=after,
            user_id=user_id,
            detail_header="Added new vehicle listing",
        )

    def _add_record(self, entity_id, operation_type, before, after, user_id, detail_header):
        record = AuditLog(
            entity="Vehicle",
            entity_id=entity_id,
            operation_type=operation_type,
            before=before,
            after=after,
            user_id=user_id,
            detail_header=detail_header,
            created_at=datetime.now(timezone.utc),
        )
        self.session.add(record)
        logger.info(
            "Audit staged: %s Vehicle id=%s by user=%s", operation_type, entity_id, user_id
        )


# ---------------------------------------------------------------------------
# Reference audit model (put in src/app/models/audit/audit_log.py):

# import uuid
# from datetime import datetime
# from sqlalchemy.dialects.postgresql import UUID, JSONB
# from sqlalchemy import Column, String, DateTime
# from db_connector import Base   # or your SQLModel base
#
# class AuditLog(Base):
#     __tablename__ = "audit_log"
#     id            = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
#     entity        = Column(String(100))           # "Vehicle"
#     entity_id     = Column(UUID(as_uuid=True))
#     operation_type= Column(String(20))            # ADD / UPDATE / DELETE
#     before        = Column(JSONB)                 # {} for ADD
#     after         = Column(JSONB)
#     user_id       = Column(UUID(as_uuid=True))
#     detail_header = Column(String(255))
#     created_at    = Column(DateTime)
# ---------------------------------------------------------------------------
