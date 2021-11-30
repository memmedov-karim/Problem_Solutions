s=input()
if s[0]=="+" or s[0]=="-" or s[0]=="*":
    print(s.count("+")+s.count("-")+s.count("*")-1)
else:
    print(s.count("+")+s.count("-")+s.count("*"))
