# Напишите информационную систему «Сотрудники».
# Программа должна обеспечивать ввод данных, редактирование данных сотрудника,
# удаление сотрудника, поиск
# сотрудника по фамилии, вывод информации обо всех
# сотрудниках, указанного возраста, или фамилия которых
# начинается на указанную букву. Организуйте возможность
# сохранения найденной информации в файл. Также весь
# список сотрудников сохраняется в файл (при выходе из
# программы — автоматически, в процессе исполнения
# программы — по команде пользователя). При старте
# программы происходит загрузка списка сотрудников из
# указанного пользователем файла


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


def add_employees(data):
    name = input("Enter your name: ")
    surname = input("Enter your surname: ")
    age = input("Enter your age: ")
    employee = {
        "Name": name,
        "Surname": surname,
        "Age": age
    }
    data.append(employee)
    print('Employee added')


def edit_employees(data):
    surname = input("Enter your surname: ")
    for employee in data:
        if employee["Surname"] == surname:
            employee['Name'] = input("Enter your new name: ")
            employee['Age'] = input("Enter your new age: ")
            print('Employee updated')
            return employee
        else:
            print('Employee not found')

def delete_employees(data):
    surname = input("Enter your surname: ")
    for employee in data:
        if employee["Surname"] == surname:
            data.remove(employee)
            print('Employee deleted')
            return employee
        else:
            print('Employee not found')


def search_employees_surname(data):
    surname = input("Enter your surname: ")
    for employee in data:
        if employee["Surname"] == surname:
            print(f'{employee} Employee found')
            return employee
        else:
            print('Employee not found')


def search_employees_age(data):
    age = input("Enter your age: ")
    for employee in data:
        found_employee = [employee for employee in data if employee["Age"] == age]
        if found_employee:
            print(f'{employee} Employee found')
            return employee
        else:
            print('Employee not found')


def search_employees_letter(data):
    letter = input("Enter your letter: ")
    found_employee = [employee for employee in data if employee['Surname'].startswith(letter)]
    if found_employee:
        print('Employee found')
        for employee in found_employee:
            print(f'{employee} Employee found')
            return employee
    else:
        print('Employee not found')

def main():
    file_name = 'employees.json'
    employees_data = load_data(file_name)

    while True:
        print('1. Add employees')
        print('2. Edit employees')
        print('3. Delete employees')
        print('4. Search employees surname')
        print('5. Search employees age')
        print('6. Search employees letter')
        print('7. Print all employees')
        print('0. Exit')

        choice = input('Enter your choice: ')

        if choice == '1':
            add_employees(employees_data)
        elif choice == '2':
            edit_employees(employees_data)
        elif choice == '3':
            delete_employees(employees_data)
        elif choice == '4':
            search_employees_surname(employees_data)
        elif choice == '5':
            search_employees_age(employees_data)
        elif choice == '6':
            search_employees_letter(employees_data)
        elif choice == '7':
            for employee in employees_data:
                print(f'{employee} Employee found')
        elif choice == '0':
            save_data(file_name, employees_data)
            print('Data saved')
            break
        else:
            print('Invalid choice')

print(main())







