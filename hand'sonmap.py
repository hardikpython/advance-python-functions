numbers1=[1,2,3,4,5]
numbers2=[4,5,6]
result=map(lambda x,y:x+y, numbers1,numbers2)
print("addition of two lists")
print(list(result))
num=[1,2,3,4,5]
def sq(n):
    return n*n
square=list(map(sq,num))
print('square of numbers in lists')
print(square)