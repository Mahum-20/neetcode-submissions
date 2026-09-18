class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted([(p , (target - p) / s ) for p, s in zip(position, speed)], reverse=True)
        fleet = 0
        curr_bottleneck = 0
        for p, t in cars:
            if t > curr_bottleneck:
                fleet += 1
                curr_bottleneck = t
        return fleet