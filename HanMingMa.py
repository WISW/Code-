import math
def HanMingOdd(K,str,length):
    line=compute(K,str,length)
    for i in range(K):   #对判断位进行翻转即可得到奇校验结果。
        a=pow(2,i)
        line[a]=(line[a]+1)%2
    return line

def HanMingEven(K,str,length):
    line=compute(K,str,length)
    return line


def compute(K,str,length):
    j =0
    line =[]
    line.append(0)
    for i in range(1,K+length+1): #bulid list by str character
        if (math.log(i,2))%1!=0:
            line.append(int(str[j]))
            j=j+1
        else:
            line.append(0)    #对于判断位使用0占位
    print(line)
    for i in range(K):      ##对于每个判断组成员的确定
        temp1 =[]
        temp1.append(pow(2,i))
        for j in range(K):
            if j!=i:
                temp2=temp1.copy()
                for q in temp2:
                    add =q+pow(2,j)
                    if add>K+length:
                        break
                    else:
                        temp1.append(add)
        print(i,"   ",temp1)
        for j in temp1:
            a=pow(2,i)
            line[a]+=line[j]
            line[a]=line[a]%2
    print(line)
    return line

if __name__ == '__main__':
    str = input("请输入源字符串")
    length = len(str)
    K=math.ceil(math.log(length,2))   #开方且向上取整
    if pow(2,K)<length+K+1:
        K=K+1
    print("K",K)
    choice = input("请选择及偶校验或奇检验（0/1）")
    if choice=='0':
        print("偶校验")
        result=HanMingEven(K,str,length)
    else:
        print("奇校验")
        result=HanMingOdd(K,str,length)
    print("结果为",result[1:])


