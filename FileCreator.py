import math
import threading
import time

from MainLibrary.MainPackage import GeneralFunctions
from MainLibrary.MainPackage import AdvancedFunctions

start_time = time.time()

iterations = math.floor(math.pow(10, 6))
amount_of_threads = 10

list_of_operations = ["+","-","*","/","^","nthroot"]
expressions = open("Expressions.txt", 'w')

old_list_of_expressions = []
list_of_results = []

for i in range(0, amount_of_threads):
    list_of_results.append([])
    old_list_of_expressions.append([])

def function1(start_from):
    list1 = GeneralFunctions.break_down_writing_expressions(start_from, iterations, amount_of_threads, list_of_operations)
    old_list_of_expressions[start_from] = list1

threads = []

for i in range(0, amount_of_threads):
    args = (i, iterations, amount_of_threads, list_of_operations)
    t1 = threading.Thread(target=function1, args=(i,))
    threads.append(t1)

    t1.start()

for i in threads:
    if i.is_alive():
        i.join()

list_of_expressions = []

for i in old_list_of_expressions:
    for j in i:
        list_of_expressions.append(j)

expressions.writelines(list_of_expressions)

print('end', time.time() - start_time)

expressions.close()

results = open("Results.txt", 'w')

def break_down_writing_results(start_from):
    start = math.floor((iterations / amount_of_threads) * start_from)
    end = start + math.floor(iterations / amount_of_threads)

    if start_from == amount_of_threads - 1:
        end = iterations

    list_of_mini_results = []

    for i in range(start, end):
        expression = list_of_expressions[i]
        expression = expression[0:expression.__len__() - 2]
        result = AdvancedFunctions.solve_expression(expression)
        list_of_mini_results.append(expression + " = " + str(result) + "\n")

    list_of_results[start_from] = list_of_mini_results

threads = []

for i in range(0, amount_of_threads):
    if i == amount_of_threads - 1:
        t1 = threading.Thread(target=break_down_writing_results, args=(i,))
    else:
        t1 = threading.Thread(target=break_down_writing_results, args=(i,))

    threads.append(t1)

    t1.start()

for i in threads:
    if i.is_alive():
        i.join()

final_list_of_results = []

for i in list_of_results:
    for j in i:
        final_list_of_results.append(j)

results.writelines(final_list_of_results)

print('Time (s): ' + str(time.time() - start_time))
print('Time (ms): ' + str(math.floor((time.time() - start_time) * 1000)))