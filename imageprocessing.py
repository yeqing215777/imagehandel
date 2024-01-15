from PIL import Image
import numpy as np
from tqdm import tqdm


class ImageHandel():
    def __init__(self, image: Image):
        self.image = image

    @staticmethod
    def config(pixel: int = 0):
        return {
            "l": (-pixel, 0),
            "r": (pixel, 0),
            "t": (0, -pixel),
            "d": (0, pixel),
            "lt": (-pixel, -pixel),
            "rt": (pixel, -pixel),
            "rd": (pixel, pixel),
            "ld": (-pixel, pixel)
        }

    def move(self, direction: str, pixel: int):
        """
        根据方位移动图像
        :param direction: 移动位置：l左，r右，t上，d下，lt左上，rt右上，ld左下，rd右下
        :param pixel: 移动的像素
        :return:
        """
        img = Image.new('RGB', self.image.size, 'black')
        img.paste(self.image, self.config(pixel)[direction])
        return np.array(img)


class SplitImage():
    def __init__(self, image):
        self.image = image
        self.size = self.image.size

    def split(self, mark):
        """
        按mark矩阵切割图片碎片
        :param mark:
        :return list:
        """
        width, height = self.image.size
        num_tiles_x = width // mark[0]
        num_tiles_y = height // mark[1]
        tiles = []
        for y in range(num_tiles_y):
            for x in range(num_tiles_x):
                left = x * mark[0]
                top = y * mark[1]
                right = left + mark[0]
                bottom = top + mark[1]
                tile = self.image.crop((left, top, right, bottom))
                tiles.append(tile)
        return tiles


if __name__ == '__main__':
    image = Image.open("1.jpg")
    ih = ImageHandel(image)
    pixel = 200
    config = ih.config()
    for k, v in tqdm(config.items(), desc=u'handeling:'):
        array = ih.move(k, pixel)
        img = Image.fromarray(array)
       #  img.save(f'out/{k}.png')
        si = SplitImage(img)
        tiles = si.split((128, 128))
        i = 0
        for tile in tiles:
            tile.save(f'out/{k}_{i}.png')
            i += 1
    #
    # image = Image.open("1.jpg")
    # si = SplitImage(image)
    # tiles = si.split((128, 64))
    # i = 0
    # for tile in tqdm(tiles, desc=u'spliting:'):
    #     tile.save(f'out/tile_{i}.png')
    #     i += 1

