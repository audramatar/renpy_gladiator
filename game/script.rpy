
default combat_message = ""

label start:
    scene bg white
    jump game_loop

    return

label game_loop:
    show screen attack_button
    show screen stats(enemy)
    show screen battleTextScreen
    "What would you like to do?"

    jump game_loop
