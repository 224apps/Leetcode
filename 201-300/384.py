import random
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.array = nums
        self.original = list(nums)

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        self.array = self.original
        self.original = list(self.original)
        return self.array
        
        

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        for i in range(len(self.array)):
            swapIdx = random.randrange(i, len(self.array))
            self.swap(self.array, i, swapIdx)
        return self.array
    
    def swap(self, array, i, j):
        temp = array[i]
        array[i] = array[j]
        array[j] = temp
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()