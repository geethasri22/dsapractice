class Solution:
    def isProduct(self, arr, target):
        # code here
        s= set()
        for num in arr:
            if target == 0:
                if num == 0 and len(arr)>1:
                    return True
            elif num != 0 and target % num == 0:
                c = target // num
                if c in s:
                    return True
            s.add(num)
        return False
'''
example as
arr1 = [10,20,30,40]
target = 400
so it returns true because 10 * 40 = 400
But
arr2 = [1,5,7,-9]
target=60
it returns false beacuae no product of any nums in the array matches the target
'''
