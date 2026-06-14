import flet as ft
from flet_calendar import FletCalendar
from custom_date import CustomDate


def main(page: ft.Page):
    page.title = "Календарь настроения"
    page.theme = ft.Theme(color_scheme_seed=ft.Colors.PINK)
    page.padding = 50

    cal = FletCalendar(page)

    content = ft.Column(
        [
            cal.calendar_container,
            ft.Container(height=30),
            cal.mood_panel,
            ft.Container(height=10),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    page.add(content)
    page.update()


if __name__ == "__main__":
    ft.run(main)