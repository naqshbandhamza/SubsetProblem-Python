temp = []
noOfsubsets = 1
def find(index,count,arr):
    global noOfsubsets
    for j in range(index,len(arr)):
        if j+count<len(arr) and count!=0:
            temp.append(j)
            find(j+1,count-1,arr)
        elif j+count<len(arr) and count==0:
            temp.append(j)
            if len(temp)>=1:
                noOfsubsets+=1
                for i in range(0,len(temp)):
                    if i==0:
                        print('[',end='')
                    #final[tempi].append(arr[temp[i]])
                    print(arr[temp[i]],end='')
                    if i==len(temp)-1:
                        print(']',end='')
                temp.pop()
        if j==len(arr)-1:
            if len(temp)!=0:
                temp.pop()
                
arr=[]
temp1 = int(input('enter element:'))
while(temp1!=-1):
    arr.append(temp1)
    temp1 = int(input('enter element:'))
print('[]',end='')
count = 0
while count<len(arr):
    index = 0
    find(index,count,arr)
    count+=1
print('no of subsets:',noOfsubsets)






































'''arr = []
#[1,2,3,4,5]
num = int(input('enter number:'))
while num!=-1:
    arr.append(num)
    num = int(input('enter number:'))
temp = []
print('[]',end='')
count = 1
final = []
tempi = 0
for index in range(0,len(arr)):
    #print('[',arr[index],']',end='')
    final.append([arr[index]])
    tempi+=1
    count+=1
    for i in range(index+1,len(arr)):
        #print('[',arr[index],arr[i],']',end='')
        final.append([arr[index],arr[i]])
        tempi+=1
        count+=1
    if index+2<len(arr):
        for j in range(index+1,len(arr)):
            if j+1<len(arr):
                for k in range(j+1,len(arr)):
                    #print('[',arr[index],',',arr[j],',',arr[k],']',end='')
                    final.append([arr[index],arr[j],arr[k]])
                    count+=1
                    tempi+=1
    add = 1
    loop = 3
    while loop<len(arr):
        for j in range(index+1,len(arr)):
            if j+add<len(arr):
                for n in range(j+add+1,len(arr)):
                    final.append([])
                    final[tempi].append(arr[index])
                    #print('[',arr[index],end='')
                    for m in range(j,j+add+1):
                        pass
                        final[tempi].append(arr[m])
                        #print(',',arr[m],end='')
                    final[tempi].append(arr[n])                     
                    #print(',',arr[n],']',end='')
                    count+=1
                    tempi+=1

        add+=1
        loop+=1
count = 0
index = 1

while count<len(arr)-1:
    list1 = arr.copy()
    del list1[index]
    #print(list1)
    for i in range(0,len(list1)):
        add = 1
        loop = 3
        while loop<len(list1):
            for j in range(i+1,len(list1)):
                if j+add<len(list1):
                    for n in range(j+add+1,len(list1)):
                        final.append([])
                        final[tempi].append(list1[i])
                        #print('[',list1[i],end='')
                        for m in range(j,j+add+1):
                            final[tempi].append(list1[m])
                            #print(',',list1[m],end='')
                        #print(',',list1[n],']',end='')
                        final[tempi].append(list1[n])
                        tempi+=1
            add+=1
            loop+=1
    index+=1
    count+=1       
length = 1
for i in range(0,len(final)):
    for j in range(0,len(final)):
        if final[i]==final[j] and i!=j:
            final[j] = 0
for i in range(0,len(final)):
    if final[i]!=0:
        print(final[i],end='')
        length+=1
print("length :",length)'''






