class Solution:
    def max_num(self, arr):
        max_val = arr[0]
        for val in arr:
            if max_val < val:
                max_val = val
        return max_val
    def replaceElements(self, arr: List[int]) -> List[int]:
        last_index = len(arr) -1
        for i in range(last_index):
            arr[i] = self.max_num(arr[i+1:])
        arr[last_index] = -1
        return arr

        