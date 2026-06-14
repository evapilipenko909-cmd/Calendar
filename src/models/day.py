from dataclasses import dataclass, field
import datetime
from typing import Any
from warnings import deprecated

import flet as ft

@dataclass(eq=True, order=True)
class DayItemStyledContainer(ft.Container):
    """
    Day element of Calendar Grid
    [Styled control][https://flet.dev/docs/cookbook/custom-controls]
    """
    alignment:ft.Alignment =ft.Alignment.CENTER
    border: ft.Border = ft.Border.all(1, ft.Colors.BLUE_100)
    border_radius:int = 10

    __date:datetime.date|str|None =  field(init=False)
    __emotion:str = field(init=False)

    content = ft.Text(
        value=f"", text_align=ft.TextAlign.CENTER, size=15
    )

class DayContainer(ft.Container):
    """Simpe class of element in Calendar Grid"""
    def __init__(self, date:datetime.date|str|None = None) -> None:
        super().__init__()
        self.alignment:ft.Alignment =ft.Alignment.CENTER
        self.border: ft.Border = ft.Border.all(1, ft.Colors.BLUE_100)
        self.border_radius:int = 10
        self.content = ft.Text(value=f"", text_align=ft.TextAlign.CENTER, size=15)

        self.__date:datetime.date|str|None = date
        self.__emotion:str = "/"
        self.content:ft.Control|None = ft.Text() #empty text for init, meybe None


    @property
    def date(self)->datetime.date|str|None:
        return self.__date
    
    @deprecated("In next code review setter mb del, data not be reinit for new value in Grid")
    @date.setter
    def date(self, date:datetime.date|str):
        """" Maybe deleted function """
        if not date:
            self.__date = date


    @property
    def emotion(self):
        return self.__emotion
    

    @deprecated("WARNING: Hard Code emoji list!")
    @emotion.setter
    def emotion(self, emotion:str):
        """ emotion used str emoji """
        if emotion in ["❤",    "👍",    "👎",    "🔥",    "🥰",    "👏",    
                       "😁",    "🤔",    "🤯",    "😱",    "🤬",    "😢",    
                       "🎉",    "🤩",    "🤮",    "💩",    "🙏",    "👌",    
                       "🕊",     "🤡",    "🥱",    "🥴",    "😍",    "🐳",    
                       "❤‍🔥",    "🌚",    "🌭",    "💯",    "🤣",    "⚡",    
                       "🍌",    "🏆",    "💔",    "🤨",    "😐",    "🍓",
                       "🍾",    "💋",    "🖕",    "😈",    "😴",    "😭",
                       "🤓",    "👻",    "👨‍💻",    "👀",    "🎃",    "🙈",    
                       "😇",    "😨",    "🤝",    "✍",    "🤗",    "🫡",   
                       "🎄",    "☃",     "💅",    "🤪",    "🗿",    "🆒",    
                       "💘",    "🙉",    "🦄",    "😘",    "💊",    "🙊",    
                       "😎",    "👾",    "🤷‍♂",    "🤷",    "🤷‍♀",    "😡",]:
            self.__emotion = emotion
    
    
    def set_content(self, content:Any)->None:
        self.content = content
    
    

    


