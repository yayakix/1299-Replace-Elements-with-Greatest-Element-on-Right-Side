class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        reversed_arr = arr[::-1]
        output = []
        max = -1
        if len(arr) == 1:
            return [-1]
        for i in range(len(arr) - 1):
            if i == 0:
                output.append(-1)
            if reversed_arr[i] > max:
                max = reversed_arr[i]
                output.append(reversed_arr[i])
            else:
                output.append(max)
        return output[::-1]
