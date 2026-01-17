str=input("Input a string:");
result="";
for x in str:
    if ('a'<= x <= 'z'):
        result=result+x.upper();
    else:
       result=result + x

print(result)