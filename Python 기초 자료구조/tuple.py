def exercise(my_language):
    # 1
    programming_languages = ('C#', 'Javascript', 'Java', 'Python', 'Matlab', 'R')

    # 2
    programming_languages = programming_languages[2:4]

    # 3
    new_programming_languages = ('Swift', 'Go')

    # 4
    programming_languages = programming_languages + new_programming_languages

    # 5
    is_my_language = my_language in programming_languages

    return is_my_language

print(exercise('R'))
