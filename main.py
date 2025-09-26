# modul_4_1
"""
Module 4, Task 1

"""

from pathlib import Path

def total_salary(path):
    

    file_name = Path(path)
    salary = list()
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            for line in file:
                
                salary.append(int(line.split(",")[1].strip()))
    except Exception as e:
        print(f'{e} with file')
        return (0, 0)
    
    total_payroll = sum((salary))
    average_salary = total_payroll / len(salary)
    result = (total_payroll,int(average_salary))
    return result


# modul_4_2
"""
Modul 4, Task 2

"""
from pathlib import Path

def get_cats_info(path):
    
    file_name = Path(path)
    list_cat = []
    keys = ["id", "name","age"]
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            for line in file:
                
                elements = line.strip().split(",")
                list_cat.append(dict(zip(keys, elements)))
                
    except Exception as e:
        print(f'{e} with file')
    return list_cat

# modul_4_4

"""
Modul 4 , Task 4
Consol Bot CLI

"""

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args,contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    name, phone = args
    #contacts.get(name, "KeyError" )
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact not found."


def show_phone(args, contacts):
    name = args[0]
    return contacts.get(name, "Contact not found.")

    

def show_all(contacts):
    if contacts:# contacts [] -> False , contacts[  ...] -> True
        lines = []
        for name, phone in contacts.items():
            lines.append(f"{name}: {phone}")
        result = "\n".join(lines)
        return result
    return "No contacts found."


def main():
    
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args,contacts))
            
        elif command == "change":
            print(change_contact(args,contacts))
        elif command == "phone":
            print(show_phone(args,contacts))
        elif command == "all":
            print(show_all(contacts))


        else:
            print("Invalid command.")
    


if __name__ == "__main__":
    main()

