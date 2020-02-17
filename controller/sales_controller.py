from model.sales import sales
from view import terminal as view
from model import data_manager as manager
from model import util


def list_transactions():
    transactions = manager.read_table_from_file(sales.DATAFILE)
    [print(transaction) for transaction in transactions]
    # return [transaction for transaction in transactions]


def add_transaction():
    transactions = manager.read_table_from_file(sales.DATAFILE)
    labels = ["Customer id", "Product", "Price", "Transaction date"]
    data = view.get_inputs(labels)
    data.insert(0, util.generate_id())
    transactions.append(data)
    # [print(transaction) for transaction in transactions]
    manager.write_table_to_file(sales.DATAFILE, transactions)


def update_transaction():
    transactions = manager.read_table_from_file(sales.DATAFILE)
    transaction_id = view.get_input('Id')
    list_options = ["Customer id", "Product", "Price", "Transaction date"]
    view.print_menu('options', list_options)
    option = int(view.get_input('Select'))
    modification = view.get_input(f"Modified {list_options[option]}")
    for transaction in transactions:
        if transaction_id in transaction:
            transaction[option + 1] = modification
    # [print(transaction) for transaction in transactions]
    manager.write_table_to_file(sales.DATAFILE, transactions)


def delete_transaction():
    transactions = manager.read_table_from_file(sales.DATAFILE)
    transaction_id = view.get_input('Id')
    [transactions.remove(transaction) for transaction in transactions if transaction_id in transaction]
    # [print(transaction) for transaction in transactions]
    manager.write_table_to_file(sales.DATAFILE, transactions)


def get_biggest_revenue_transaction():
    view.print_error_message("Not implemented yet.")


def get_biggest_revenue_product():
    view.print_error_message("Not implemented yet.")


def count_transactions_between():
    view.print_error_message("Not implemented yet.")


def sum_transactions_between():
    view.print_error_message("Not implemented yet.")


def run_operation(option):
    if option == 1:
        list_transactions()
    elif option == 2:
        add_transaction()
    elif option == 3:
        update_transaction()
    elif option == 4:
        delete_transaction()
    elif option == 5:
        get_biggest_revenue_transaction()
    elif option == 6:
        get_biggest_revenue_product()
    elif option == 7:
        count_transactions_between()
    elif option == 8:
        sum_transactions_between()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List transactions",
               "Add new transaction",
               "Update transaction",
               "Remove transaction",
               "Get the transaction that made the biggest revenue",
               "Get the product that made the biggest revenue altogether",
               "Count number of transactions between",
               "Sum number of transactions between"]
    view.print_menu("Sales", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
