from model import util
from model.crm import crm
from view import terminal as view
from model import data_manager as manager


def list_customers():
    # TODO: Awaiting for view.terminal.print_table to be done, until then it remains wrecked.
    try:
        customers = manager.read_table_from_file(crm.DATAFILE)
        print('Customers:')
        util.generate_id()
        for customer in customers:
            subscribed = 'yes' if customer[3] == '1' else 'no'

            table = (f"  id - {customer[0]}\n"
                     f"  email - {customer[2]}\n"
                     f"  subscribed - {subscribed}")

            print(customer[1])
            print(table)

    except:
        view.print_error_message("Something went wrong.")


def add_customer():
    try:
        customers = manager.read_table_from_file(crm.DATAFILE)
        labels = ["Name", "Email", "Subscribed"]
        data = view.get_inputs(labels)
        data.insert(0, util.generate_id())
        customers.append(data)
        manager.write_table_to_file(crm.DATAFILE, customers)
    except:
        view.print_error_message("Something went wrong.")


def update_customer():
    try:
        customers = manager.read_table_from_file(crm.DATAFILE)
        name = view.get_input('Name')
        list_options = ['email', 'subscription']
        view.print_menu('Options', list_options)
        option = int(view.get_input('Select module')) + 2

        for customer in customers:
            if customer[1] == name:
                customer[option] = view.get_input(customer[option])

        manager.write_table_to_file(crm.DATAFILE, customers)
    except:
        view.print_error_message("Something went wrong.")


def delete_customer():
    try:
        customers = manager.read_table_from_file(crm.DATAFILE)
        name = view.get_input('Name')

        for customer in customers:
            if customer[1] == name:
                customers.remove(customer)
                break

        manager.write_table_to_file(crm.DATAFILE, customers)
    except:
        view.print_error_message("Something went wrong.")


def get_subscribed_emails():
    try:
        customers = manager.read_table_from_file(crm.DATAFILE)
        subscribed = []

        for customer in customers:

            if customer[3] == '1':
                table = (f"name: {customer[1]}\n"
                         f"  email - {customer[2]}")
                print(table)

    except:
        view.print_error_message("Something went wrong.")


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
