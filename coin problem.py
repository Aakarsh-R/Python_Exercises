
def coin(N, K):
    
    if K > N and (K >= 1 and K <= 500):
        
        a = (N**2 - N)/2
        
        if K == a:
            return 'Y'
        else:
            return 'N'
    else:
        return 'N'

N = 0
K = 5
res = coin(N, K)
print(res)

