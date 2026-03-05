from pydantic import BaseModel
from datetime import datetime

class LogSchema(BaseModel):
    timestamp: datetime
    service_name: str
    log_level: str
    message: str
    response_time_ms: float
    status_code: int
    ip_address: str


class AnomalySchema(BaseModel):
    timestamp: datetime
    anomaly_type: str
    severity: str
    service_name: str
    details: str