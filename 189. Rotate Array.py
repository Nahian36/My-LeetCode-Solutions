def rotate(nums: list[int], k: int):
        """
        Do not return anything, modify nums in-place instead.
        """
        nums[:] = __import__("numpy").roll(nums, k).tolist()

rotate(nums = [1,2,3,4,5,6,7], k = 3)
rotate(nums = [-1,-100,3,99], k = 2)