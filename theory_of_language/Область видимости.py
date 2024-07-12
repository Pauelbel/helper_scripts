var = "global"


def main():

    var = "local"
    print(var)  # 1 - local (локальная область видимости)

    def sub_main():
        nonlocal var  # теперь это ссылается на var из main()
        var = "sub_local"
        print(var)  # 2 - sub_local (измененная локальная переменная main)

    sub_main()
    print(var)  # будет выводить "sub_local", так как var была изменена в sub_main


if __name__ == "__main__":
    main()
    print(var)  # 3 - global (глобальная область видимости)

#добавь функцию для сложения двух чисел

