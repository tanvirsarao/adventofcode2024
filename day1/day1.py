import pandas as pd
day = 1

def selectionSort(arr):
    for i in range(len(arr)):
        elem = i
        for j in range(i+1, len(arr)):
            if (arr[j] < arr[elem]):
                elem = j


        temp = arr[i]
        arr[i] = arr[elem]
        arr[elem] = temp

input = pd.read_csv('input.txt', header = None, delim_whitespace=True)

array1 = input[0]
array2 = input[1]

selectionSort(array1)
selectionSort(array2)

df = pd.DataFrame({'Sorted Array1': array1,
                   'Sorted Array2': array2})

difference = (df['Sorted Array1'] - df['Sorted Array2']).abs()
result_part_1 = difference.sum()

score = 0
for i in df['Sorted Array1']:
    for j in df['Sorted Array2']:
        if j == i:
            score += i

result_part_2 = score


print(f"--- Day {day}: ---") #1
print(f"Part 1: {result_part_1}") #1765812
print(f"Part 2: {result_part_2}") #20520794
