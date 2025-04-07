name="gopal sharma"
print(type(name))
print(name.upper())
print(name.lower())
print(name.title())

name="Gopal Sharma"
print(name.strip())
print(name.rstrip())
print(name.islower())

## list==[] ,, ordered, duplicate store, multiple data type,mutuable
lst=["hello",1,2,3,22.1,True]
print(lst)
print(type(lst))

lst=["red","black","blue","red"]
print(lst.count("red"))
lst.append("green")
print(lst)
print(lst.pop(1))
lst.remove("red")
print(lst)

## tuple -- () ,,, immutable,ordered,duplicate store, multiple data 
tpl=("hello",)
print(type(tpl))

## sets --{} -- unorder , immutable (but we can do add or remove in it.)
st={1,2,3,22.3,True}
print(st)

## dict={key:value} ,, ordered
dict={ "sonu":[1,2,3,4],
      "monu":[3,54,6,8],
      "gopal":[5,36,3,6]}

for i,j in dict.items():
    print(i,j)
    
## arbitary arguments --args --*
# def child(*name):
    # bn 
# modue vs package vs lib

# user define module
def add(a,b):
    return a+b