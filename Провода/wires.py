import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import label
import skimage.morphology as sm

# Исходное

wires = np.load("data_wires/wires2.npy")

plt.subplot(141)
plt.imshow(wires)

# Исходное -> уменьшаем толщину провода и убираем те что тоньше 3px

mask = np.array([
    [0, 1, 0],
    [0, 1, 0],
    [0, 1, 0],
])

wires = sm.binary_erosion(wires, mask)

plt.subplot(142)
plt.imshow(wires)

# Массив с восстановленными проводами

mask = np.zeros((3, 3))
mask[1, :] = 1

restored_wires = sm.binary_dilation(wires, mask)

plt.subplot(143)
plt.imshow(restored_wires)

# label -> Массив с восстановленными проводами 

mark_restored_wires, wires_quantity = label(restored_wires, return_num=True)

plt.subplot(144)
plt.imshow(mark_restored_wires)
print(f"Количество проводов: {wires_quantity}")

# 

for num_label in range(1, wires_quantity + 1):
    mask_only_now_wire = np.where(mark_restored_wires == num_label, 1, 0)   # Берем маску текущего провода
    only_now_wire = np.multiply(wires, mask_only_now_wire)   # Достаем его исходник
    marked_only_now_wire, num_parts = label(only_now_wire, return_num=True)   # Маркируем

    print(f"Количество разрывов провода {num_label}: {num_parts - 1} (частей: {num_parts})")   # Выввод

plt.show()