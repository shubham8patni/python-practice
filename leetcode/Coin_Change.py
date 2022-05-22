class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        queue = []
        res = float("inf")
        visited = set()
        for coin in coins:
            queue.append([amount - coin,  1])
            visited.add(amount-coin)
        while queue:
            curr_amount, curr_coin = queue.pop(0)
            if curr_amount == 0:
                res = min(curr_coin, res)
            elif curr_amount > 0:
                for coin in coins:
                    if curr_amount - coin not in visited:
                        queue.append([curr_amount - coin,  curr_coin + 1])
                        visited.add(curr_amount-coin)
        return res if res != float("inf") else -1