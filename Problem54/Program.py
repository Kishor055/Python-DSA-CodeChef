def max_profit(prices):
    n = len(prices)
    max_profit = 0

    for i in range(n):
        for j in range(i + 1, n):
            max_profit = max(max_profit, prices[j] - prices[i])

    return max_profit
