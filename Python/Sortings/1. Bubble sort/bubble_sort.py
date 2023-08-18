# Реализация сортировки пузырьком

def bubble_sort(array: list[int]) -> list[int]:
    array_length = len(array)  # The length of the array list
    for i in range(array_length - 1):  # The first loop where you choose which digit you will move
        flag: int = 0  # The flag for break
        for j in range(0, array_length - 1):  # The second loop where you move a one digit to end
            if array[j] > array[j + 1]:
                helper: int = array[j + 1]
                array[j + 1] = array[j]
                array[j] = helper
                flag = 1
                if flag == 0:
                    break
    return array


unsorted_array: list[int] = [2, 4, 5, 1, 3]
print(bubble_sort(unsorted_array))
