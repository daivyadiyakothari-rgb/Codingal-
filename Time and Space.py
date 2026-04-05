# Activity 1
def fun1(n):
    return n * (n+1) /2
print(fun1(100))

# Activity 2
n = int(input("Enter a number: "))
result = fun1(n)
print("Sum of first", n, "natural number is", result)

# After Class Project
def multiply_iterative(n,m):
    result = 0
    for i in range(m):
        result += n
    return result

n = int(input("Enter value of N: "))
m = int(input("Enter value of M: "))

direct_result = n * m
iterative_result = multiply_iterative(n,m)

print("\nUsing direct multiplication: ", direct_result)
print("Using iterative multiplication: ", iterative_result)
