let no = 0
let count = 0
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    no = 1
    count = randint(10, 100)
    basic.showString("NUMBER IS " + ("" + ("" + count)))
    while (no <= count) {
        basic.showString("" + ("" + no))
        no = no + 1
    }
})
