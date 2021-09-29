# find the total profit for the earnings as mentioned below:
# {13,5,3,8,12}
# output: 9


def findProfit(earnings: list) -> float:
    if earnings is None or len(earnings) == 0: return
    length = len(earnings)
    if length == 1: return 0

    dailyDifferences = [0] * (length-1)

    for i in range(1, length):
        dailyDifferences[i-1] = earnings[i] - earnings[i-1]
    
    return sum(list(filter(lambda x: x > 0, dailyDifferences)))

def findProfitWithoutExtraSpaceComplexity(earnings: list) -> float:
    if earnings is None or len(earnings) == 0: return
    length = len(earnings)
    if length == 1: return 0

    profits:float = 0.0
    for i in range(1, length):
        dailyProfitDiff = earnings[i]-earnings[i-1]
        if dailyProfitDiff > 0: profits += dailyProfitDiff
    
    return profits


earnings = [13,5,3,8,12]

print(f"the total profit for the earnings is: {findProfit(earnings)}")
print(f"the total profit for the earnings is: {findProfitWithoutExtraSpaceComplexity(earnings)}")
