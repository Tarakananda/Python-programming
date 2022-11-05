import re
def text_match(ip_txt):
    return(bool(re.match("^[a-z]+_[a-z]+$",ip_txt)))
T=int(input())
while(T):
    ip_txt=input()
    #print(bool(re.match("[a-z_a-z]*$",ip_txt)))
    #print(bool(re.match("^[a-z]+_[a-z]+$",ip_txt)))
    print(text_match(ip_txt))
    T-=1