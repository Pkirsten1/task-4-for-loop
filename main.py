def on_button_pressed_a():
    for index in range(5):
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . # . .
                        . . . . .
                        . . . . .
        """)
        basic.show_icon(IconNames.SMALL_SQUARE)
        basic.show_icon(IconNames.SQUARE)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
input.on_button_pressed(Button.A, on_button_pressed_a)
