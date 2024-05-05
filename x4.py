def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Invalid input format."
        except IndexError:
            return "Not enough arguments provided."

    return inner

# Функція для додавання контакту
@input_error
def add_contact(args, contacts):
    if len(args) != 2:
        raise IndexError
    name, phone = args
    contacts[name] = phone
    return "Contact added."

# Функція для видалення контакту
@input_error
def delete_contact(args, contacts):
    if len(args) != 1:
        raise IndexError
    name = args[0]
    del contacts[name]
    return "Contact deleted."

# Функція для отримання номеру телефону
@input_error
def get_phone(args, contacts):
    if len(args) != 1:
        raise IndexError
    name = args[0]
    return contacts[name]

# Функція для отримання списку всіх контактів
@input_error
def get_all_contacts(args, contacts):
    if len(args) != 0:
        raise IndexError
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

def main():
    contacts = {}
    while True:
        command = input("Enter a command: ").strip().split()
        if command:
            cmd = command[0].lower()
            args = command[1:]
            if cmd == "add":
                print(add_contact(args, contacts))
            elif cmd == "delete":
                print(delete_contact(args, contacts))
            elif cmd == "phone":
                print(get_phone(args, contacts))
            elif cmd == "all":
                print(get_all_contacts(args, contacts))
            elif cmd == "exit":
                break
            else:
                print("Invalid command.")

if __name__ == "__main__":
    main()