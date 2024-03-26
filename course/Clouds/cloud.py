from voxelgrid import VoxelGrid
from camera import Camera
from nois import Noise
from point import Point
from myscene import Scene
from PyQt6.QtGui import QColor
from vector3 import Vector3

from PyQt6.QtWidgets import QMessageBox


class Cloud:
    def __init__(self, size, x, y, z, d):
        self.vGrid = VoxelGrid(size, x, y, z, d)

    def generateVoxelGridRandom(self, seed):
        self.vGrid = VoxelGrid(0.1, 50, 50, 50, 0)
        noise = Noise(0.5, 5, seed)  # Seed = 188

        # Get max length from grid center to grid surface
        center = Point(self.vGrid.get_max_x() * 0.5, self.vGrid.get_max_y() * 0.5, self.vGrid.get_max_z() * 0.5)
        voxel_origin = Point(0 + 0.5, 0 + 0.5, 0 + 0.5)
        displacement = Vector3(voxel_origin.x(), voxel_origin.y(), voxel_origin.z()).__sub__(Vector3(center.x(), center.y(), center.z()))
        max_distance = displacement.length()
        max_ratio = 1 / max_distance

        # Generate random density
        for kk in range(self.vGrid.get_max_z()):
            for jj in range(self.vGrid.get_max_y()):
                for ii in range(self.vGrid.get_max_x()):
                    cloud = noise.perlin_noise3(ii * self.vGrid.get_voxel_size(), jj * self.vGrid.get_voxel_size(),
                                                kk * self.vGrid.get_voxel_size())

                    voxel = Point(ii + 0.5, jj + 0.5, kk + 0.5)
                    displacement = Vector3(voxel.x(), voxel.y(), voxel.z()).__sub__(Vector3(center.x(), center.y(), center.z()))
                    distance = displacement.length()  # Distance from current voxel to grid center
                    cover = distance * max_ratio + 0.2  # Amount of cloud (0.93)

                    cloud = cloud - cover
                    if cloud < 0:
                        cloud = 0
                    self.vGrid.set_voxel_density(ii, jj, kk, cloud)

                    color = QColor(255, 255, 255)
                    self.vGrid.set_voxel_color(ii, jj, kk, color)

        del noise

    def generatevoxelgridrandom(self, seed, x, y, z):
        self.vGrid = VoxelGrid(0.1, x, y, z, 0)
        noise = Noise(0.5, 5, seed)
        for kk in range(self.vGrid.get_max_z()):
            for jj in range(self.vGrid.get_max_y()):
                for ii in range(self.vGrid.get_max_x()):
                    cloud = noise.perlin_noise3(ii * self.vGrid.get_voxel_size(), jj * self.vGrid.get_voxel_size(),
                                               kk * self.vGrid.get_voxel_size())
                    self.vGrid.set_voxel_density(ii, jj, kk, cloud)
                    color = QColor(255, 255, 255)
                    self.vGrid.set_voxel_color(ii, jj, kk, color)

        del noise

    def putPointsToCache(self, densityDelta):
        self.pointsCache = []
        self.colorCache = []
        center = Point(self.vGrid.get_max_x() / 2, self.vGrid.get_max_y() / 2, self.vGrid.get_max_z() / 2)
        mybuffer = [[0] * self.vGrid.get_max_x() for _ in range(self.vGrid.get_max_z())]
        for yy in range(self.vGrid.get_max_y() - 1, -1, -1):
            for zz in range(self.vGrid.get_max_z()):
                for xx in range(self.vGrid.get_max_x()):
                    if self.vGrid.get_voxel_density(xx, yy, zz) > densityDelta:
                        c = self.vGrid.get_voxel_color(xx, yy, zz)
                        red_component = c.red()
                        green_component = c.green()
                        blue_component = c.blue()
                        color = QColor(
                            int(red_component),
                            int(green_component),
                            int(blue_component),
                            int(self.vGrid.get_voxel_density(xx, yy, zz) * 40)
                        )

                        colorKoef = int(1.5 * mybuffer[zz][xx])

                        color.setRed(color.red() - colorKoef)
                        color.setGreen(color.green() - colorKoef)
                        color.setBlue(color.blue() - colorKoef)
                        mybuffer[zz][xx] += 1
                        self.colorCache.append(color)
                        self.pointsCache.append(Point(xx * 2 - center.x() * 2, yy * 2 - center.y() * 2, zz * 2 - center.z() * 2))

    def renderFromCache(self, scene):
        if not self.pointsCache:
            return
        for i in range(len(self.pointsCache)):
            scene.drawCircle(self.pointsCache[i], 1.5, self.colorCache[i])

    def saveToFile(self, filename):
        with open(filename, 'w') as f:
            f.write(str(len(self.pointsCache)) + '\n')
            for i in range(len(self.pointsCache)):
                p = self.pointsCache[i]
                q = self.colorCache[i]
                f.write(f"{int(p.x())} {int(p.y())} {int(p.z())} {q.red()} {q.green()} {q.blue()} {q.alpha()}\n")

    def readFromFile(self, filename):
        self.vGrid = VoxelGrid(0.1, 5, 5, 5, 0)
        self.pointsCache = []
        self.colorCache = []
        with open(filename, 'r') as f:
            size = int(f.readline().strip())
            for _ in range(size):
                x, y, z, r, g, b, a = map(int, f.readline().strip().split())
                p = Point(x, y, z)
                q = QColor(r, g, b, a)
                self.pointsCache.append(p)
                self.colorCache.append(q)

    def clear(self):
        self.pointsCache = []
        self.colorCache = []

    def getGrid(self):
        return self.vGrid

    def cacheCount(self):
        return len(self.pointsCache)

    def getCenter(self):
        return Point(self.vGrid.get_max_x() / 2, self.vGrid.get_max_y() / 2, self.vGrid.get_max_z() / 2)

