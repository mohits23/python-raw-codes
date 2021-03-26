class Solution:
    def __init__(self, num_stack, num_plates, required_plates, stack):
        self.num_stack = num_stack
        self.num_plates = num_plates
        self.required_plates = required_plates
        self.stack = stack

    def solving(self):
        sum_beauty = 0
        max_beauty = []
        rounds = self.required_plates % self.num_plates
        
        for i in range(self.num_stack):
            for j in range(self.num_plates):
                sum_beauty += self.stack[i][j]
            yield sum_beauty
            max_beauty.append(sum_beauty)
            sum_beauty = 0
            
        max_beauty.sort()
        yield max_beauty


T = int(input())
for i in range(T):
    N, K, P = input().split()
    N, K, P = [int(N), int(K), int(P)]
    A = []
    for j in range(N):
        ele = []
        ele = input().split()
        ele = list(map(lambda x: int(x),ele))
        A.append(ele)
    sol = Solution(N,K,P,A)
    it = sol.solving()
    for ele in it:
        print(ele)
    
