from enum import Enum


class TimeRange(str, Enum):
    week = "week"
    month = "month"
    year = "year"