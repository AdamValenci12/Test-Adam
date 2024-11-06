# start
# תנאים:
#Q1:
float1: float = float(input('enter first float number: '))
float2: float = float(input('enter second float number: '))

smaller_num = min(float1, float2)
print((str(smaller_num) + " ") * 3)

#Q2:
num1: int = int(input("enter first number: "))
num2: int = int(input("enter second number: "))
average = (num1 + num2) / 2
print(average)

#Q3:
num1: int = int(input("enter first number: "))
num2: int = int(input("enter second number: "))
num3: int = int(input("enter third number: "))
max_1_2_3 = max(num1, num2, num3)
print(f"The biggest number is", max_1_2_3)
#Q4:
movie_time: int = int(input("Enter time of movie: "))
hours = movie_time // 60
remaining_minutes = movie_time % 60

print(f" The movies took {hours} hours and {remaining_minutes} minutes")
#Q5:
number = int(input("Enter 4 numbers digit: "))
if 1000 <= number <= 9999:
    right_digit = number % 10
    print("the right number is", right_digit)
else:
    print("invalid number")
#Q6:
number2 = int(input("Enter 4 numbers digit: "))
if 1000 <= number2 <= 9999:
    second_right = (number2 // 10) % 10
    print("the right number is", second_right)
else:
     print("invalid number")
#Q7:
two_digit: int = int(input("enter 2 number digit: "))
if 10 <= two_digit <= 99:
    asarot = two_digit // 10
    ahadot = two_digit % 10

    sum_of_digit = asarot + ahadot
    print(f"the digits sum is", sum_of_digit)
else:
    print(f" invalid numbers")
#Q8:
num: int = int(input("enter a number: "))
if 10 <= num <= 99:
    asarot = num // 10
    ahadot = num % 10
    reve_num = (ahadot * 10) + asarot
    print(f"the opposite num is: ", reve_num)
else:
    print(f"invalid number")
#Q9:
num: int = int(input("enter a number:"))
if num % 2 == 0:
    print("even")
else:
    print("odd")
#Q11:
age: int = int(input("enter age: "))
height: float = float(input("enter height: "))
if 8 <= age <= 18 and height > 1.15:
    print("have a permission to get in")
elif height > 1.00 and age > 18:
    print("have a permission to get in")
else:
    print("dont have permission")
###########################################################################
# לולאות:
#Q1:
top: int = int(input("enter a number: "))
if top > 0:
    for i in range(1, top + 1):
        print(i, end=" ")
else:
    print("the number invalid")
#Q2:
num1: int = int(input("enter a number: "))
num2: int = int(input("enter a number: "))

first = min(num1, num2)
second = max(num1, num2)
for i in range(first, second + 1):
    print(i, end=" ")
#Q3:
positive: int = int(input("enter a number: "))
if positive >= 0:
    for i in range(0, positive + 1):
        if i % 2 == 0:
            print(i, end=" ")
else:
    print("the number invalid")
# Q4:
max_num: int = int(input("enter a max number: "))
den_num: int = int(input("enter a den number: "))
if max_num > 0 and den_num > 0:
    for i in range (den_num, max_num + 1, den_num):
        print(i, end=" ")
else:
    print("the numbers invalid")
##################################################
# עיבוד נתונים:
# Q1:
total_sum = 0
first_input = True

while True:
    num = int(input("enter a number: "))
    if num == 99:
        if first_input:
            print(None)
    else:
        print(f"the sum numbers is ", total_sum)

    total_sum += num
    first_input = False
# Q2:

highest = None
lowest = None
first_input = True
while True:
    num = int(input("enter a number: "))

    if num == 99 and first_input:
        print(None)
    if num == 0:
        if highest is None or lowest is None:
            print(None)
        else:
            print(f"the highest number is: {highest}")
            print(f"the lowest number is: {lowest}")
    if highest is None or num > highest:
        highest = num
    if lowest is None or num < lowest:
        lowest = num
    first_input = False
#Q3:

max_value = None
max_position = 0

for i in range(1, 6):
    num = int(input(f"enter first number {i}: "))

    if max_value is None or num > max_value:
        max_value = num
        max_position = i

print("the highest one is:", max_position)
########################################################,
# לולאה מורכבת
# Q1:
temperatures = []

for i in range(12):
    try:
        temp = float(input(f"enter temperture:  {i + 1}: "))

        if temp < -5 or temp > 40:
            print("wrong data")
            break

        temperatures.append(temp)

    except ValueError:
        print("נא להכניס מספר תקין")

if len(temperatures) == 12:
    print("correct data")

    avg_temp = sum(temperatures) / len(temperatures)
    max_temp = max(temperatures)
    min_temp = min(temperatures)

    print(f"ממוצע הטמפרטורות: {avg_temp}")
    print(f"הטמפרטורה הגבוהה ביותר: {max_temp}")
    print(f"הטמפרטורה הנמוכה ביותר: {min_temp}")