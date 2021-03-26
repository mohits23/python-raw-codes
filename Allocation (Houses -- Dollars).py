class Solution:
    def __init__(self,num_houses,budget,houses):
        self.num_houses = num_houses
        self.budget = budget
        self.houses = houses

    def solving(self):
        self.houses.sort()
        bought = self.houses[0]
        count = 0
        for i in range(1,self.num_houses):
            if bought > B:
                break                                        
            bought += self.houses[i]
            count += 1
        return count

T = int(input())
for i in range(T):
    N, B = input().split()
    N, B = [int(N), int(B)]
    A = [int(k) for k in input().split()]
    sol = Solution(N,B,A)
    print('Case #{}: {}'.format(i+1,sol.solving()))
