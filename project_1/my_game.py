import math

import numpy as np
from numpy import random


def my_game(number: int = 1) -> int:
    count = 0
    predict = np.random.randint(1, 101)
    while number != predict:
        count += 1
        
        if number < predict and math.fabs(number-predict) >= 10:
            predict = (predict//10-1) * 10 
            if predict <= 0:
                continue
        elif number < predict and math.fabs(number-predict) < 10:
            predict -= 1
            
            
        elif number > predict and math.fabs(number-predict) >= 10:
            predict = (predict//10+1) * 10
        elif number > predict and math.fabs(number-predict) < 10:
            predict += 1
    return count



def score_game(my_game) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        my_game ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали списоконлайн переводчик чисел

    for number in random_array:
        count_ls.append(my_game(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")


if __name__ == '__main__':
    score_game(my_game)