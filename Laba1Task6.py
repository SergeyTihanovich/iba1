#Дано натуральное трехзначное число n. Верно ли, что среди его цифр есть 0 или 9?
print('Данная программа определяет имеется ли во введенном вами трехзначном числе цифра 0 или цифра 9')
x=int(input('Введите трехзначное число : '))
print()
firstNumber=x//100
secondNumber=x//10%10
thirdNumber=x%10
if firstNumber==0 or firstNumber==9:
    print('В веденном вами числе первая цифра удовлетворяет условиию и равна =', firstNumber)
if secondNumber==0 or secondNumber==9:
    print('В веденном вами числе вторая цифра удовлетворяет условиию и равна =', secondNumber)
if thirdNumber == 0 or thirdNumber == 9:
    print('В веденном вами числе третья цифра удовлетворяет условиию и равна =', thirdNumber)
else:
    print('В данной цифре нет искомых цифр!')
