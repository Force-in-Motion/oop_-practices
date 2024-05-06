#
# class Animal:
#     def __init__(self, name: str, type: str, age: int, sound: str):
#         """
#         Формирует шаблон объекта Animal
#         :param name: Пренимает имя животного
#         :param type: Пренимает вид животного
#         :param age: Пренимает возраст животного
#         :param sound: Пренимает звук, создаваемый животным
#         """
#         self.name = name
#         self.type = type
#         self.age = age
#         self.sound = sound
#
#     def print_sound_animal(self):
#         """
#         Выводит в консоль строку с принятым иенем животного его типом и звуком который оно издает
#         :return:
#         """
#         print(f'{self.type} с именем {self.name} издает звук: {self.sound}')
#         print()
#
#     def print_info_animal(self):
#         """
#         Выводит в консоль всю информацию о животном в созданном объекте на базе класса Animal
#         :return:
#         """
#         print(f'Информационный блок о созданном вами животном :'
#               f'\nВид животного : {self.type}'
#               f'\nИмя животного : {self.name}'
#               f'\nВозраст животного: {self.age}'
#               f'\nЗвук который издает животное: {self.sound}')
#         print()
#
#
# dog = Animal('Шнырь', 'Пес', 7, 'Рррррааааааввв Рррррааааааввв')
#
# dog.print_info_animal()
# dog.print_sound_animal()


class Book:

    def __init__(self, name: str, author: str, count_pages: int):
        """
        Формирует шаблон объекта Book
        :param name: Пренимает название книги
        :param author: Пренимает автора книги
        :param count_pages: Пренимает количество страниц книги
        """
        self.name = name
        self.author = author
        self.count_pages = count_pages

    def open_page(self):
        """
        Выполняет проверки и если они пройдены выводит строку- открылась страница или нет
        :return:
        """
        number_page = int(input('Введите номер страницы, которую требуется открыть >> '))

        if number_page <= self.count_pages and number_page > 0:
            print('Страница в вашей книге найдена и открыта')
            print()
        else:
            print('Номер указанной страницы в вашей книге отсутствует')
            print()


    def print_book_info(self):
        """
        Выводит в консоль всю информацию о книге в созданном объекте на базе класса Book
        :return:
        """
        print(f'Информационный блок о вашей книге :'
              f'\nНазвание книги: {self.name}'
              f'\nАвтор книги: {self.author}'
              f'\nКоличество страниц: {self.count_pages}')
        print()

war_and_world = Book('Война и мир', 'Лев Толстой', 1300)
war_and_world.open_page()
war_and_world.print_book_info()
