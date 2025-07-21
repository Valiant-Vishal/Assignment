
def onescompliment(s) -> str:
    ans = ''
    for bit in s:
        if bit == "0":
            ans += "1"
        else:
            ans += "0"
    return ans


def twoscompliment(s) -> str:

    ones = onescompliment(s)
    ans = list(ones)
    n = len(ones)

    carry = '1'

    for bit in range(n-1,-1,-1):
        if ans[bit] == '0':
            ans[bit] = '1'
            carry = '0'
            break
        else:
            ans[bit] = '0'
    
    if carry == '1':
        ans.insert(0, '1')


    return "".join(ans)

print(twoscompliment('0101100'))