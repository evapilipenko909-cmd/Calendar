import calendar
import datetime
import random

import flet as ft
from src.ui.components import DayContainer
from src.utils.settings import Settings


def main(page: ft.Page):
    page.title = "Календарь"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # текст для отобр. выбранной даты
    selected_date_text = ft.Text("Выберите дату", size=16)

    current_year = 2026
    current_month = 6

    month_title = ft.Text(
        value=datetime.date(current_year, current_month, 1).strftime("%B %Y"),
        size=24,
        weight=ft.FontWeight.BOLD
    )

    # сетка календаря
    grid = ft.GridView(
        expand=True,
        runs_count=7,
        child_aspect_ratio=1.0,
        spacing=5
    )

    # заголовки дней недели
    weekdays_row = ft.Row(
        alignment=ft.MainAxisAlignment.SPACE_AROUND
    )

    for day in ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]:
        weekdays_row.controls.append(
            ft.Text(day, width=40, text_align=ft.TextAlign.CENTER, weight=ft.FontWeight.BOLD)
        )

    def on_day_click(e):
        # content теперь ListTile, а Text внутри title
        date_str = e.control.content.title.value
        if date_str:
            selected_date_text.value = f"Выбрано: {date_str}"
            page.update()

    def build_calendar():
        nonlocal current_year, current_month
        month_title.value = datetime.date(current_year, current_month, 1).strftime("%B %Y")
        grid.controls.clear()

        # получ. матрицу дней месяца
        days_matrix = calendar.monthcalendar(current_year, current_month)

        # доб. дни в сетку
        for week in days_matrix:
            for day in week:
                date = datetime.date(current_year, current_month, day) if day != 0 else None
                emoji = random.choice(Settings.emoji) if date else ""
                grid.controls.append(DayContainer(date=date, emoji=emoji, on_click=on_day_click))

    def on_prev_month(e): #стрелка назад
        nonlocal current_year, current_month
        if current_year == 2026 and current_month == 5: #не выходим за май
            return
        current_month -= 1
        if current_month < 1:
            current_month = 12
            current_year -= 1
        build_calendar()
        page.update()

    def on_next_month(e):
        nonlocal current_year, current_month
        if current_year == 2026 and current_month == 7:
            return
        current_month += 1
        if current_month > 12:
            current_month = 1
            current_year += 1
        build_calendar()
        page.update()

    btn_prev = ft.IconButton(icon=ft.Icons.CHEVRON_LEFT, icon_size=30, on_click=on_prev_month)
    btn_next = ft.IconButton(icon=ft.Icons.CHEVRON_RIGHT, icon_size=30, on_click=on_next_month)
    #кнопки навигации
    nav_row = ft.Row(
        controls=[btn_prev, month_title, btn_next],
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )

    # доб. всё на страницу через Column в Container
    page.add(
        ft.Container(
            content=ft.Column(
                controls=[
                    selected_date_text,
                    nav_row,
                    weekdays_row,
                    grid
                ],
                spacing=10,
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            width=600,
            height=700,
            padding=10
        )
    )

    build_calendar()


if __name__ == "__main__":
    ft.run(main)