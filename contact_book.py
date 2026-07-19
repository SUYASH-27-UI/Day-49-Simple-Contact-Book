contacts = {}

while True:
    name = input("Enter contact name (or type 'done' to finish): ")

    if name.lower() == "done":
        break

    phone = input("Enter phone number: ")

    contacts[name] = phone

print("\nContact List:")

for name, phone in contacts.items():
    print(name, ":", phone)
