class Solution:
    def isHappy(self, n: int) -> bool:
        hmap = {}
        number = n
        while True:
            snum = str(number)
            temp = 0
            for i in range(len(snum)):
                temp += int(snum[i]) ** 2

            if temp == 1:
                return True
            
            if temp in hmap:
                return False
            
            hmap[number] = temp
            number = temp

