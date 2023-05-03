import contacts_m
import notes
import clener_sorter
import dop

def command_error(func):
    def inner(*args):
        try:
            return func(*args)
        except KeyError:
            return 'Unknown command, type "help" to see the list of commands'
        except IndexError:
            return 'IndexError occured'
        except TypeError:
            return 'TypeError occured'
        except ValueError:
            return 'ValueError occured'
    return inner

def parcer(user_input):
    user_input += ","
    disected_input = user_input.lower().split(",")
    disected_input.remove('')
    results = list()
    for i in disected_input:
        results.append(i.lower().strip(' '))
    return results







contacts = contacts_m.AddressBook()
notebook = notes.Notebook()



def greeting(*args):
    print("Hello! How can i help you?")

def add_ct(name, phone, *args:tuple): #допрацювати для всіх необовязкових параметрів bd=None, address=None, mail=None, 
    tupl = tuple(args)
    name = contacts_m.Name(name)
    phone = contacts_m.Phone(phone)
    bd = None
    address = None
    mail = None
    if len(tupl) > 0:
        bd = contacts_m.Birthday(tupl[0])
    if len(tupl) > 1:
        address = tupl[1]
    if len(tupl) > 2:
        mail = tupl[2]
    rec = contacts_m.Record(name, [phone], bd, address, mail)
    if name.value in contacts:
        for key_contact in contacts:
            if key_contact == name.value and phone.value not in contacts[key_contact].phones:
                return contacts[key_contact].add_phone(phone)
    else:
        contacts.add_contact(rec)
        return f'Contact {name.value} added'

def add_bd(name, bd, *args):
    name = contacts_m.Name(name)
    bd = contacts_m.Birthday(bd)
    if name.value in contacts.keys():
        contacts[name.value].birthday = bd

#@command_error
def dell_phone(name, phone, *args:tuple):
    name = contacts_m.Name(name)
    phone = contacts_m.Phone(phone)  
    for key_contact in contacts:
        if key_contact == name.value:        
            return contacts[key_contact].dell_phone(phone)
    return 'An entry with the specified name was not found' 

@command_error
def dell_contact(name, *args:tuple):
    # tupl = args[0].split(",")
    name = contacts_m.Name(name)
    return contacts.dell_contact(name)

@command_error
def change_phone(name, old_phone, new_phone, *args:tuple):
    if name in contacts.keys():
        name = contacts_m.Name(name)
        old_phone = contacts_m.Phone(old_phone)
        new_phone = contacts_m.Phone(new_phone)
        record = contacts[name.value]
        return record.change(old_phone, new_phone)
    return f"Can't find {name} in the Addressbook"

def delta_days(name, *args):
    name = contacts_m.Name(name)
    return contacts[name.value].days_to_birthday()

def show_all(step = None, *args):
    return contacts.show_all(step, *args)

def find_phone(name, *args:tuple):
    name = contacts_m.Name(name)
    return contacts.find_phone(name)

def find(keyword, *args:tuple):
    return contacts.find(keyword)

def cleaner(path, *args:tuple):
    
    clener_sorter.main_clean(path)

def help(*args):
    commands = [{"command": "hello", "description": "show greeting"},
                {"command": "help", "description": "show all available commands"},
                {"command": "add contact, name, phone_number", "description": "add a new contact"},
                {"command": "add birthday, name, day.month.year", "description": "add a birthday date to a contact"},
                {"command": "delete contact, name, phone_number", "description": "delete  target contact"},
                {"command": "delete phone, name, phone_number", "description": "delete  phone in contact"},
                {"command": "change, name, new_phone_number", "description": "change the phone number of an existing contact"},
                {"command": "days to birthday, name", "description": "days to birthday of contact"},
                {"command": "show all", "description": "show all contacts"},
                {"command": "find phone, name", "description": "show the phone number of a contact"},
                {"command": "find , part of name  or phone", "description": "show contacts that include this part"},
                {"command": "clener , folder", "description": "sort all file by folder"},
                {"command": "add note, text", "description": "save note whith text"},
                {"command": "search, keyword", "description": "Search for notes by keywords in names, contents, or tags"},
                {"command": "remove note, note name", "description": "remove target note"},
                {"command": "add tag, note, tegs", "description": "add tag to note"},
                {"command": "remove tag, note, tegs", "description": "remove tag from note"},
                {"command": "goodbye", "description": "exit Phonebook manager"},
                {"command": "close", "description": "exit Phonebook manager"},
                {"command": "exit", "description": "exit Phonebook manager"}]
    result = ""
    for item in commands:
        result += f'{item["command"]}: {item["description"]}\n'
    return result




@command_error
def handler(command, args):
    functions = {
                "hello": greeting,
                "help": help,
                "add contact": add_ct,
                "add birthday": add_bd,
                "change phone": change_phone,
                "remove phone": dell_phone,
                "remove contact": dell_contact,
                "show all": show_all,
                "search phone": find_phone,
                "search name": find,
                "days to birthday": delta_days,
                "add note": notebook.add_note,
                "remove note": notebook.remove_note,
                "add tag": notebook.add_tag,
                "remove tag": notebook.remove_tag,
                "edit note": notebook.edit_note,
                "search note": notebook.search_by_note,
                "cleaner": cleaner
                }
    if command in functions.keys():
        return functions[command](*args)
    else:
        return dop.cheker(command)



def main():

    contacts.read_file()
    notebook.load()

    while True:
        user_input = parcer(input('Enter a command: \n>>> '))
        command = user_input[0]
        user_input.remove(command)
        args = [arg for arg in user_input]
        if command in ("goodbye", "close", "exit"):
            print("Goodbye!")
            break

        result = handler(command, args)
        if result != "" and result != None: 
            print(result)

if __name__ == '__main__':
    main()