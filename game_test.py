from random import randint
import random
import numpy as np
import pygame
import time
import sys
import os


class Border(pygame.sprite.Sprite):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(all_sprites)
        if x1 == x2:  # вертикальная стенка
            self.add(vertical_borders)
            self.image = pygame.Surface([1, y2 - y1])
            self.rect = pygame.Rect(x1, y1, 1, y2 - y1)
        else:  # горизонтальная стенка
            self.add(horizontal_borders)
            self.image = pygame.Surface([x2 - x1, 1])
            self.rect = pygame.Rect(x1, y1, x2 - x1, 1)


class Border_1(pygame.sprite.Sprite):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(all_sprites)
        if x1 == x2:  # вертикальная стенка
            self.add(vertical_borders)
            self.image = pygame.Surface([1, y2 - y1])
            self.rect = pygame.Rect(x1, y1, 1, y2 - y1)
        else:  # горизонтальная стенка
            self.add(horizontal_borders)
            self.image = pygame.Surface([x2 - x1, 1])
            self.rect = pygame.Rect(x1, y1, x2 - x1, 1)


def load_image(name):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname)
    return image


class Ball(pygame.sprite.Sprite):
    image = load_image('snow.png')

    def __init__(self, radius, x, y):
        super().__init__(all_sprites)
        self.radius = radius
        self.image = Ball.image
        self.rect = pygame.Rect(x, y, 2 * radius, 2 * radius)
        self.vx = random.randint(-5, 5)
        self.vy = random.randrange(-5, 5)

    def update(self):
        self.rect = self.rect.move(self.vx, self.vy)

    def update(self):
        self.rect = self.rect.move(self.vx, self.vy)
        if pygame.sprite.spritecollideany(self, horizontal_borders):
            self.vy = -self.vy
        if pygame.sprite.spritecollideany(self, vertical_borders):
            self.vx = -self.vx


class Car(pygame.sprite.Sprite):
    def __init__(self, x, surf, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = surf
        self.rect = self.image.get_rect(
            center=(0, x))
        # добавляем в группу
        self.add(group)
        self.speed = randint(1, 3)

    def update(self):
        if self.rect.x < size[1]:  # как едут
            self.rect.x += self.speed
        else:
            self.kill()


def start_screen(screen):
    intro_text = ["ПЯТНАШКИ", "",
                  "Правила игры :",
                  "ваша задача расположить цифры",
                  "в порядке возрастания,",
                  "чтобы передвинуть цифру на свободное поле",
                  " просто нажмите на нее. ",
                  "Если вы готовы начать",
                  "кликните правой кнопкой мышки",
                  "Да пребудет с тобой удача"
                  ]
    Fps = 50
    clock = pygame.time.Clock()
    fon = screen
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color((255, 109, 23)))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру
        pygame.display.flip()
        clock.tick(Fps)


def terminate():
    pygame.quit()
    sys.exit()


def start_screen2(screen, surfac):
    intro_text = ["  ПОБЕДА!!!",
                  "для перехода ",
                  "на следующий ",
                  "уровень",
                  "кликните мышкой", ]
    Fps = 50
    clock = pygame.time.Clock()
    fon = surfac
    # fon = screen

    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 90)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return True  # начинаем игру
        pygame.display.flip()
        clock.tick(Fps)


def start_screen3(screen, surfac):
    intro_text = ["  ПОБЕДА",
                  "вы прошли всю игру ",
                  "поздравляю!!!:) ",
                  "теперь вы мастер пятнашек", ]
    Fps = 50
    clock = pygame.time.Clock()
    fon = surfac
    # fon = screen

    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 90)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return True  # начинаем игру
        pygame.display.flip()
        clock.tick(Fps)


class Board:
    # создание поля размером width на height
    def __init__(self, width, height, level):
        self.width = width  # ширшна поля
        self.height = height
        self.level = level
        self.board = [[0] * width for _ in range(height)]
        # отступы слева и сверху, размер ячейки
        self.left = 20
        self.top = 20
        self.cell_size = 30
        self.current_cell = ()
        self._start_field()
        self.flag_finish = False

    def _start_field(self):
        self.num_dict = {}

        candidate_cell_coords = (np.random.randint(self.width), np.random.randint(self.height))
        num_list = [i for i in range(1, self.width ** 2)]
        num_list.append(0)
        for y in range(self.height):
            for x in range(self.width):
                self.num_dict[(x, y)] = num_list[self.width * y + x]
                if self.num_dict[(x, y)] == 0:
                    self.empty_cell = (x, y)
                    i = 0
        while i < self.level:
            for x in range(self.height):
                for y in range(self.width):
                    if (candidate_cell_coords[0] + 1, candidate_cell_coords[1]) == self.empty_cell or \
                            (candidate_cell_coords[0] - 1, candidate_cell_coords[1]) == self.empty_cell or \
                            (candidate_cell_coords[0], candidate_cell_coords[1] + 1) == self.empty_cell or \
                            (candidate_cell_coords[0], candidate_cell_coords[1] - 1) == self.empty_cell:
                        b = self.num_dict[candidate_cell_coords]
                        self.num_dict[candidate_cell_coords] = 0
                        self.num_dict[self.empty_cell] = b
                        self.empty_cell = candidate_cell_coords
                        i += 1
                        candidate_cell_coords = (np.random.randint(self.width), np.random.randint(self.height))

                    else:
                        pass  # print('not neighbouring cell, new attempt;', candidate_cell_coords)
            candidate_cell_coords = (np.random.randint(self.width), np.random.randint(self.height))

    def draw_num(self):
        # print('draw_num')
        for y in range(self.height):
            for x in range(self.width):
                if self.num_dict[(x, y)] == 0:
                    continue
                font = pygame.font.Font(None, 30)
                text = font.render(str(self.num_dict[(x, y)]), False, (100, 255, 100))
                screen.blit(text, (x * self.cell_size + self.left + int(self.cell_size / 2),
                                   y * self.cell_size + self.top + int(self.cell_size / 2)))

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                pygame.draw.rect(screen, pygame.Color(255, 255, 255), (
                    x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size,
                    self.cell_size), 1)
        self.draw_num()
        if self.is_win():
            print('win')
            self.flag_finish = True

    def is_win(self):
        if self.num_dict[(0, 0)] != 1 or self.num_dict[(self.width - 1, self.height - 1)] != 0:
            return False
        else:
            i = 0
            for x in range(self.height):

                for y in range(self.width):
                    # print('x', x, 'y', y)
                    if (x == 0 and y == 0) or (x == self.width - 1 and y == self.height - 1):
                        continue

                    else:

                        if self.num_dict[(x, y)] != self.width * y + x + 1:
                            i += 1


            if self.num_dict[(self.width - 1, self.height - 1)] == 0 and i == 0:
                print('you win')
                return True

    def get_click(self, mouse_pos, screen):
        self.current_cell = self.get_cell(mouse_pos)
        self.on_click(self.current_cell, screen)

    def get_cell(self, mouse_pos):
        mouse_x, mouse_y = mouse_pos
        cell_coords = (mouse_x - self.left) // self.cell_size, \
                      (mouse_y - self.top) // self.cell_size

        return cell_coords

    def on_click(self, cell_coords, screen):
        if cell_coords[0] < 0 or cell_coords[0] > 3 or cell_coords[1] < 0 or cell_coords[1] > 3:
            return
        if (cell_coords[0] + 1, cell_coords[1]) == self.empty_cell or \
                (cell_coords[0] - 1, cell_coords[1]) == self.empty_cell or \
                (cell_coords[0], cell_coords[1] + 1) == self.empty_cell or \
                (cell_coords[0], cell_coords[1] - 1) == self.empty_cell:
            b = self.num_dict[cell_coords]
            self.num_dict[cell_coords] = 0
            self.num_dict[self.empty_cell] = b
            self.empty_cell = cell_coords



pygame.init()
pygame.font.init()
size = width, height = 600, 600
screen = pygame.display.set_mode(size)
surfac = pygame.Surface((size[0], size[1]))
surfac.fill((150, 0, 34))
start_screen = start_screen(screen)
level = 5
board = Board(3, 3, level)
board.set_view(50, 50, 55)
###################
all_sprites = pygame.sprite.Group()
horizontal_borders = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()
left_top = 20 * 2
board_num = 3 * 2
cell_size = 30
Border(left_top, left_top, width - left_top, left_top)
Border(left_top, height - left_top, width - left_top, height - left_top)
Border(left_top, left_top + cell_size * board_num, left_top + cell_size * board_num, height - left_top)
Border((cell_size * board_num + left_top), left_top, cell_size * board_num + left_top, cell_size * board_num + left_top)
####################
Border(5, 5, width - 5, 5)
Border(5, height - 5, width - 5, height - 5)
Border(5, 5, 5, height - 5)
Border(width - 5, 5, width - 5, height - 5)
#############
draw_im = (os.path.join('data', 'snow.png'))
for i in range(30):
    Ball(12, 300, 300)
###########
pygame.time.set_timer(pygame.USEREVENT, 3000)
CARS = (os.path.join('data', 'car_new.png'), os.path.join('data', 'car_new.png'), os.path.join('data', 'car_new.png'))
CARS_SURF = []
for i in range(len(CARS)):
    CARS_SURF.append(
        pygame.image.load(CARS[i]).convert_alpha())
cars = pygame.sprite.Group()
Car(300,
    CARS_SURF[0], cars)  # координата
print(CARS_SURF)
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.get_click(event.pos, screen)
            pygame.display.update()
            break

    screen.fill((0, 0, 0))
    board.render(screen)  # прорисовка поля
    if board.flag_finish or board.is_win():
        Car(randint(1, size[0]),
            CARS_SURF[randint(0, 1)], cars)
        start_screen = start_screen2(screen, surfac)

        level += 16
        board = Board(3, 3, level)
        board.set_view(50, 50, 55)
        if level > 80:
            running = False
        continue
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.time.delay(20)

    pygame.display.update()
    pygame.display.flip()

##############################

if start_screen2:
    level = 21
    run = True
    board = Board(4, 4, level)
    board.set_view(50, 50, 55)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.USEREVENT:
                Car(randint(1, size[0]),
                    CARS_SURF[randint(0, 1)], cars)
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(event.pos, screen)
                pygame.display.update()
                break

        screen.fill((0, 0, 0))
        board.render(screen)
        cars.draw(screen)
        cars.update()

        pygame.display.update()
        if board.flag_finish or board.is_win():
            start_screen = start_screen2(screen, surfac)
            level += 20
            board = Board(4, 4, level)
            board.set_view(50, 50, 55)
            if level > 60:
                start_screen = start_screen3(screen, surfac)

            continue

        pygame.display.flip()
