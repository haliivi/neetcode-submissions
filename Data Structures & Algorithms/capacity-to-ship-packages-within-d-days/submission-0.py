class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = r

        def can_ship(cap):
            ships, cur_cap = 1, cap
            for w in weights:
                if cur_cap - w < 0:
                    ships += 1
                    cur_cap = cap
                cur_cap -= w
            return ships <= days

        while l <= r:
            cap = l + r >> 1
            if can_ship(cap):
                r = cap - 1
                res = min(res, cap)
            else:
                l = cap + 1

        return res