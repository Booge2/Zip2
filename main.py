import json
import time
import pickle


class Timer:
    def __init__(self):
        self.start_time = 0
        self.elapsed_time = 0

    def save_state(self):
        with open("timer_state.json", "w") as file:
            json.dump({"start_time": self.start_time, "elapsed_time": self.elapsed_time}, file)

    def load_state(self):
        try:
            with open("timer_state.json", "r") as file:
                data = json.load(file)
                self.start_time = data["start_time"]
                self.elapsed_time = data["elapsed_time"]
        except FileNotFoundError:
            pass

    def start(self):
        self.load_state()
        self.start_time = time.time()
        self.save_state()
        print("Таймер почав відлік.")

    def stop(self):
        elapsed_time = time.time() - self.start_time
        self.elapsed_time += elapsed_time
        self.save_state()
        print("Таймер зупинений.")

    def display(self):
        self.load_state()
        total_time = self.elapsed_time
        print("Пройшло часу:", total_time, "секунд")


def main():
    timer = Timer()
    while True:
        print("\nМеню:")
        print("1. Старт таймера")
        print("2. Зупинка таймера")
        print("3. Відображення часу")
        print("0. Вихід")

        choice = input("Виберіть опцію: ")

        if choice == "1":
            timer.start()
        elif choice == "2":
            timer.stop()
        elif choice == "3":
            timer.display()
        elif choice == "0":
            break
        else:
            print("Неправильний вибір опції.")


if __name__ == "__main__":
    main()


# Завдання 2

class TaskManager:
    def __init__(self):
        self.tasks = []

    def load_tasks(self):
        try:
            with open("tasks.json", "r", encoding="utf-8") as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            print("Файл з завданнями не знайдено. Створено новий список завдань.")

    def save_tasks(self):
        with open("tasks.json", "w", encoding="utf-8") as file:
            json.dump(self.tasks, file)
        print("Завдання збережено.")

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            self.save_tasks()
        else:
            print("Завдання не знайдено.")

    def display_tasks(self):
        print("Список завдань:")
        for idx, task in enumerate(self.tasks, 1):
            print(f"{idx}. {task}")


def main():
    task_manager = TaskManager()
    task_manager.load_tasks()

    while True:
        print("\nМеню:")
        print("1. Додати завдання")
        print("2. Видалити завдання")
        print("3. Показати завдання")
        print("0. Вихід")

        choice = input("Виберіть опцію: ")

        if choice == "1":
            new_task = input("Введіть нове завдання: ")
            task_manager.add_task(new_task)
        elif choice == "2":
            task_to_remove = input("Введіть завдання для видалення: ")
            task_manager.remove_task(task_to_remove)
        elif choice == "3":
            task_manager.display_tasks()
        elif choice == "0":
            task_manager.save_tasks()
            break
        else:
            print("Неправильний вибір опції.")


if __name__ == "__main__":
    main()


# Завдання 3


class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def pack_in_json(self):
        fraction_dict = {"numerator": self.numerator, "denominator": self.denominator}
        return json.dumps(fraction_dict)

    @staticmethod
    def unpacked_with_json(json_str):
        fraction_dict = json.loads(json_str)
        return Fraction(fraction_dict["numerator"], fraction_dict["denominator"])

    def pack_in_pickle(self):
        return pickle.dumps(self)

    @staticmethod
    def unpacked_with_pickle(pickle_data):
        return pickle.loads(pickle_data)


fraction = Fraction(3, 4)

json_data = fraction.pack_in_json()
print("JSON дані:", json_data)

unpacked_fraction = fraction.unpacked_with_json(json_data)
print("Розпакований fraction:", unpacked_fraction.numerator, "/", unpacked_fraction.denominator)

pickle_data = fraction.pack_in_pickle()
print("Pickle дані:", pickle_data)

unpacked_fraction = fraction.unpacked_with_pickle(pickle_data)
print("Розпакований fraction:", unpacked_fraction.numerator, "/", unpacked_fraction.denominator)


# Завдання 4


class Clock:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def pack_in_json(self):
        return json.dumps({"hours": self.hours, "minutes": self.minutes, "seconds": self.seconds})

    @staticmethod
    def unpacked_with_json(json_data):
        dct_clock = json.loads(json_data)
        return Clock(dct_clock["hours"], dct_clock["minutes"], dct_clock["seconds"])

    def pack_in_pickle(self):
        return pickle.dumps({"hours": self.hours, "minutes": self.minutes, "seconds": self.seconds})

    @staticmethod
    def unpacked_with_pickle(pickle_data):
        dct_clock = pickle.loads(pickle_data)
        return Clock(dct_clock["hours"], dct_clock["minutes"], dct_clock["seconds"])


clock = Clock(10, 30, 45)

json_data = clock.pack_in_json()
print("JSON дані:", json_data)

unpacked_clock = clock.unpacked_with_json(json_data)
print("Розпакований годинник:", unpacked_clock.hours, "год", unpacked_clock.minutes, "хв", unpacked_clock.seconds, "сек")

pickle_data = clock.pack_in_pickle()
print("Pickle дані:", pickle_data)

unpacked_clock = clock.unpacked_with_pickle(pickle_data)
print("Розпакований годинник:", unpacked_clock.hours, "год", unpacked_clock.minutes, "хв", unpacked_clock.seconds, "сек")
