def add(x,y):
    return x+y
result=add(10,20)
print("The sum is",result)
print("The sum is",add(100,200))
print(add(10,20))

def calc(a,b):
    sum=a+b
    sub=a-b
    mul=a*b
    div=a/b
    return sum,sub,mul,div
t=calc(100,50)
print("The results are",t)

def wish(name,msg):
    print("Hello",name,msg)
wish(name="Durga",msg="Good Morning")
wish(msg="Good Morning",name="Durga")

def wish(name="Guest"):
    print("Hello",name,"Goood Morning")
wish("Durga")
wish()

s=lambda n:n*n
print("Square",s(4))
print(s)

def string(a):
    def str(b):
            return len(b)

s=add(20,30)
s.update((50,30))
print(s)



