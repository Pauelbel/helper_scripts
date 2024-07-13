class Person:
    """Класс для описания человека"""

    def __init__(self, name: str, age: int, profession: str):
        """
        Конструктор класса

        :param name: Имя человека
        :param age: Возраст человека лет в годах
        :param profession: Пол человека
        """
        self.name = name
        self.__age = age
        self.__profession = profession

    def say_hello(self):
        """Метод для печати приветствия"""
        print(
            f"\nПривет, меня зовут {self.name}, мне {self.__age} лет, я {self.__profession}."
        )

    def change_profession(self, new_profession: str):
        """
        Смена профессии человека

        :param new_profession: Новая профессия человека
        """
        print(f"я изменил профессию {self.__profession} на {new_profession}.")
        self.__profession = new_profession



def main():
    person_pavel = Person("Павел", 30, "QA Engineer")
    person_pavel.say_hello()
    person_pavel.change_profession("Долларовый миллионер")
    person_pavel.say_hello()


if __name__ == "__main__":
    main()
