import numpy as np
from scipy.signal import correlate2d

# note: only works for kernels of odd dim and equal dims on both axes
def var_correlate2d(array, kernel_list, token_array):
    array_len = len(array)
    result = np.ones_like(array, dtype=float)

    idx_row = 0
    while (idx_row <= array_len - 1):
        idx_col = 0
        while (idx_col <= array_len - 1):
            kernel = kernel_list[token_array[idx_row][idx_col]]
            half_kernel = len(kernel) // 2

            # l:left, r:right, t:top, b:bottom
            hk = half_kernel
            hkl = half_kernel
            hkr = half_kernel
            hkt = half_kernel
            hkb = half_kernel
            if idx_col < hkl:
                hkl = idx_col
            if (array_len - idx_col - 1) < hkr:
                hkr = array_len - (idx_col + 1)
            if idx_row < hkt:
                hkt = idx_row
            if (array_len - idx_row - 1) < hkb:
                hkb = array_len - (idx_row + 1)
            temp_kernel = np.array([i[hk-hkl:hk+hkr+1] for i in kernel[hk-hkt:hk+hkb+1]], dtype=float)

            # print(idx_row, idx_col, temp_kernel.shape, np.array([i[idx_col-hkl:idx_col+hkr+1] for i in array[idx_row-hkt:idx_row+hkb+1]], dtype=float).shape)
            if (idx_row == 4) and (idx_col == 4):
                window = np.array([i[idx_col-hkl:idx_col+hkr+1] for i in array[idx_row-hkt:idx_row+hkb+1]])
                print(window)
                print((temp_kernel))
                print(window*kernel)
                print(sum(sum(window*kernel)))
                # print(result)
                # return
            val = sum(sum(np.array([i[idx_col-hkl:idx_col+hkr+1] for i in array[idx_row-hkt:idx_row+hkb+1]], dtype=float) * temp_kernel))
            result[idx_row][idx_col] = val

            idx_col += 1
        idx_row += 1

    # Applying kernel to the token array
    kernel = np.array([[0, 0.25, 0],
                       [0.25,-1, 0.25],
                       [0, 0.25, 0]])

    new_token_array = correlate2d(token_array, kernel, mode='same')
    return result, new_token_array

array = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 0, 0, 0],
         [0, 0, 0, 1, 4, 1, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0]]

token_array = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0]])

kernel_list = [np.array([[0, 0.25, 0],
                         [0.25,-1, 0.25],
                         [0, 0.25, 0]], dtype=float),
                         
               np.array([[0.1, 0.25, 0.1],
                         [0.25,-1, 0.25],
                         [0.1, 0.25, 0.1]], dtype=float),]

# kernel = [[0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 0]]

kernel = np.array([[0, 0.25, 0],
                   [0.25,-1, 0.25],
                   [0, 0.25, 0]], dtype=float)

cut_array = np.array([i[5-2:5+3] for i in array[5-2:5+3]])
kernel = np.array(kernel)
# for i in cut_array:
#     print(i)
# print(sum(cut_array * kernel))

print(np.array(array, dtype=float))
# print(var_correlate2d(array, kernel_list, token_array))
print(var_correlate2d(array, [kernel], token_array))
print(correlate2d(array, kernel, mode='same'))