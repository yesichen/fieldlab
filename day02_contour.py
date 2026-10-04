import numpy as np
import matplotlib.pyplot as plt

# 1. 生成一维坐标
x = np.linspace(-3, 3, 100)   # x 从 -3 到 3，100 个点
y = np.linspace(-3, 3, 100)   # y 从 -3 到 3，100 个点

# 2. 生成二维网格
X, Y = np.meshgrid(x, y)

print("X shape:", X.shape)   # (100, 100)
print("Y shape:", Y.shape)   # (100, 100)
print("X[0, :5] =", X[0, :5]) # 第一行的前5个x值
print("Y[:5, 0] =", Y[:5, 0]) # 第一列的前5个y值

# 3. 定义标量场 f(x,y) = x^2 +/- y^2
Z = X**2 - Y**2

# 4. 画等高线
plt.figure(figsize=(8, 6))

# 画填充等高线（颜色表示数值大小）
contour_filled = plt.contourf(X, Y, Z, levels=15, cmap='viridis')
plt.colorbar(contour_filled, label='f(x,y)')

# 画等高线线条，并标注数值
contour_lines = plt.contour(X, Y, Z, levels=10, colors='black', linewidths=0.8)
plt.clabel(contour_lines, inline=True, fontsize=10, fmt='%.1f')

# 5. 标注
plt.xlabel('x')
plt.ylabel('y')
# 抛物面
#plt.title(r'Contour of $f(x,y) = x^2 + y^2$')
# 马鞍面
plt.title(r'Contour of $f(x,y) = x^2 - y^2$')
plt.axis('equal')   # 保持 x 和 y 比例一致
plt.grid(True, alpha=0.3)

# 6. 保存
plt.savefig('day02_contour.png', dpi=150, bbox_inches='tight')
# 抛物面
#plt.savefig(r'D:\py_proj\fieldlab\day02_contour_x2_plus_y2.png', dpi=150, bbox_inches='tight')
# 马鞍面
#plt.savefig(r'D:\py_proj\fieldlab\day02_contour_x2_minus_y2.png', dpi=150, bbox_inches='tight')
plt.show()

print("图片已保存为 day02_contour.png")
#print("图片已保存为 day02_contour_x2_plus_y2.png")
#print("图片已保存为 day02_contour_x2_minus_y2.png")
