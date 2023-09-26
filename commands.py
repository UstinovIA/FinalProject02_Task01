import os.path
from note import MyNote

path_file = "file.txt"
notes = []

def add(text):
    notes.append(MyNote(text))

def get_list_notes():
    print("Список заметок: ")
    for i, item in enumerate(notes):
        print(i+1, item.get_text(), "\nДата изменения: ", item.get_time_last_update())
    print()

def update(num, text):
    if 0 < num <= len(notes):
        MyNote.update(notes[num-1], text)
        return True
    else:
        return False
    

def delete(num):
    if 0 < num <= len(notes):
        notes.pop(num-1)
        return True
    else:
        return False

def sort_notes():
    notes.sort(key=MyNote.get_time_last_update) 
    
def open_file():
    if os.path.exists(path_file):
        file = open(path_file, 'r', encoding="utf-8")
        data = file.readlines()
        split_file(data)
        file.close()

def split_file(data):
    notes.clear()
    for item in data:
        item = item.replace("{", "")
        item = item.replace("}", "")
        item = item.replace("\n", "")
        temp = item.split(";")
        note = MyNote(temp[0], temp[1])
        notes.append(note)


def save_file():
    file = open(path_file, 'w', encoding="utf-8")
    for item in notes:
        file.write("{")
        file.write(item.get_text())
        file.write(";")
        file.write(item.get_time_last_update().isoformat())
        file.write("}")
        if item != notes[-1]:
            file.write("\n")
    file.close()
