class Elevator:
    _instance = None
    _initialized = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Elevator, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not Elevator._initialized:
            self.current_floor = 1
            self.direction = 0  # 0 - стоит, 1 - вверх, -1 - вниз
            self.is_moving = False
            self.capacity = 10
            self.occupants = 0
            Elevator._initialized = True

    def move_to_floor(self, floor):
        if floor == self.current_floor:
            print(f"Лифт уже на этаже {floor}")
            return

        self.direction = 1 if floor > self.current_floor else -1
        self.is_moving = True

        print(f"Лифт движется с этажа {self.current_floor} на этаж {floor}")
        self.current_floor = floor
        self.is_moving = False
        self.direction = 0
        print(f"Лифт прибыл на этаж {self.current_floor}")

    def add_occupants(self, count):
        if self.occupants + count <= self.capacity:
            self.occupants += count
            print(f"В лифт вошли {count} человек. Теперь в лифте: {self.occupants}")
        else:
            print(f"Недостаточно места в лифте. Максимум: {self.capacity}")

    def remove_occupants(self, count):
        if self.occupants >= count:
            self.occupants -= count
            print(f"Из лифта вышли {count} человек. Теперь в лифте: {self.occupants}")
        else:
            print(f"В лифте недостаточно людей. Сейчас в лифте: {self.occupants}")

    def get_status(self):
        status = "движется" if self.is_moving else "стоит"
        direction = "вверх" if self.direction == 1 else "вниз" if self.direction == -1 else ""
        return f"Лифт на этаже {self.current_floor}, {status} {direction}. Пассажиров: {self.occupants}/{self.capacity}"


class Room:
    def __init__(self, number, room_type="Офис"):
        self.number = number
        self.type = room_type

    def __str__(self):
        return f"{self.type} №{self.number}"


class Floor:
    def __init__(self, number, rooms_count=5):
        self.number = number
        self.rooms = [Room(i + 1) for i in range(rooms_count)]
        self.elevator = Elevator()  # Все этажи ссылаются на один и тот же лифт

    def call_elevator(self):
        print(f"Вызов лифта на этаж {self.number}")
        self.elevator.move_to_floor(self.number)

    def __str__(self):
        return f"Этаж {self.number}. Помещения: {len(self.rooms)}"


class Building:
    _instance = None
    _initialized = False

    def __new__(cls, name="Бизнес-центр", floors_count=10):
        if cls._instance is None:
            cls._instance = super(Building, cls).__new__(cls)
        return cls._instance

    def __init__(self, name="Бизнес-центр", floors_count=10):
        if not Building._initialized:
            self.name = name
            self.floors = [Floor(i + 1) for i in range(floors_count)]
            self.elevator = Elevator()  # Здание также ссылается на единственный лифт
            Building._initialized = True

    def get_floor(self, number):
        if 1 <= number <= len(self.floors):
            return self.floors[number - 1]
        return None

    def building_info(self):
        return f"Здание: {self.name}. Этажей: {len(self.floors)}. {self.elevator.get_status()}"


# Демонстрация работы системы
if __name__ == "__main__":
    print("=== Создание первого здания ===")
    building1 = Building("Башня А", 5)
    print(building1.building_info())

    print("\n=== Создание второго здания (должно вернуть тот же экземпляр) ===")
    building2 = Building("Башня Б", 20)  # Параметры игнорируются, т.к. здание уже создано
    print(building2.building_info())

    print("\n=== Проверка, что это один и тот же объект ===")
    print(f"building1 is building2: {building1 is building2}")

    print("\n=== Работа с лифтом ===")
    elevator1 = Elevator()
    elevator2 = Elevator()

    print(f"elevator1 is elevator2: {elevator1 is elevator2}")
    print(f"Лифт в building1 это elevator1: {building1.elevator is elevator1}")

    print("\n=== Демонстрация работы лифта ===")
    # Вызов лифта на 3 этаж
    third_floor = building1.get_floor(3)
    third_floor.call_elevator()

    # Добавление людей в лифт
    elevator1.add_occupants(3)

    # Перемещение лифта на 1 этаж
    first_floor = building1.get_floor(1)
    first_floor.call_elevator()

    # Выход людей из лифта
    elevator1.remove_occupants(2)

    print("\n=== Проверка статуса через разные ссылки ===")
    print(f"Через building1: {building1.elevator.get_status()}")
    print(f"Через elevator1: {elevator1.get_status()}")
    print(f"Через этаж: {third_floor.elevator.get_status()}")

    print("\n=== Информация о здании ===")
    for floor in building1.floors:
        print(floor)