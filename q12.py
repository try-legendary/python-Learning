##Swap three variables in circular rotation (a->b, b->c, c->a)


a, b, c=input("enter 3 variables with space:").split();

a,b,c=c,b,a;


print(a, b, c)
