# Реализация сортировки Шелла

def shell_sort(data: list[int]) -> list[int]:
    last_index = len(data)
    step = len(data)//2
    while step > 0:
        for i in range(step, last_index, 1):
            j = i
            delta = j - step
            while delta >= 0 and data[delta] > data[j]:
                data[delta], data[j] = data[j], data[delta]
                j = delta
                delta = j - step
        step //= 2
    return data


unsorted_array: list[int] = [2, 4, 5, 1, 3]
print("Unsorted list: ",  unsorted_array)
gap = len(unsorted_array)
print("sorted list: ", shell_sort(unsorted_array))
