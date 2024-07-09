class Solution:
    #its o(n) solution
    def hIndex(self, citations: List[int]) -> int:
        if sum(citations)==0:
            return 0

        max_index=min(max(citations),len(citations))

        if max_index == 1:
            return 1
        h_indexes = [0]*(max_index+1) 

        for citation in citations:
            if citation >= max_index:
                h_indexes[max_index] += 1
            else:
                h_indexes[citation] += 1
        counter = 0
        for i in range(max_index,-1,-1):
            if counter + h_indexes[i] >= i:
                return i
            else:
                counter += h_indexes[i]





class Solution2:
    # this is not time efficient solution - drity one
    def hIndex(self, citations: List[int]) -> int:
        if sum(citations)==0:
            return 0

        max_index=min(max(citations),len(citations))

        if max_index == 1:
            return 1
        for i in range(max_index,0,-1):
            if sum([1 for x in citations if x>=i])>=i:
                return i
