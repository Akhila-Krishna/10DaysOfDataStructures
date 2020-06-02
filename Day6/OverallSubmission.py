def buy_and_sell_stock_once(prices):
    maximum = 0
    for i in range(0,n-1):
        for j in range(1,n):
            if prices[i]-prices[j] > maximum:
                maximum = prices[j]-prices[i]
    return maximum

prices = []
n = int(input("Enter Number of Elements : "))
for i in range(0,n):
    element = int(input())
    prices.append(element)
profit = buy_and_sell_stock_once(prices)
print(profit)