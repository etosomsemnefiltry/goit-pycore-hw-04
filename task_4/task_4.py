'''
Напишите консольный бот помощника, который будет распознавать команды, вводимые с клавиатуры, и будет соответствовать введенной команде.
'''
# Словарь с примерами контактов
CONTACTS = {
    "Vasya": '0670001199',
    "Hariton": '0995550011',
    "Stepan": '0635554422'
}

def parse_input(user_input):
    # Парсим команды и приводим в нижний регистр чтобы не было путаницы
    cmd, * args =user_input. split ()
    cmd = cmd.strip().lower()
    return cmd, * args

def add_contact( args ):
    name, phone = args
    # Добавим контакт, если такого еще нет
    if not CONTACTS[name]:
        CONTACTS[name] = phone
        return  "Contact added."
    else:
        return  "Contact already exist."

def show_all ():
    res = ''
    # Сделаем удобный для чтения список
    for name, number in CONTACTS.items():
        res += name + ' - ' + number + '\n'
    return res

def change_contact ( args ):
    name, phone = args
    # Меняем контакт, если такой есть
    if CONTACTS[name]:
        CONTACTS[name] = phone
        return name + ' changed'
    else:
        return  'Contact not found.'

def show_phone( args ):
    name = args[0]
    #  Покажем контакт, если он есть
    if CONTACTS[name]:
        return name + ' - ' + CONTACTS[name]
    else:
        return  'Contact not found.'

def main():
    print ( "Велкует к требованию!" )
    # Бот всегда слушает наши команды
    while True:
        user_input = input ( "Enter a command: " )
        command , * args = parse_input(user_input)
        # Делигируем в соответствии с командой.
        match command:
            case "close", "exit":
                print ( "Good bye!" )
                break 
            case "hello" :
                print ( "How can I help you?" )
            case "add" :
                print (add_contact( args ))
            case "change" :
                print (change_contact( args ))
            case "phone" :
                print (show_phone( args ))
            case "all" :
                print (show_all())
            case _:
                print ( "Invalid command." )

if __name__ == "__main__" :
    main()