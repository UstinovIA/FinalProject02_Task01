import os.path

path_file = "file.txt"
notes = []

def add(text):
    notes.append(text)

def get_list_notes():
    print("Список заметок: ")
    for i, item in enumerate(notes):
        print(i+1, item)
    print()

def update(num, text):
    if 0 < num <= len(notes):
        notes[num-1] = text
        return True
    else:
        return False
    

def delete(num):
    if 0 < num <= len(notes):
        notes.pop(num-1)
        return True
    else:
        return False
    
def open_file():
    if os.path.exists(path_file):
        file = open(path_file, '', encoding="utf-8")
        data = file.read()
        if data != "":
            notes.clear()
            for i in data.split("\n"):
                notes.append(i)
            file.close()

def save_file():
    file = open(path_file, 'w', encoding="utf-8")
    for item in notes:
        file.write(item)
        if item != notes[-1]:
            file.write("\n")
    file.close()
