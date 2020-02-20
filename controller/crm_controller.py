from model import util
from model.crm import crm
from view import terminal as view
from model import data_manager as manager


def list_customers():
    """ Print customers """

    try:
        customers = manager.read_table_from_file(crm.DATAFILE)
        view.print_table(customers, crm.HEADERS)
    except:
        view.print_error_message("Something went wrong.")


def add_customer():
    """ Add a customer to the crm.csv file """

    try:
        customers = manager.read_table_from_file(crm.DATAFILE)
        # Necessary information of the customer
        labels = ["Name", "Email", "Subscribed"]
        # Ask series of inputs (labels)
        data = view.get_inputs(labels)

        # For input use words instead of digits
        if data[2] == 'yes':
            data[2] = '1'
        elif data[2] == 'no':
            data[2] = '0'

        # Put id beginning of the line
        data.insert(0, util.generate_id())
        customers.append(data)
        manager.write_table_to_file(crm.DATAFILE, customers)
    except:
        view.print_error_message("Something went wrong.")


def update_customer():
    """ Update customers information (email, subs) """

    try:
        customers = manager.read_table_from_file(crm.DATAFILE)

        # Get ID as input
        id = view.get_input('Customer id')
        # Options to change
        list_options = ['email', 'subscription']

        view.print_menu('Options', list_options)
        # Selected option from list_options
        option = int(view.get_input('Select module')) + 2

        for customer in customers:
            if customer[0] == id:
                # Update option
                customer[option] = view.get_input(customer[option])

        # Write file
        manager.write_table_to_file(crm.DATAFILE, customers)
    except:
        view.print_error_message("Something went wrong.")


def delete_customer():
    """ Deletes customer by its name """

    try:
        customers = manager.read_table_from_file(crm.DATAFILE)
        # Get name as input
        id = view.get_input('Customer id')

        for customer in customers:
            if customer[0] == id:
                # Remove customer by name
                customers.remove(customer)
                break

        manager.write_table_to_file(crm.DATAFILE, customers)
    except:
        view.print_error_message("Something went wrong.")


def get_subscribed_emails():
    """ Prints emails of subscribed personels """

    try:
        customers = manager.read_table_from_file(crm.DATAFILE)

        subscribed = [customer for customer in customers if customer[3] == '1']
        view.print_table(subscribed, crm.HEADERS)
    except:
        view.print_error_message("Something went wrong.")


def run_operation(option):
    """ Runs selected function based on option.

    :param option :int

    """

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
    """ Displays menu. """

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
