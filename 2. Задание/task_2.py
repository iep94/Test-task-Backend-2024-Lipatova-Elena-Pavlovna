def custom_sort(A, B):
    # Создаем словарь для хранения индексов элементов из массива B
    index_map = {val: i for i, val in enumerate(B)}
    
    # Сортируем массив A с использованием кастомной функции сортировки
    A.sort(key=lambda x: (index_map.get(x, len(B)), -x))
    
    return A

A = [2, 4, 1, 3, 2, 4, 6, 7, 9, 2, 19]
B = [2, 1, 4, 3, 6, 9]

result = custom_sort(A, B)
print(result)