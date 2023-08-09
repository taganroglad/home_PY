class Phonebook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone_number):
        self.contacts[name] = phone_number

    def update_contact(self, name, new_phone_number):
        if name in self.contacts:
            self.contacts[name] = new_phone_number
            print(f"Контакт {name} успешно обновлен.")
        else:
            print(f"Контакт {name} не найден.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Контакт {name} успешно удален.")
        else:
            print(f"Контакт {name} не найден.")

    def find_contact(self, name):
        if name in self.contacts:
            return f"Имя: {name}, Телефон: {self.contacts[name]}"
        else:
            return f"Контакт {name} не найден."

    def display_contacts(self):
        for name, phone_number in self.contacts.items():
            print(f"Имя: {name}, Телефон: {phone_number}")

def main():
    phonebook = Phonebook()

    while True:
        print("\nМеню:")
        print("1. Добавить контакт")
        print("2. Изменить контакт")
        print("3. Удалить контакт")
        print("4. Найти контакт")
        print("5. Показать все контакты")
        print("6. Выйти")
        choice = input("Выберите опцию: ")

        if choice == "1":
            name = input("Введите имя контакта: ")
            phone_number = input("Введите номер телефона: ")
            phonebook.add_contact(name, phone_number)
        elif choice == "2":
            name = input("Введите имя контакта для изменения: ")
            new_phone_number = input("Введите новый номер телефона: ")
            phonebook.update_contact(name, new_phone_number)
        elif choice == "3":
            name = input("Введите имя контакта для удаления: ")
            phonebook.delete_contact(name)
        elif choice == "4":
            name = input("Введите имя контакта для поиска: ")
            result = phonebook.find_contact(name)
            print(result)
        elif choice == "5":
            phonebook.display_contacts()
        elif choice == "6":
            break
        else:
            print("Некорректный выбор. Пожалуйста, выберите снова.")

if __name__ == "__main__":
    main()
