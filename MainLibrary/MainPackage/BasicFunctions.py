def ask_for_string(text, possible_values):
    current_string = input(text)
    if possible_values:
        if possible_values.__contains__(current_string):
            return current_string
        else:
            print('Invalid operation, try again.')
            return ask_for_string(text, possible_values)
    else:
        return current_string

def ask_for_float(text, input1):
    if input1:
        current_string = input1
    else:
        current_string = input(text)

    try:
        current_string = float(current_string)
        return current_string
    except ValueError:
        if current_string.__contains__(','):
            current_string = current_string.replace(',', '.')
            return ask_for_float(text, current_string)
        else:
            print("Invalid number, try again")
            return ask_for_float(text, False)