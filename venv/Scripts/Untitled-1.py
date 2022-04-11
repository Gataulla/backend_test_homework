class Training:
    """Базовый класс Training"""
    def __init__(self, 
    action: int, 
    duration: float, 
    weight: float, 
    LEN_STEP: float = 0.65, 
    M_IN_KM: int = 1000) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight
        self.LEN_STEP = LEN_STEP
        self.M_IN_KM = M_IN_KM
    
    def get_distance(self) -> float:
        """Дистанция, преодаленная пользователем."""
        self.way = self.action * self.LEN_STEP / self.M_IN_KM
        return self.way
    
    def get_mean_speed(self) -> float:
        """Средняя скорость движения."""
        self.average_speed = self.way / self.duration

    def get_spent_calories(self):
        """Подсчет потраченных калорий."""
        pass

    def show(self):
        """Показывает полученные данные"""
        print(f'Тип тренировки:'
              f'Длительность тренировки: {self.duration}'
              f'Преодоленная дистанция: {self.way}'
              f'Средняя скорость: {self.average_speed}'
              f'Расход энергии:')

if __name__ == '__main__':
    packages = [        
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training) 