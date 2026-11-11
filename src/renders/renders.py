"""Модуль для отрисовки игровых объектов на экране."""

import pygame
from src.models.animation_model import Bird


class Renderer:
    """Класс, отвечающий за визуализацию модели данных."""

    def __init__(self, screen: pygame.Surface):
        """Инициализация рендерера с привязкой к окну."""
        self.screen = screen
        self.bg_color = (135, 206, 235)  # Небесно-голубой
        self.bird_color = (255, 255, 0)  # Желтый
        self.pipe_color = (34, 139, 34)  # Зеленый
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

    def draw_bg(self):
        """Очищает экран фоновым цветом."""
        self.screen.fill(self.bg_color)

    def draw_bird(self, bird: Bird):
        """Отрисовывает птицу."""
        pygame.draw.circle(
            self.screen, self.bird_color, (int(bird.x), int(bird.y)), bird.radius
        )
        # Хитбокс (опционально, для дебага можно раскомментировать)
        # pygame.draw.rect(self.screen, (255,0,0), bird.get_rect(), 1)

    def draw_pipes(self, pipes: list):
        """Отрисовывает список труб."""
        for pipe in pipes:
            top_rect, bottom_rect = pipe.get_rects()
            pygame.draw.rect(self.screen, self.pipe_color, top_rect)
            pygame.draw.rect(self.screen, self.pipe_color, bottom_rect)

    def draw_score(self, score: int):
        """Отображает текущий счет."""
        score_surface = self.font.render(f"Score: {score}", True, self.text_color)
        self.screen.blit(score_surface, (10, 10))

    def draw_game_over(self):
        """Отрисовывает экран проигрыша."""
        text = self.font.render("Game Over! Press R to Restart", True, (255, 0, 0))
        text_rect = text.get_rect(
            center=(self.screen.get_width() // 2, self.screen.get_height() // 2)
        )
        self.screen.blit(text, text_rect)
