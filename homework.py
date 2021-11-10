from dataclasses import dataclass
from typing import ClassVar


@dataclass
class InfoMessage:
    """Информационное сообщение о тренировке."""
    training_type: str                  # Если не использовать 'round',
    duration: float                     # то программа не проходит
    distance: float                     # тесты. Выводимые значения
    speed: float                        # отличаются от ожидаемых.
    calories: float

    def get_message(self) -> str:
        """Вывести сообщение о тренировке на экран"""
        return (f'Тип тренировки: {self.training_type};'
                f' Длительность: {self.duration:.3f} ч.;'
                f' Дистанция: {self.distance:.3f} км;'
                f' Ср. скорость: {self.speed:.3f} км/ч;'
                f' Потрачено ккал: {self.calories:.3f}.')


@dataclass
class Training: 
    """Базовый класс тренировки."""

    LEN_STEP: ClassVar[float] = 0.65
    M_IN_KM: ClassVar[int] = 1000
    H_IN_MIN: ClassVar[int] = 60
    action: int
    duration: float
    weight: float
        
    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        distance = self.action * self.LEN_STEP / self.M_IN_KM
        return distance

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        mean_speed = self.get_distance() / self.duration
        return mean_speed

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        workout_type = type(self).__name__
        duration = self.duration
        distance = self.get_distance()
        mean_speed = self.get_mean_speed()
        spent_calories = self.get_spent_calories()
        messsage = InfoMessage(workout_type, duration, distance, mean_speed,
                               spent_calories)
        return messsage


class Running(Training):
    """Тренировка: бег."""

    COEFF_CALORIES_1: ClassVar[int] = 18
    COEFF_CALORIES_2: ClassVar[int] = 20

    def get_spent_calories(self) -> float:
        spent_calories = (((self.COEFF_CALORIES_1 * self.get_mean_speed()
                          - self.COEFF_CALORIES_2)
                          * self.weight / self.M_IN_KM) * self.duration
                          * self.H_IN_MIN
                          )
        return spent_calories


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""

    COEFF_CALORIES_1: ClassVar[float] = 0.035
    COEFF_CALORIES_2: ClassVar[float] = 0.029
    height: float
    
    def get_spent_calories(self) -> float:
        spent_calories = (self.COEFF_CALORIES_1 * self.weight
                          + (self.get_mean_speed() ** 2 // self.height)
                          * self.COEFF_CALORIES_2
                          * self.weight) * self.duration * self.H_IN_MIN
        return spent_calories


class Swimming(Training):
    """Тренировка: плавание."""

    LEN_STEP: ClassVar[float] = 1.38
    COEFF_CALORIES_1: ClassVar[float] = 1.1
    COEFF_CALORIES_2: ClassVar[int] = 2
    
    length_pool: int
    count_pool: int
        
    def get_mean_speed(self) -> float:
        mean_speed = (self.length_pool * self.count_pool
                      / self.M_IN_KM / self.duration)
        return mean_speed

    def get_spent_calories(self) -> float:
        speed = self.get_mean_speed()
        spent_calories = ((speed + self.COEFF_CALORIES_1)
                          * self.COEFF_CALORIES_2 * self.weight)
        return spent_calories


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""

    if workout_type == 'SWM':
        swimming = Swimming(data[0], data[1], data[2], data[3], data[4])
        return swimming
    elif workout_type == 'RUN':
        runninig = Running(data[0], data[1], data[2],)
        return runninig
    elif workout_type == 'WLK':
        walking = SportsWalking(data[0], data[1], data[2], data[3])
        return walking


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
