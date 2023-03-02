import uuid

from sqlalchemy import Column, VARCHAR, DATE, BINARY, Integer
from util import Base


class Schedules(Base):
    __tablename__ = 'tbl_school_schedule'

    id = Column(BINARY(16), primary_key=True)
    date = Column(DATE, nullable=False)
    name = Column(VARCHAR(255), nullable=False)
