#Unpack a tuple into a,b,c and re-pack it reversed
tuple=(1,2,3);
a,b,c= tuple;
print(a,b,c);


list=[a,b,c];
list.reverse();
tuple1=(list,);
print(tuple1);
