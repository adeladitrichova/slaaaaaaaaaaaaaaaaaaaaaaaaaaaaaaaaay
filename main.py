start = 0
pins.touch_set_mode(TouchTarget.P1, TouchTargetMode.CAPACITIVE)
pins.touch_set_mode(TouchTarget.P2, TouchTargetMode.CAPACITIVE)

def on_forever():
    console.log_value("Analog", pins.analog_read_pin(AnalogPin.P1))
    global start
    start = randint(3000, 10000)
    music.play_tone(Note.C, start)
    basic.forever(on_forever)

def on_pin_pressed_p1():
    
    player1WIN = basic.show_number(1)


input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)









