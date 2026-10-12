import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # Windows 用黑体，Mac 可改成 ['Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False    # 解决坐标轴负号显示为方框的问题

# 1. 生成网格（用较密的网格，便于观察误差）
x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)

# 2. 定义标量场
Z = X**2 + Y**2

# 3. 解析梯度
U_exact = 2 * X
V_exact = 2 * Y

# 4. 数值梯度（中心差分）
h = x[1] - x[0]   # 网格间距
U_num = np.zeros_like(Z)
V_num = np.zeros_like(Z)

# 对内部点用中心差分
for i in range(1, len(y)-1):
    for j in range(1, len(x)-1):
        U_num[i, j] = (Z[i, j+1] - Z[i, j-1]) / (2*h)
        V_num[i, j] = (Z[i+1, j] - Z[i-1, j]) / (2*h)

# 边界点用前向/后向差分（简化处理）
U_num[:, 0] = (Z[:, 1] - Z[:, 0]) / h
U_num[:, -1] = (Z[:, -1] - Z[:, -2]) / h
V_num[0, :] = (Z[1, :] - Z[0, :]) / h
V_num[-1, :] = (Z[-1, :] - Z[-2, :]) / h

# 5. 计算误差
error = np.sqrt((U_num - U_exact)**2 + (V_num - V_exact)**2)
max_error = np.max(error)
print(f"最大绝对误差: {max_error:.6e}")

# 6. 画误差热力图
plt.figure(figsize=(8, 6))
plt.contourf(X, Y, error, levels=20, cmap='hot')
plt.colorbar(label='梯度误差')
plt.xlabel('x')
plt.ylabel('y')
plt.title('数值梯度误差（中心差分）')
plt.axis('equal')
plt.savefig('day04_grad_error.png', dpi=150, bbox_inches='tight')
#plt.savefig(r'D:\py_proj\fieldlab\day04_grad_error.png', dpi=150, bbox_inches='tight')
plt.show()

print("图片已保存为 day04_grad_error.png")