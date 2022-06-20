def calculateFrequencies():
    global f1
    f1 = ConcertA * twototheonetwelfth ** step1
    basic.show_number(f1)

def on_button_pressed_a():
    global step1
    step1 = step1 - 1
    basic.show_arrow(ArrowNames.SOUTH)
    calculateFrequencies()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global step1
    step1 = step1 + 1
    basic.show_arrow(ArrowNames.NORTH)
    calculateFrequencies()
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_pin_pressed_p1():
    music.play_tone(f1, music.beat(BeatFraction.WHOLE))
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)

f1 = 0
twototheonetwelfth = 0
ConcertA = 0
step1 = 0
step1 = 0
ConcertA = 440
twototheonetwelfth = 2 ** (1 / 12)
calculateFrequencies()
basic.show_icon(IconNames.EIGTH_NOTE)