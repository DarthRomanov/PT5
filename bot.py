import contacts_m
import notes
import clener_sorter

def input_errors(func):
    def inner(*args):
        try:
            return func(*args)
        except (KeyError, IndexError, ValueError):
            return "Not enough arguments."
        except FileNotFoundError:
            return 'I don`t find file.'
    return inner


contacts = contacts_m.AddressBook
notebook = notes.Notebook()

def hello():
    print("Hello! How can i help you?")
def add_ct(*args:tuple): #допрацювати для всіх необовязкових параметрів
    tupl = args[0].split(",")
    name = contacts_m.Name(tupl[1])
    phone = contacts_m.Phone(tupl[2])
    Bp = None
    if len(tupl) == 4:
        Bp = tupl[-1]
    rec = contacts_m.Record(name, [phone], Bp)
    if name.value in contacts:
        for key_contact in contacts:
            if key_contact == name.value and phone.value not in contacts[key_contact].phones:
                return contacts[key_contact].add_phone(name, phone)
    else:
        contacts.add_contact(rec)
        return 'I add new contact'
def add_bd(*args):
    tupl = args[0].split(",")
    name = contacts_m.Name(tupl[1])
    bd = contacts_m.Birthday(tupl[2])
    for key_contact in contacts:
        if key_contact == name.value:
            contacts[key_contact].birthday = tupl[2]
@input_errors
def dell_phone(*args:tuple):
    tupl = args[0].split(",")
    name = contacts_m.Name(tupl[1])
    phone = contacts_m.Phone(tupl[2])  
    for key_contact in contacts:
        if key_contact == name.value:        
            return contacts[key_contact].dell_phone(name, phone)
    return 'I did not find an entry with the specified name' 
@input_errors
def dell_contact(*args:tuple):
    tupl = args[0].split(",")
    name = contacts_m.Name(tupl[1])
    return contacts.dell_contact(name)
@input_errors
def change(*args:tuple):
    tupl = args[0].split(",")
    name = contacts_m.Name(tupl[1])
    old_phone = contacts_m.Phone(tupl[2])
    new_phone = contacts_m.Phone(tupl[3])
    rec = contacts.get(name.value)
    return rec.change(name, old_phone, new_phone)
def delta_days(*args):
    tupl = args[0].split(",")
    name = contacts_m.Name(tupl[1])
    return contacts[name.value].days_to_birthday()
def show_all(*args):
    tupl = args[0].split(",")
    step = 5
    return contacts.iteranor(step)
def find_phone(*args:tuple):
    tupl = args[0].split(",")
    name = contacts_m.Name(tupl[1])
    return contacts.find_phone(name)
def find(*args:tuple):
    tupl = args[0].split(",")
    value = tupl[1]
    return contacts.find(value)
def clener(*args:tuple):
    tupl = args[0].split(",")
    arg = tupl[1]
    clener_sorter.main_clean(arg)
def add_nt(*args:tuple):
    tupl = args[0].split(",")
    notebook.add_note(tupl)
    notebook.save
def search_by_nt(*args:tuple):
    tupl = args[0].split(",")
    searchable = tupl[1]
    notebook.search_by_note(searchable)
def remove_nt(*args:tuple):
    tupl = args[0].split(",")
    note = tupl[1]
    notebook.remove_note(note)
    notebook.save
def tag_add(*args:tuple):
    tupl = args[0].split(",")
    note = tupl[1]
    tag = tupl[2]
    notebook.add_tag(note, tag)
    notebook.save
def tag_remove(*args:tuple):
    tupl = args[0].split(",")
    note = tupl[1]
    tags = []
    for i in range(tupl[2], tupl[-1]):
        tags.append(i)
    notebook.remove_tag(note, tags)
    notebook.save
def comand_enoter():
    return 'Unknow comand. Please, try again.'

@input_errors
def hendler(text:str):
   
    if text == 'hello':
        return hello()
    
    elif text.startswith('add contact'):
        return add_ct(text)
    elif text.startswith('add birthday'):
        return add_bd(text)
    elif text.startswith('delete phone'):
        return dell_phone(text)
    elif text.startswith('delete contact'):
        return dell_contact(text)
    elif text.startswith('change phone'):
        return change(text)
    elif text.startswith('days to birthday'):
        return delta_days(text)
    elif text.startswith('show all'):
        return show_all()
    elif text.startswith('find phone'):
        return find_phone(text) 
    elif text.startswith('find'):
        return find(text)
    elif text.startswith('clener'):
        return clener(text)
    elif text.startswith('add note'):
        return add_nt(text)
    elif text.startswith('search'):
        return search_by_nt(text)
    elif text.startswith('remove note'):
        return remove_nt(text)
    elif text.startswith('add tag'):
        return tag_add(text)
    elif text.startswith('remove tag'):
        return tag_remove(text)
    else:
        return comand_enoter()



def main():
    contacts.read_file
    notebook.load

    while True:
        input_comand = input('Pleace, enter comand:').lower()
        if input_comand == 'exit' or input_comand =='close' or input_comand == 'good bye':
            print("Good bye!")
            contacts.save_file()
            break

        comand = hendler(input_comand)
        print(comand)
        
if __name__ == '__main__':
    main()