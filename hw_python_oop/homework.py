from typing import Dict


class InfoMessage:
    """Информационное сообщение о тренировке."""

    def __init__(
        self,
        training_type: str,
        duration: float,
        distance: float,
        speed: float,
        calories: float
    ) -> None:
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories

    def get_message(self):
        return (f'Тип тренировки: {self.training_type}; '
                f'Длительность: {self.duration:.3f} ч.; '
                f'Дистанция: {self.distance:.3f} км; '
                f'Ср. скорость: {self.speed:.3f} км/ч; '
                f'Потрачено ккал: {self.calories:.3f}.')

    def __str__(self) -> str:
        return self.get_message()


class Training:
    """Базовый класс тренировки."""
    LEN_STEP: float = 0.65
    M_IN_KM: float = 1000
    CONVERT_HOURS_MIN: int = 60  # Константа для конвертации ч. в мин.

    def __init__(
        self,
        action: int,
        duration: float,
        weight: float
    ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        """Дистанция, пройденная пользователем."""
        return self.action * self.LEN_STEP / self.M_IN_KM

    def get_mean_speed(self) -> float:
        """Средняя скорость движения."""
        return self.get_distance() / self.duration

    def get_spent_calories(self) -> float:
        """Потраченные колорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Информация о выполненной тренировке."""
        return InfoMessage(
            training_type=type(self).__name__,
            duration=self.duration,
            distance=self.get_distance(),
            speed=self.get_mean_speed(),
            calories=self.get_spent_calories())


class Swimming(Training):
    """Тренировка: плавание."""
    LEN_STEP: float = 1.38
    COEF_SWIM_1: float = 1.1
    COEF_SWIM_2: float = 2

    def __init__(
        self,
        action: int,
        duration: float,
        weight: float,
        length_pool: float,
        count_pool: int
    ) -> None:
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_spent_calories(self) -> float:
        return ((self.get_mean_speed() + self.COEF_SWIM_1) 
                 * self.COEF_SWIM_2 * self.weight)


class Running(Training):
    """Тренировка: бег."""

    COEF_CALORIES_1: int = 18
    COEF_CALORIES_2: int = 20

    def __init__(
        self,
        action: int,
        duration: float,
        weight: float
    ) -> None:
        super().__init__(action, duration, weight)

    def get_spent_calories(self):
        return ((self.COEF_CALORIES_1 * self.get_mean_speed()
                 - self.COEF_CALORIES_2) * self.weight
                 / self.M_IN_KM * self.duration * self.CONVERT_HOURS_MIN)


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    COEF_WLK_1: float = 0.035
    COEF_WLK_2: float = 0.029

    def __init__(
        self,
        action: int,
        duration: float,
        weight: float,
        height: float
    ) -> None:
        super().__init__(action, duration, weight)
        self.height = height

    def get_spent_calories(self):
        return ((self.COEF_WLK_1 * self.weight
                 + (self.get_mean_speed() ** 2 // self.height)
                 * self.COEF_WLK_2 * self.weight)
                 * self.duration * self.CONVERT_HOURS_MIN)


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    workout_types: Dict[str, type[Training]] = {
        'SWM': Swimming,
        'WLK': SportsWalking,
        'RUN': Running
    }
    if workout_type not in workout_types:
        raise ValueError(f'В словаре "packages" отстуствует данная тренировки'
                         f'внимательно проверьте {workout_type}')
    return workout_types[workout_type](*data)


def main(training: Training) -> None:
    """Главная функция."""
    info = training.show_training_info()
    print(info.get_message())


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
