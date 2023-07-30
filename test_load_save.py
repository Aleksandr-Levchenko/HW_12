import pickle
import re

# Код классов Field, Name, Phone, Birthday и Record (см. ваше описание)

# Определение функции __reduce__ для каждого класса
def reduce_name(name):
    return (Name, (name.value,))

def reduce_phone(phone):
    return (Phone, (phone.value,))

def reduce_birthday(birthday):
    return (Birthday, (birthday.value,))

# Связываем функции reduce_* с соответствующими классами
pickle.Pickler.dispatch[Name] = reduce_name
pickle.Pickler.dispatch[Phone] = reduce_phone
pickle.Pickler.dispatch[Birthday] = reduce_birthday

def main():
    # Создаем объекты
    name = Name("John Doe")
    birthday = Birthday("31.12.1990")
    phones = [Phone("0931234567"), Phone("0507654321")]

    record = Record(name, birthday, phones)

    # Сериализация объекта record в файл
    with open("record.pkl", "wb") as file:
        pickle.dump(record, file)

    # Десериализация объекта record из файла
    with open("record.pkl", "rb") as file:
        loaded_record = pickle.load(file)

    # Проверка результатов десериализации
    print(loaded_record.name.value)        # Вывод: John Doe
    print(loaded_record.birthday.value)    # Вывод: 31.12.1990
    for phone in loaded_record.phones:
        print(phone.value)                 # Вывод: 0931234567, 0507654321

if __name__ == "__main__":
    main()
