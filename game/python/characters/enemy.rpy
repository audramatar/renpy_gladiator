init:
    default enemy = Enemy("Enemy")

    init 2 python:
        class Enemy(Person):
            def __init__(self, name):
                super(Enemy, self).__init__(name)
