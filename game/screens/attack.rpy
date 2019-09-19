screen attack_button():
    imagebutton auto "attack_%s.png":
        xalign 0.5 yalign 0.5
        action Function(enemy.defend, attack_object = player.attack_object())
