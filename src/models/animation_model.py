"""Модуль, содержащий математическую модель игры Flappy Bird."""

import random
import pygame


class Bird:
    """Класс, описывающий птицу и её физику."""

    def __init__(self, x: int, y: int):
        """Инициализация птицы на заданных координатах."""
        self.x = x
        self.y = y
        self.velocity = 0.0
        self.gravity = 0.5
        self.jump_strength = -8.0
        self.radius = 15

    def jump(self):
        """Применяет импульс для прыжка птицы вверх."""
        self.velocity = self.jump_strength

    def update(self):
        """Обновляет позицию птицы, применяя гравитацию (математический блок)."""
        # Скорость увеличивается на значение гравитации с каждым кадром
        self.velocity += self.gravity
        self.y += self.velocity

    def get_rect(self) -> pygame.Rect:
        """Возвращает хитбокс птицы для просчета коллизий."""
        return pygame.Rect(
            self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2
        )


class Pipe:
    """Класс препятствия (трубы)."""

    def __init__(self, x: int, screen_height: int):
        """Инициализация трубы со случайным зазором."""
        self.x = x
        self.width = 60
        self.gap = 150
        self.speed = 3
        # Вычисляем случайное положение зазора
        self.top_height = random.randint(50, screen_height - self.gap - 50)
        self.bottom_y = self.top_height + self.gap
        self.screen_height = screen_height
        self.passed = False

    def update(self):
        """Смещает трубу влево."""
        self.x -= self.speed

    def get_rects(self):
        """Возвращает хитбоксы верхней и нижней частей трубы."""
        top_rect = pygame.Rect(self.x, 0, self.width, self.top_height)
        bottom_rect = pygame.Rect(
            self.x, self.bottom_y, self.width, self.screen_height - self.bottom_y
        )
        return top_rect, bottom_rect
