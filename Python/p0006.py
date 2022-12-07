# Problem 6

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

if __name__ == "__main__":

    regsum = 0
    sqsum = 0
    for i in range(1, 101):
        regsum += i
        sqsum += i**2

    regsum = regsum**2
    print(regsum - sqsum)
#%%
