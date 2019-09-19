init:
    default player = Player("Player")

    init 2 python:
        class Player(Person):
            def __init__(self, name):
                super(Player, self).__init__(name)
