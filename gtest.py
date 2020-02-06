import tkinter
import time
from dlib_68_ref import refShape

# width of the animation window
animation_window_width = 800
# height of the animation window
animation_window_height = 800
# delay between successive frames in seconds
animation_refresh_seconds = 2

# The main window of the animation
def create_animation_window():
    window = tkinter.Tk()
    window.title("Render Face")
    window.geometry(f'{animation_window_width}x{animation_window_height}')
    return window

# Create a canvas for animation and add it to main window
def create_animation_canvas(window):
    canvas = tkinter.Canvas(window)
    canvas.configure(bg="white")
    canvas.pack(fill="both", expand=True)
    return canvas

# Draw the face and save to file
# or actively stream the data to this screen
def draw_face(window, canvas, shape):

    canvas.delete("all")

    # Draw Right eye
    canvas.create_polygon(shape[36:42],fill="white", outline="black")
    window.update()

    # Draw nose
    canvas.create_line(shape[27:31])
    canvas.create_line(shape[31:36])
    window.update()

    # Draw Left Eye
    canvas.create_polygon(shape[42:48],fill="white", outline="black")
    window.update()

    # Draw eyebrows
    canvas.create_line(shape[17:22])
    canvas.create_line(shape[22:27])
    
    # Draw lips
    canvas.create_polygon(shape[48:60],fill="white", outline="black")
    canvas.create_polygon(shape[60:68],fill="white", outline="black")
    window.update()

    # Draw Jaw
    canvas.create_line(shape[0:17])
    window.update()

    time.sleep(animation_refresh_seconds)

    # window.mainloop()


# Testing
animation_window = create_animation_window()
animation_canvas = create_animation_canvas(animation_window)
draw_face(animation_window, animation_canvas, refShape)

