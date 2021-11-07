


class InfoMessage:
    """Информационное сообщение о тренировке."""
    def __init__(self, 
                 training_type: str,
                 duration: float,
                 distance: float,
                 mean_speed: float,
                 spent_calories: float) -> None:
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.mean_speed = mean_speed
        self.spent_calories = spent_calories         
        
        
    def show_info(self):
        """Вывести сообщение о тренировке на экран"""
        print(f'{self.training_type}; Длительность: {self.duration} ч.;'
              f' Дистанция: {self.distance} км; Ср. скорость: {self.speed} км/ч; Потрачено ккал: {self.calories}.')


class Training:
    """Базовый класс тренировки."""
    LEN_STEP: float = 0.65
    M_IN_KM : int = 1000

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action = action  
        self.duration = duration 
        self.weight = weight     
        

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        distance = self.action * self.LEN_STEP /self.M_IN_KM
        return distance

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        mean_speed = distance/duration
        return mean_speed

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self, training_type, duration, distance, mean_speed, spent_calories) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        messsage = InfoMessage(training_type, duration, distance, mean_speed, spent_calories) 
        return messsage
        


class Running(Training):
    """Тренировка: бег."""
    coeff_calories_1: int = 18
    coeff_calories_2: int = 20
    

    def __init__(self, action: int, duration: float, weight: float) -> None:
        super().__init__(action, duration, weight)
               

    def get_spent_calories(self) -> float:
        spent_calories = (self.coeff_calories_1 * self.get_distance - self.coeff_calories_2) * self.weight/self.M_IN_KM * self.duration   
        return spent_calories

class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    coeff_calories_1: float = 0.035
    coeff_calories_2: float = 0.029

    def __init__(self, action: int, duration: float, weight: float, height: float) -> None:
        super().__init__(action, duration, weight)
        self.height = height
        
    def get_spent_calories(self) -> float:
        spent_calories = (self.coeff_calories_1 * self.weight + (self.get_mean_speed**2 //self.height) * self.coeff_calories_2 * self.weight) * self.duration
        return spent_calories


class Swimming(Training):
    """Тренировка: плавание."""
    LEN_STEP: float = 1.38
    coeff_calories_1: float = 1.1
    coeff_calories_2: int = 2


    def __init__(self, action: int, duration: float, weight: float, length_pool: int, count_pool: int) -> None:
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool
        

    def get_mean_speed(self) -> float:
        mean_speed = self.length_pool * self.count_pool/self.M_IN_KM/self.duration
        return mean_speed

    def get_spent_calories(self) -> float:
        speed = self.get_mean_speed()
        spent_calories = (speed + self.coeff_calories_1) * self.coeff_calories_2 * self.weight
        return spent_calories       
        


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    
    if workout_type =='SWM':
        swiming = Swimming(data[0], data[1], data[2], data[3], data[4])
        return swiming
    elif workout_type == 'RUN':
        runninig = Running(data[0], data[1], data[2])
        return runninig
    elif workout_type == 'WLK':
        walking = SportsWalking(data[0], data[1], data[2], data[3])
        return walking    




def main(training: Training) -> None:
    """Главная функция."""
    distance = training.get_distance()
    mean_speed = training.get_mean_speed()
    spent_calories = training.get_spent_calories()
    duration = self.duration
    info = training.show_training_info(workout_type, duration, distance, mean_speed, spent_calories)
    info.show_info()


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)

