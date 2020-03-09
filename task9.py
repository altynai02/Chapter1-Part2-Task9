# 9. In mathematics, the factorial of an integer n, denoted by n! is the following
# product:
# n!=1×2×...×n
# For the given integer n
# calculate the value n!. Don't use math module in this exercise.

number = int(input("Enter a number: "))
count = 1

for i in range(1,number+1):
    count*=i
    # print(count) #shows every multiple
print(count)  #shows only result
