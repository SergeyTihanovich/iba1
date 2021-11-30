#Задача 1.	В матрице найти номер строки, сумма чисел в которой максимальна.

import numpy as np
A=np.array([[1,20,3,4,5],[10,20,30,57,98],[32,48,96,101,115],[38,56,99,85,48]])

#решил расширить себе задание и найти максимальный элемент массива:
maximum=A[0][0]
for j in range (0,len(A)):
    for i in range (0,len(A[j])):
        if maximum<A[j][i]:
           maximum=A[j][i]
print('Максимальный элемент массива =',maximum)
print()
#номер строки, сумма чисел в которой максимальна:
count = 0
maxSum = 0
rowSum = 0
for x in range(0, len(A)):
    rowSum = 0
    for y in range(0, len(A[x])):
        rowSum += A[x][y]
        if maxSum < rowSum:
            maxSum = rowSum
            count = x
print('Максимальная сумма строки массива =', maxSum)
print('Это строка номер :',x)