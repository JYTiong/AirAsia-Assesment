# this is a helper function to count the number of ways to reach the N number of rocks with 1 or 2 jumps
def fib_helper(n):
    if n <= 1:
        return n

    return fib_helper(n - 1) + fib_helper(n - 2)


# for this question, since a person can jump either 1 or 2 rocks, for N rocks, a person can jump n+1 and n+2 steps each
# time. Therefore, we can use a recursive function to calculate the ways to reach the end given N number of rocks
def findJumpingWays(n):
    return "There are " + str(fib_helper(n + 1)) + " ways to reach the end given " + str(n) + " rocks"
