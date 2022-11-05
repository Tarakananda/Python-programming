import re
T=int(input())
while(T):
    ip_txt=input()
    print(bool(re.match("^[A-Z '45'$a-z0-9]*$",ip_txt)))
    T-=1