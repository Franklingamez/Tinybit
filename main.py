no = 0
count = 0

def on_button_pressed_a():
    global no, count
    no = 1
    count = randint(10, 100)
    basic.show_string("NUMBER IS " + ("" + str(count)))
    while no <= count:
        basic.show_string("" + str(no))
        no = no + 1
input.on_button_pressed(Button.A, on_button_pressed_a)
