str=input("Enter a string:");
len=len(str);
result=""
for x in range(len-1,-1,-1):
 char=str[x];
 result=result+char;

print(result);