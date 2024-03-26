import math
import time
import random

class Noise:
    def __init__(self, persistence, octaves, seed):
        self.persistence = persistence
        self.octaves = octaves

        # Add more randomness
        seed = seed + random.randint(0, 99)

        self.seed1 = seed * 3  # *0.3
        self.seed2 = seed * 7  # *0.7

    def noise1(self, x):
        n = x
        n = (n << 13) ^ n
        noise = 1.0 - ((n * (n * n * 15731 + 789221) + 1376312589) & 0x7fffffff) / 1073741824.0  # [-1.0, 1.0]
        return noise

    def noise2(self, x, y):
        n = x + y * self.seed1
        n = (n << 13) ^ n
        noise = 1.0 - ((n * (n * n * 15731 + 789221) + 1376312589) & 0x7fffffff) / 1073741824.0  # [-1.0, 1.0]
        return noise

    def noise3(self, x, y, z):
        n = x + y * self.seed1 + z * self.seed2
        n = (n << 13) ^ n
        noise = 1.0 - ((n * (n * n * 15731 + 789221) + 1376312589) & 0x7fffffff) / 1073741824.0  # [-1.0, 1.0]
        return noise

    def smooth_noise1(self, x):
        edges = (self.noise1(x - 1) + self.noise1(x + 1)) * 0.25  # /4
        center = self.noise1(x) * 0.5  # /2

        return center + edges

    def smooth_noise2(self, x, y):
        corners = (self.noise2(x - 1, y - 1) + self.noise2(x + 1, y - 1) +
                   self.noise2(x - 1, y + 1) + self.noise2(x + 1, y + 1)) * 0.0625  # /16
        edges = (self.noise2(x - 1, y) + self.noise2(x + 1, y) + self.noise2(x, y - 1) + self.noise2(x, y + 1)) * 0.125  # /8
        center = self.noise2(x, y) * 0.25  # /4

        return corners + edges + center

    def smooth_noise3(self, x, y, z):
        corners = (self.noise3(x + 1, y + 1, z + 1) + self.noise3(x + 1, y + 1, z - 1) +
                   self.noise3(x + 1, y - 1, z + 1) + self.noise3(x + 1, y - 1, z - 1) +
                   self.noise3(x - 1, y + 1, z + 1) + self.noise3(x - 1, y + 1, z - 1) +
                   self.noise3(x - 1, y - 1, z + 1) + self.noise3(x - 1, y - 1, z - 1)) * 0.015625  # /64
        edges = (self.noise3(x + 1, y + 1, z) + self.noise3(x + 1, y - 1, z) +
                 self.noise3(x - 1, y + 1, z) + self.noise3(x - 1, y - 1, z) +
                 self.noise3(x, y + 1, z + 1) + self.noise3(x, y + 1, z - 1) +
                 self.noise3(x, y - 1, z + 1) + self.noise3(x, y - 1, z - 1) +
                 self.noise3(x + 1, y, z + 1) + self.noise3(x + 1, y, z - 1) +
                 self.noise3(x - 1, y, z + 1) + self.noise3(x - 1, y, z - 1)) * 0.03125  # /32
        faces = (self.noise3(x + 1, y, z) + self.noise3(x - 1, y, z) + self.noise3(x, y + 1, z) +
                 self.noise3(x, y - 1, z) + self.noise3(x, y, z + 1) + self.noise3(x, y, z - 1)) * 0.0625  # /16
        center = self.noise3(x, y, z) * 0.125  # /8

        return corners + edges + faces + center

    def linear_interpolate(self, a, b, x):
        return a * (1 - x) + b * x

    def cosine_interpolate(self, a, b, x):
        ft = x * math.pi
        f = (1 - math.cos(ft)) * 0.5

        return a * (1 - f) + b * f

    def cubic_interpolate(self, v0, v1, v2, v3, x):
        p = (v3 - v2) - (v0 - v1)
        q = (v0 - v1) - p
        r = v2 - v0
        s = v1

        return p * x * x * x + q * x * x + r * x + s

    def interpolate_noise1(self, x):
        i_x = int(x)
        f_x = x - i_x

        u = [0, 0]

        u[0] = self.smooth_noise1(i_x)
        u[1] = self.smooth_noise1(i_x + 1)

        return self.cosine_interpolate(u[0], u[1], f_x)

    def interpolate_noise2(self, x, y):
        i_x = int(x)
        i_y = int(x)
        f_x = x - i_x
        f_y = y - i_y

        u = [0, 0, 0, 0]
        v = [0, 0]

        u[0] = self.smooth_noise2(i_x, i_y)
        u[1] = self.smooth_noise2(i_x + 1, i_y)
        u[3] = self.smooth_noise2(i_x, i_y + 1)
        u[4] = self.smooth_noise2(i_x + 1, i_y + 1)

        v[0] = self.cosine_interpolate(u[0], u[1], f_x)
        v[1] = self.cosine_interpolate(u[2], u[3], f_x)

        return self.cosine_interpolate(v[0], v[1], f_y)

    def interpolate_noise3(self, x, y, z):
        i_x = int(x)
        i_y = int(y)
        i_z = int(z)
        f_x = x - i_x
        f_y = y - i_y
        f_z = z - i_z

        u = [0, 0, 0, 0, 0, 0, 0, 0]
        v = [0, 0, 0, 0]
        w = [0, 0]

        u[0] = self.smooth_noise3(i_x, i_y, i_z)
        u[1] = self.smooth_noise3(i_x + 1, i_y, i_z)
        u[2] = self.smooth_noise3(i_x, i_y + 1, i_z)
        u[3] = self.smooth_noise3(i_x + 1, i_y + 1, i_z)
        u[4] = self.smooth_noise3(i_x, i_y, i_z + 1)
        u[5] = self.smooth_noise3(i_x + 1, i_y, i_z + 1)
        u[6] = self.smooth_noise3(i_x, i_y + 1, i_z + 1)
        u[7] = self.smooth_noise3(i_x + 1, i_y + 1, i_z + 1)

        v[0] = self.cosine_interpolate(u[0], u[1], f_x)
        v[1] = self.cosine_interpolate(u[2], u[3], f_x)
        v[2] = self.cosine_interpolate(u[4], u[5], f_x)
        v[3] = self.cosine_interpolate(u[6], u[7], f_x)

        w[0] = self.cosine_interpolate(v[0], v[1], f_y)
        w[1] = self.cosine_interpolate(v[2], v[3], f_y)

        return self.cosine_interpolate(w[0], w[1], f_z)

    def perlin_noise1(self, x):
        total = 0
        p = self.persistence
        n = self.octaves - 1

        for ii in range(n):
            frequency = 2 ** ii
            amplitude = p ** ii

            total += self.interpolate_noise1(x * frequency) * amplitude

        # [0.0, 1.0] (need positive density)
        if total < 0:
            total += 1.0
        if total > 1:
            total -= 1.0

        return total

    def perlin_noise2(self, x, y):
        total = 0
        p = self.persistence
        n = self.octaves - 1

        for ii in range(n):
            frequency = 2 ** ii
            amplitude = p ** ii

            total += self.interpolate_noise2(x * frequency, y * frequency) * amplitude

        # [0.0, 1.0] (need positive density)
        if total < 0:
            total += 1.0
        if total > 1:
            total -= 1.0

        return total

    def perlin_noise3(self, x, y, z):
        total = 0
        p = self.persistence
        n = self.octaves - 1

        for ii in range(n):
            frequency = 2 ** ii
            amplitude = p ** ii

            total += self.interpolate_noise3(x * frequency, y * frequency, z * frequency) * amplitude

        # [0.0, 1.0] (need positive density)
        if total < 0:
            total += 1.0
        if total > 1:
            total -= 1.0

        return total
