import pypboy
import pygame
import game
import settings


class Module(pypboy.SubModule):

    label = "SKILLS"

    def __init__(self, *args, **kwargs):
        super(Module, self).__init__(*args, **kwargs)

        self.menu = pypboy.ui.Menu(settings.SKILLS)
        self.menu.rect[0] = settings.menu_x
        self.menu.rect[1] = settings.menu_y
        self.add(self.menu)

        self.footer = pypboy.ui.Footer(settings.STATUS_FOOTER)
        self.footer.rect[0] = settings.footer_x
        self.footer.rect[1] = settings.footer_y
        self.add(self.footer)