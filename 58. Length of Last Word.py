class Solution:
    def priceNextMonth(self, A, B, C, D):
    
        price = A / B
        
        if D > price:
            nextMonthPrice = A + (C * (D - price))
        else:
            nextMonthPrice = A
        
        return nextMonthPrice

a = Solution()
print(a.priceNextMonth(100  ,10  ,12,  1))