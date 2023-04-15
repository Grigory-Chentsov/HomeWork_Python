""" Задача 38:
Дополнить телефонный справочник возможностью изменения и удаления данных. Пользователь также может ввести имя или
фамилию, и Вы должны реализовать функционал для изменения и удаления данных
 """


# функция для вывода данных
def display_contacts():
    with open("phonebook.txt", "r") as f:
        for line in f:
            print(line)


# функция для добавления контакта в файл
def save_contacts(contacts):
    with open(f"phonebook.txt", "a+") as f:
        for contact in contacts:
            f.write(f"{contact['Фамилия']},{contact['Имя']},{contact['Отчество']},{contact['Номер телефона']}\n")
    print("Данные успешно сохранены в файле.")


# функция для поиска данных из файла
def find_contacts(criterion, value):
    contacts = []
    with open("phonebook.txt", "r") as f:
        for line in f:
            fields = line.strip().split(",")
            contacts.append({
                "Фамилия": fields[0],
                "Имя": fields[1],
                "Отчество": fields[2],
                "Номер телефона": fields[3]
            })

    for contact in contacts:
        if contact[criterion] == value:
            record = f"{contact['Фамилия']} {contact['Имя']} {contact['Отчество']}: {contact['Номер телефона']}"
            print(record)


# функция для изменения записи по заданному критерию
def change_contact(criterion, value):
    contacts = []
    with open("phonebook.txt", "r") as f:
        for line in f:
            fields = line.strip().split(",")
            contacts.append({
                "Фамилия": fields[0],
                "Имя": fields[1],
                "Отчество": fields[2],
                "Номер телефона": fields[3]
            })

    for contact in contacts:
        if contact[criterion] == value:
            print("Изменить Фамилия, Имя, Отчество, Номер телефона")
            choice = input("Выберите изменение: ")
            contact[choice] = input("Введите новые данные: ")
    with open("phonebook.txt", "w+") as f:
        for contact in contacts:
            f.write(f"{contact['Фамилия']},{contact['Имя']},{contact['Отчество']},{contact['Номер телефона']}\n")
    print("Данные успешно изменены.")


# Функция для удаления контакта
def del_contact(criterion, value):
    contacts = []
    with open("phonebook.txt", "r") as f:
        for line in f:
            fields = line.strip().split(",")
            contacts.append({
                "Фамилия": fields[0],
                "Имя": fields[1],
                "Отчество": fields[2],
                "Номер телефона": fields[3]
            })

    for contact in contacts:
        index = contacts.index(contact)
        if contact[criterion] == value:
            contacts.pop(index)
    with open("phonebook.txt", "w+") as f:
        for contact in contacts:
            f.write(f"{contact['Фамилия']},{contact['Имя']},{contact['Отчество']},{contact['Номер телефона']}\n")
    print("Данные успешно удалены.")


# основная программа
contacts = []
while True:
    print("1. Вывести записи")
    print("2. Добавить запись")
    print("3. Найти записи")
    print("4. Изменить запись")
    print("5. Удалить запись из файла")
    print("6. Выйти")
    choice = input("Выберите действие: ")
    if choice == "1":
        display_contacts()
    elif choice == "2":
        second_name = input("Введите фамилию: ")
        name = input("Введите имя: ")
        surname = input("Введите отчество: ")
        phone = input("Введите номер телефона: ")
        contacts.append({
            "Фамилия": second_name,
            "Имя": name,
            "Отчество": surname,
            "Номер телефона": phone
        })
        save_contacts(contacts)
        print("Запись успешно добавлена.")
    elif choice == "3":
        criterion = input("Введите критерий поиска (Фамилия, Имя, Отчество или Номер телефона): ")
        value = input("Введите значение: ")
        find_contacts(criterion, value)
    elif choice == "4":
        criterion = input("Введите контакт изменения (Фамилия, Имя, Отчество или Номер телефона): ")
        value = input("Введите значение: ")
        change_contact(criterion, value)
    elif choice == "5":
        criterion = input("Введите контакт изменения (Фамилия, Имя, Отчество или Номер телефона): ")
        value = input("Введите значение: ")
        del_contact(criterion, value)
    elif choice == "6":
        break
    else:
        print("Некорректный ввод")
