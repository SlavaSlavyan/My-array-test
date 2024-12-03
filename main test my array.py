class MyArray:
    def __init__(self):
        self.size = 0  # Количество элементов
        self.first_element = None  # Указатель на первый элемент
        self.last_element = None  # Указатель на последний элемент

    class Node:
        """Вспомогательный класс для хранения элемента и ссылки на следующий."""
        def __init__(self, value):
            self.value = value
            self.next = None

    def append(self, value):
        """Добавляет элемент в конец массива."""
        new_node = self.Node(value)  # Создаем новый узел
        if self.first_element is None:  # Если массив пуст
            self.first_element = new_node
            self.last_element = new_node
        else:
            self.last_element.next = new_node  # Присоединяем новый узел к концу
            self.last_element = new_node  # Обновляем указатель на последний элемент
        self.size += 1  # Увеличиваем размер

    def get(self, index):
        """Возвращает элемент по индексу."""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        current = self.first_element
        for _ in range(index):
            current = current.next  # Перемещаемся к нужному элементу
        return current.value

    def remove(self, index):
        """Удаляет элемент по индексу."""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        
        if index == 0:  # Удаление первого элемента
            self.first_element = self.first_element.next
            if self.first_element is None:  # Если массив стал пустым
                self.last_element = None
        else:
            current = self.first_element
            for _ in range(index - 1):
                current = current.next  # Находим элемент перед удаляемым
            current.next = current.next.next  # Удаляем узел

            if current.next is None:  # Если удаляем последний элемент
                self.last_element = current  # Обновляем указатель на последний элемент

        self.size -= 1  # Уменьшаем размер

    def __len__(self):
        """Возвращает количество элементов в массиве."""
        return self.size

    def __str__(self):
        """Строковое представление массива без использования готовых массивов."""
        current = self.first_element
        result = "["  # Начинаем строку с открывающей квадратной скобки
        if current is not None:
            result += str(current.value)  # Добавляем первый элемент
            current = current.next  # Переходим к следующему элементу
        while current is not None:  # Пока есть элементы
            result += ", " + str(current.value)  # Добавляем запятую и следующий элемент
            current = current.next  # Переходим к следующему элементу
        result += "]"  # Закрываем строку квадратной скобкой
        return result


# Пример использования
my_array = MyArray()
my_array.append(1)
my_array.append(2)
my_array.append(3)
print(my_array)  # [1, 2, 3]
print(my_array.get(1))  # 2
my_array.remove(1)
print(my_array)  # [1, 3]
print(len(my_array))  # 2
print(my_array.get(500))