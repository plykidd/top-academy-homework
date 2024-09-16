
import json


def load_data(file_name):
    try:
        with open(file_name, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return []


def save_data(file_name, data):
    with open(file_name, 'w') as file:
        json.dump(data, file)


def add_employee(data):
    name = input("Введите имя сотрудника: ")
    surname = input("Введите фамилию сотрудника: ")
    age = int(input("Введите возраст сотрудника: "))
    employee = {
        "name": name,
        "surname": surname,
        "age": age
    }
    data.append(employee)
    print("Сотрудник успешно добавлен!")


def edit_employee(data):
    surname = input("Введите фамилию сотрудника для редактирования: ")
    for employee in data:
        if employee["surname"] == surname:
            employee["name"] = input("Введите новое имя сотрудника: ")
            employee["age"] = int(input("Введите новый возраст сотрудника: "))
            print("Данные сотрудника успешно обновлены!")
            return
    print("Сотрудник с указанной фамилией не найден!")


def delete_employee(data):
    surname = input("Введите фамилию сотрудника для удаления: ")
    for employee in data:
        if employee["surname"] == surname:
            data.remove(employee)
            print("Сотрудник успешно удален!")
            return
    print("Сотрудник с указанной фамилией не найден!")


def search_by_surname(data):
    surname = input("Введите фамилию сотрудника для поиска: ")
    found_employees = [employee for employee in data if employee["surname"] == surname]
    if found_employees:
        print("Найденные сотрудники:")
        for employee in found_employees:
            print(f"Имя: {employee['name']}, Возраст: {employee['age']}")
    else:
        print("Сотрудник с указанной фамилией не найден!")


def search_by_age(data):
    age = int(input("Введите возраст для поиска сотрудников: "))
    found_employees = [employee for employee in data if employee["age"] == age]
    if found_employees:
        print("Найденные сотрудники:")
        for employee in found_employees:
            print(f"Имя: {employee['name']}, Фамилия: {employee['surname']}")
    else:
        print("Сотрудники указанного возраста не найдены!")


def search_by_letter(data):
    letter = input("Введите букву для поиска сотрудников с фамилией, начинающейся на нее: ")
    found_employees = [employee for employee in data if employee["surname"].startswith(letter)]
    if found_employees:
        print("Найденные сотрудники:")
        for employee in found_employees:
            print(f"Имя: {employee['name']}, Возраст: {employee['age']}")
    else:
        print("Сотрудники с указанной буквой в фамилии не найдены!")


def main():
    file_name = "employees.json"
    employees_data = load_data(file_name)

    while True:
        print("\n=== Информационная система 'Сотрудники' ===")
        print("1. Добавить сотрудника")
        print("2. Редактировать данные сотрудника")
        print("3. Удалить сотрудника")
        print("4. Поиск сотрудника по фамилии")
        print("5. Поиск сотрудников по возрасту")
        print("6. Поиск сотрудников по первой букве фамилии")
        print("7. Вывести информацию обо всех сотрудниках")
        print("0. Сохранить и выйти")

        choice = input("Введите номер команды: ")

        if choice == "1":
            add_employee(employees_data)
        elif choice == "2":
            edit_employee(employees_data)
        elif choice == "3":
            delete_employee(employees_data)
        elif choice == "4":
            search_by_surname(employees_data)
        elif choice == "5":
            search_by_age(employees_data)
        elif choice == "6":
            search_by_letter(employees_data)
        elif choice == "7":
            print("Список всех сотрудников:")
            for employee in employees_data:
                print(f"Имя: {employee['name']}, Фамилия: {employee['surname']}, Возраст: {employee['age']}")
        elif choice == "0":
            save_data(file_name, employees_data)
            print("Данные успешно сохранены. Выход из программы.")
            break
        else:
            print("Некорректный ввод. Попробуйте снова.")


if __name__ == "__main__":
    main()
