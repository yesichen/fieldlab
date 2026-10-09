import numpy as np
import matplotlib.pyplot as plt

# 1. 生成网格
x = np.linspace(-3, 3, 30)   # 注意：箭头图不需要太密，30 个点即可
y = np.linspace(-3, 3, 30)
X, Y = np.meshgrid(x, y)

# 2. 定义标量场
Z = X**2 + Y**2

# 3. 解析梯度
U = 2 * X   # ∂f/∂x = 2x
V = 2 * Y   # ∂f/∂y = 2y

print("在 (1,1) 处，梯度 =", (2*1, 2*1))  # 应该输出 (2, 2)
# 4. 创建画布
plt.figure(figsize=(8, 6))

# 5. 画填充等高线（背景）
contour_filled = plt.contourf(X, Y, Z, levels=15, cmap='viridis', alpha=0.7)
plt.colorbar(contour_filled, label='f(x,y)')

# 6. 画梯度箭头
# quiver(X, Y, U, V) 在 (X,Y) 处画箭头，方向 (U,V)
plt.quiver(X, Y, U, V, color='white', pivot='mid', scale=40, width=0.004)

# 7. 标注
plt.xlabel('x')
plt.ylabel('y')
plt.title(r'Gradient field of $f(x,y) = x^2 + y^2$')
plt.axis('equal')
plt.grid(True, alpha=0.3)

# 8. 保存
plt.savefig('day03_gradient_quiver.png', dpi=150, bbox_inches='tight')
#plt.savefig(r'D:\py_proj\fieldlab\day03_gradient_quiver.png', dpi=150, bbox_inches='tight')
plt.show()

print("图片已保存为 day03_gradient_quiver.png")