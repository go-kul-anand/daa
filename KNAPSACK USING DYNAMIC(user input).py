def knapSack(W, wt, val, n):
    if n == 0 or W == 0:
        return 0
    if wt[n-1] > W:
        return knapSack(W, wt, val, n-1)
    else:
        return max(val[n-1] + knapSack(W-wt[n-1], wt, val, n-1), knapSack(W, wt, val, n-1))

if __name__ == '__main__':
    n = int(input("Enter the number of items: "))
    profit = []
    weight = []
    for i in range(n):
        val = int(input(f"Enter profit of item {i+1}: "))
        wt = int(input(f"Enter weight of item {i+1}: "))
        profit.append(val)
        weight.append(wt)
    W = int(input("Enter the capacity of the knapsack: "))
    print("The Value is ",knapSack(W, weight, profit, n))
