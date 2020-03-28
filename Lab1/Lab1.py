import collections
import string
import random


def word_counter(text):
    c = collections.Counter(text.split())
    print(c)
    for k, v in c.most_common(10):
        yield '{} - {}'.format(k, v)


def quick_sort(array, fst=0, lst=None):
    if lst is None:
        lst = len(array) - 1
    if fst >= lst:
        return
    i, j = fst, lst
    pivot = array[random.randint(fst, lst)]

    while i <= j:
        while array[i] < pivot:
            i += 1
        while array[j] > pivot:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i, j = i + 1, j - 1
    quick_sort(array, fst, j)
    quick_sort(array, i, lst)


def merge_sort(arr):
    n = len(arr)
    if n < 2:
        return arr

    l = merge_sort(arr[:n // 2])
    r = merge_sort(arr[n // 2:n])

    i = j = 0
    result = []
    while i < len(l) or j < len(r):
        if not i < len(l):
            result.append(r[j])
            j += 1
        elif not j < len(r):
            result.append(l[i])
            i += 1
        elif l[i] < r[j]:
            result.append(l[i])
            i += 1
        else:
            result.append(r[j])
            j += 1

    return result


def fibonacci(number):
    a, b = 0, 1
    while a < number:  # создаёт часть итерируемого объекта
        yield a
        a, b = b, a + b


filename = input()
with open(filename) as file_handler:
    fix = str.maketrans(dict.fromkeys(string.punctuation))
    for line in file_handler:
        line = line.translate(fix)
        for i in word_counter(line):
            print(i)

numbers1 = numbers2 = list(map(int, input().split()))

quick_sort(numbers1)
print(numbers1)
print(merge_sort(numbers2))

n = int(input())
for k in fibonacci(n):
    print(k)
