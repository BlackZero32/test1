x = 0
y = 0

def on_button_pressed_a():
    global x, y
    while True:
        x = randint(0, 10)
        basic.show_number(x)
        y = x % 2
        if y == 0:
            basic.show_icon(IconNames.YES)
        elif y == 1:
            basic.show_icon(IconNames.NO)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_forever():
    pass
basic.forever(on_forever)
