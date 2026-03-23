# 📓 深度学习（PyTorch）核心笔记（精简版）

---

## 🧠 一、整体训练流程（主线）

```
数据（Tensor）
→ 模型（Linear / MLP）
→ 损失函数（Loss）
→ 反向传播（backward）
→ 优化器（Optimizer）
→ 参数更新
→ 循环训练（epoch）
```

---

## 📦 二、Tensor（数据）

### ✅ 本质

* 多维数组 + 自动求导

### ✅ 要点

* 形状：`[样本数, 特征数]`
* 类型：`float32`（必须）
* 自动求导：

```python
x = torch.tensor(..., requires_grad=True)
```

---

## 🧱 三、模型（Model）

### 1️⃣ 线性模型（Linear）

```
y = wx + b
```

```python
torch.nn.Linear(in_features, out_features)
```

👉 只能拟合**线性关系**

---

### 2️⃣ 多层感知机（MLP）

```
x → Linear → 激活 → Linear → y
```

👉 能拟合**非线性关系**

---

## ⚡ 四、激活函数（Activation）

### ✅ 作用

* 引入非线性（否则多层 = 一层）

### 常见函数

* ReLU：`f(x) = max(0, x)`（最常用）
* Sigmoid：`(0,1)` 概率输出
* Tanh：`(-1,1)` 居中

---

## 📉 五、损失函数（Loss）

### ✅ 作用

* 衡量预测值 vs 真实值误差

---

### 1️⃣ 回归：MSE

```
MSE = (1/n) Σ(y - ŷ)^2
```

```python
torch.nn.MSELoss()
```

---

### 2️⃣ 分类：交叉熵

```
Loss = - Σ y log(ŷ)
```

```python
torch.nn.CrossEntropyLoss()
```

### ⚠️ 注意

* 不要手动 softmax
* 标签用类别索引（不是 one-hot）

---

## 🔁 六、反向传播（Backward）

### ✅ 本质

* 自动求导（链式法则）

```python
loss.backward()
```

### ⚠️ 注意

* 梯度默认**累加**
* 禁止 `.data`，用 `.detach()`

---

## ⚙️ 七、优化器（Optimizer）

### ✅ 作用

* 根据梯度更新参数（w, b）

---

### 常用优化器

* SGD：

```
w = w - η∇L
```

* Adam（推荐）：

  * 自适应学习率 + 动量
  * 收敛更快更稳定

---

## 🔁 八、训练流程（必须掌握）

```python
for epoch in range(N):

    y_pred = model(x)        # 前向传播
    loss = criterion(y_pred, y)

    optimizer.zero_grad()    # 清梯度
    loss.backward()          # 反向传播
    optimizer.step()         # 更新参数
```

### ❗关键点

* `zero_grad()`：防止梯度累加

---

## 📊 九、分类任务流程

```
输入 → Linear → logits
→ CrossEntropyLoss（内部含 softmax）
→ loss
```

---

## 🧠 十、核心原理总结

### 🎯 梯度下降

* 沿着 loss 下降最快方向更新参数

### 🎯 深度学习本质

* 不断调整参数，让预测更接近真实值

### 🎯 模型能力来源

* 多层结构 + 激活函数 → 非线性表达能力

---

## 🚨 十一、常见错误（高频）

| 错误          | 原因               |
| ----------- | ---------------- |
| dtype错误     | Long vs Float    |
| 不 zero_grad | 梯度累加             |
| 使用 `.data`  | 破坏计算图            |
| 手动 softmax  | 重复计算             |
| 标签 one-hot  | CrossEntropy 不支持 |

---

## 🎯 十二、面试模板（背这个）

```
1. 构造 Tensor 数据
2. 定义模型（Linear / MLP）
3. 定义损失函数
4. 前向传播
5. 计算 loss
6. 反向传播
7. 优化器更新参数
8. 循环直到收敛
```

---

## 🚀 总结一句话

```
深度学习 = 神经网络拟合函数 + 梯度下降优化参数
```

---
