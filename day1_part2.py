def calcul_sum(list_str):
    list_int = [int(i) for i in list_str]
    return sum(list_int)


def create_list(data_str):
    list_number = []
    data_str = data_str[:-1]

    step = len(data_str) // 2

    for s in range(len(data_str)):
        index = s - step
        digit_to_compare = data_str[index]
        if digit_to_compare == data_str[s]:
            list_number.append(data_str[s])

    return list_number


def day1(path):
    file_to_read = open(path, 'r')
    txt = file_to_read.read()
    list_to_sum = create_list(txt)
    # list_to_sum = create_list(str(path))
    result = calcul_sum(list_to_sum)
    print(result)


# day1(12131415)
day1('./day1_input.d')
