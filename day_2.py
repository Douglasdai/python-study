#number
#type()显示数据类型
a,b,c,d= 20 ,2.2,True, 4+3j
print(type(a),type(b),type(c),type(d))
#isinstance 可以判断
a=111
isinstance(a,int)
#del 删除对象引用

#"" '' 字符串表示，并且 \ 可以换行，不耽误任何东西
str = 'Runoob'

print (str)          # 输出字符串
print (str[0:-1])    # 输出第一个到倒数第二个的所有字符
print (str[0])       # 输出字符串第一个字符
print (str[2:5])     # 输出从第三个开始到第五个的字符
print (str[2:])      # 输出从第三个开始的后的所有字符
print (str * 2)      # 输出字符串两次，也可以写成 print (2 * str)
print (str + "TEST") # 连接字符串

#列表
list = ['abcd', 786, 2.23, 'runoob',70.2]
tinylist = [123, 'runoob']

print(list)     #打印列表list
print(list[0])  #打印列表中0位置元素
print(list[1:3])#打印list中1到3 位置的元素 即第二个至第四个
print(list[2:]) #打印从第三个开始的元素
print(tinylist*2)#打印两遍该列表   
print(list + tinylist)#连接两个列表

#反转字符串
def reversWords(input):
    inputWords = input.split(" ")

    inputWords = inputWords[-1::-1]
    output = ' '.join(inputWords)

    return output

if __name__=="__main__":
    input = 'I like runoob'
    rw = reversWords(input)
    print(rw)

#数值计算
a=3
b=5
c=a+b
print(c)
print(a)
print(b)

#python中不可变数据为：number string tuple
#可变数据为 ：list dictionary set
