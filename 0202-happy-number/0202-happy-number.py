class Solution:
    def isHappy(self, n: int) -> bool:
        hmap = {}
        number = n
        temp = 0
        while temp != 1:
            snum = str(number)
            temp = 0
            for i in range(len(snum)):
                temp += int(snum[i]) ** 2

            if temp in hmap:
                return False
            
            hmap[number] = temp
            number = temp
        
        return temp == 1

