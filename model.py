from scipy.signal import correlate2d
import numpy as np
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

    def step(self):
        a1 = self.array1
        a2 = self.array2
        c1 = correlate2d(a1, self.kernel, mode='same')
        c2 = correlate2d(a2, self.kernel, mode='same')

        # print(np.shape(a1))
        # print(np.shape(a2))
        reaction = a1 * a2**2
        # print(np.shape(reaction))
        # print(np.shape(c1))
        self.array1 += self.diff_rate_a * c1 - reaction + self.feed_rate * (1 - a1)
        self.array2 += self.diff_rate_b * c2 + reaction - (self.feed_rate + self.kill_rate) * a2


a = reaction_diffusion(200, diff_rate_a=0.5, diff_rate_b=0.25, feed_rate=0.02, kill_rate=0.05, noise=0.1)
for i in range(1500):
    a.step()
# plt.imshow(a.array1, cmap='Greys')
plt.imshow(a.array2 - a.array1, cmap='Blues')
plt.show()