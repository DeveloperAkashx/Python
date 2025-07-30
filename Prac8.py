def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def permutation(n, r):
    if r > n:
        return "Invalid: r cannot be greater than n."
    return factorial(n) // factorial(n - r)

n = int(input("Enter value of n: "))
r = int(input("Enter value of r: "))

print(f"Permutation (nPr) is: {permutation(n, r)}")
