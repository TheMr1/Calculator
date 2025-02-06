from random import randint

from MainLibrary.MainPackage import BasicFunctions

def solve_expression(expression):
    # 2 + 4 * 3 ^ 2
    numbers_start = []
    operators = []
    number_streak = []

    def add_number_streak(number_streak1, numbers_start1):
        if number_streak1.__len__() > 0:
            numbers_start1.append(number_streak1)
            number_streak1 = []
        return number_streak1, numbers_start1

    previous_sign = 'operator' #operator / number

    for i1 in range(0, expression.__len__()):
        i = expression[i1]

        if i == " " or 'throot'.__contains__(i):
            continue

        if (i == "+") or (i == "-") or (i == "*") or (i == "/") or (i == "^") or (i == "n"):
            if i == '-':
                if previous_sign == 'operator':
                    pass
                else:
                    previous_sign = 'operator'
                    operators.append(i)
                    number_streak, numbers_start = add_number_streak(number_streak, numbers_start)
                    continue
            elif i == 'n':
                if expression[i1:i1+7] == 'nthroot':
                    previous_sign = 'operator'
                    operators.append('nthroot')
                    number_streak, numbers_start = add_number_streak(number_streak, numbers_start)
                    continue
            else:
                previous_sign = 'operator'
                operators.append(i)
                number_streak, numbers_start = add_number_streak(number_streak, numbers_start)
                continue

        current_num = 'e'

        try:
            current_num = int(i)
        except ValueError:
            pass

        if current_num != 'e' or i == '.' or i == '-':
            if i == '.' or i == '-':
                if i == '-':
                    previous_sign = 'number'
                    number_streak, numbers_start = add_number_streak(number_streak, numbers_start)
                    number_streak.append(i)
                else:
                    previous_sign = 'number'
                    number_streak.append(i)
            else:
                previous_sign = 'number'
                number_streak.append(current_num)
        else:
            previous_sign = 'number'
            number_streak, numbers_start = add_number_streak(number_streak, numbers_start)

    number_streak, numbers_start = add_number_streak(number_streak, numbers_start)

    true_numbers = []

    for i in numbers_start:
        current_string = ''
        for j in i:
            current_string = current_string + str(j)
        try:
            true_numbers.append(float(current_string))
        except ValueError:
            pass

    combined_list = []

    for i in range(0, true_numbers.__len__() + operators.__len__()):
        if i % 2 == 0:
            combined_list.append(true_numbers[int(i / 2)])
        else:
            combined_list.append(operators[int((i - 1) / 2)])

    def find_current_operator():
        current_operator1 = 0

        if combined_list.__contains__("^") or combined_list.__contains__("nthroot"):
            for i1 in range(0, combined_list.__len__()):
                i = combined_list[i1]

                if i == "^":
                    current_operator1 = i1
                    break
                elif i == "nthroot":
                    current_operator1 = i1
                    break
        elif combined_list.__contains__("*") or combined_list.__contains__("/"):
            for i1 in range(0, combined_list.__len__()):
                i = combined_list[i1]

                if i == "*" or i == "/":
                    current_operator1 = i1
                    break
        elif combined_list.__contains__("+") or combined_list.__contains__("-"):
            for i1 in range(0, combined_list.__len__()):
                i = combined_list[i1]

                if i == "+" or i == "-":
                    current_operator1 = i1
                    break

        return current_operator1

    def solve_equation():
        current_operator = find_current_operator()

        result = BasicFunctions.calculate(combined_list[current_operator], combined_list[current_operator - 1],
                                 combined_list[current_operator + 1])

        if result["OK"]:
            combined_list[current_operator] = result["calculated_value"]
            combined_list.pop(current_operator + 1)
            combined_list.pop(current_operator - 1)
        else:
            combined_list[0] = result['error_message']
            return


        #print(combined_list)

        if combined_list.__len__() > 1:
            solve_equation()

    solve_equation()

    #print('result:', combined_list[0])

    return combined_list[0]

def generate_expression(max_operators, list_of_operations : list):
    operators = randint(1, max_operators)
    expression = ''

    for i in range(0, 2 * operators + 1):
        if i % 2 == 0:
            expression += str(randint(-100, 100))
        else:
            expression += list_of_operations[randint(0,list_of_operations.__len__() - 1)]
        expression += " "

    return expression