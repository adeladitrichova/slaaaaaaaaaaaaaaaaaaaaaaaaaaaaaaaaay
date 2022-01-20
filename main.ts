let start = 0
let Player1WIN = 0
pins.touchSetMode(TouchTarget.P1, TouchTargetMode.Capacitive)
pins.touchSetMode(TouchTarget.P2, TouchTargetMode.Capacitive)
input.onPinPressed(TouchPin.P1, function on_pin_pressed_p1() {
    let player1WIN = []
    basic.showNumber(1)
})
