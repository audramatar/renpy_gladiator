screen all_stats(character, enemy):
    use stats(character)
    use stats(enemy)

screen stats(character):
    frame:
        padding (0, 0)
        top_padding 3
        left_padding 2
        grid 1 3:
            text "[character.name]"
            text "HP: [character.hp]"
            text "Alive: [character.alive]"
