class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        output = []
        second_arr = arr.copy()
        for i in range(len(arr)):
            if len(second_arr) > 1:
                second_arr.pop(0)
                maxi = max(second_arr)
                output.append(maxi)
        output.append(-1)
        return output
