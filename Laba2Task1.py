#Вариант 1
#Удалить в списке все числа, которые повторяются более двух раз.
my_list = [1, 2, 3, 4, 3, 4, 8, 12, 14, 16, 12, 18, 14, 25]
new_list = []
for x in my_list:
    if x not in new_list:
        new_list.append(x)
print(f'Новый список без дублирующихся значений= {new_list}\n')
print('Теперь из полученного списка сформируем подмножество сумма элементов которого даст искомое число:')

#Найти подмножество данного множества чисел такое, что сумма его элементов равна заданному числу.
findNumber=int(input('Введите заданное число :'))
Sum_list=[]
NewSum_list=[]
count=0
for x in new_list:
    for y in new_list:
        for z in new_list:
            if x+y+z==findNumber :
                NewSum_list.append(x)
                NewSum_list.append(y)
                NewSum_list.append(z)
                print(f'Новое подмножество= {NewSum_list}')
                NewSum_list.clear()
                count+=1
if count==0:
    print('не возможно собрать подмножество путем сложения трех элементов,,, нужно добавлять циклы')






