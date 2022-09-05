from typing import List

def maxProfit( prices: List[int]) -> int:

    if len(prices) < 2:
        return 0
    max_profit = 0
    minprice = prices[0]
    for i in range(1, len(prices)):
        if  minprice > prices[i]:
            minprice = prices[i]
        else:
            max_profit=max(max_profit, prices[i]-minprice)
    return max_profit


prices = [7,1,5,3,6,4]
print(maxProfit(prices))

        