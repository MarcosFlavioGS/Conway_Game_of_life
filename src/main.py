import pygame as py
import random
import numpy
import scipy.signal


def update_grid(grid):
    arr = grid
    arr = numpy.array(arr)
    counts = scipy.signal.convolve2d(arr, numpy.ones((3, 3)), mode='same')
    arr = numpy.where((counts == 3) | (counts == 4) & (arr == 1), 1, 0)
    return arr


def draw_grid(grid, screen, pos, size, mouse=py.Vector2(300, 800)):
    mouse_grid_x = int((mouse.x - pos.x) / size)
    mouse_grid_y = int((mouse.y - pos.y) / size)

    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            posx = pos.x + j * size
            posy = pos.y + i * size
            rect_pos = py.Vector2(posx, posy)
            if i == mouse_grid_y and j == mouse_grid_x:
                grid[i][j] = 1
                py.draw.rect(screen, "White", py.Rect(rect_pos.x,
                                                      rect_pos.y, size, size))
            if val == 1:
                py.draw.rect(screen, "White", py.Rect(rect_pos.x,
                                                      rect_pos.y, size, size))


py.init()
screen = py.display.set_mode((1280, 730))
clock = py.time.Clock()
running = True
dt = 0

update = False
pos = py.Vector2(0, 0)
cols = 160
rows = 80
cell_size = 10
grid = [[random.randint(0, 1) for i in range(cols)]for j in range(rows)]
for row in grid:  # visualizing grid
    print(row)

while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False

    screen.fill("Black")

    keys = py.key.get_pressed()
    if keys[py.K_ESCAPE]:  # Exit execution on Esc
        running = False
    if keys[py.K_w]:  # Start execution
        update = True
    if keys[py.K_s]:  # Pause execution
        update = False
    if update:
        grid = update_grid(grid)

    if py.mouse.get_pressed() == (1, 0, 0):
        mouse_pos = py.Vector2(py.mouse.get_pos())  # Get mouse position to draw cell on
        print(mouse_pos)
        draw_grid(grid, screen, pos, cell_size, mouse_pos)
    else:
        draw_grid(grid, screen, pos, cell_size)

    py.display.flip()

    dt = clock.tick(60) / 1000

py.quit()
