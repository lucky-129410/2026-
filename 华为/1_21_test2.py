str = input("请输入字符串：")
my_set = set(str)

#print(f"字符串中不同的字符有：{my_set},共{len(my_set)}个")

my_list = list(my_set)

for i in str:

    if i not in my_list:
        my_list.append(i)

print(f"字符串中不同的字符有：{my_list},共{len(my_list)}个")
