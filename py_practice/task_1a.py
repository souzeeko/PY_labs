# [Шейкерная сортировка]
def shaker_sort(array):
    print("given array:", *array) 
    swapped = True # указываем, что массив не отсортирован
    start = 0 
    end = len(array) - 1
    iteration = 1
    while (swapped == True): 
        swapped = False
        for i in range(start, end): 
            if (array[i] > array[i + 1]): 
                array[i], array[i + 1] = array[i + 1], array[i] 
                swapped = True     
        if (not(swapped)): 
            break
        swapped = False
        end -= 1
        for i in range(end - 1, start - 1, -1): 
            if (array[i] > array[i + 1]): 
                array[i], array[i + 1] = array[i + 1], array[i] 
                swapped = True
                
        start += 1
        print("left going digits,", iteration, "iteration:", *array)
        iteration += 1
# [main]
print("Shaker sort")
print("Input your array in format input/space:")
a = [int(i) for i in input().split()]
shaker_sort(a) 
print("Sorted array:", *a)