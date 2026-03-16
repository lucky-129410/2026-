pred_str = input("请输入预测类别：")
pred_list = list(map(float, pred_str.split(" ")))

trueY_str = input("请输入真实类别：")
trueY_list = list(map(float, trueY_str.split(" ")))

weigths_str = input("请输入权重：")
weigths_list = list(map(float, weigths_str.split(" ")))


final_list = []

for i in range(len(weigths_list)):
    tp = 0
    fp = 0
    tn = 0
    for j in range(len(pred_list)):
        if pred_list[j] == i and trueY_list[j] == i:
            tp += 1
        elif pred_list[j] == i and trueY_list[j] != i:
            fp += 1
        
        elif pred_list[j] != i and trueY_list[j] == i:
            tn += 1
        
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0
    recall = tp / (tp + tn) if (tp + tn) > 0 else 0
    f1_score = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0
    my_tup = (precision, recall, f1_score)
    final_list.append(my_tup)


for i in range(len(final_list)):
    total_count = 0
    for j in range(len(final_list[i])):
        total_count += final_list[j][i] * weigths_list[j]
    print("%.2f" % total_count)

