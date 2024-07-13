class Person:
    """Класс для описания человека"""

    def __init__(self, name: str):
        """
        Конструктор класса

        :param name: Имя человека

        """
        self.__name = name


    @property # Свойство для получения имени
    def name(self):
        return self.__name

    @name.setter # Свойство для установки имени 
    def name(self, new_name):
        if len(new_name) <= 0 or not isinstance(new_name, str):
            raise ValueError("Имя должно быть строкой")
        self.__name = new_name


def main():
    person_pavel = Person("Павел")

    print(person_pavel.name)
    person_pavel.name = "asdasdasd"
    print(person_pavel.name)


if __name__ == "__main__":
    main()
