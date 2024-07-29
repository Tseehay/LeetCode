class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        peak=max(arr)
        peak_index=arr.index(peak)
        left, right= True,True
        
        if peak_index==len(arr)-1 or peak_index==0:
            return False
        if len(arr) <= 2 or arr.count(peak) > 1:
            return False

        for i in range(len(arr)-1):
            if i < peak_index:
                if arr[i] >= arr[i+1]:
                    left = False
            elif i > peak_index:
                if arr[i] <= arr[i+1]:
                    right = False

        return right and left