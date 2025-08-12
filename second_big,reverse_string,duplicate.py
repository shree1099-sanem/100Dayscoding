s1="shreelatha"
d={}
for i in s1:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
for i in d:
    if d[i]>1:
        print(i)


l1="palle tech pvt ltd"
x=l1.split()
y=""
for i in x:
    y=y+" "+i[::-1]
print(y)

def second_big(num):
    big1 =0
    big2 = 0
    for i in num:
        if i>big1:
            big2=big1
            big1=i
        elif i>big2 and i<big1:
            big2=i
    return big2
res=second_big([1,19,87,13,5,10,7,3,2,99,9])
print("second biggest number is",res)