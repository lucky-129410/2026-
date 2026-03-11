k = int(input("请输入聚类点的个数:"))
my_list = []
for i in range(k):
    my_str = input("请输入%d个聚类点的坐标:" % (i + 1))
    my_tup = tuple(map(float,my_str.split()))
    my_list.append(my_tup)

count = int(input("请输入迭代次数:"))
number = int(input("请输入需要聚类的点的个数:"))

my_list2 = []
for i in range(number):
    my_str = input("请输入%d个聚类点的坐标:" % (i + 1))
    my_tup = tuple(map(float,my_str.split()))
    my_list2.append(my_tup)
#先建立二维列表存储分裂的元组
my_list3 = []
for i in range(k):
    my_list3.append([])

for i in range(1):
    for j in range(number):
        min_distance = float('inf')
        min_index = -1
        for m in range(k):
            distance = ((my_list[m][0] - my_list2[j][0]) ** 2 + (my_list[m][1] - my_list2[j][1]) ** 2 + (my_list[m][2] - my_list2[j][2]) ** 2) ** 0.5
            if distance < min_distance:
                    min_distance = distance
                    min_index = m

        my_list3[min_index].append(my_list2[j])
    my_list.clear()#先把初始聚类中心清空
    for i in range(k):
        x = 0
        y = 0
        z = 0
        for j in range(len(my_list3[i])):
            x += my_list3[i][j][0]
            y += my_list3[i][j][1]
            z += my_list3[i][j][2]
        my_tup = (x / len(my_list3[i]), y / len(my_list3[i]), z / len(my_list3[i]))
        my_list.append(my_tup)

print("聚类中心的坐标为:")
for i in range(k):
    print(my_list[i])










 

