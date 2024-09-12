from collections import UserDict
from datetime import datetime
import re
import pickle




class Field:
    def __init__(self, value):
        self.value = value
    
    def __str__(self) -> str:
        return str(self.value)

class Name(Field):
    pass


class Phone(Field):


    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, value: str):
        if value.isalpha() or not value.startswith('+380') or len(value) != 13:
            raise ValueError
        self.__value = value

    def __repr__(self) -> str:
        return self.value
    
class Birthday(Field):
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if value is None:
            self.__value = value
        else:
            self.__value = self.__set_date(value)

    @staticmethod
    def __set_date(bday: str):
        date_types = ["%d/%m/%Y", "%d/%m"]
        for date_type in date_types:
            try:
                date = datetime.strptime(bday, date_type).date()
                return date
            except ValueError:
                pass
        raise TypeError("Incorrect date format, should be dd/mm/yyyy or dd/mm")
        
    def __str__(self) -> str:
        return str(self.value)
    
class Adress(Field):
    pass

class Email(Field):
    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, val):
        if re.match(r'[a-zA-Z]{1}\S+@[a-zA-Z]+\.\w\w+', val):
            self.__value = val
        else:
            self.__value = 'E-mail doesn`t correct'
    







class Record:
    def __init__(self, name: Name, phones: list[Phone] = [], birthday = None, adress: Adress = None, email:Email = None) -> None:
        self.name = name
        self.phones = phones
        self.birthday = birthday
        self.adress = adress
        self.email = email

    def days_to_birthday(self):
        self.day = int(self.birthday.split('/')[0])
        self.month = int(self.birthday.split('/')[1])
        today = datetime.today()
        bd_date = datetime(day= self.day, month= self.month, year= today.year)
        count_days = bd_date-today
        return f'{count_days.days} days'

    def add_phone(self, name: Name, phone: Phone):
        if phone not in self.phones:
            self.phones.append(phone)
            return f'I add new number phone {phone.value} to contact {name.value}.'
        else:
            return 'This phone number already exists.'
        
    def dell_phone(self, name:Name, phone: Phone):
        for p in self.phones:
            if p.value == phone.value:
                self.phones.remove(p)
                return f'I remove number phone {p.value}.'
        return f"I don't find this number."
    
    def change(self, name: Name ,phone: Phone, new_phone: Phone):
        self.dell_phone(name, phone)
        self.add_phone(name, new_phone)
        return 'Done!'

    def __str__(self) -> str:
        return ', '.join([str(p) for p in self.phones])
    
    def __repr__(self) -> str:
        return str(self)




class AddressBook(UserDict):
    index = 0
    def add_contact(self, record: Record):
        self.data[record.name.value] = record

    def find_phone(self, name: Name):
        for contact in self.data:
            if contact == name.value:
                return self.data[contact]
        return "I don't find this contact"
    def dell_contact(self, name: Name):
        for contact in self.data:
            if contact == name.value:
                self.data.pop(contact)
                return f"I removed contact{name}."
        return 'I dont find contact.'
    
    def save_file (self):
        name_file = 'contacts.bin'
        with open(name_file, "wb") as fh:
            pickle.dump(self.data, fh)

    def read_file(self):
        name_file = 'contacts.bin'
        with open(name_file, "rb") as fh:
            self.data = pickle.load(fh)
    
    def iteranor(self, step):
        lst = [f'{key}: {val.phones}' for key, val in self.data.items()]
        lst_slice = lst[self.index:self.index + int(step)]
        if self.index < len(lst):
            self.index += int(step)
        result = '\n'.join(lst_slice)
        return result
    
    def find(self, value):
        for key, rec in self.data.items():
            if value in key:
                print(f'{key}: {rec.phones}')
            else:
                for phone in rec.phones:
                    if value in phone.value:
                        print(f'{key}: {rec.phones}')

        return ''
    
        
    def __str__(self):
        result = []
        for record in self.data.values():
            result.append(f"{record.name.value}: {', '.join([phone.value for phone in record.phones])} Birthday: {record.birthday}")
        return "\n".join(result)








def maint():
    print(Email('qwe'))

if __name__=='__main__':
    maint()