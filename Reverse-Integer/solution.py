class Solution:
    def reverse(self, x: int) -> int:
        neg=False
        i = 0
        if x < 0:
            neg=True
            x = x * -1

        while(x>0):
            a = x%10
            i = i*10 + a
            x =  int((x-a)/10)
        if i >= -2147483648 and i<= 2147483647:
            if neg ==True:
                return -i
            else:
                return i
        else:
            return 0