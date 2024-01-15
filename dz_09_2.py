#phones_dict = {"Anonim Anonimenko": "+380969998877", "Biba Bobenko": "+380969998875", "Pupa Vasenko": "+380969998873"}
phones_dict = {"Anonim Anonimenko": "0969998877", "Biba Bobenko": "0969998875", "Pupa Vasenko": "0969998873"}
stop_words = ["good bye", "close", "exit"]


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found"
        except ValueError:
            return "Incorrect phone number"
        except IndexError:
            return "Give me name and phone please"
    return wrapper

# я заглянула в условия следующего ДЗ (10го ДЗ), там просят делать валидацию формата номера телефона, чтобы он содержал 10 цифр
# сделаю так же и здесь
@input_error
def add_phone(user_input):
    new_name_and_phone = user_input.split(" ", 1)
    new_name = new_name_and_phone[1].rsplit(" ", 1)[0]
    new_phone = new_name_and_phone[1].rsplit(" ", 1)[1]

    if new_phone.isdigit() and len(new_phone) == 10:
        phones_dict[new_name] = new_phone
    else:
        raise ValueError


@input_error
def change_phone(user_input):
    new_phone = user_input.split(" ")
    exist_name_new_phone = user_input.split(" ", 1)
    exist_name = exist_name_new_phone[1].rsplit(" ", 1)[0]
    new_phone = exist_name_new_phone[1].rsplit(" ", 1)[1]

    if new_phone.isdigit() and len(new_phone) == 10:
        phones_dict[exist_name] = new_phone
    else:
        raise ValueError

    if exist_name in phones_dict.keys():
        phones_dict[exist_name] = new_phone
    else:
        raise IndexError


@input_error
def show_phone(user_input):
    exist_name = user_input.split(" ", 1)[1]
    return f"{exist_name}: {phones_dict[exist_name]}"


#@input_error
def main():
    while True:
        user_input = (input("Enter some command please: "))
        user_input_lower = user_input.lower()

        if user_input_lower == "hello":
            print("How can I help you?")

        if user_input_lower.startswith("add"):
            print(add_phone(user_input))

        if user_input_lower.startswith("change"):
            print(change_phone(user_input))

        if user_input_lower.startswith("phone"):
            print(show_phone(user_input))

        if user_input_lower == "show all":
            for key, value in phones_dict.items():
                print (f"{key}: {value}")

        if user_input_lower in stop_words:
            print("Good bye!")
            break


main()

#print(phones_dict)



