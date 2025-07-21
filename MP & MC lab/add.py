def add(first, second) -> list:
    n_bit = max(len(first),len(second))
    A = first.zfill(n_bit)
    B = second.zfill(n_bit)
    ans = []
    
    carry = 0
    
    for i,j in zip(A[::-1],B[::-1]):
        sum = carry + int(i) + int(j)
        if sum == 0:
            ans.insert(0,'0')
            carry = 0
        elif sum == 1:
            ans.insert(0,'1')
            carry = 0
        elif sum == 2:
            ans.insert(0,'0')
            carry = 1
        elif sum == 3:
            ans.insert(0,'1')
            carry = 1
    
    
    
    if carry == 1:
        return [''.join(ans) , '1']
    
    else:
        return [''.join(ans) , '0']
    
