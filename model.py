from scipy.signal import correlate2d
import numpy as np
import math
import matplotlib.pyplot as plt

def add_island(array, dim, height=0.1):
    dim = dim // 2
    arr_len = len(array) // 2
    for i in range(arr_len - dim, arr_len + dim):
        for ii in range(arr_len - dim, arr_len + dim):
            array[i][ii] += height

class reaction_diffusion:
    def __init__(self, dim, island_dim=10, diff_rate_a=0.5, diff_rate_b=0.25, feed_rate=0.035, kill_rate=0.057, noise=0.1):
        self.diff_rate_a = diff_rate_a
        self.diff_rate_b = diff_rate_b
        self.feed_rate = feed_rate
        self.kill_rate = kill_rate
        self.array1 = np.ones((dim, dim))
        self.array2 = noise * np.random.random((dim, dim))
        add_island(self.array2, island_dim)
        self.kernel = np.array([[0, 0.25, 0],
                                [0.25,-1, 0.25],
                                [0, 0.25, 0]])
        # self.kernel = np.array([[0, 0.167, 0.167],
        #                         [0.167,-1, 0.167],
        #                         [0, 0.167, 0.167]])

    def step(self):
        a1 = self.array1
        a2 = self.array2
        c1 = correlate2d(a1, self.kernel, mode='same')
        c2 = correlate2d(a2, self.kernel, mode='same')

        reaction = a1 * a2**2
        self.array1 += self.diff_rate_a * c1 - reaction + self.feed_rate * (1 - a1)
        self.array2 += self.diff_rate_b * c2 + reaction - (self.feed_rate + self.kill_rate) * a2

class token_reaction_diffusion:
    def __init__(self, dim, island_dim=10, diff_rate_a=0.5, diff_rate_b=0.25, feed_rate=0.035, kill_rate=0.057, noise=0.1, token_range=2):
        self.diff_rate_a = diff_rate_a
        self.diff_rate_b = diff_rate_b
        self.feed_rate = feed_rate
        self.kill_rate = kill_rate
        self.token_range = token_range
        self.array1 = np.ones((dim, dim))
        self.array2 = noise * np.random.random((dim, dim))
        add_island(self.array2, island_dim)
        self.token_array = ((np.array(np.random.random((dim, dim)) * 10, dtype=int)) % token_range)
        self.kernel_list = [np.array([[0, 0.25, 0],
                                      [0.25,-1, 0.25],
                                      [0, 0.25, 0]], dtype=float),
                                    
                            np.array([[0, 0, 0.125, 0, 0],
                                      [0, 0, 0.125, 0, 0],
                                      [0.125, 0.125, -1, 0.125, 0.125],
                                      [0, 0, 0.125, 0, 0],
                                      [0, 0, 0.125, 0, 0]], dtype=float),
                                    
                            np.array([[0, 0, 0, 0.083, 0, 0, 0],
                                      [0, 0, 0, 0.083, 0, 0, 0],
                                      [0, 0, 0, 0.083, 0, 0, 0],
                                      [0.083, 0.083, 0.083, 1, 0.083, 0.083, 0.083],
                                      [0, 0, 0, 0.083, 0, 0, 0],
                                      [0, 0, 0, 0.083, 0, 0, 0],
                                      [0, 0, 0, 0.083, 0, 0, 0]], dtype=float)]
        # self.kernel_list = [np.array([[0, 0.25, 0],
        #                               [0.25,-1, 0.25],
        #                               [0, 0.25, 0]], dtype=float),
                                    
        #                     np.array([[0, 0.125, 0],
        #                               [0.125,-1, 0.125],
        #                               [0, 0.125, 0]], dtype=float),
                                    
        #                     np.array([[0, 0.083, 0],
        #                               [0.083,-1, 0.083],
        #                               [0, 0.083, 0]], dtype=float)]

    def var_correlate2d(self, array, kernel_list, token_array):
        array_len = len(array)
        result = np.ones_like(array, dtype=float)

        idx_row = 0
        while (idx_row <= array_len - 1):
            idx_col = 0
            while (idx_col <= array_len - 1):
                # print("kernel index: ", int(token_array[idx_row][idx_col]))
                idx = int(token_array[idx_row][idx_col])
                kernel = kernel_list[idx]
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
                # if (idx_row == 4) and (idx_col == 4):
                #     window = np.array([i[idx_col-hkl:idx_col+hkr+1] for i in array[idx_row-hkt:idx_row+hkb+1]])
                #     print(window)
                #     print((temp_kernel))
                #     print(window*kernel)
                #     print(sum(sum(window*kernel)))
                #     # print(result)
                #     # return
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

    def step(self):
        a1 = self.array1
        a2 = self.array2
        c1, self.token_array = self.var_correlate2d(a1, self.kernel_list, self.token_array)
        c2, self.token_array = self.var_correlate2d(a2, self.kernel_list, self.token_array)
        self.token_array = np.array([[int(ii % self.token_range) for ii in i] for i in self.token_array])
        # self.token_array = np.array([[(0 if ii >= self.token_range else ii) for ii in i] for i in self.token_array])


        reaction = a1 * a2**2
        self.array1 += self.diff_rate_a * c1 - reaction + self.feed_rate * (1 - a1)
        self.array2 += self.diff_rate_b * c2 + reaction - (self.feed_rate + self.kill_rate) * a2


# a = reaction_diffusion(300, diff_rate_a=0.5, diff_rate_b=0.25, feed_rate=0.02, kill_rate=0.05, noise=0.1)
# for i in range(1500):
#     a.step()
# # plt.imshow(a.array1, cmap='Greys')
# plt.imshow(a.array2 - a.array1, cmap='Blues')
# plt.show()

a = token_reaction_diffusion(50)
for i in range (5):
    print(a.token_array)
    print(a.array1)
    a.step()
# print(a.token_array)
plt.imshow(a.array2 - a.array1, cmap='Blues')
plt.show()

# a = reaction_diffusion(50)
# for i in range(200):
#     a.step()
# # print(a.token_array)
# plt.imshow(a.array2 - a.array1, cmap='Blues')
# plt.show()