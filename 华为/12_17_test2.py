import numpy as np

k = int(input("请输入如手机个数:"))

my_list_x = []
my_list_y = []

for i in range(k):
    my_str = input("请输入第{}个手机的数据:".format(i + 1))
    temp_list = my_str.split(" ")
    temp_list2_x = []
    temp_list2_x.append(1)
    temp_list2_y = []

    for j in range(len(temp_list)):
        if j == len(temp_list) - 1:
            temp_list2_y.append(float(temp_list[j]))
        else:
            temp_list2_x.append(float(temp_list[j]))
    
    my_list_x.append(temp_list2_x)
    my_list_y.append(temp_list2_y)

X = np.array(my_list_x)
Y = np.array(my_list_y)

seta = np.linalag.inv(X.T.dot(X)).dot(X.T).dot(Y)


N = int(input("请输入测试数据的个数:"))

my_lsit_n = []

for i in range(N):
    my_str = input("请输入第{}个测试数据:".format(i + 1))
    temp_list = my_str.split(" ")
    temp_list2 = []

    temp_list2.append(1)
   
    for j in range(len(temp_list)):
        temp_list2.append(float(temp_list[j]))
    
    my_lsit_n.append(temp_list2)
my_lsit_n = np.array(my_lsit_n)
result = my_lsit_n.dot(seta)


print("预测结果为:")
for i in range(N):
    print("第{}个测试数据的预测结果为:{}".format(i + 1, result[i][0]))  

