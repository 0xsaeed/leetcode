class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        idx = -1
        gas_tank = 0
        for i in range(len(gas)):
            deficit = gas[i] - cost[i]
            if deficit >= 0:
                if idx == -1:
                    idx = i
                gas_tank += deficit 
            else:
                if idx != -1:
                    gas_tank += deficit
                if gas_tank < 0:
                    idx = -1
                    gas_tank = 0
        return idx