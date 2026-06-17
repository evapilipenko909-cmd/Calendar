from dataclasses import dataclass, field
import datetime
from typing import Any
import flet as ft
from src.models.model import DayStruct, Emotion


@dataclass()
class DayItemStyledContainer(ft.Container):
    """
    Day element of Calendar Grid
    [Styled control][https://flet.dev/docs/cookbook/custom-controls]
    """
    alignment: ft.Alignment = field(default_factory=lambda: ft.Alignment.CENTER)
    border: ft.Border = field(default_factory=lambda: ft.Border.all(1, ft.Colors.BLUE_100))
    border_radius: int = field(default=10)

    __date: datetime.date | str | None = field(init=False, default=None)
    __emotion: str = field(init=False, default="")

    def __init__(self):
        super().__init__()
        self.alignment = ft.Alignment.CENTER
        self.border = ft.Border.all(1, ft.Colors.BLUE_100)
        self.border_radius = 10
        self.content = ft.Text(value="", text_align=ft.TextAlign.CENTER, size=15)


class DayContainer(ft.Container):
    """Simple class of element in Calendar Grid"""
    def __init__(self, date: datetime.date | str | None = None, emoji: str = "", on_click=None) -> None:
        # форматируем дату, только число дня
        if isinstance(date, datetime.date):
            text_value = str(date.day)
        else:
            text_value = ""

        # создаём ListTile с числом и эмодзи
        list_tile = ft.ListTile(
            title=ft.Text(value=text_value, text_align=ft.TextAlign.CENTER, size=15),
            subtitle=ft.Text(value=emoji, text_align=ft.TextAlign.CENTER, size=20) if emoji else None,
            title_alignment=ft.ListTileTitleAlignment.CENTER,
            content_padding=ft.Padding(0, 0, 0, 0),
            dense=True,
        )

        super().__init__()
        self.alignment = ft.Alignment.CENTER
        self.border = ft.Border.all(1, ft.Colors.BLUE_100)
        self.border_radius = 10
        self.content = list_tile
        self.on_click = on_click
        self.ink = True

        self.day: DayStruct = DayStruct()

        if emoji:
            self.day.set_emotion(Emotion(img=None, emoji=emoji))

    def set_content(self, content: Any) -> None:
        self.content = content