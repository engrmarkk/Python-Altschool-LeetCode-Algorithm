class Solution(object):
    def generate(self, numRow:int)->List[List[int]]:
        arr=[]
        for i in range(numRow):
            arr.append([])
            for j in range(i+1):
                if j==0 or j==i:
                    arr[i].append(1)
                else:
                    arr[i].append(arr[i-1][j-1]+arr[i-1][j])
        return arr

num=Solution()
print(num.generate(9))
