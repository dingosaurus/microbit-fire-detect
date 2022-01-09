basic.show_leds("""
    # # # # #
        # . . . #
        # . . . #
        # . . . #
        # # # # #
""")
basic.pause(200)
basic.show_leds("""
    . . . . .
        . # # # .
        . # . # .
        . # # # .
        . . . . .
""")
basic.pause(200)
basic.show_leds("""
    . . . . .
        . . . . .
        . . # . .
        . . . . .
        . . . . .
""")
basic.pause(200)
basic.show_leds("""
    . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
""")

def on_forever():
    if pins.digital_read_pin(DigitalPin.P0) == 1:
        pass
basic.forever(on_forever)
