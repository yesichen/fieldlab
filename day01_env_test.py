import numpy as np
import matplotlib.pyplot as plt

# 创建数据
x = np.linspace(0, 2 * np.pi, 200)
y = np.sin(x)

# 绘图
plt.figure(figsize=(8, 5))
plt.plot(x, y, 'b-', linewidth=2, label=r'$y = \sin(x)$')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Day 1 Environment Test')
plt.legend()
plt.grid(True, alpha=0.3)

# 保存图片（在 show 之前保存）
plt.savefig('day01_env_test.png', dpi=150, bbox_inches='tight')
plt.show()

print("图片已保存为 day01_env_test.png")