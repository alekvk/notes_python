from datetime import datetime
import Notes
from Notes import Note

def display_notes():
    array = read_file()
    print("Список заметок:")
    for i in array:
        print(i)


def add_note(heading, body):
    array = read_file()
    id_ = get_id(array)
    time = str(datetime.now())
    note = Note(id_, heading, body, time)
    array.append(note)
    write_file(array, 'a')
    print("Заметка добавлена")


def update_note(id_, heading, body):
    array = read_file()
    time = str(datetime.now())
    for i in array:
        if i.get_id() == id_:
            i.set_heading(heading)
            i.set_body(body)
            i.set_timedate(str(datetime.now()))
    write_file(array, 'a')
    print("Заметка изменена")



def remove_note(id_):
    array = read_file()
    n = 0
    for i in array:
        if i.get_id() == id_:
            n = 1
            array.remove(i)
            write_file(array, 'a')
            print("Заметка удалена")
    if n == 0:
        print("Заметка с указанным идентификатором не найдена")

def show_note(id_):
    array = read_file()
    result = []
    for i in array:
       if i.get_id() == id_:
            result.append(i)
    if len(result) == 0:
        print("Отсутствует заметка с заданным идентификатором")
    else:
        for i in result:
            print(i)

def show_note_timedate(timedate):
    array = read_file()
    result = []
    for i in array:
        if (i.get_timedate())[0:10] == timedate:
            result.append(i)
    if len(result) == 0:
        print("Отсутствуют заметки с указанным временем создания(изменения)")
    else:
        for i in result:
            print(i)

def read_file():
    try:
        array = []
        file = open("notes.csv", "r", encoding = 'utf-8')
        notes = file.read().strip().split("\n")
        for n in notes:
            split_n = n.split(';')
            note = Note(split_n[0], split_n[1], split_n[2], split_n[3])
            array.append(note)
    except Exception:
        print('Нет сохраненных заметок...')
    finally:
        return array


def write_file(array, mode):
    file = open("notes.csv", mode='w', encoding='utf-8')
    file.seek(0)
    file.close()
    file = open("notes.csv", mode=mode, encoding='utf-8')
    for notes in array:
        file.write(Note.to_string(notes))
        file.write('\n')


def get_id(array):
    if len(array) == 0:
        return "1"
    else:
        array_int = []
        for i in array:
            j = int(i.get_id())
            array_int.append(j)
        return str(max(array_int) + 1)
