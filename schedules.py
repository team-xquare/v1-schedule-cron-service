from sqlalchemy import Column, VARCHAR, DATE, BINARY, Integer
from util import Base


class Schedules(Base):
    __tablename__ = 'schedule'

    id = Column(BINARY(16), primary_key=True)
    data = Column(DATE, nullable=False)
    name = Column(VARCHAR(255), nullable=False)
