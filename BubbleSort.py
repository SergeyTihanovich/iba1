import random
import datetime
import prettytable                  # пакет для таблицы
import matplotlib.pyplot as plt     # библиотека для графика

def BubbleSort(A):                  # сортировка пузырьком
    for i in range(len(A)):
        for j in range(len(A)-1-i):
            if A[j] > A[j+1]:
                a = A[j]
                A[j] = A[j+1]
                A[j+1] = a

def InsertSort(C):                   #Функция сортировки вставками insert:
   for i in range(1,len(C)):
       t = C[i]  # C[i] - вставляемый элементДействие – новая переменная
       j = i  # j - позиция в отсортированной части списка
       while j>=0 and C[j-1]  > t:
             C[j] = C[j - 1] # эл-ты отсортированной части, большие вставляемого
             j -= 1  # уступают место – сдвигаются (копируются) вправо # j остановится на посл. эл-те, большем вставляемого
             C[j] = t  # вставляемый эл-т ставится на освободившееся место

def ShakerSort(D):                       #Функция шейкерной (коктейльной) сортировки shaker - модификации пузырьковой:

   for i in range (0, len(D)//2):                 # i - счетчик пар проходов по списку,лева направо# сравнение текущего элемента со следующим
       for j in range(i,len(D)-1-i):               # которых в 2 раза меньше, чем в пузырьковой
           if D[j] > D[j + 1]:                      # j - номер позиции при проходе по списку с
               n = D[j]
               D[j] = D[j + 1]
               D[j + 1] = n
       for j in range(len(D)-2-i,i+1): 		# j - номер позиции при проходе по списку справа налево
           if D[j]<D[j-1] :		# сравнение текущего элемента с предыдущим
              n1=D[j]
              D[j]=D[j-1]
              D[j-1]=n1



def QuickSort(A, fst, lst):         # быстрая сортировка
    if fst >= lst:
        return

    #i, j = fst, lst
    pivot = A[fst]
    # pivot = A[random.randint(fst, lst)]
    first_bigger = fst+1
    while first_bigger <= lst:
        if A[first_bigger] >= pivot:
            break
        first_bigger += 1
    i = first_bigger+1
    while i <= lst:
        if A[i] < pivot:
            A[i], A[first_bigger] = A[first_bigger], A[i]
            first_bigger += 1
        i += 1

    last_smaller = first_bigger-1
    A[fst], A[last_smaller] = A[last_smaller], A[fst]
    QuickSort(A, fst, last_smaller-1)
    QuickSort(A, first_bigger, lst)


table = prettytable.PrettyTable(["Размер списка", "Время пузырька", "Время быстрой", "Время Insert", "Время Shaker"])
x=[]
y1=[]
y2=[]
y3=[]
y4=[]



for N in range(1000,10001,1000):
    x.append(N)
    min=1
    max=N
    A=[]
    for i in range (N):
        A.append(int(round(random.random()*(max-min)+min)))

    #print(A)

    B = A.copy()
    # print(B)
    C = A.copy()
    D = A.copy()

    # BubbleSort(A)
    print("---")
    # print(A)


    # QuickSort(B, 0, len(B)-1)
    print("---")
    # print(B)

    t1 = datetime.datetime.now()
    BubbleSort(A)
    t2 = datetime.datetime.now()
    y1.append((t2-t1).total_seconds())
    print("Пузырьковая сортировка   " +str(N)+"   заняла   "+str((t2-t1).total_seconds()) + "c")

    t3 = datetime.datetime.now()
    QuickSort(B, 0, len(B)-1)
    t4 = datetime.datetime.now()
    y2.append((t4 - t3).total_seconds())
    print("Быстрая   " +str(N)+"   заняла   "+str((t4-t3).total_seconds()) + "c")

    t5 = datetime.datetime.now()
    InsertSort(C)
    t6 = datetime.datetime.now()
    y3.append((t6 - t5).total_seconds())
    print("Insert  " + str(N) + "   заняла   " + str((t6 - t5).total_seconds()) + "c")

    t7 = datetime.datetime.now()
    ShakerSort(D)
    t8 = datetime.datetime.now()
    y4.append((t8 - t7).total_seconds())
    print("Shaker  " + str(N) + "   заняла   " + str((t8 - t7).total_seconds()) + "c")

    table.add_row([str(N), str((t2-t1).total_seconds()), str((t4-t3).total_seconds()),str((t6-t5).total_seconds()),str((t8-t7).total_seconds())])
print(table)

plt.plot(x, y1, "C0")
plt.plot(x, y2, "C1")
plt.plot(x, y3, "C2")
plt.plot(x, y4, "C3")
plt.show()