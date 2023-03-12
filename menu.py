# -*- coding: utf8 -*-

from Notes import Notes
from Note import Note
from data_time import data_time


class Menu(data_time):

    def __init__(self):
        self.__notes = Notes()

    def main_menu(self):
        while True:

            print("Меню :\n" +
                  "\t1. Показать все заметки;\n" +
                  "\t2. Найти заметку по индексу;\n" +
                  "\t3. Добавить новую заметку;\n" +
                  "\t4. Изменить заметку;\n" +
                  "\t5. Удалить заметку;\n" +
                  "\t6. Сортировать по дате(возрастание);\n" +
                  "\t7. Сортировка по дате(убывание).\n" +
                  "\t8. Выход.\n" +
                  "\n***Введите ваш выбор ----->> ")
            try:
                choice = int(input())
                match choice:
                    case 1:
                        self.__notes.__str__()
                    case 2:
                        idx = int(input("Введите ID заметки: "))
                        print(self.__notes.get_info(idx))
                    case 3:
                        print("Создание новой заметки... ")
                        name = input("Введите имя заметки: ")
                        body = input("Введите текст заметки: ")
                        data = data_time.creat_data(self)
                        time = data_time.creat_time(self)
                        self.__notes.add_note(Note(self.__notes.idx(), name, body, data, time))
                    case 4:
                        self.__notes.__str__()
                        idx = int(input("Введите индекс заметки, которую хотите изменить:  "))
                        print(self.__notes.get_info(idx))
                        name = input("Введите новое имя: ")
                        body = input("Введите новый текст: ")
                        data = data_time.creat_data(self)
                        time = data_time.creat_time(self)
                        self.__notes.modified_note(idx, Note(idx, name, body, data, time))
                    case 5:
                        idx = int(input("Введите ID заметки, для её удаления: "))
                        self.__notes.delete_note(idx)
                    case 6:
                        print("Сортировка по возрастанию")
                        print("Сортировка завершена")
                        self.__notes.sorted(False)
                    case 7:
                        print("Сортировка по убиванию")
                        print("Сортировка завершена")
                        self.__notes.sorted(True)
                    case 8:
                        break
            except (Exception):
                print('Возника ошибка при выполнении операции. Повторите действие.')
