def exercise(big_list):
    # 1
    small_list = []

    # 2
    for x in big_list:
        small_list.append(x.lower())

    return small_list

print(exercise(['C#', 'JAVASCRIPT', 'JAVA', 'PYTHON', 'MATLAB', 'R']))
