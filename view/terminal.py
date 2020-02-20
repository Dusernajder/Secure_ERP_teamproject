import os


def print_menu(title, list_options):
    """Prints options in standard menu format like this:

    Main menu:
    (1) Store manager
    (2) Human resources manager
    (3) Inventory manager
    (0) Exit program

    Args:
        title (str): the title of the menu (first row)
        list_options (list): list of the menu options (listed starting from 1, 0th element goes to the end)
    """

    print(title)
    for i, opt in enumerate(list_options):
        print(f'({i}) {opt}')


def print_message(message):
    """Prints a single message to the terminal.

    Args:
        message: str - the message
    """
    print(message)


def print_general_results(result, label):
    """Prints out any type of non-tabular data.
    It should print numbers (like "@label: @value", floats with 2 digits after the decimal),
    lists/tuples (like "@label: \n  @item1; @item2"), and dictionaries
    (like "@label \n  @key1: @value1; @key2: @value2")
    """
    pass


# /--------------------------------\
# |   id   |  product   |   type   |
# |--------|------------|----------|
# |   0    |  Bazooka   | portable |
# |--------|------------|----------|
# |   1    | Sidewinder | missile  |
# \--------------------------------/
def print_table(table, headers):
    """Prints tabular data like above.

    Args:
        table: list of lists - the table to print out
    """
    clear()
    
    full_table = table
    full_table.insert(0, headers)
    length_elements = [[len(x) for x in full_table[i]] for i in range(len(full_table))]

    space_out_by = 15
    longest_elements = [0 for _ in range(len(headers))]
    for ppl in length_elements:
        for index, char in enumerate(ppl):
            if int(char) > longest_elements[index]:
                longest_elements[index] = int(char)+space_out_by

    chart = [int(x) * '-' for x in longest_elements]

    print(f'/{"-".join(chart)}\\')
    for index, employee in enumerate(full_table):
        string = ""
        for i in range(len(employee)):
            string += "|" + employee[i].center(longest_elements[i])

        print(string + '|')
        if index == len(full_table) - 1:
            print(f'\\{"-".join(chart)}/')
        else:
            print(f'|{"|".join(chart)}|')


def get_input(label):
    """Gets single string input from the user.

    Args:
        label: str - the label before the user prompt
    """
    # TODO: try - except
    spam = input(f"{label}: ")
    print()
    return spam


def get_inputs(labels):
    """Gets a list of string inputs from the user.

    Args:
        labels: list - the list of the labels to be displayed before each prompt
    """
    lst = []
    for l in labels:
        lst.append(input(f'{l}: '))
        print()
    return lst


def print_error_message(message):
    """Prints an error message to the terminal.

    Args:
        message: str - the error message
    """
    raise Exception(message)


def clear():
    """ Clears screen. """
    os.system('clear')
