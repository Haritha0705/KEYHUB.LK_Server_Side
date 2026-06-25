from app.schemas.base import Base

class AuditLog(Base):

    __tablename__ = "audit_log"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    entity = Column(String(100))  # "Vehicle"
    entity_id = Column(UUID(as_uuid=True))
    operation_type = Column(String(20))  # ADD / UPDATE / DELETE
    before = Column(JSONB)  # {} for ADD
    after = Column(JSONB)
    user_id = Column(UUID(as_uuid=True))
    detail_header = Column(String(255))
    created_at = Column(DateTime)
