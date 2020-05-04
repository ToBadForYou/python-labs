from calc import *


def eval_program(p, table={}):
    """
    Interprets a Calc program to Python and returns a table of variables
    """
    if isprogram(p):
        return eval_statements(program_statements(p), table)
    else:
        raise TypeError("Invalid Program")


def eval_statements(p, table):
    """
    Runs through all the statements with recursion
    """
    if isstatements(p):
        table = eval_statement(first_statement(p), table)
        if not empty_statements(rest_statements(p)):
            table = eval_statements(rest_statements(p), table)
        return table


def eval_statement(statement, table):
    """
    Determines what kind of statement it is and runs different functions
    accordingly
    """
    if isassignment(statement):
        return eval_assignment(assignment_variable(statement),
                               assignment_expression(statement), table)
    elif isrepetition(statement):
        return eval_repetition(repetition_condition(statement),
                               repetition_statements(statement), table)
    elif isselection(statement):
        return eval_selection(statement, table)
    elif isinput(statement):
        return eval_input(input_variable(statement), table)
    elif isoutput(statement):
        variable = output_variable(statement)
        eval_output(variable, table[variable])
        return table


def eval_assignment(variable, expression, table):
    """
    Determines what kind of expression it is and returns a copy of the table
    with a modified value of the given variable
    """
    table_copy = table.copy()
    value = eval_expression(expression, table)
    table_copy[variable] = value
    return table_copy


def eval_expression(expression, table):
    """
    Determines what kind of expression it is, interprets it and returns the
    result
    """
    if isbinary(expression):
        left_val = eval_expression(binary_left(expression), table)
        right_val = eval_expression(binary_right(expression), table)
        operator = binary_operator(expression)
        if operator == "+":
            return left_val + right_val
        if operator == "-":
            return left_val - right_val
        if operator == "/":
            return left_val / right_val
        if operator == "*":
            return left_val * right_val
    if isvariable(expression):
        return table[expression]
    if isconstant(expression):
        return expression


def eval_repetition(condition, statements, table):
    """
    Repeats given statement until the condition is no longer true
    """
    if eval_condition(condition, table):
        table = eval_statements(statements, table)
        return eval_repetition(condition, statements, table)
    return table


def eval_condition(condition, table):
    """
    Interprets the condition and returns true or false
    """
    left_val = eval_expression(condition_left(condition), table)
    right_val = eval_expression(condition_right(condition), table)
    operator = condition_operator(condition)
    if operator == "<":
        return left_val < right_val
    if operator == ">":
        return left_val > right_val
    if operator == "=":
        return left_val == right_val


def eval_selection(statement, table):
    """
    Runs different statements depending on the condition
    """
    condition = eval_condition(selection_condition(statement), table)
    if condition:
        return eval_statement(selection_true(statement), table)
    elif hasfalse(statement):
        return eval_statement(selection_false(statement), table)
    return table


def eval_input(variable, table):
    """
    Requests user input for given variable and assigns it to a copy of the
    table
    """
    copy_table = table.copy()
    input_val = int(input("Enter value for " + variable + ": "))
    copy_table[variable] = input_val
    return copy_table


def eval_output(variable, value):
    """
    Prints the variable and the value
    """
    print(variable + " = " + str(value))
