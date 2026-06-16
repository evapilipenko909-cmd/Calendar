
from dataclasses import dataclass
import datetime
from functools import total_ordering
from abc import ABC, abstractmethod


class AbstractDay(ABC):
    @abstractmethod
    def get_date(self)->datetime.date:...

    @abstractmethod
    def get_description(self)->str:...
    
    @abstractmethod
    def set_emotion(self, emotion:Emotion)->None:...
@dataclass(frozen=True)
class Emotion:
    img:str|None
    emoji:str




@total_ordering 
class DayStruct(AbstractDay):
    def __init__(self) -> None:
        self.date:datetime.date|None = None
        self.emotion:Emotion|None = None
        self.description:str = ""

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, DayStruct):
            return NotImplemented
        if self.date is None or other.date is None:
            return self.date is other.date
        return self.date == other.date
    
    def __lt__(self, other):
        if not isinstance(other, DayStruct):
            return NotImplemented
        if self.date is None or other.date is None:
            return False
        return self.date < other.date