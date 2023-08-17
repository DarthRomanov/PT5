

def main():
    print("Greetings, user! Phonebook manager online")
    
    #file_path = 'contacts.bin'
    #try:
    #    address_book = Addressbook.load(file_path)
    #except FileNotFoundError:
    #    address_book = Addressbook()

    close_book = ['exit', 'close', 'goodbye', 'bye', 'see you', 'bb', 'off', 'out']
    yes_input = ['y', 'yes', '+', 'ok', 'right', 'sure', 'yep', 'course']
    grettings = ['hello', 'hi', 'hey', 'yo', 'morning', 'afternoon', 'evening', 'sup', 'hiya']
    supports = 'Type "help" to see the list of commands'

    while True:
        first_input = input('Enter a command: \n>>> ')
        if first_input.lower() in grettings:
            print('Hello! How can I help you?')
        elif first_input.lower() in ['menu', 'guide', 'commands', 'men', 'comand', 'command']:
            help_correct_input = input('Do you mean, that you would like to see available commands? y/n >>> ')
            print("If you'd like to see available comands, use this command  ->  help") \
                if help_correct_input.lower() in yes_input else print('Please, use the available commands')
        #elif any(word in first_input.lower() for word in ['note ', 'not', 'noter', 'nots', 'message', 'reminder', 'record', 'notes', 'notation', 'comment', 'remark']):
        #    note_correct_input = input('Do you mean, that you would like to work with notes? 1. Add. 2. Search by note. 3. Remove. 4. Edit.  1/2/3/4 >>> ')
        #    if note_correct_input == '1':
        #        print("If you'd like to add note, use this command  ->  add, note_name, text")
        #    elif note_correct_input == '2':
        #        print("If you'd like to search by note, use this command  ->  search, text")
        #    elif note_correct_input == '3':
        #        print("If you'd like to remove note, use this command  ->  remove, note_name")
        #    elif note_correct_input == '4':
        #        print("If you'd like to edit the note, use this command  ->  edit, note_name, text")
        #    else:
        #        print(supports)
        
        elif any(word in first_input.lower() for word in [' add birthday', ' birthday ', 'birthday ', 'bday', 'birthdate', 'bd', 'birth', 'date']):
                birthday_correct_input = input('Do you mean, that you would like to add birthday date to a contact? y/n >>> ')
                print("If you'd like to add birthday date to a contact, use this command  ->  add birthday, name, day.month.year") \
                    if birthday_correct_input.lower() in yes_input else print(supports)
        elif any(word in first_input.lower() for word in [' add ', ' add', 'ad', 'aad', 'append', 'plus', 'put', 'join', 'include']):
                add_correct_input = input('Do you mean, that you would like to add a contact? y/n >>> ')
                print("If you'd like to add contact, use this command  ->  add, name, phone_number") \
                    if add_correct_input.lower() in yes_input else print(supports)
        elif any(word in first_input.lower() for word in [' change ', ' change', 'change ', 'swap', 'exchange', 'rewrite', 'switch', 'replace', 'new']):
                change_correct_input = input('Do you mean, that you would like to change the contact? y/n >>> ')
                print("If you'd like to change the contact, use this command  ->  change, name, new_phone_number") \
                    if change_correct_input.lower() in yes_input else print(supports)
        elif any(word in first_input.lower() for word in [' show', 'see', ' show all', 'show me', 'aal', 'show all ', 'display', 'look', 'watch', 'view', 'each']):
                show_contact_correct_input = input('Do you mean, that you would like to see contacts? 1. Show all or show by pages. 2. Show phone number by name. 1/2 >>> ')
                if show_contact_correct_input == '1':
                    print("If you'd like to see all contacts, use this command  ->  show all")
                    print("If you'd like to see contacts by pages, use this command  ->  show all, number.\nNumber (optional) indicates the amount of contacts displayed per page")
                elif show_contact_correct_input == '2':
                    print("If you'd like to see the phone number by name, use this command  ->  phone, name")
                else:
                    print(supports)

        #elif any(word in first_input.lower() for word in [' remove', 'remov', ' delete', 'del', 'cut off', 'take out', 'clean']):
        #        remove_correct_input = input('Do you mean, that you would like to remove the phone? y/n >>> ')
        #        print("If you'd like to remove the phone, use this command  ->  remove, name") \
        #            if remove_correct_input.lower() in yes_input else print(supports)
        #elif any(word in first_input.lower() for word in ['find', ' search', 'seach', 'searh', 'sarch', 'serch', 'realize', 'notice', 'detect']):
        #        search_correct_input = input('Do you mean, that you would like to search smth? y/n >>> ')
        #        print("If you'd like to search smth, use this command  ->  search ...") \
        #            if search_correct_input.lower() in yes_input else print(supports)
        
        #elif any(word in first_input.lower() for word in ['marker', 'keyword', 'keywords', 'label', 'sticker', 'teg', 'tags', 'tegs']):
        #        tag_correct_input = input('Do you mean, that you would like to add or remove tag? 1. Add tag. 2. Remove tag. 1/2 >>> ')
        #        if tag_correct_input == '1':
        #            print("If you'd like to add tag, use this command  ->  add, note_name, tag")
        #        elif tag_correct_input == '2':
        #            print("If you'd like to remove tag, use this command  ->  remove, note_name, tag")
        #        else:
        #            print(supports)

        else:
            user_input = parcer(first_input)
            command = user_input[0]
            user_input.remove(command)
            args = [arg for arg in user_input]
        
            if command in close_book:
                #addressbook.save(file_path)
                print("Goodbye!")
                break
        
        
            result = handler(command, args)
            if result == "":
                result = "Seems like your list of contacts is empty. Try adding some" 
            print(result)

main()
