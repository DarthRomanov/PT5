

def cheker(text):
    yes_input = ['y', 'yes', '+', 'ok', 'right', 'sure', 'yep', 'course']
    if any(word in text.lower() for word in ['add', 'ad', 'aad', 'aadd', 'append', 'plus', 'put', 'join', 'include']):
        add_correct_input = input('Do you mean, that you would like to add something? \nFour options (please, choose one): 1. Contact. 2. Birthday. 3. Note. 4. Tag. 1/2/3/4 >>> ')
        if add_correct_input == '1':
            print("If you'd like to add contact, use this command  ->  add contact, name, phone_number, birthday, address, email. \nBirthday, address and email are optional.")
        elif add_correct_input == '2':
            print("If you'd like to add birthday for contact, use this command  ->  add birthday, name, birthday. \nFormat of birthday looks like this: day.month.year")
        elif add_correct_input == '3':
            print("If you'd like to add note, use this command  ->  add note, text")
        elif add_correct_input == '4':
            print("If you'd like to add tag, use this command  ->  add tag, note, tag")
        else:
            print('Unknown command, type "help" to see the list of commands')
    elif any(word in text.lower() for word in ['remove', 'delete', 'rem', 'remowe', 'remov', 'del', 'delet', 'cut off', 'cut', 'take out', 'clean']):
        remove_correct_input = input('Do you mean, that you would like to delete something? \nFour options (please, choose one): 1. Phone. 2. Contact. 3. Note. 4. Tag. 1/2/3/4 >>> ')
        if remove_correct_input == '1':
            print("If you'd like to delete phone, use this command  ->  delete phone, name, phone_number")
        elif remove_correct_input == '2':
            print("If you'd like to delete contact, use this command  ->  delete contact, name, phone_number")
        elif remove_correct_input == '3':
            print("If you'd like to remove note, use this command  ->  remove note, note_name")
        elif remove_correct_input == '4':
            print("If you'd like to remove tag, use this command  ->  remove tag, note_name, tag")
        else:
            print('Unknown command, type "help" to see the list of commands')
    elif any(word in text.lower() for word in [' find', 'fnd', 'fid', 'search ', 'seach', 'searh', 'sarch', 'serch', 'realize', 'notice', 'detect']):
        find_correct_input = input('Do you mean, that you would like to find something? \nThree options (please, choose one): 1. Phone. 2. Information about contact by part of name or phone. 3. Search for notes.  1/2/3 >>> ')
        if find_correct_input == '1':
            print("If you'd like to find phone, use this command  ->  find phone, name")
        elif find_correct_input == '2':
            print("If you'd like to find information about contact, use this command  ->  find, part of name/phone")
        elif find_correct_input == '3':
            print("If you'd like to search for notes, use this command  ->  search, keyword")
        else:
            print('Unknown command, type "help" to see the list of commands')
    elif any(word in text.lower() for word in ['change', ' change', 'chage', 'chenge', 'swap', 'exchange', 'rewrite', 'switch', 'replace', 'new']):
        change_correct_input = input('Do you mean, that you would like to change the phone? y/n >>> ')
        print("If you'd like to change the phone, use this command  ->  change phone, name, new_phone_number") \
            if change_correct_input.lower() in yes_input else print('Unknown command, type "help" to see the list of commands')
    elif any(word in text.lower() for word in ['birthday', 'day', ' birthday ', 'birthday ', 'bday', 'birthdate', 'bd', 'birth', 'date']):
        birthday_correct_input = input('Do you mean, that you would like to do smth with birthday? \nTwo options (please, choose one): 1. Add birthday. 2. Days to birthday. 1/2 >>> ')
        if birthday_correct_input == '1':
            print("If you'd like to add birthday to contact, use this command  ->  add birthday, name, birthday \nFormat of birthday looks like this: day.month.year")
        elif birthday_correct_input == '2':
            print("If you'd like to see how many days to birthday of contact, use this command  ->  days to birthday, name")
        else:
            print('Unknown command, type "help" to see the list of commands')
    elif any(word in text.lower() for word in [' show', 'show', 'see', ' show all', 'show me', 'aal', 'display', 'look', 'watch', 'view', 'each']):
        show_contact_correct_input = input('Do you mean, that you would like to see contacts?  y/n >>> ')
        print("If you'd like to see the contacts, use this command  ->  show all") \
            if show_contact_correct_input.lower() in yes_input else print('Unknown command, type "help" to see the list of commands')
    elif any(word in text.lower() for word in ['note ', 'not', 'note', 'noter', 'nots', 'message', 'reminder', 'record', 'notes', 'notation', 'comment', 'remark']):
        note_correct_input = input('Do you mean, that you would like to do smth with notes? \nTwo options (please, choose one): 1. Add. 2. Remove.  1/2 >>> ')
        if note_correct_input == '1':
            print("If you'd like to add note, use this command  ->  add note, text")
        elif note_correct_input == '2':
            print("If you'd like to remove note, use this command  ->  remove note, note_name")
        else:
            print('Unknown command, type "help" to see the list of commands')
    elif any(word in text.lower() for word in ['marker', 'key', 'keyword', 'keywords', 'label', 'sticker', 'tag', 'teg', 'tags', 'tegs']):
        tag_correct_input = input('Do you mean, that you would like to do smth with tag? \nTwo options (please, choose one): 1. Add. 2. Remove. 1/2 >>> ')
        if tag_correct_input == '1':
            print("If you'd like to add tag, use this command  ->  add tag, note, tag")
        elif tag_correct_input == '2':
            print("If you'd like to remove tag, use this command  ->  remove tag, note, tag")
        else:
            print('Unknown command, type "help" to see the list of commands')
    elif any(word in text.lower() for word in ['clean', 'sort', 'file', 'files', 'cleen', 'clen', 'classify', 'category']):
        cleaner_correct_input = input('Do you mean, that you would like to sort all file by folder?  y/n >>> ')
        print("If you'd like to sort all file by folder, use this command  ->  cleaner, folder") \
            if cleaner_correct_input.lower() in yes_input else print('Unknown command, type "help" to see the list of commands')
    elif any(word in text.lower() for word in ['hi', 'hey', 'yo', 'morning', 'afternoon', 'evening', 'sup', 'hiya']):
        print('Hello! How can I help you?')
    