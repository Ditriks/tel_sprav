def interaction():
    action = int(input('Введите команду: \n1 - сделать запись\n2 - получить запись   '))
    if action == 1:
        text_input = input('Введите ФИО и номер через пробел: ')
        return (text_input, action)
    if action == 2:
        text_input = input('Введите фамилию/имя/отчество: ')
        return (text_input, action)
    

def res_find(string):
    print(string)