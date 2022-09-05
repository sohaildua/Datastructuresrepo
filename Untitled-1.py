def max_profit(prices: list, 
               days: int) -> int:
    profit = 0
  
    for i in range(1, days):
  
        # Checks if elements are adjacent 
        # and in increasing order
        if prices[i] > prices[i-1]:
  
            # Difference added to 'profit'
            profit += prices[i] - prices[i-1]
  
    return profit
  
# Driver Code
if __name__ == '__main__':
  
    # Stock prices on consecutive days
    prices = []
    
  
    # Function call
    profit = max_profit(prices, len(prices))
    print(profit)
  