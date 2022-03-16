class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend < 0 and divisor < 0 :
            ans = dividend/divisor
        if dividend < 0:
            dividend = dividend * -1
            ans =  0 - dividend/divisor
        elif divisor < 0:
            divisor = divisor * -1
            ans =  0 - dividend/divisor
        else:
            ans =  dividend/divisor
        
        if int(ans) > 2147483647:
            return 2147483647
        elif (ans) < -2147483648:
            return -2147483648
        else:
            
            return int(ans)