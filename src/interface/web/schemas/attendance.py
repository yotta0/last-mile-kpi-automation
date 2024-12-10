from pydantic import BaseModel, field_validator
from datetime import datetime
from typing import Optional


class AttendanceSchema(BaseModel):
    id: int
    client_id: int
    green_angel_id: int
    hub_id: int
    limit_date: datetime
    attendance_date: Optional[datetime] = None
    is_active: bool

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True
        from_attributes = True

class AttendancesPaginatedSchema(BaseModel):
    total_pages: int
    page: int
    per_page: int
    attendances: list[AttendanceSchema]

    class Config:
        arbitrary_types_allowed = True
        from_attributes = True

class AttendanceCreateSchema(BaseModel):
    client_id: int
    green_angel_id: int
    hub_id: int
    limit_date: datetime
    attendance_date: Optional[datetime] = None
    is_active: Optional[bool] = None

    @staticmethod
    def parse_datetime(value):
        if isinstance(value, str):
            return datetime.strptime(value, '%d-%m-%Y %H:%M:%S')
        return value

    @field_validator('limit_date', 'attendance_date', mode='before')
    def validate_dates(cls, value):
        return cls.parse_datetime(value)

    class Config:
        arbitrary_types_allowed = True
        from_attributes = True


class AttendanceUpdateSchema(BaseModel):
    green_angel_id: Optional[int] = None
    hub_id: Optional[int] = None
    limit_date: Optional[datetime] = None
    attendance_date: Optional[datetime] = None

    @staticmethod
    def parse_datetime(value):
        if isinstance(value, str):
            return datetime.strptime(value, '%d-%m-%Y %H:%M:%S')
        return value

    @field_validator('limit_date', 'attendance_date', mode='before')
    def validate_dates(cls, value):
        return cls.parse_datetime(value)

    class Config:
        arbitrary_types_allowed = True
        from_attributes = True