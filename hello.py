from time import sleep

import flet
from flet import Page, Text


def main(page: Page):

    page.add(Text("Hello! world i am mohamed"))

    sleep(1)
    page.window_visible = True
    page.update()


flet.app(target=main, view=flet.FLET_APP_HIDDEN)
