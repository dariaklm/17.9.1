def num_sort(list_int):
    for i in range(1, len(list_int)):
        x = list_int[i]
        idx = i
        while idx > 0 and list_int[idx - 1] > x:
            list_int[idx] = list_int[idx - 1]
            idx -= 1
        list_int[idx] = x
    return list_int

def index_search(array, element, left, right):
    if left > right:
        return right
    middle = (right + left) // 2
    if array[middle] == element:
        return middle
    elif element < array[middle]:
        return index_search(array, element, left, middle - 1)
    else:
        return index_search(array, element, middle + 1, right)

nums = input("Введите последовательность чисел через пробел: ")
nums_list = list(map(int, nums.split()))
nums_sorted = num_sort(nums_list)
print("Числа по возрастанию: ", nums_sorted)
element = int(input("Введите любое число: "))

for i in nums_sorted:
   if  min(nums_sorted) > element:
     print("Число не соответствует заданному условию, повторите ввод: ")
     element = int(input("Введите любое число: "))
   elif  max(nums_sorted) < element:
       print("Число не соответствует заданному условию, повторите ввод. ")
       element = int(input("Введите любое число: "))
   elif i== element:
       break
element_index = index_search(nums_sorted, element, 0, len(nums_sorted))
print("Номер позиции элемента, который меньше введенного вами числа ", element_index)
