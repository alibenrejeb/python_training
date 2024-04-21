import random

def generate_random_list(n, min, max):
    random_list = []
    for i in range(0, n):
        random_int = random.randint(min,max)
        random_list.append(random_int)
    return random_list

def selection_sort(l: list):
    for unsorted_index in range(0, len(l)):
        min = l[unsorted_index]
        min_index = unsorted_index
        for i in range(unsorted_index + 1, len(l)):
            if l[i] < min:
                min = l[i]
                min_index = i
        l[unsorted_index], l[min_index] = l[min_index], l[unsorted_index]
    return l

def quick_sort(l: list, start: int, end: int):
    pivot = l[end - 1]
    cursor = start

    if end - start < 1:
        return l

    for i in range(start, end -1):
        if l[i] < pivot:
            l[cursor], l[i] = l[i], l[cursor]
            cursor += 1
    l[end -1], l[cursor] = l[cursor], l[end -1]

    quick_sort(l, start, cursor)
    return quick_sort(l, cursor+1, end)

l = generate_random_list(10, -1000, 1000)
print(l)
print(selection_sort(l))
print(quick_sort(l, 0, len(l)))