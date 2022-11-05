import re
def snake_to_camel(word):
    return ''.join(word.capitalize() or '_'for x in word.split())
def camel_to_snake(str):
    return re.sub('([a-z0-9])([A-Z])',r'\1_\2',str).lower()
T=int(input())
while(T):
    ip_txt1=input()
    print(snake_to_camel(ip_txt1))
    ip_txt2=input()
    print(camel_to_snake(ip_txt2))
    T-=1