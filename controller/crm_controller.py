from model import util
from model.crm import crm
from view import terminal as view
from model import data_manager as manager


def list_customers():
    try:
        customers = manager.read_table_from_file(crm.DATAFILE)
        return [customer[1] for customer in customers]
    except:
        view.print_error_message("Not implemented yet.")


def add_customer():
    try:
        customers = manager.read_table_from_file(crm.DATAFILE)
        labels = ["Name", "Email", "Subscribed"]
        data = view.get_inputs(labels)
        data.insert(0, util.generate_id())
        customers.append(data)
        # print(customers)
        manager.write_table_to_file(crm.DATAFILE, customers)
    except:
        view.print_error_message("Not implemented yet.")


def update_customer():
    try:
        customers = manager.read_table_from_file(crm.DATAFILE)
        name = view.get_input('Name')
        list_options = ['email', 'subscription']
        view.print_menu('Options', list_options)
        option = int(view.get_input('Select module')) + 2
    except:
        view.print_error_message("Not implemented yet.")


def delete_customer():
    view.print_error_message("Not implemented yet.")


def get_subscribed_emails():
    try:
        customers = manager.read_table_from_file(crm.DATAFILE)
        subscribed = []
        for customer in customers:
            if customer[3] == '1':
                subscribed.append(customer[2])
        print(subscribed)
    except:
        view.print_error_message("Not implemented yet.")


def run_operation(option):
    if option == 1:
        list_customers()
    elif option == 2:
        add_customer()
    elif option == 3:
        update_customer()
    elif option == 4:
        delete_customer()
    elif option == 5:
        get_subscribed_emails()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List customers",
               "Add new customer",
               "Update customer",
               "Remove customer",
               "Subscribed customer emails"]
    view.print_menu("Customer Relationship Management", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
