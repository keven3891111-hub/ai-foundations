# -*- coding: utf-8 -*-
"""手写数字分类。详细教学说明见配套 Notebook。
安装依赖：python -m pip install numpy matplotlib scikit-learn
运行：python cv_digits_demo.py
"""

# %% 第 1 个代码单元
import sys
import numpy as np
import matplotlib.pyplot as plt
import sklearn
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

print('Python:', sys.version.split()[0], '| scikit-learn:', sklearn.__version__)
digits = load_digits()
images = digits.images
labels = digits.target

print('图片集合:', images.shape)
print('标签集合:', labels.shape)
print('单张图片:', images[0].shape)
print('像素 dtype:', images.dtype)
print('像素范围:', images.min(), images.max())
print('第一张图的标签:', labels[0])

# %% 第 2 个代码单元
image = images[0]
print('第一张图的像素矩阵：')
print(image)
print('第 3 行、第 6 列的像素：', image[2, 5])

fig, axes = plt.subplots(1, 2, figsize=(9, 4.4))
for ax in axes:
    ax.imshow(image, cmap='gray', vmin=0, vmax=16, interpolation='nearest')
    ax.set_xticks(range(8))
    ax.set_yticks(range(8))
    ax.set_xlabel('x / column (0-7)')
    ax.set_ylabel('y / row (0-7)')
axes[0].set_title(f'Image | label = {labels[0]}')
axes[1].set_title('The same image | pixel values')
for row in range(8):
    for col in range(8):
        value = image[row, col]
        axes[1].text(col, row, str(int(value)), ha='center', va='center',
                     color='white' if value < 8 else 'black', fontsize=10)
plt.tight_layout()
plt.show()

# %% 第 3 个代码单元
X = images.reshape(len(images), 64) / 16.0
y = labels

print('X 的形状:', X.shape)
print('X 的范围:', X.min(), X.max())
print('y 的形状:', y.shape)
print('第一张图的前 8 个特征:', X[0, :8])

# %% 第 4 个代码单元
X_pool, X_test, y_pool, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)
X_train, X_val, y_train, y_val = train_test_split(
    X_pool, y_pool, test_size=0.25, random_state=42, stratify=y_pool
)

print('训练集:', X_train.shape, y_train.shape)
print('验证集:', X_val.shape, y_val.shape)
print('测试集:', X_test.shape, y_test.shape)

# %% 第 5 个代码单元
best_model = None
best_val_acc = -1.0
best_C = None

for C in [0.1, 1.0, 10.0]:
    model = LogisticRegression(C=C, solver='lbfgs', max_iter=1000)
    model.fit(X_train, y_train)  # 学习参数：只使用训练集

    train_pred = model.predict(X_train)
    val_pred = model.predict(X_val)  # 验证时不更新权重
    train_acc = accuracy_score(y_train, train_pred)
    val_acc = accuracy_score(y_val, val_pred)
    print(f'C={C:4.1f} | 训练准确率={train_acc:.2%} | 验证准确率={val_acc:.2%}')

    if val_acc > best_val_acc:
        best_val_acc = val_acc
        best_model = model
        best_C = C

print(f'选定 C={best_C}，验证准确率={best_val_acc:.2%}')
print('学到的权重形状:', best_model.coef_.shape)
print('学到的偏置形状:', best_model.intercept_.shape)

# %% 第 6 个代码单元
test_pred = best_model.predict(X_test)
test_acc = accuracy_score(y_test, test_pred)
correct = np.sum(test_pred == y_test)

print(f'最终测试准确率: {test_acc:.2%}')
print(f'预测正确: {correct} / {len(y_test)}')
print(f'预测错误: {len(y_test) - correct}')

# %% 第 7 个代码单元
fig, axes = plt.subplots(2, 6, figsize=(12, 4))
for i, ax in enumerate(axes.flat):
    ax.imshow(X_test[i].reshape(8, 8), cmap='gray', vmin=0, vmax=1,
              interpolation='nearest')
    color = 'seagreen' if test_pred[i] == y_test[i] else 'crimson'
    ax.set_title(f'True {y_test[i]} / Pred {test_pred[i]}', color=color)
    ax.axis('off')
plt.tight_layout()
plt.show()

wrong_indices = []
for i in range(len(y_test)):
    if test_pred[i] != y_test[i]:
        wrong_indices.append(i)

if len(wrong_indices) == 0:
    print('本次测试没有误判。')
else:
    fig, axes = plt.subplots(2, 4, figsize=(9, 4.5))
    for ax in axes.flat:
        ax.axis('off')
    for ax, i in zip(axes.flat, wrong_indices[:8]):
        ax.imshow(X_test[i].reshape(8, 8), cmap='gray', vmin=0, vmax=1,
                  interpolation='nearest')
        ax.set_title(f'True {y_test[i]} / Pred {test_pred[i]}', color='crimson')
    plt.tight_layout()
    plt.show()

