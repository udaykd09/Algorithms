"""
8.1 Triple Step: A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3
steps at a time. Implement a method to count how many possible ways the child can run up the
stairs.
"""

def countWays(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return countWays(n - 1) + countWays(n - 2) + countWays(n - 3)

def countWaysDP(n, memo):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif memo[n] > -1:
        return memo[n]
    else:
        memo[n] = countWaysDP(n - 1, memo) + countWaysDP(n - 2, memo) + countWaysDP(n - 3, memo)
        return memo[n]

n = 3
print(countWays(n))
print(countWaysDP(n, [-1]*(n+1)))