def generate_sequence(max_value=50):
    """Функция генерации последовательности чисел от 0 до max_value + 1"""
    values = []
    for number in range(0, max_value + 1):

        # Если использовать этот блок кода то при большом max_value может не хватить оперативной памяти
        #     values.append(number)
        # return values

        # Правильно использовать итерацию с использованием генератора
        yield number

def add_two(value):
    return value + 2

def main():
    values_list = [add_two(number) for number in generate_sequence() if number % 2 == 0]
    values_dict = {add_two(number): number for number in generate_sequence() if number % 2 == 0}
    print(values_list)
    print(values_dict)


if __name__ == "__main__":
    main()
