from commands import *

def menu_start():
    open_file()
    while True:
        text_menu = ("1. Добавить заметку\n"
                    "2. Редактировать заметку\n"
                    "3. Удалить заметку\n"
                    "4. Список заметок\n"
                    "5. Сортировать список заметок по дате изменения\n"
                    "6. Выход\n")
        print(text_menu)
        choice = input("Введите номер команды: ")
        match choice:
            case "1":
                add(input("Введите текст заметки: "))
            case "2":
                get_list_notes()
                num = input("Введите номер заметки: ")
                if num.isdigit():
                    num = int(num)
                    text = input("Введите новый текст заметки: ")
                    if not update(num, text):
                        print("Введено некорректное значение!")
                    else:
                        print("Заметка успешно отредактирована")
                else:
                    print("Введено некорректное значение!")
            case "3":
                get_list_notes()
                num = input("Введите номер заметки: ")
                if num.isdigit():
                    num = int(num)
                    if not delete(num):
                        print("Введено некорректное значение!")
                    else:
                        print("Заметка успешно удалена")
                else:
                    print("Введено некорректное значение!")
            case "4":
                get_list_notes()
            case "5":
                sort_notes()
            case "6":
                save_file()
                break
            case default:
                print("Введено некорректное значение!")