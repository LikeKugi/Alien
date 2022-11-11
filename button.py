import pygame.font


class Button:
    """
    Buttons
    """

    def __init__(self, ai_game, msg: str) -> None:
        """
        Init the button
        :param ai_game: Invasion
        :param msg: str
            text of the button
        """
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # size and properties
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        #  creating rect of the button in the middle of the screen
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        #  message on the button
        self.prep_msg = msg

    def _prep_msg(self, msg: str) -> None:
        """
        convert msg to rect and center the text
        :param msg: str
            text to convert
        :return: None
        """
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self) -> None:
        """
        show the empty button and the message
        :return: None
        """
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
