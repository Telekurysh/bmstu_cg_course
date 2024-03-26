class Voxel:
    def __init__(self):
        self.color = (0, 0, 0)  # RGB color tuple
        self.density = 0.0
        self.transmissivity = 0.0

    def print_info(self):
        print(f"Voxel: color{self.color}, density: {self.density}, transm.: {self.transmissivity}")


class VoxelGrid:
    def __init__(self, size=0.0, x=0, y=0, z=0, d=0.0):
        self.xcount = x
        self.ycount = y
        self.zcount = z
        self.voxelsize = size
        self.default_density = d

        self.grid = [Voxel() for _ in range(self.xcount * self.ycount * self.zcount)]
        for voxel in self.grid:
            voxel.density = self.default_density
        # self.grid = []
        #
        # for kk in range(self.zcount):
        #     for jj in range(self.ycount):
        #         for ii in range(self.xcount):
        #             voxel = Voxel()
        #             voxel.density = self.default_density
        #             self.grid.append(voxel)

    def outside(self, x, y, z):
        if (x >= self.xcount) or (y >= self.ycount) or (z >= self.zcount) or (x < 0) or (y < 0) or (z < 0):
            return True
        return False

    def get_voxel_index(self, x, y, z):
        return x + y * self.xcount + z * self.xcount * self.ycount

    def set_voxel_color(self, x, y, z, rgb):
        if self.outside(x, y, z):
            return

        index = self.get_voxel_index(x, y, z)
        self.grid[index].color = rgb

    def set_voxel_density(self, x, y, z, d):
        if self.outside(x, y, z):
            return

        index = self.get_voxel_index(x, y, z)
        self.grid[index].density = d

    def set_voxel_transmissivity(self, x, y, z, q):
        if self.outside(x, y, z):
            return

        index = self.get_voxel_index(x, y, z)
        self.grid[index].transmissivity = q

    def get_voxel_color(self, x, y, z):
        if self.outside(x, y, z):
            return (0, 0, 0)

        index = self.get_voxel_index(x, y, z)
        return self.grid[index].color

    def get_voxel_density(self, x, y, z):
        if self.outside(x, y, z):
            return self.default_density

        index = self.get_voxel_index(x, y, z)
        return self.grid[index].density

    def get_voxel_transmissivity(self, x, y, z):
        if self.outside(x, y, z):
            return 0.0

        index = self.get_voxel_index(x, y, z)
        return self.grid[index].transmissivity

    def get_voxel_grid(self):
        return self.grid

    def get_voxel_size(self):
        return self.voxelsize

    def get_default_density(self):
        return self.default_density

    def get_max_x(self):
        return self.xcount

    def get_max_y(self):
        return self.ycount

    def get_max_z(self):
        return self.zcount
