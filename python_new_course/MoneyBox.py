class MoneyBox:
    def __init__(self, capacity):
        # конструктор с аргументом – вместимость копилки
        self.count_coin = 0
        self.capacity = capacity
    def can_add(self, v):
        # True, если можно добавить v монет, False иначе
        return self.count_coin + v <= self.capacity
    def add(self, v):
        if self.can_add(v):
            # положить v монет в копилку
            self.count_coin += v