import pygame as py
import random
import numpy
import scipy.signal


def new_grid(cols, rows, num=0):
    return [[num for i in range(cols)]for j in range(rows)]


def random_grid(cols, rows):
    return [[random.randint(0, 1) for i in range(cols)]for j in range(rows)]


def update_grid(grid):
    arr = grid
    arr = numpy.array(arr)
    counts = scipy.signal.convolve2d(arr, numpy.ones((3, 3)), mode='same')
    arr = numpy.where((counts == 3) | (counts == 4) & (arr == 1), 1, 0)
    return arr


def draw_grid(grid, screen, pos, size, mouse=None):
    if mouse:
        mouse_grid_x = int((mouse.x - pos.x) / size)
        mouse_grid_y = int((mouse.y - pos.y) / size)
    else:
        mouse_grid_x = None
        mouse_grid_y = None

    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            posx = pos.x + j * size
            posy = pos.y + i * size
            rect_pos = py.Vector2(posx, posy)
            if i == mouse_grid_y and j == mouse_grid_x:
                grid[i][j] = 1
                py.draw.rect(screen, "#4CBB17",
                             py.Rect(rect_pos.x, rect_pos.y, size, size))
            if val == 1:
                py.draw.rect(screen, "#4CBB17",
                             py.Rect(rect_pos.x, rect_pos.y, size, size))


py.init()
screen_info = py.display.Info()
screen_width = screen_info.current_w
screen_height = screen_info.current_h
screen = py.display.set_mode((screen_width, screen_height))
clock = py.time.Clock()
running = True
dt = 0

update = False
pos = py.Vector2(0, 0)
cell_size = 10
cols = int(screen_width / cell_size)
rows = int(screen_height / cell_size)
grid = new_grid(cols, rows)  # Initial grid
for row in grid:  # visualizing grid
    print(row)

while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False

    screen.fill("#71797E")

    keys = py.key.get_pressed()
    if keys[py.K_ESCAPE]:  # Exit execution on Esc
        running = False
    if keys[py.K_w]:  # Start execution
        update = True
    if keys[py.K_s]:  # Pause execution
        update = False
    if keys[py.K_r]:  # Put random cells all over the screen
        grid = random_grid(cols, rows)
    if keys[py.K_c]:  # Clean grid
        grid = new_grid(cols, rows)
    if update:
        grid = update_grid(grid)

    if py.mouse.get_pressed() == (1, 0, 0):
        mouse_pos = py.Vector2(py.mouse.get_pos())
        print(mouse_pos)
        draw_grid(grid, screen, pos, cell_size, mouse_pos)
    else:
        draw_grid(grid, screen, pos, cell_size)

    py.display.flip()

    dt = clock.tick(10) / 1000  # Frames. Seting to 10 to visualize better

py.quit()
