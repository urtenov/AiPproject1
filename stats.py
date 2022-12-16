class Stats():
    """
    отслеживание статистики
    """

    def __init__(self):
        """
        Инициализация статистики
        """
        self.reset_stats()
        self.run_game = True

    def reset_stats(self):
        """
        изменение статистики во время игры, задание количества жизней самолета и количества очков в начале игры
        """
        self.guns_left = 1
        self.score = 0

