from bisect import bisect_right
def maxProfitAssignment(difficulty, profit, worker):
    jobs = sorted(zip(difficulty, profit))
    worker.sort()
    max_profit = 0
    curr_max = 0
   for i in range(len(worker)):
        curr_max = max(curr_max, max(p for d, p in jobs if d <= worker[i]))
        max_profit += curr_max

    return max_profit
difficulty = [2, 4, 6, 8, 10]
profit = [10, 20, 30, 40, 50]
worker = [4, 5, 6, 7]
print(maxProfitAssignment(difficulty, profit, worker))  
