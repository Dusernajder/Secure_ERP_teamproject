from model.sales import sales
from view import terminal as view
from model import data_manager as manager
from model import util
from datetime import date


def list_transactions():
    transactions = manager.read_table_from_file(sales.DATAFILE)
    #[print(transaction) for transaction in transactions]
    return [transaction for transaction in transactions]


def add_transaction():
    transactions = manager.read_table_from_file(sales.DATAFILE)
    labels = ["Customer id", "Product", "Price"]
    data = view.get_inputs(labels)
    data.insert(0, util.generate_id())
    data.append(str(date.today()))
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
    transactions = manager.read_table_from_file(sales.DATAFILE)
    biggest_transaction = transactions[0]
    for transaction in transactions:
        if float(transaction[3]) > float(biggest_transaction[3]):
            biggest_transaction = transaction[3]
    print(biggest_transaction)


def get_biggest_revenue_product():
    transactions = manager.read_table_from_file(sales.DATAFILE)
    biggest_revenue_product = [transactions[0][2], transactions[0][3]]
    for transaction in transactions:
        if float(transaction[3]) > float(biggest_revenue_product[1]):
            biggest_revenue_product = [transaction[2], transaction[3]]
    print(*biggest_revenue_product)


def count_transactions_between():
    transactions = manager.read_table_from_file(sales.DATAFILE)
    date_from = view.get_input('Date from')
    date_to = view.get_input('Date to')
    transaction_counter = 0
    list_for_return = []
    for transaction in transactions:
        if date_to >= transaction[4] >= date_from:
            transaction_counter += 1
    # print(f"\nNumber of transactions: {transaction_counter}\n")
    list_for_return.append(['Number of transactions', str(transaction_counter)])
    return list_for_return


def sum_transactions_between():
    transactions = manager.read_table_from_file(sales.DATAFILE)
    date_from = view.get_input('Date from')
    date_to = view.get_input('Date to')
    sum_of_transactions = 0.0
    list_for_return = []
    for transaction in transactions:
        if date_to >= transaction[4] >= date_from:
            sum_of_transactions += float(transaction[3])
    list_for_return.append(['Sum of transactions', str(sum_of_transactions)])
    return list_for_return


def run_operation(option):
    if option == 1:
        view.print_table(list_transactions(), sales.HEADERS)
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
        view.print_table(count_transactions_between(), sales.HEADERS_two)
    elif option == 8:
        view.print_table(sum_transactions_between(), sales.HEADERS_two)
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
