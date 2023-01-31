class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        output = []
        for i in range(len(arr)):
            max = 0
            for j in range(len(arr)):
                if i != j and j > i:
                    if arr[j] > max:
                        max = arr[j]
            output.append(max)
        output[-1] = -1
        return output
            
