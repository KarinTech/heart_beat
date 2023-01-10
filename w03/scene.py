# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_sky(canvas)
    for i in range(200, 601, 100):
        draw_tiny_cols(canvas, i, 50, 100, 250, 'gray90')
    draw_clouds(canvas, 80, 400, 'steelBlue1')
    draw_clouds(canvas, 150, 420, 'steelBlue1')
    draw_clouds(canvas, 100, 430, 'steelBlue1')
    draw_clouds(canvas, 710, 400, 'steelBlue1')
    draw_clouds(canvas, 750, 430, 'steelBlue1')
    draw_clouds(canvas, 750, 390, 'steelBlue1')
    draw_cols(canvas, 100, 50, 100, 300, 'gray90')
    draw_cols(canvas, 600, 50, 100, 300, 'gray90')
    draw_grass(canvas, 0, 0, 800, 50, 'forestGreen')
    draw_tree(canvas, 50, 0, 100, 'green')
    draw_tree(canvas, 100, 20, 80, 'forestGreen')
    draw_tree(canvas, 700, 30, 75, 'darkGreen')
    draw_tree(canvas, 730, 35, 60, 'green4')
    draw_tree(canvas, 75, 10, 65, 'chartreuse4')

    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.

def draw_clouds(canvas, bottom_x, bottom_y, color):
    draw_oval(canvas, bottom_x, bottom_y, bottom_x + 100, bottom_y + 50, width=0, fill=color)


def draw_sky(canvas):
    draw_rectangle(canvas, 0, 50, 800, 500, fill='lightSkyBlue1')


def draw_tree(canvas, center, bottom_y, height, color):
    draw_rectangle(canvas, center - 10, bottom_y, center + 10, bottom_y + height, width=0, fill='tan4')
    draw_oval(canvas, center - 40, bottom_y + height, center + 40,
              bottom_y + height + height * 2, width=0, fill=color)


def draw_grass(canvas, bottom_x, bottom_y, width, height, color):
    draw_rectangle(canvas, bottom_x, bottom_y, width, height, fill=color)


def draw_portal(canvas, bottom_x, bottom_y, width):
    draw_oval(canvas, bottom_x + 25, bottom_y + 75, bottom_x + width - 25, bottom_y + 125, width=0, fill='gray80')
    draw_rectangle(canvas, bottom_x + 25, bottom_y, bottom_x + width - 25, bottom_y + 100, width=0, fill='gray80')


def draw_tiny_cols(canvas, bottom_x, bottom_y, width, height, color):
    draw_rectangle(canvas, bottom_x, bottom_y, bottom_x + width, bottom_y + height, width=0, fill=color)
    draw_oval(canvas, bottom_x + 25, bottom_y + height - 75, bottom_x + 75, bottom_y + height - 25, width=0, fill='gray80')
    draw_portal(canvas, bottom_x, bottom_y, width)
    draw_line(canvas, bottom_x + 25, bottom_y + height - 100, bottom_x + 75,
              bottom_y + height - 100, width=2, fill='gray80')
    draw_line(canvas, bottom_x, bottom_y, bottom_x, bottom_y + height - 50, width=2, fill='gray80')


def draw_cols(canvas, bottom_x, bottom_y, width, height, color):
    draw_rectangle(canvas, bottom_x, bottom_y, bottom_x + width, bottom_y + height, width=0, fill=color)
    draw_polygon(canvas, bottom_x, bottom_y + height, width / 2 + bottom_x,
                 height + bottom_y + 100, bottom_x + width, bottom_y + height, width=0, outline='gray99', fill=color)
    draw_portal(canvas, bottom_x, bottom_y, width)
    draw_portal(canvas, bottom_x, bottom_y + 150, width)


def draw_grid(canvas, width, height, interval):
    label_y = 15
    for x in range(interval, width, interval):
        draw_line(canvas, x, 0, x, height)
        draw_text(canvas, x, label_y, f'{x}')

    label_x = 15
    for y in range(interval, height, interval):
        draw_line(canvas, 0, y, width, y)
        draw_text(canvas, label_x, y, f'{y}')


# Call the main function so that
# this program will start executing.
main()
