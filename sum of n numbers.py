#task2 Sum of Integers from 1 to 50 Using a Loop
n = int(input('Enter the number: '))
sum = 0
for i in range(1,n):
    sum = sum + i
print('Sum of Integers From 1 to',n,'is :',sum)