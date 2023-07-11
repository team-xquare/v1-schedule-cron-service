from sqlalchemy import Column, VARCHAR, DATE, CHAR
from src.model import Base, BaseMixin


class Schedules(Base, BaseMixin):
    __tablename__ = 'tbl_school_schedule'
    id = Column(CHAR(36), primary_key=True)
    date = Column(DATE, nullable=False)
    name = Column(VARCHAR(255), nullable=False)

    class Config:
        orm_mode = True