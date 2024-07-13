def log_function_using(fuctor):

    def decorate(val):
        print("Функция была вызвана")
        result = fuctor(val)
        print(f"Функция была завершена. Результат: {result}")

        return result

    return decorate


@log_function_using
def inc_expireince(old_value):
    return old_value + 1


def main():
    exp = 6
    exp = inc_expireince(exp)
    print(f"Значение exp после изменения: {exp}")


if __name__ == "__main__":
    main()
