def my_test_function(first_arg, second_arg: int = 0):
    """ 
    Тестовый текст
    :param first_arg: Первый аргумент
    :second_arg: Второй аргумент
    """
    print(first_arg, second_arg)

my_test_function(1, 2)
my_test_function(1)
my_test_function(1, second_arg=2)
my_test_function(first_arg=1, second_arg=2)