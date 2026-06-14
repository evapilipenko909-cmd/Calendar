import flet as ft
import calendar
from color import ThemeColors
from custom_date import CustomDate


class FletCalendar:
    MOODS_CONFIG = [
        ("👍", "like", ThemeColors.LIKE_COLOR),
        ("😐", "neutral", ThemeColors.NEUTRAL_COLOR),
        ("👎", "dislike", ThemeColors.DISLIKE_COLOR),
    ]

    def __init__(self, page: ft.Page):
        self.page = page
        self.moods = {}

        today = CustomDate()
        self.current_year = today.year
        self.current_month = today.month
        self.current_day = today.day

        self.border_color = ThemeColors.BORDER_COLOR
        self.text_color = ThemeColors.TEXT_COLOR
        self.current_day_color = ThemeColors.CURRENT_DAY_COLOR

        self.selected_date_str = None
        self.selected_date_display = None

        # инициализация контейнеров
        self.calendar_container = ft.Container(
            width=400, height=320, padding=5,
            border=ft.Border.all(2, self.border_color), border_radius=10
        )

        self.mood_panel = ft.Container(
            content=ft.Text("👆 Кликни на день", color=self.text_color),
            padding=20,
            visible=True
        )

        self.build()

    def navigate(self, months: int):
        # сдвигает календарь на опр колво месяцев
        next_date = CustomDate(self.current_year, self.current_month, 1).add_months(months)
        self.current_year, self.current_month = next_date.year, next_date.month
        self.build()
        self.page.update()

    def on_day_click(self, e: ft.Event): # e as Event in new Flet 
        # обрабатывает клик по дню в календаре
        month, day, year = e.control.data
        self.selected_date_str = f"{year}-{month:02d}-{day:02d}"
        self.selected_date_display = f"{day:02d}.{month:02d}.{year}"
        self.show_mood_selection()

    def make_button(self, emoji: str, mood_type: str, color: str, is_selected: bool) -> ft.Container:
        # создает кнопку настроения с усл оформ
        border_color = color if is_selected else self.border_color

        return ft.Container(
            content=ft.Text(emoji, size=40),
            width=80, height=80,
            bgcolor=color if is_selected else ft.Colors.TRANSPARENT,
            border=ft.Border.all(3, border_color),
            border_radius=15,
            alignment=ft.Alignment.CENTER,
            ink=True,
            on_click=lambda _, m=mood_type: self.on_mood_click(m)
        )

    def show_mood_selection(self): 
        
        # отобр панель выбора настроения для даты
        current_mood = self.moods.get(self.selected_date_str) # < - fix it1!

        # ген. кнопок
        mood_buttons: list[ft.Control] = [
            self.make_button(emoji, mood_type, color, current_mood == mood_type)
            for emoji, mood_type, color in self.MOODS_CONFIG
        ] # refactor listgenerator!

        # прямое об. сод. панели
        self.mood_panel.content = ft.Column(
            controls=[
                ft.Text(f"📅 {self.selected_date_display}", size=18, color=self.text_color),
                ft.Row(controls=mood_buttons, spacing=20, alignment=ft.MainAxisAlignment.CENTER),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

        self.mood_panel.visible = True
        self.page.update()

    def on_mood_click(self, mood_type: str):
        # Если настроение уже выбрано, удаляем его (повторный клик снимает выбор)
        if self.moods.get(self.selected_date_str) == mood_type:
            del self.moods[self.selected_date_str]
        else:
            self.moods[self.selected_date_str] = mood_type

        # Обновляем, затем рисуем экран
        self.show_mood_selection()
        self.build()
        # self.page.update() вызывается внутри show_mood_selection, но здесь нужен еще один, так как build() изменил calendar_container
        self.page.update()

    def build(self):
       #визуализация календ
        current_calendar = calendar.monthcalendar(self.current_year, self.current_month)
        current_date = CustomDate(self.current_year, self.current_month, 1)
        month_name = current_date.get_month_name("en")

        header = ft.Row([
            ft.Container(ft.Text("<", size=24), on_click=lambda _: self.navigate(-1), padding=5, ink=True),
            ft.Text(f"{month_name} {self.current_year}", size=20, color=self.text_color, expand=True),
            ft.Container(ft.Text(">", size=24), on_click=lambda _: self.navigate(1), padding=5, ink=True),
        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

        col = ft.Column([header, ft.Divider()], spacing=2, width=355)

        for week in current_calendar:
            row = ft.Row(spacing=2, alignment=ft.MainAxisAlignment.CENTER)
            for day in week:
                if day > 0:
                    date_str = f"{self.current_year}-{self.current_month:02d}-{day:02d}"
                    mood = self.moods.get(date_str)
                    is_today = (day == self.current_day)

                    display_map = {"like": "👍", "neutral": "😐", "dislike": "👎"}
                    display = display_map.get(mood, f"{day:02d}") # Fit

                    btn = ft.Container(
                        content=ft.Text(display, size=16 if mood else 14, color=self.text_color),
                        on_click=self.on_day_click,
                        data=(self.current_month, day, self.current_year),
                        width=45, height=45, ink=True,
                        alignment=ft.Alignment.CENTER,
                        border_radius=10,
                        bgcolor=self.current_day_color if is_today and not mood else ft.Colors.TRANSPARENT,
                    )
                else:
                    btn = ft.Container(width=45, height=45)

                row.controls.append(btn)
            col.controls.append(row)

        self.calendar_container.content = col
        return ft.Column([self.calendar_container, self.mood_panel])