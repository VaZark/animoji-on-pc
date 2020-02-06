import tkinter
import time
from dlib_68_ref import refShape

# width of the animation window
animation_window_width = 800
# height of the animation window
animation_window_height = 600
# delay between successive frames in seconds
animation_refresh_seconds = 0.01

# The main window of the animation


def create_animation_window():
    window = tkinter.Tk()
    window.title("Render Face")
    # Uses python 3.6+ string interpolation
    window.geometry(f'{animation_window_width}x{animation_window_height}')
    return window

# Create a canvas for animation and add it to main window


def create_animation_canvas(window):
    canvas = tkinter.Canvas(window)
    canvas.configure(bg="black")
    canvas.pack(fill="both", expand=True)
    return canvas

# Draw the face and save to file


def draw_face(window, canvas, shape):
    # Split Contours of the face
    j_shape = shape[0:17]
    rb_shape = shape[17:22]
    lb_shape = shape[22:27]
    n_shape = shape[27:35]
    re_shape = shape[35:42]
    le_shape = shape[42:48]
    m_shape = shape[48:68]

    # Draw Right eye
    canvas.create_line(55, 85, 155, 85, 105, 180, 55, 85)

    canvas.move(ball, xinc, yinc)
    window.update()
    time.sleep(animation_refresh_seconds)
    ball_pos = canvas.coords(ball)


# The actual execution starts here
animation_window = create_animation_window()
animation_canvas = create_animation_canvas(animation_window)
draw_face(animation_window, animation_canvas, refShape)
