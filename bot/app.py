def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    if len(args) != 2:
        return "Incorrect arguments quantity. To add a new contact use 'add <name> <phone>' command."
    name, phone = args
    if name in contacts:
        return (f"User with name {name} already exists in contacts. "
                f"If you want to update the phone number please use add {name} {phone}.")
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    if len(args) != 2:
        return "Incorrect arguments quantity. For changing use 'change <name> <phone>' command."
    name, phone = args
    if name not in contacts:
        return f"{name} doesn't exist in the contacts. Use 'add {name} {phone}' command for adding a new contact."
    contacts[name] = phone
    return "Contact changed."


def get_phone(args, contacts):
    if len(args) != 1:
        return "Incorrect arguments quantity. To get the user's phone number please use 'phone <name>' command."
    name = args[0]
    if name not in contacts:
        return f"{name} doesn't exist in the contacts."
    return f"{name}'s phone: {contacts[name]}"


def get_all_contacts(contacts):
    items = contacts.items()
    if len(items) == 0:
        return "Contacts are empty. To add a new contact please use 'add <name> <phone>' command."
    return "\n".join([f"{name}'s phone: {phone}" for name, phone in items])


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
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(get_phone(args, contacts))
        elif command == "all":
            print(get_all_contacts(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()