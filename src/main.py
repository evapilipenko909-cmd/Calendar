import calendar
import datetime

import flet as ft

def main(page: ft.Page):
    grid:ft.GridView = ft.GridView(
        expand=True,
        runs_count=7, # 
        scroll=ft.ScrollMode.ALWAYS,
        child_aspect_ratio=1.0,
        spacing=5

    )

    weekdays_row:ft.Row = ft.Row(
        alignment=ft.MainAxisAlignment.SPACE_AROUND
    )

    page.add(
        ft.Container(
            ft.Column(
                controls=[weekdays_row, grid],
                spacing=10,
                alignment = ft.MainAxisAlignment.CENTER,

                scroll=ft.ScrollMode.AUTO

            ),
            width=300,
            height=400,
        )

    )

if __name__ == "__main__":
    ft.run(main)