def is_allowed(ip_string):
    allowed_chars=set("0123456789abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    validation=set(ip_string)
    if validation.issubset(allowed_chars):
        return True
    else:
        return False
T=int(input())
while(T):
    ip_txt=input()
    print(is_allowed(ip_txt))
    T-=1