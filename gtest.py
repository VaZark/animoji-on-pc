import tkinter
import time
from dlib_68_ref import refShape

# width of the animation window
animation_window_width = 600
# height of the animation window
animation_window_height = 600
# delay between successive frames in seconds
animation_refresh_seconds = 0.2

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
    canvas.configure(bg="blue")
    canvas.pack(fill="both", expand=True)
    return canvas

# Draw the face and save to file
# or actively stream the data to this screen
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
    tleft_x, _ = shape[37]
    _ , tleft_y = shape[38]
    
    bright_x, _ = shape[40]
    _ , bright_y = shape[41]
    c = canvas.create_oval(tleft_x, tleft_y, bright_x, bright_y)
    window.update()
    time.sleep(animation_refresh_seconds)
    canvas.delete("all")
    c = canvas.create_oval(tleft_x+30, tleft_y, bright_x, bright_y)
    window.update()
    time.sleep(animation_refresh_seconds)

    # window.mainloop()


# The actual execution starts here
animation_window = create_animation_window()
animation_canvas = create_animation_canvas(animation_window)
draw_face(animation_window, animation_canvas, refShape)

# # PIL create an empty image and draw object to draw on memory only, not visible
# image1 = Image.new("RGB", (animation_window_width, animation_window_height), "white")
# draw = ImageDraw.Draw(image1)
# dra.create_oval(tleft_x, tleft_y, bright_x, bright_y)
# filename = "test.jpg"
# image1.save(filename)
