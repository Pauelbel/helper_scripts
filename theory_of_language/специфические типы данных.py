from collections import deque
from collections import namedtuple
from collections import defaultdict
from collections import Counter

def main():
    names = ["John", "Paul", "Paul", "Paul", "Paul", "Ringo", "George", "Pete"]
    
    # frozenset - неизменяемое множество из уникальных имен
    frozen_names = frozenset(names)
    print(frozen_names)  # frozenset({'Pete', 'Paul', 'Ringo', 'John', 'George'})
    
    # deque - двусторонняя очередь
    deque_names = deque(names)
    last_value = deque_names.pop() # Получить крайнее правое значение списка = "Pete"
    deque_names.appendleft(last_value) # Добавить "Pete" в начало списка
    print(deque_names)
    
    # namedtuple
    Authors = namedtuple("Authors", ("name", "birth_year", "country"))
    authors = Authors(name="PAVEL", birth_year=2000, country="RUSSIA")
    print(authors)
    print(authors.name)
     
    # defaultdict - словарь с умолчанием
    def default_name():
        return "AAAAAAA"
    
    names_dict = defaultdict(default_name)
    names_dict["John"] = "John Doe"
    names_dict["Paul"] = "Paul McCartney"
    print(names_dict)

    # Counter
    word_counter = Counter()
    word_counter['John'] += 1
    word_counter['John'] += 2
    word_counter['John'] += 1
    word_counter['John'] += 6
    word_counter['апаппапапап'] += 40


    print(word_counter)
    print(word_counter.most_common(1)) # топ по вхождениюю слова


if __name__ == "__main__":
    main()
