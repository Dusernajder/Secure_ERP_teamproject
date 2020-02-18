from model.hr import hr
from view import terminal as view
from model import data_manager


def list_employees():
    employees = data_manager.read_table_from_file(hr.DATAFILE)
    print(employees)
    return employees


def add_employee():
    all_employees = list_employees()
    all_employees.append(view.get_inputs(['ID', 'user_name', 'birth_date', 'department', 'clearance']))
    data_manager.write_table_to_file(hr.DATAFILE, all_employees)


def update_employee():
    employees = list_employees()
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
    employees = list_employees()
    for index, employee in enumerate(employees, 1):
        print(f'{index}. {", ".join(employee)}')

    employee = int(view.get_input('Which employee do you want to delete? Select a number: '))
    employees.remove(employees[employee-1])

    data_manager.write_table_to_file(hr.DATAFILE, employees)


def get_oldest_and_youngest():
    employees = list_employees()

    view.print_error_message("Not implemented yet.")


def get_average_age():
    view.print_error_message("Not implemented yet.")


def next_birthdays():
    view.print_error_message("Not implemented yet.")


def count_employees_with_clearance():
    clearance_index = 4
    clearances = [people[clearance_index] for people in list_employees()]

    clearance_dict = {}
    for i in clearances:
        if i in clearance_dict:
            clearance_dict[i] += 1
        else:
            clearance_dict[i] = 1

    input_level = int(view.get_input('Enter the clearance level: '))
    print(sum(int(clearance_dict[level]) for level in clearance_dict if int(level) >= input_level))


def count_employees_per_department():
    department_index = 3
    departments = [people[department_index] for people in list_employees()]

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
