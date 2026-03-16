layer = int(input("请输入层数："))
threshold = input("精度损失阈值：")
my_list = []

for i in range(layer):
    my_str = input(f"请输入第{i + 1}层的数据：")
    temp_list1 = my_str.split(" ")
    temp_list2 = []
    for item in temp_list1:
        if "bit" not in item:
            temp_list2.append(float(item))
        else:
            temp_list2.append(item)

    my_list.append(temp_list2)

# 主要的思想是把阈值加起来满足小于等于预定阈值的 把内存加起来 最后选一个最小的内存的
print(my_list)
my_list_num = []
for i in range(layer): 
    temp_list = []
    if my_list[i][0] == 1:
        temp_list.append(my_list[i][2])
    else:
        temp_list.append(my_list[i][2])
        temp_list.append(my_list[i][5])
    my_list_num.append(temp_list)

# 动态规划 每次处理两个组数据 然后依次把剩下的数据添加进去






