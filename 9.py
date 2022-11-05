import re
def is_allowed(string):
    charRe=re.compile(r'[^a-zA-Z0-9]')
    res=charRe.search(string)
    return not bool(res)
T=int(input())
while(T):
    ip_txt=input()
    print(is_allowed(ip_txt))
    T-=1