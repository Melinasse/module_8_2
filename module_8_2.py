def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    try:
        for i in numbers:
            if isinstance(i, int):
                result += i
            # else:
            #     incorrect_data += 1
    except TypeError:
        incorrect_data += 1
    return result, incorrect_data


def calculate_average(numbers):
    if not isinstance(numbers, (list, tuple, set, dict, str)):
        print(f'Некорректный тип данных для подсчёта суммы')
        return None
    try:
        sum_result, incorrect = personal_sum(numbers)
        sum_average = sum_result / len(numbers) - incorrect
        return sum_average
    except ZeroDivisionError:
        return 0
    except TypeError:
        print(f'В numbers записан некорректный тип данных')
        return None


calculate_average("1, 2, 3")
print(f'Результат 1: {calculate_average("1, 2, 3")}')
calculate_average([1, "Строка", 3, "Ещё Строка"])
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
calculate_average(567)
print(f'Результат 3: {calculate_average(567)}')
calculate_average([42, 15, 36, 13])
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')