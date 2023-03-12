# -*- coding: utf8 -*-
import os
from Note import Note

class Notes():

    def __init__(self):
        self.notes = self.new_notes()

    def add_note(self, note):
        with open("file_notes.csv", "r") as f:
            self.notes = f.readlines()
            self.notes.append(note)
        with open("file_notes.csv", "w") as f:
            for c in self.notes:
                f.write(str(c))

    def new_notes(self):
        with open("file_notes.csv", 'r') as file:
            new_notes = []
            if os.stat('file_notes.csv').st_size == 0:
                print("Заметок пока нет.")
                return new_notes
            else:
                for i in file:
                    note = Note(i.split(';')[0], i.split(';')[1], i.split(';')[2], i.split(';')[3], i.split(';')[4])
                    new_notes.append(note)
                return new_notes

    def get_info(self, idx):
        with open("file_notes.csv", 'r') as file:
            for i in file.readlines():
                if int(i.partition(';')[0]) == idx:
                    return i

    def get_note(self, idx):
        return self.new_notes()[idx]

    def save(self, char):
        with open("file_notes.csv", char) as file:
            for i in self.notes:
                file.write(i)

    def get_len(self):
        return len(self.notes)

    def idx(self):
        with open("file_notes.csv", 'r') as file:
            id = 0
            for i in file.readlines():
                if id < int(i.partition(';')[0]):
                    id = int(i.partition(';')[0])
            return id + 1


    def delete_note(self, idx):
        with open("file_notes.csv", "r") as f:
            lines = f.readlines()
        with open("file_notes.csv", "w") as f:
            for line in lines:
                if line.partition(';')[0] not in str(idx):
                    f.write(line)
                if line.partition(';')[0] in str(idx):
                    print('Заметка удалена')


    def modified_note(self, idx, note):
        with open("file_notes.csv", "r") as f:
            lines = f.readlines()
            for line in lines:
                if line.partition(';')[0] == str(idx):
                    lines.insert(lines.index(line), str(note))
                    lines.pop(lines.index(line))
        with open("file_notes.csv", 'w') as file:
            for line in lines:
                file.write(str(line))

    def sorted(self, bool):
        with open("file_notes.csv", 'r') as file:
            notes = []
            for i in file.readlines():
                notes.append(Note(i.split(';')[0], i.split(';')[1], i.split(';')[2], i.split(';')[3], i.split(';')[4]))
            notes.sort(key=lambda Note: Note.creat_data  , reverse=bool)
            notes.sort(key=lambda Note: Note.creat_time, reverse=bool)
            for s in notes:
                print('ID:', s.id, '\n')
                print('Название:', s.name, '\n')
                print('Текст:', s.body, '\n')
                print('Дата и время последнего изменения:', s.creat_data, s.creat_time)
                print('----------------------------------------------------------------')

    def __str__(self):
        with open("file_notes.csv", 'r') as file:
            for i in file.readlines():
                print('ID:', i.split(';')[0], '\n')
                print('Название:', i.split(';')[1], '\n')
                print('Текст:', i.split(';')[2], '\n')
                print('Дата и время последнего изменения:', i.split(';')[3], i.split(';')[4])
                print('----------------------------------------------------------------')
