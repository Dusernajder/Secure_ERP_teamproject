from model.hr import hr
from view import terminal as view
from model import data_manager
from datetime import datetime


def list_employees():
    employees = data_manager.read_table_from_file(hr.DATAFILE)
    view.print_table(employees, hr.HEADERS)


def add_employee():
    all_employees = data_manager.read_table_from_file(hr.DATAFILE)
    all_employees.append(view.get_inputs(['ID', 'user_name', 'birth_date', 'department', 'clearance']))
    data_manager.write_table_to_file(hr.DATAFILE, all_employees)


def update_employee():
    employees = data_manager.read_table_from_file(hr.DATAFILE)
    for index, employee in enumerate(employees, 1):
        print(f'{index}. {", ".join(employee)}')

    employee = int(view.get_input('Which employee do you want to update? Select number: '))

    for index, data in enumerate(employees[employee-1], 1):
        print(f'{index}. {data}')

    employee_data = int(view.get_input('Which data to update? Select a number: '))
    updated_data = view.get_input('Enter the data')

    employees[employee-1][employee_data-1] = updated_data
    data_manager.write_table_to_file(hr.DATAFILE, employees)


def delete_employee():
    employees = data_manager.read_table_from_file(hr.DATAFILE)
    for index, employee in enumerate(employees, 1):
        print(f'{index}. {", ".join(employee)}')

    employee = int(view.get_input('Which employee do you want to delete? Select a number: '))
    employees.remove(employees[employee-1])

    data_manager.write_table_to_file(hr.DATAFILE, employees)


def get_oldest_and_youngest():
    employees = data_manager.read_table_from_file(hr.DATAFILE)
    year_index = 2
    sorted_key = lambda num: (int(num[year_index][:4]), int(num[year_index][5:7]), int(num[year_index][8:10]))
    sorted_departments = sorted([x for x in employees], key=sorted_key, reverse=False)
    oldest = sorted_departments[0][1]
    youngest = sorted_departments[-1][1]
    print(f'The oldest employee is: {oldest}')
    print(f'The youngest employee is: {youngest}')
    print(sorted_departments)


def get_average_age():
    current_date = datetime.today().strftime('%Y-%m-%d')
    date_format = '%Y-%m-%d'

    employees = data_manager.read_table_from_file(hr.DATAFILE)
    year_index = 2
    list_of_ages = []
    for employee in employees:
        employee_age = datetime.strptime(employee[year_index], date_format)
        today = datetime.strptime(current_date, date_format)
        difference = today - employee_age
        list_of_ages.append(int(difference.days//365.25))

    average = sum(list_of_ages)//len(list_of_ages)
    print(f' The average age of employees is: {average}')


def next_birthdays():
    month_and_days = {'1': 31, '2': 28, '3': 31, '4': 30, '5': 31, '6': 30, '7': 31, '8': 31, '9': 30, '10': 31,
                      '11': 30, '12': 31}
    birthday_check = view.get_input('Enter month and day in "mm-dd" format: ')

    month = int(birthday_check.split('-')[0])
    day = int(birthday_check.split('-')[1])

    input_sum_days = sum(month_and_days[str(i)] for i in range(1, month))
    input_sum_days += day

    employees = data_manager.read_table_from_file(hr.DATAFILE)

    for employee in employees:
        employee_month = int(employee[2].split('-')[1])
        employee_day = int(employee[2].split('-')[2])

        employee_sum_day = sum(month_and_days[str(i)] for i in range(1, employee_month))
        employee_sum_day += employee_day

        minus_two_weeks = input_sum_days - 14
        plus_two_weeks = input_sum_days + 14
        person_name = employee[1]

        if employee_sum_day in range(minus_two_weeks, plus_two_weeks+1):
            print(person_name)


def count_employees_with_clearance():
    employees = data_manager.read_table_from_file(hr.DATAFILE)
    clearance_index = 4
    clearances = [people[clearance_index] for people in employees]

    clearance_dict = {}
    for i in clearances:
        if i in clearance_dict:
            clearance_dict[i] += 1
        else:
            clearance_dict[i] = 1

    input_level = int(view.get_input('Enter the clearance level: '))
    print(sum(int(clearance_dict[level]) for level in clearance_dict if int(level) >= input_level))


def count_employees_per_department():
    employees = data_manager.read_table_from_file(hr.DATAFILE)
    department_index = 3
    departments = [people[department_index] for people in employees]

    department_dict = {}
    for i in departments:
        if i in department_dict:
            department_dict[i] += 1
        else:
            department_dict[i] = 1

    sorted_departments = sorted([x for x in department_dict.items()], key=lambda num: num[1], reverse=True)
    department_index = 0
    number_index = 1
    for i in range(len(sorted_departments)):
        print(f'The {sorted_departments[i][department_index]} department has {sorted_departments[i][number_index]} employee(s)')


def run_operation(option):
    if option == 1:
        list_employees()
    elif option == 2:
        add_employee()
    elif option == 3:
        update_employee()
    elif option == 4:
        delete_employee()
    elif option == 5:
        get_oldest_and_youngest()
    elif option == 6:
        get_average_age()
    elif option == 7:
        next_birthdays()
    elif option == 8:
        count_employees_with_clearance()
    elif option == 9:
        count_employees_per_department()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List employees",
               "Add new employee",
               "Update employee",
               "Remove employee",
               "Oldest and youngest employees",
               "Employees average age",
               "Employees with birthdays in the next two weeks",
               "Employees with clearance level",
               "Employee numbers by department"]
    view.print_menu("Human resources", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
