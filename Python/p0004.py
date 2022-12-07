# Problem 4

# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

if __name__ == "__main__":

    ans = -1
    for int2 in range(999,0,-1):
        for int1 in range(999, int2-1, -1):
            prod = int1*int2
            if str(prod) == str(prod)[::-1] and prod > ans:
                ans = prod
    print(ans)
#%%
