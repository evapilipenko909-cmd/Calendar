from dataclasses import dataclass
import datetime
from functools import total_ordering
from abc import ABC, abstractmethod


@dataclass(frozen=True)
class Emotion:
    img: str | None
    emoji: str


class AbstractDay(ABC):
    @abstractmethod
    def get_date(self) -> datetime.date:
        ...

    @abstractmethod
    def get_description(self) -> str:
        ...

    @abstractmethod
    def set_emotion(self, emotion: Emotion) -> None:
        ...


@total_ordering
class DayStruct(AbstractDay):
    def __init__(self, date: datetime.date | None = None) -> None:
        self.date: datetime.date | None = date
        self.emotion: Emotion | None = None
        self.description: str = ""

    def get_date(self) -> datetime.date:
        return self.date

    def get_description(self) -> str:
        return self.description

    def set_emotion(self, emotion: Emotion) -> None:
        self.emotion = emotion

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, DayStruct):
            return NotImplemented
        return self.date == other.date

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, DayStruct):
            return NotImplemented
        return self.date < other.date