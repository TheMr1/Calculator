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

    for i1 in range(0, expression.__len__()):
        i = expression[i1]
        if (i == "+") or (i == "-") or (i == "*") or (i == "/") or (i == "^"):
            if i == '-':
                if expression[i1 + 1].isnumeric():
                    pass
                else:
                    operators.append(i)
                    number_streak, numbers_start = add_number_streak(number_streak, numbers_start)
                    continue
            else:
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
                number_streak.append(i)
            else:
                number_streak.append(current_num)
        else:
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

    #print(combined_list)

    def find_current_operator():
        current_operator1 = 0

        if combined_list.__contains__("^"):
            for i1 in range(0, combined_list.__len__()):
                i = combined_list[i1]

                if i == "^":
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

        combined_list[current_operator] = \
        BasicFunctions.calculate(combined_list[current_operator], combined_list[current_operator - 1],
                                 combined_list[current_operator + 1])["calculated_value"]
        combined_list.pop(current_operator + 1)
        combined_list.pop(current_operator - 1)

        #print(combined_list)

        if combined_list.__len__() > 1:
            solve_equation()

    solve_equation()

    return combined_list[0]