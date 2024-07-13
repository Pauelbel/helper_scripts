class Person:
    """Класс для описания человека"""

    def __init__(self, name: str):
        """
        Конструктор класса

        :param name: Имя человека

        """
        self.__name = name

    @property  # Свойство для получения имени
    def name(self):
        return self.__name

    @name.setter  # Свойство для установки имени
    def name(self, new_name):
        if len(new_name) <= 0 or not isinstance(new_name, str):
            raise ValueError("Имя должно быть строкой")
        self.__name = new_name


class PersonDev(Person):

    def __init__(self, name: str, favorite_language: str):
        """
        Конструктор класса

        :param name: Имя человека
        :param favorite_language: Любимый язык программирования
        """
        super().__init__(name)
        self.__favorite_language = favorite_language

    def write_programm(self, code_row_count: int):
        print(
            f" я {self.name}, пишу код на {code_row_count} строк с помощью {self.__favorite_language}..."
        )


def main():
    person_toma = PersonDev("Тома", "Python")
    print(person_toma.name)
    print(person_toma.write_programm(666))


if __name__ == "__main__":
    main()
