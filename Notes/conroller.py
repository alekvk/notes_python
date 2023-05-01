import sys

from Notes import Note
import view as v

# Необходимо написать проект, содержащий функционал работы с заметками.
# Программа должна уметь создавать заметку, сохранять её, читать список
# заметок, редактировать заметку, удалять заметку.


def start():
    input_user = ''
    while input != '7':
        v.menu()
        input_user = input().strip()
        if input_user == '1':
            m.display_notes()
        elif input_user == '2':
            headnote = input("Введите заголовок заметки: ")
            bodynote = input("Введите текст заметки: ")
            m.add_note(headnote, bodynote)
        elif input_user == '3':
            id_ = input("Введите идентификатор обновляемой заметки ")
            headnote = input("Введите заголовок заметки: ")
            bodynote = input("Введите текст заметки: ")
            m.update_note(id_, headnote, bodynote)
        elif input_user == '4':
            id_ = input("Введите идентификатор удаляемой заметки ")
            m.remove_note(id_)
        elif input_user == '5':
            id_ = input("Введите идентификатор заметки ")
            m.show_note(id_)
        elif input_user == '6':
            id_ = input("Введите дату создания(изменения) заметки в формате yyyy-mm-dd ")
            m.show_note_timedate(id_)
        elif input_user == '7':
            sys.exit("Работа программы завершена")
        else:
            print("Необходимо ввести пункт в диапазоне от 1 до 7")














