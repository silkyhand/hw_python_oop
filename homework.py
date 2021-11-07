class InfoMessage:
    """Информационное сообщение о тренировке."""
    def __init__(self,
                 training_type: str,
                 duration: float,
                 distance: float,
                 speed: float,
                 calories: float) -> None:
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories         
        
    def show_info(self):
        """Вывести сообщение о тренировке на экран"""
        print(f'{self.training_type}; Длительность: {self.duration} ч.;'
              f' Дистанция: {self.distance} км; Ср. скорость: {self.speed} км/ч; Потрачено ккал: {self.calories}.')


class Training:
    """Базовый класс тренировки."""

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action = action  
        self.duration = duration 
        self.weight = weight     
        LEN_STEP: float = 0.65
        M_IN_KM : int = 1000

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        distance = self.action * LEN_STEP / M_IN_KM
        return distance

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        mean_speed = distance/duration
        return mean_speed

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self, training_type, distance, mean_speed, spent_calories) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        messsage = InfoMessage(training_type, duration, distance,mean_speed, spent_calories) 
        return messsage
        


class Running(Training):
    """Тренировка: бег."""
    def __init__(self, action: int, duration: float, weight: float) -> None:
        super().__init__(action, duration, weight)
        # add new  for counting calories
        coeff_calories_1: int = 18
        coeff_calories_2: int = 20

    def get_spent_calories(self) -> float:
        spent_calories = (coeff_calories_1 * self.get_distance - spent_calories_2) * self.weight/M_IN_KM * self.duration   
        return spent_calories

class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    def __init__(self, action: int, duration: float, weight: float, height: float) -> None:
        super().__init__(action, duration, weight)
        self.height = height
        coeff_calories_1: float = 0.035
        coeff_calories_2: float = 0.029

    def get_spent_calories(self) -> float:
        spent_calories = (coeff_calories_1 * self.weight + (self.get_mean_speed**2 //self.height) * coeff_calories_2 * self.weight) * self.duration
        return spent_calories


class Swimming(Training):
    """Тренировка: плавание."""
    def __init__(self, action: int, duration: float, weight: float, length_pool: int, count_pool: int) -> None:
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool
        LEN_STEP: float = 1.38
        coeff_calories_1: float = 1.1
        coeff_calories_2: int = 2

    def get_mean_speed(self) -> float:
        mean_speed = self.length_pool * self.count_pool/M_IN_KM/self.duration
        return mean_speed

    def get_spent_calories(self) -> float:
        spent_calories = (self.get_mean_speed + coeff_calories_1) * coeff_calories_2 * self.weight
        return spent_calories       
        


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    pass


def main(training: Training) -> None:
    """Главная функция."""
    pass


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)

