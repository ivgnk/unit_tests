def factorial(number:int):
    '''
    Только для тестирования: вычисление факториала,
    https://it-start.online/articles/3-sposoba-vychislit-faktorial-v-python
    '''
    factorial = 1
    while number > 1:
        factorial = factorial * number
        number = number - 1
    return factorial