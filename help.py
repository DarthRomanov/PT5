
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


