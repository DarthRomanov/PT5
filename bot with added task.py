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
            return 'I didn`t find file.'
    return inner


contacts = contacts_m.AddressBook
notebook = notes.Notebook()

def hello():
    print("Hello! How can I help you?")
def add_ct(*args:tuple): #допрацювати для всіх необовязкових параметрів
    print(args)
    for arg in args:
        print(arg)
    tupl = args[0].split(",")
    name = contacts_m.Name(tupl[1])
    phone = contacts_m.Phone(tupl[2])
    Bp = None
    adress = None
    mail = None
    if len(tupl) > 3:
        Bp = tupl[3]
    if len(tupl) > 4:
        adress = tupl[4]
    if len(tupl) > 5:
        mail = tupl[5]
    rec = contacts_m.Record(name, [phone], Bp, adress, mail)
    if name.value in contacts:
        for key_contact in contacts:
            if key_contact == name.value and phone.value not in contacts[key_contact].phones:
                return contacts[key_contact].add_phone(name, phone)
    else:
        contacts.add_contact(rec)
        return 'New contact was added.'
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
    return 'Unknown command. Please, try again.'

@input_errors
def hendler(text:str):
    yes_input = ['y', 'yes', '+', 'ok', 'right', 'sure', 'yep', 'course']
   
    if text in ['hello', 'hi', 'hey', 'yo', 'morning', 'afternoon', 'evening', 'sup', 'hiya']:
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
    

    elif any(word in text.lower() for word in ['add', 'ad', 'aad', 'append', 'plus', 'put', 'join', 'include']):
        add_correct_input = input('Do you mean, that you would like to add something? \nFour options (choose one): 1. Contact. 2. Birthday. 3. Note. 4. Tag. 1/2/3/4 >>> ')
        if add_correct_input == '1':
            print("If you'd like to add contact, use this command  ->  add contact, name, phone_number, birthday, address, email. \nBirthday, address and email are optional.")
        elif add_correct_input == '2':
            print("If you'd like to add birthday for contact, use this command  ->  add birthday, name, birthday")
        elif add_correct_input == '3':
            print("If you'd like to add note, use this command  ->  add note, note_name, text")
        elif add_correct_input == '4':
            print("If you'd like to add tag, use this command  ->  add tag, note_name, tag")
        else:
            print('Unknown command. Please, try again.')
    elif any(word in text.lower() for word in ['remove', 'delete', 'rem', 'del', 'delet', 'cut off', 'cut', 'take out', 'clean']):
        remove_correct_input = input('Do you mean, that you would like to delete something? \nFour options (choose one): 1. Phone. 2. Contact. 3. Note. 4. Tag. 1/2/3/4 >>> ')
        if remove_correct_input == '1':
            print("If you'd like to delete phone, use this command  ->  delete phone, name, phone_number")
        elif remove_correct_input == '2':
            print("If you'd like to delete contact, use this command  ->  delete contact, name")
        elif remove_correct_input == '3':
            print("If you'd like to delete note, use this command  ->  remove note, note_name")
        elif remove_correct_input == '4':
            print("If you'd like to delete tag, use this command  ->  remove tag, note_name, tag")
        else:
            print('Unknown command. Please, try again.')
    elif any(word in text.lower() for word in [' find', 'fnd', 'fid', 'search ', 'seach', 'searh', 'sarch', 'serch', 'realize', 'notice', 'detect']):
        find_correct_input = input('Do you mean, that you would like to find something? \nThree options (choose one): 1. Phone. 2. Information about contact. 3. Text in note.  1/2/3 >>> ')
        if find_correct_input == '1':
            print("If you'd like to find phone, use this command  ->  find phone, name")
        elif find_correct_input == '2':
            print("If you'd like to find information about contact, use this command  ->  find, name/number")
        elif find_correct_input == '3':
            print("If you'd like to find text in note, use this command  ->  search, text")
        else:
            print('Unknown command. Please, try again.')
    elif any(word in text.lower() for word in ['change', ' change', 'chage', 'chenge', 'swap', 'exchange', 'rewrite', 'switch', 'replace', 'new']):
        change_correct_input = input('Do you mean, that you would like to change the phone? y/n >>> ')
        print("If you'd like to change the phone, use this command  ->  change phone, name, old_number, new_number") \
            if change_correct_input.lower() in yes_input else print('Unknown command. Please, try again.')
    elif any(word in text.lower() for word in [' add birthday', 'day', ' birthday ', 'birthday ', 'bday', 'birthdate', 'bd', 'birth', 'date']):
        birthday_correct_input = input('Do you mean, that you would like to do smth with birthday? \nTwo options (choose one): 1. Add birthday. 2. Days to birthday. 1/2 >>> ')
        if birthday_correct_input == '1':
            print("If you'd like to add birthday, use this command  ->  add birthday, name, birthday")
        elif birthday_correct_input == '2':
            print("If you'd like to see how many days to birthday, use this command  ->  days to birthday, name")
        else:
            print('Unknown command. Please, try again.')
    elif any(word in text.lower() for word in [' show', 'show', 'see', ' show all', 'show me', 'aal', 'display', 'look', 'watch', 'view', 'each']):
        show_contact_correct_input = input('Do you mean, that you would like to see contacts?  y/n >>> ')
        print("If you'd like to see the contacts, use this command  ->  show all") \
            if show_contact_correct_input.lower() in yes_input else print('Unknown command. Please, try again.')
    elif any(word in text.lower() for word in ['note ', 'not', 'note', 'noter', 'nots', 'message', 'reminder', 'record', 'notes', 'notation', 'comment', 'remark']):
        note_correct_input = input('Do you mean, that you would like to work with notes? \nTwo options (choose one): 1. Add. 2. Remove.  1/2 >>> ')
        if note_correct_input == '1':
            print("If you'd like to add note, use this command  ->  add note, note_name, text")
        elif note_correct_input == '2':
            print("If you'd like to remove note, use this command  ->  remove note, note_name")
        else:
            print('Unknown command. Please, try again.')
    elif any(word in text.lower() for word in ['marker', 'key', 'keyword', 'keywords', 'label', 'sticker', 'tag', 'teg', 'tags', 'tegs']):
        tag_correct_input = input('Do you mean, that you would like to add or remove tag? \nTwo options (choose one): 1. Add tag. 2. Remove tag. 1/2 >>> ')
        if tag_correct_input == '1':
            print("If you'd like to add tag, use this command  ->  add tag, note_name, tag")
        elif tag_correct_input == '2':
            print("If you'd like to remove tag, use this command  ->  remove tag, note_name, tag")
        else:
            print('Unknown command. Please, try again.')


    else:
        return comand_enoter()





def main():
    contacts.read_file
    notebook.load

    while True:
        input_comand = input('Please, enter a command:').lower()
        if input_comand in ['exit', 'close', 'good bye' 'goodbye', 'bye', 'see you', 'bb', 'off', 'out']:
            print("Good bye!")
            contacts.save_file()
            break

        comand = hendler(input_comand)
        print(comand)
        
if __name__ == '__main__':
    main()