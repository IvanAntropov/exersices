# Реализовать сортировку вставками
# В этой сортировке цифра сравнивается со всеми цифрами слева/справа и если оно больше/меньше то она двигается

def insertion_sort(array: list[int]) -> list[int]:
    array_length: int = len(array)
    for i in range(1, array_length):
        key_item = array[i]
        j = i - 1
        while j >= 0 and array[j] > key_item:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key_item
    return array


unsorted_array: list[int] = [2, 4, 5, 1, 3]
print("Unsorted list: ",  unsorted_array)
print("Sorted list: ", insertion_sort(unsorted_array))
