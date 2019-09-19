screen battleTextScreen():
    zorder 12

    frame:
        xsize 500
        ysize 120

        padding(10, 10)

        xalign 0.45
        yalign 0.9

        # background Frame("images/icons/combat_text_box.png")
        background "#add8e6"

        text "[combat_message]":
            size 28
            kerning 2
            xalign 0.1
            yalign 0.1
            xmaximum 450
