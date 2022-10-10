import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import label
import skimage.morphology as sm

def _rotate(arr):
    res = np.zeros((arr.shape[1], arr.shape[0]))

    for i in range(arr.shape[0] - 1, -1, -1):
        res[ : , i] = arr[arr.shape[0] - 1- i]

    return res

# Исходный

image = np.load("ps.npy")

plt.subplot(121)
plt.title("Исходный")
plt.imshow(image)

# Исходный с метками

label_image, q_obj = label(image, return_num=True)
plt.subplot(122)
plt.title("Исходный с метками")
plt.imshow(label_image)

print(f"Количество объектов: {q_obj}")

# --------- Поиск фигур ---------

plt.figure()

# Маска

mask = np.array([
    [1, 1, 0, 0, 1, 1],
    [1, 1, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
])

check_find_quantity_figure = 0

# Обработка одинаковой фигуры, которая может быть повернута на 4 разные стороны

for i in range(1, 5):
    figure = sm.binary_opening(image, mask)
    figure_label, figure_counter = label(figure, return_num=True)
    plt.subplot(150 + i)
    plt.title(f"Фигура {i}: {figure_counter}")
    check_find_quantity_figure += figure_counter
    plt.imshow(figure)
    mask = _rotate(mask)

# Обработка прямоугольников

mask[ : , : ] = 1
figure = sm.binary_opening(image, mask)
figure_label, figure_counter = label(figure, return_num=True)
plt.subplot(155)
plt.title(f"Фигура {5}: {figure_counter}")
check_find_quantity_figure += figure_counter
plt.imshow(figure)

print(f"Определено фигур: {check_find_quantity_figure}")

plt.show()