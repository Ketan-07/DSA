def possible_ways(s,res):
    cnt = 0
    if len(s) == 0:
        print(res)
        return 1

    for i in range(len(s)):
        ch = s[i]  #A
        left = s[:i] #""
        right = s[i+1:] # "BC"

        cnt += possible_ways(left + right, ch + res)
    return cnt

count = possible_ways("abcd","")
print("Possible ways are :",count)