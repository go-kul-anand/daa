def knapSack(W, wt, val, n):
    if n == 0 or W == 0:
        return 0
    if wt[n-1] > W:
        return knapSack(W, wt, val, n-1)
    else:
        return max(val[n-1] + knapSack(W-wt[n-1], wt, val, n-1), knapSack(W, wt, val, n-1))

val = [40, 60, 100]
wt = [20, 30, 50]
W = 70
n = len(val)

print("The Maximum value that can be put in knapsack is:", knapSack(W, wt, val, n))
