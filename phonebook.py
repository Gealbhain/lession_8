"""
with...as...
with - это менеджер контекста,
as - это команда для alias: with open ('rext.txt')
as file
режим работы с файлами 
1. "r" - red, брать данные из файла чтобы программа интерфейса выводила их на экран
    позволяет читать данные из файла
    если вы попробуетие считать данные из файла, каоторого не существует, программа выдаст ошибку 
2. "w" - write, перезапись,нужно удалить все данные изз файла для перезаписи
    позволяет записывать данные и создавать если файл, если его не существует.
3. "a" - append, открытие для добавления данных.
    позволяет дописывать что-то в имеющийся файл 
    если вы попробуете дописать что-то в несуществующий файл то, то файл будет создан  и в него начнется запись 
4. "w+" - 
    позволяет от крывать файл для записи и читать из него. 
    если файа не существует, он будет создан.
5. "r+" - 
    позволяет открывать файл для чтения и дописыать в него. 
    если файла не существует, программа выдаст ошибку.
"""


def ask_data():
    f_name = input('Введите имя: ').title()
    s_name = input('Введите фамилию: ').title()
    m_name = input('Введите отчество: ').title()
    phone = input('Введите номер телефона: ')
    return f'{s_name} {f_name} {m_name} {phone}\n\n'
    
def add_new_contact():
    contact = ask_data()
    with open('phonebook.txt', 'a', encoding = "utf-8") as file:
        file.write(contact)
    return True

def open_contact():
    with open('phonebook.txt', 'r') as file:
        сontacts = file.read()
    contacts_dict = сontacts.split('\n\n')
    for n, contact in enumerate(contacts_dict, 1):
            print(n, contact)
def find():
    print("Выберите пораметр поиска:\n"
          "1. По фамилии.\n"
          "2. По имени.\n"
          "3. По отчеству.\n"
          "4. По телефону.\n"
          "0. Отмена.\n")
    var = input("Введите вариант поиска: ")
    while var not in ("12340"):
        print('некоректные данные')
        var = input("Введите вариант поиска: ")
    index = int(var)-1
    search = input('Введите данные: ').title()
    with open ('phonebook.txt', 'r') as file:
        contact = file.read()
    list = contact.split('\n\n')
    finded_contact = []
    for list_str in list:
        list_1 = list_str.rsplit(' ')
        if search in list_1[index]:
            finded_contact.append(list_1)
    for n, contact in enumerate(finded_contact, 1):
            print(n, *contact)
    print()
    print("Какое действие вы хотите предпринять\n"
          "1. Копировать\n"
          "0. Выйти в меню\n")
    act_1 = input("Выберите действие: ")
    print()
    while act_1 not in ('1','0'):
        print("невозможное действие")
        act_1 = input("Выберите действие: ")
    if act_1 == '1':
        print('Выберите контакт который копировать: ')
        copy = int(input("> "))
        for number, cont in enumerate(finded_contact, 1):
            if number == copy:
                print(cont)
                with open ("phonebook_coppied.txt", 'a') as file:
                    file.write(f'{cont} \n\n')
        print('копирование завершено')
    else:
        quit()
    

def main():
    isStop = 1
    while isStop != 0:
        print(f'Выберите что хотите сделать:\n1. найти\n2. добавить\n3. открыть всю внигу\n0. выход')
        isStop = input("Введите какое действие выполлнить: ")
        while isStop not in '1230':
            print('Нет такого действия')
            isStop = input("Введите какое действие выполлнить: ")
        print()
        
        match isStop:
            case '1':
                find()
            case '2':
                add_new_contact()
            case '3':
                open_contact()
            case '0':
                exit()
            

        # if isStop == 1:
        #     find()
        # elif isStop == 2:
        #     add_new_contact()
        # elif isStop == 3:
        #     open_contact()
        input("Нажмите enter, чтобы продолжить")

main()