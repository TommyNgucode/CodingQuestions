class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        j = len(numbers) - 1
        i = 0
        while i < j:
            l = numbers[i]
            r = numbers[j]
            print(l)
            print(r)
            if l + r == target:
                return [i  + 1, j + 1]
            else:
                j-=1
                if j == i:
                    i+=1
                    j = len(numbers) - 1
        
        return [0, 0]