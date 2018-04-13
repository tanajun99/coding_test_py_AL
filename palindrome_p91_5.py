

def palindrome(s):
    for i in range(1,len(s)+1):
        last_s=s[:i]
        invest_s=s+last_s[::-1]
        flag=True
        for j in range(int(len(invest_s)/2)):
            if invest_s[j]!=invest_s[-1*(j+1)]:
                flag=False
                break
        if flag:
            return len(invest_s)

if __name__=="__main__":
    s = input().strip()
    result = palindrome(s)
    print(result)
    # print (" ".join(map(str, result)))
