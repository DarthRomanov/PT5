from collections import UserDict
from datetime import datetime, date
import json


class Field:

    def __init__(self, value):
        self.__value = None
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, value):
        if len(value) < 3:
            raise ValueError("The name is too short")
        self.__value = value


class Phone(Field):
    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, value):
        if not (len(value) >= 7 and len(value) <= 15):
            raise ValueError("The phone number should be 7 to 15 characters long and written with numbers")
        self.__value = value


class Birthday(Field):
    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, value):
        if value["month"] > 12 or value["day"] > 31:
            raise ValueError("The birthday date seems weird")
        self.__value = value


class Record:
    def __init__(self, name:Name, *phone_numbers:Phone):
        self.name = name
        self.phone_numbers = []
        self.birthday = None
        if phone_numbers:
            for i in phone_numbers:
                self.phone_numbers.append(i)

    def add_phone_number(self, phone_number:Phone):
        if phone_number not in self.phone_numbers:
            self.phone_numbers.append(phone_number)
            return f"Phone number {phone_number.value} was added to {self.name.value.capitalize()}"
        else:
            return f"Phone number {phone_number.value} already exists in{self.name.value.capitalize()}"

    def remove_phone_number(self, phone_number:Phone):
        if phone_number in self.phone_numbers:
            self.phone_numbers.remove(phone_number)
            return f"Phone number {phone_number.value} was removed from {self.name.value.capitalize()}"
        else:
            return f"Phone number {phone_number.value} was not found in {self.name.value.capitalize()}"

    def edit_phone_number(self, new_number:Phone, old_number:Phone=None):
        self.remove_phone_number(old_number)
        self.add_phone_number(new_number)

    def set_birthday(self, birthday:Birthday):
        self.birthday = birthday
    
    def days_to_birthday(self):
        bday_date =  date(date.today().year, self.birthday.value["month"], self.birthday.value["day"])
        today = date.today()
        if today > bday_date:
            bday_date = date(date.today().year + 1, self.birthday.value["month"], self.birthday.value["day"])
        difference = bday_date - today
        return f'Birthday coming in {difference.days} days\n'


class Addressbook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def to_dict(self):
        data = {}
        for name, record in self.data.items():
            data[str(name)] = {"phones": [str(phone.value) for phone in record.phone_numbers],
                               "birthday": str(None) if not record.birthday else [str(record.birthday.value["day"]), str(record.birthday.value["month"]), str(record.birthday.value["year"])]
                              }
        return data

    def from_dict(self, data):
        for name, value in data.items():
            self.add_record(Record(Name(name), *[Phone(phone) for phone in value["phones"]]))
            if value["birthday"] != "None":
                self.data[name].set_birthday(Birthday({"year":int(value["birthday"][2]), "month":int(value["birthday"][1]), "day":int(value["birthday"][0])}))

    def display_contact(self, name):
        output = f"---------------------------------------------------------\n{name.capitalize()}:\n"
        for phone in self.data[name].phone_numbers:
            output += f"{phone.value}\n"
        if self.data[name].birthday:
            output += self.data[name].days_to_birthday()
        return output
    
    def iterator(self, items_per_page, *args):
        start = 0
        keys = list(self.data.keys())
        while True:
            result = ""
            current_keys = keys[start:start + items_per_page]
            if not current_keys:
                break
            for name in current_keys:
                result += self.display_contact(name)
            yield result
            start += items_per_page
    
    def search(self, keyword, *args):
        result = ""
        for name in self.data.keys():
            content = str(self.display_contact(name)).lower()
            matched = content.find(keyword.lower())
            if matched != -1:
                result += self.display_contact(name)
        if result == "":
            result = "No matches\n" 
        return result

    def show_all(self, arg = None, *args):
        if arg:
            items_per_page = int(arg)
            result = "that was the last page \n"
            pg = self.iterator(items_per_page)
            for i in pg:
                print(i)
                input("Press Enter to see the next page\n>>>")
        else:
            result = ""
            for name in self.data.keys():
                result += self.display_contact(name)
        return result

    def load(self):
        try:
            with open("data.json", "r") as file:
                recovered_data = json.load(file)
            if recovered_data != {}:
                self.from_dict(recovered_data)
        except FileNotFoundError:
            print("data.json was not found")

    def save(self):
        converted_data = self.to_dict()
        with open("data.json", "w") as file:
            json.dump(converted_data, file)



############################################################################################################################################################################################################

# зберігати нотатки з текстовою інформацією;
# проводити пошук за нотатками;
# редагувати та видаляти нотатки;
# додавати в нотатки "теги", ключові слова, що описують тему та предмет запису;
# здійснювати пошук та сортування нотаток за ключовими словами (тегами);

############################################################################################################################################################################################################

from collections import UserDict # Імпорт необхідних модулів 
from datetime import date
import json
import pickle

class Note(): 

    def __init__(self, name, text):
        self.name = name #Стара версія імені: datetime.now().strftime("%S%M%H-%d%m%y")
        self.value = text
        self.tags = []

    def add_tag(self, *tags):
        for tag in tags:
            self.tags.append(tag)

    def __str__(self):
        output = ("-" * 70) + f"\nNote {self.name}:\n{self.value}\n"
        if self.tags != []:
            output += f"Tags: {self.tags}\n"
        output += ("-" * 70) + "\n"
        return output


class Notebook(UserDict):

    def __init__(self):
        self.data = {}

    def add_note(self, *data): # Додавання нотатки, у якості агрументів - рядки що приходять від парсера. оскільки мій парсер ріже текст на фрагменти у місцях, де були коми, кількість цих рядків може бути довільною.
        if self.data != {}:
            name = str(int(list(self.data.keys())[-1]) + 1)
        else: name = "1"
        text = ", ".join(data) # Як зазначено вище, текст складається із довільної кількості рякдів, тому з них слід зібрати один цілісний текст і повернути на місце коми, стерті парсером.
        if not text or text == "":
            return f"An empty note cannot be added"
        note = Note(name, text)
        self.data[note.name] = note
        return f"Note {note.name} was added"

    def search_by_note(self, *keywords):   # Пошук нотаток за ключовими словами в іменах, вмісті, або тегах. Якщо не введене ключове слово, показує всі нотатки (аналог show all із телефонної книги). Зараз пошук працює у щедрому режимі - збіг навіть в одного слова із багатьох дає позитивний результат.
        result = ""
        if not keywords:
            for note in self.data.values():
                result += str(note)
            return result
        notes_to_show = []
        for keyword in keywords:
            for note in self.data.values():
                if (keyword in note.name or keyword in note.value or keyword in note.tags) and note.name not in notes_to_show:
                    result += str(note)
                    notes_to_show.append(note.name)
        if result == "":
            return f"No matching notes found"
        return result

    def remove_note(self, note_name, *args): # Видалення нотаток за ім'ям.
        if not note_name or note_name == "":
            return "Note name was not specified"        
        if note_name in self.data.keys():
            del self.data[note_name]
            return f"Note {note_name} removed"
        return f"Seems like note {note_name} does not exist already"
    
    def edit_note(self, note_name, *new_text): # Редагування вмісту нотатки за ім'ям. Як і раніше, збирає текст докупи після того, що з ним робить парсер.
        if note_name in self.data.keys():
            text = ", ".join(new_text)
            if not text or text == "":
                return f"An empty note cannot be added"
            self.data[note_name].value = text
            return f"The content of note {note_name} was edited"
        return f"Note {note_name} was not found"

    def add_tag(self, note, *tags): # Додає теги (довільну кількість) до нотатки за ім'ям. 
        if note not in self.data.keys():
            return f"Note {note} not found"
        result = ""
        for tag in tags:
            if tag != "":
                self.data[note].add_tag(tag)
                result += f"Tag [{tag}] added\n"
        return f"An empty tag cannot be added" if result == "" else result

    def remove_tag(self, note_name, *tags): # Видаляє теги (довільну кількість) із нотатки за ім'ям.
        result = ""
        for tag in tags:
            if tag in self.data[note_name].tags:
                self.data[note_name].tags.remove(tag)
                result += f"Tag {tag} was removed from note {note_name}\n"
            else:
                result += f"Tag {tag} not found in note {note_name}\n"
        return result

    def to_dict(self):
        data = {}
        for name, note in self.data.items():
            data[name] = {"text": note.value,"tags": note.tags}
        return data

    def from_dict(self, file_data):
        for name, value in file_data.items():
            note = Note(name, value["text"])
            note.tags = value["tags"]
            self.data[note.name] = note

    def save(self):
        converted_data = self.to_dict()
        with open("notebook_data.json", "w") as file:
            json.dump(converted_data, file)
        # with open("notebook_data.pickle", "wb") as file:
        #     pickle.dump(self, file, protocol=-1)

    def load(self):
        try:
            with open("notebook_data.json", "r") as file:
                recovered_data = json.load(file)
            if recovered_data != {}:
                self.from_dict(recovered_data)
        except FileNotFoundError:
            print("notebook_data.json was not found")
        # try:
        #     with open("notebook_data.pickle", "rb") as file:
        #         self = pickle.load(file)
        # except FileNotFoundError:
        #     print('File "notebook_data.pickle" was not found')


############################################################################################################################################################################################################


notebook = Notebook()
addressbook = Addressbook()


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

def greeting(*args):
    return "How can I help you?"

def help(*args):
    commands = [{"command": "hello", "description": "show greeting"},
                {"command": "help", "description": "show all available commands"},
                {"command": "add, name, phone_number", "description": "add a new contact"},
                {"command": "add birthday, name, day.month.year", "description": "add a birthday date to a contact"},
                {"command": "change, name, new_phone_number", "description": "change the phone number of an existing contact"},
                {"command": "phone, name", "description": "show the phone number of a contact"},
                {"command": "show all, number", "description": "show all contacts in console, number (optional) indicates the amount of contacts displayed per page"},
                {"command": "goodbye", "description": "exit Phonebook manager"},
                {"command": "close", "description": "exit Phonebook manager"},
                {"command": "exit", "description": "exit Phonebook manager"},
                # Команди для роботи з нотатками:
                {"command": "add note, text", "description": "Add a new note."},
                {"command": "remove note, note name", "description": "Remove an existing note."},
                {"command": "edit note, note name, new text", "description": "Replace the text of an existing note."},
                {"command": "search note, keyword", "description": "Display all notes, containing the keyword (or multiple keywords) in it's name, text or tags. If the keyword is not specified, display all notes."},
                {"command": "add tag, note name, tag", "description": "Add a tag (or multiple tags) to an existing note."},
                {"command": "remove tag, note name, tag", "description": "Remove tag (or multiple tags) from an existing note"}]
    result = ""
    for item in commands:
        result += f'{item["command"]}: {item["description"]}\n'
    return result

def parcer(user_input):
    user_input += ","
    disected_input = user_input.lower().split(",")
    disected_input.remove('')
    results = list()
    for i in disected_input:
        results.append(i.lower().strip(' '))
    return results

def add(name, *args):
    #print(args)
    if name in addressbook.data.keys():
        result = str()
        for arg in args:            
            result += addressbook.data[name].add_phone_number(Phone(arg)) + "\n"
        return result
    name = Name(name)
    phones = [Phone(p) for p in args]
    record = Record(name, *phones)
    addressbook.add_record(record)
    return f"Contact added: {name.value.capitalize()}: {[phone.value for phone in phones]}"

def add_bday(name, date:str, *args):
    date = date.split(".")
    y = int(date[2])
    m = int(date[1])
    d = int(date[0])
    birthday = Birthday({"year":y, "month":m, "day":d})
    addressbook.data[name].set_birthday(birthday)
    return f"Birthday {birthday} was added to {name.capitalize()}"

def change(name, *args):
    if name in addressbook.data.keys():
        addressbook.data[name].phone_numbers = [Phone(p) for p in args]
        return f"Contact changed to {name.capitalize()}: {[(p) for p in args]}"
    return 'Contact not found'

def change_phone(name, old_phone, *new_phones):
    pass

def remove_phone(name, phone, *args):
    pass

def show_contact(*names):
    result_found = ""
    result_not = ""
    for name in names:
        if name in addressbook.data.keys():
            result_found += addressbook.display_contact(name)
        else: result_not += f"---------------------------------------------------------\n{name} not found\n"
    return f"{result_found}{result_not}"


@command_error
def handler(command, args):
    functions = {
                "hello": greeting,
                "help": help,
                "add": add,
                "add birthday": add_bday,
                "change": change,
                "phone": show_contact,
                "show all": addressbook.show_all,
                "search": addressbook.search,
                "add note": notebook.add_note,
                "add tag": notebook.add_tag,
                "remove tag": notebook.remove_tag,
                "edit note": notebook.edit_note,
                "remove note": notebook.remove_note,
                "search note": notebook.search_by_note,
                }
    return functions[command](*args)

def main():
    print("Greetings, user! Phonebook manager online")
    addressbook.load()
    notebook.load()
    while True:
        user_input = parcer(input('Enter a command: \n>>> '))
        command = user_input[0]
        user_input.remove(command)
        args = [arg for arg in user_input]
        #print(user_input)
        if command in ("goodbye", "close", "exit"):
            print("Goodbye!")
            break
        result = handler(command, args)
        if result == "":
            result = "Seems like your list of contacts is empty. Try adding some" 
        print(result)
    addressbook.save()
    notebook.save()

main()