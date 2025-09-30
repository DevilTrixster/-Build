import copy
import random
from abc import ABC, abstractmethod

# Базовый класс для всех фигур
class Shape(ABC):
    def __init__(self, name, cells):
        self.name = name
        self.cells = cells  # Количество клеток

    @abstractmethod
    def draw(self):
        pass

    def clone(self):
        """Реализация паттерна Prototype - создание копии объекта"""
        return copy.deepcopy(self)

    def __str__(self):
        return f"{self.name} ({self.cells} клеток)"


# Конкретные классы обычных фигур
class Square(Shape):
    def __init__(self):
        super().__init__("Квадрат", 4)

    def draw(self):
        return "▢"


class Triangle(Shape):
    def __init__(self):
        super().__init__("Треугольник", 3)

    def draw(self):
        return "△"


class Circle(Shape):
    def __init__(self):
        super().__init__("Круг", 1)  # Упрощенно - 1 клетка

    def draw(self):
        return "○"


# Классы супер-фигур (с большим числом клеток)
class SuperSquare(Shape):
    def __init__(self):
        super().__init__("Супер-квадрат", 16)  # Больше клеток

    def draw(self):
        return "■"


class SuperTriangle(Shape):
    def __init__(self):
        super().__init__("Супер-треугольник", 9)

    def draw(self):
        return "▲"


class SuperCircle(Shape):
    def __init__(self):
        super().__init__("Супер-круг", 4)  # Больше клеток

    def draw(self):
        return "●"


# Абстрактная фабрика (Factory Method)
class ShapeFactory(ABC):
    @abstractmethod
    def create_shape(self):
        pass


# Конкретные фабрики для обычных фигур
class SquareFactory(ShapeFactory):
    def create_shape(self):
        return Square()


class TriangleFactory(ShapeFactory):
    def create_shape(self):
        return Triangle()


class CircleFactory(ShapeFactory):
    def create_shape(self):
        return Circle()


# Конкретные фабрики для супер-фигур
class SuperSquareFactory(ShapeFactory):
    def create_shape(self):
        return SuperSquare()


class SuperTriangleFactory(ShapeFactory):
    def create_shape(self):
        return SuperTriangle()


class SuperCircleFactory(ShapeFactory):
    def create_shape(self):
        return SuperCircle()


# Класс для управления процессом выбора фигур
class ShapeSelector:
    def __init__(self):
        # Список всех доступных фабрик
        self.regular_factories = [
            SquareFactory(),
            TriangleFactory(),
            CircleFactory()
        ]

        self.super_factories = [
            SuperSquareFactory(),
            SuperTriangleFactory(),
            SuperCircleFactory()
        ]

        self.all_factories = self.regular_factories + self.super_factories

    def select_random_shape(self, super_probability=0.3):
        """Случайный выбор фигуры с вероятностью появления супер-фигуры"""
        if random.random() < super_probability:
            # Выбираем супер-фигуру
            factory = random.choice(self.super_factories)
        else:
            # Выбираем обычную фигуру
            factory = random.choice(self.regular_factories)

        return factory.create_shape()

    def select_specific_shape(self, shape_type, is_super=False):
        """Выбор конкретной фигуры по типу"""
        factories = self.super_factories if is_super else self.regular_factories

        for factory in factories:
            shape = factory.create_shape()
            if shape.name.lower() == shape_type.lower():
                return shape

        raise ValueError(f"Фигура типа '{shape_type}' не найдена")

    def create_shape_copy(self, shape):
        """Создание копии фигуры с использованием паттерна Prototype"""
        return shape.clone()


# Демонстрация работы
if __name__ == "__main__":
    selector = ShapeSelector()

    print("=== Случайный выбор фигур ===")
    for i in range(5):
        shape = selector.select_random_shape()
        print(f"{i + 1}. {shape} - {shape.draw()}")

    print("\n=== Создание копий фигур ===")
    original_shape = selector.select_specific_shape("квадрат")
    shape_copy = selector.create_shape_copy(original_shape)

    print(f"Оригинал: {original_shape}")
    print(f"Копия: {shape_copy}")

    # Проверка, что это разные объекты
    print(f"Это один и тот же объект? {original_shape is shape_copy}")

    print("\n=== Супер-фигуры ===")
    super_shape = selector.select_specific_shape("треугольник", is_super=True)
    print(f"Супер-фигура: {super_shape} - {super_shape.draw()}")

    print("\n=== Сравнение обычной и супер-фигуры ===")
    regular_triangle = selector.select_specific_shape("треугольник")
    super_triangle = selector.select_specific_shape("треугольник", is_super=True)

    print(f"Обычный: {regular_triangle}")
    print(f"Супер: {super_triangle}")