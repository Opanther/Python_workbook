#First 100 number

for i in range(1, 101):
    if i % 3 == 0 and i % 5 ==0 :
        print(f"the number is {i} and FizzBuzz!!!")
    elif i % 3 == 0:
        print(f"the number is {i} and fizz!!!")
    elif i % 5 == 0:
        print(f"the number is {i} and buzz!!!")
    else:
        print(f" The number {i} is not divisible by 3 or 5")


