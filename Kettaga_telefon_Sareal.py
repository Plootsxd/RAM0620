import tkinter as tk
import math

root = tk.Tk()
root.title("Kettatelefon")

canvas = tk.Canvas(root, width=450, height=450, bg="#1c1c1c")
canvas.pack()

cx = 225
cy = 225

radius = 170
hole_r = 18
ring_r = 115

rotation = 0
dragging = False
current_digit = None
max_rotation = 0
last_angle = 0

number_list = []

digits = [1,2,3,4,5,6,7,8,9,0]

stopper_angle = 60

base_angles = {}
for d in digits:
    n = d if d != 0 else 10
    base_angles[d] = (stopper_angle - n*30) % 360


def get_angle(x, y):
    angle = math.degrees(math.atan2(y - cy, x - cx))
    return angle % 360


def get_pos(angle, r):
    rad = math.radians(angle)
    return cx + r*math.cos(rad), cy + r*math.sin(rad)


def hole_pos(d):
    angle = (base_angles[d] + rotation) % 360
    return get_pos(angle, ring_r)


def find_digit(x, y):
    for d in digits:
        hx, hy = hole_pos(d)
        if math.hypot(x - hx, y - hy) < hole_r + 5:
            return d
    return None


def mouse_down(e):
    global dragging, current_digit, last_angle, max_rotation

    d = find_digit(e.x, e.y)
    if d is not None:
        dragging = True
        current_digit = d
        last_angle = get_angle(e.x, e.y)

        if d == 0:
            max_rotation = 300
        else:
            max_rotation = d * 30


def mouse_move(e):
    global rotation, last_angle

    if not dragging:
        return

    ang = get_angle(e.x, e.y)
    diff = (ang - last_angle) % 360

    if diff > 180:
        diff -= 360

    last_angle = ang

    rotation += diff

    if rotation < 0:
        rotation = 0
    if rotation > max_rotation:
        rotation = max_rotation

    draw()


def mouse_up(e):
    global dragging, rotation

    dragging = False

    if rotation > max_rotation - 10:
        number_list.append(current_digit)
        update_text()

    return_back()


def return_back():
    global rotation

    if rotation > 0:
        rotation -= 5
        if rotation < 0:
            rotation = 0
        draw()
        root.after(15, return_back)


def update_text():
    txt = ""
    for n in number_list:
        txt += str(n)
    label.config(text=txt)


def call():
    txt = ""
    for n in number_list:
        txt += str(n)

    if txt == "":
        result.config(text="Sisesta number")
    else:
        result.config(text="Helistan: " + txt)


def clear():
    number_list.clear()
    label.config(text="")
    result.config(text="")


def draw():
    canvas.delete("all")

    canvas.create_oval(cx-200, cy-200, cx+200, cy+200, fill="#2c2c2c")
    canvas.create_oval(cx-radius, cy-radius, cx+radius, cy+radius, fill="#b0b0b0")

    for d in digits:
        x, y = hole_pos(d)

        canvas.create_oval(x-hole_r, y-hole_r, x+hole_r, y+hole_r, fill="black")
        canvas.create_text(x, y, text=str(d), fill="white")

    # stopper
    sx, sy = get_pos(stopper_angle, radius-10)
    canvas.create_oval(sx-10, sy-10, sx+10, sy+10, fill="black")


label = tk.Label(root, text="", font=("Arial", 18))
label.pack()

result = tk.Label(root, text="", font=("Arial", 12))
result.pack()

btn_frame = tk.Frame(root)
btn_frame.pack()

tk.Button(btn_frame, text="Helista", command=call).pack(side="left", padx=10)
tk.Button(btn_frame, text="Kustuta", command=clear).pack(side="left", padx=10)

canvas.bind("<Button-1>", mouse_down)
canvas.bind("<B1-Motion>", mouse_move)
canvas.bind("<ButtonRelease-1>", mouse_up)

draw()

root.mainloop()