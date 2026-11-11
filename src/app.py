"""Главный модуль, содержащий контроллер приложения."""

import pygame
import sys
from src.models.animation_model import Bird, Pipe
from src.renderers.renderer import Renderer


class App:
    """Класс главного приложения (окно, цикл, события)."""

    def __init__(self):
        """Инициализирует Pygame и начальное состояние игры."""
        pygame.init()
        self.width = 400
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Flappy Bird OOP")

        self.clock = pygame.time.Clock()
        self.renderer = Renderer(self.screen)

        self.reset_game()

    def reset_game(self):
        """Сбрасывает состояние игры к начальному."""
        self.bird = Bird(100, self.height // 2)
        self.pipes = [Pipe(self.width + 100, self.height)]
        self.score = 0
        self.is_game_over = False

    def handle_events(self):
        """Обрабатывает пользовательский ввод."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not self.is_game_over:
                    self.bird.jump()
                if event.key == pygame.K_r and self.is_game_over:
                    self.reset_game()

    def update_logic(self):
        """Обновляет логику игры и проверяет коллизии."""
        if self.is_game_over:
            return

        self.bird.update()

        # Генерация новых труб
        if self.pipes[-1].x < self.width - 200:
            self.pipes.append(Pipe(self.width, self.height))

        bird_rect = self.bird.get_rect()

        for pipe in self.pipes:
            pipe.update()

            # Подсчет очков
            if pipe.x + pipe.width < self.bird.x and not pipe.passed:
                self.score += 1
                pipe.passed = True

            # Проверка коллизий с трубами
            top_rect, bottom_rect = pipe.get_rects()
            if bird_rect.colliderect(top_rect) or bird_rect.colliderect(bottom_rect):
                self.is_game_over = True

        # Удаление труб, ушедших за экран
        if self.pipes[0].x + self.pipes[0].width < 0:
            self.pipes.pop(0)

        # Проверка падения или вылета за верхний край
        if self.bird.y > self.height or self.bird.y < 0:
            self.is_game_over = True

    def run(self):
        """Запускает главный игровой цикл (60 FPS)."""
        while True:
            self.handle_events()
            self.update_logic()

            self.renderer.draw_bg()
            self.renderer.draw_pipes(self.pipes)
            self.renderer.draw_bird(self.bird)
            self.renderer.draw_score(self.score)

            if self.is_game_over:
                self.renderer.draw_game_over()

            pygame.display.flip()
            self.clock.tick(60)
