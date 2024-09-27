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

    def to_dict(self): # Перетворює всю інформацію про нотатки у словник, придатний для запису у файл
        data = {}
        for name, note in self.data.items():
            data[name] = {"text": note.value,"tags": note.tags}
        return data

    def from_dict(self, file_data): # Перетворює словник із файлу в інформацію про нотатки
        for name, value in file_data.items():
            note = Note(name, value["text"])
            note.tags = value["tags"]
            self.data[note.name] = note

    def save(self): # Зберігає словник у файл json
        converted_data = self.to_dict()
        with open("notebook_data.json", "w") as file:
            json.dump(converted_data, file)

    def load(self): # Завантажує словник із файлу json
        try:
            with open("notebook_data.json", "r") as file:
                recovered_data = json.load(file)
            if recovered_data != {}:
                self.from_dict(recovered_data)
        except FileNotFoundError:
            print("notebook_data.json was not found")

############################################################################################################################################################################################################


notebook = Notebook() # Створюємо екземпляр класу 


############################################################################################################################################################################################################


# Команди для роботи з нотатками:

# {"command": "add note, text", "description": "Add a new note."},
# {"command": "remove note, note name", "description": "Remove an existing note."},
# {"command": "edit note, note name, new text", "description": "Replace the text of an existing note."},
# {"command": "search note, keyword", "description": "Display all notes, containing the keyword (or multiple keywords) in it's name, text or tags. If the keyword is not specified, display all notes."},
# {"command": "add tag, note name, tag", "description": "Add a tag (or multiple tags) to an existing note."},
# {"command": "remove tag, note name, tag", "description": "Remove tag (or multiple tags) from an existing note"}