def guess_slow(target: int, low: int, high: int) -> tuple[int, int] | str:
    """
    Угадывает число с помощью алгоритма медленного перебора

    Параметры:
        target (int): Загаданное число, которое нужно угадать
        low (int): Нижняя граница диапазона поиска
        high (int): Верхняя граница диапазона поиска

    Результаты:
        tuple[int, int]: Кортеж (угаданное число, количество попыток) или str при отсутствии в диапазоне или неправильном типе данных

    Пример:
        guess_slow(7, 1, 10)
        (7, 7)
    """
    if type(target) != int:
        return 'Enter an integer'
    
    am_of_attempts = 0
    for guess in range(low, high + 1):
        am_of_attempts += 1
        if guess == target:
            return guess, am_of_attempts
    return 'Number is out of range'


def guess_binary(target: int, low: int, high: int) -> tuple[int, int] | str:
    """
    Угадывает число с помощью алгоритма бинарного поиска

    Параметры:
        target (int): Загаданное число, которое нужно угадать
        low (int): Нижняя граница диапазона поиска
        high (int): Верхняя граница диапазона поиска

    Результаты:
        tuple[int, int]: Кортеж (угаданное число, количество попыток) или str при отсутствии в диапазоне или неправильном типе данных

    Пример:
        guess_binary(7, 1, 10)
        (7, 4)
    """
    am_of_attempts = 0
    if type(target) != int:
        return 'Enter an integer'
    
    while low <= high:
        am_of_attempts += 1
        mid = (low + high) // 2
        if mid == target:
            return mid, am_of_attempts
        elif mid < target:
            low = mid + 1
        else:
            high = mid - 1
    return 'Number is out of range'


def main(target: int, low: int, high: int, var: str ="bin"):
    """
    Объединяет две функции guess_slow и guess_binary, даёт пользователю возможность выбрать между двумя

    Параметры:
        target (int): Загаданное число, которое нужно угадать
        low (int): Нижняя граница диапазона поиска
        high (int): Верхняя граница диапазона поиска
        var (str): Вариант функции

    Результаты:
        tuple[int, int]: Кортеж (угаданное число, количество попыток) или str при отсутствии в диапазоне

    Пример:
        main(7, 1, 10, 'slow')
        (7, 7)
    """
    if var == "bin":
        return guess_binary(target, low, high)
    elif var == "slow":
        return guess_slow(target, low, high)
    else:
        return 'Wrong function'

print(main(7, 1, 10, 'slow'))