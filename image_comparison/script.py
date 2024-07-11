""" 
Скрипт для сравнения двух изображений и отображения разницы между ними.

Зависимости: 

- pip install Pillow
- pip install numpy

"""

from PIL import Image
import numpy


class Config:
    """Класс для хранения конфигурационных параметров"""

    expectation_path = "./image_comparison/expected_screenshot.png"
    actual_path = "./image_comparison/actual_screenshot.png"
    difference_path = "./image_comparison/output_difference_screenshot.png"


class ImageLoader:
    """Класс для загрузки изображений"""

    def __init__(self, image_path):
        self.image_path = image_path
        self.image = None

    def load_image(self):
        self.image = Image.open(self.image_path).convert("RGB")
        return self.image


class ImageComparer:
    """Класс для сравнения двух изображений"""

    def __init__(self, img1, img2):
        if img1.size != img2.size:
            raise ValueError("Изображения разного размера.")
        self.img1 = img1
        self.img2 = img2

    def calculate_difference(self):
        img1_array = numpy.array(self.img1)
        img2_array = numpy.array(self.img2)
        diff = numpy.abs(img1_array - img2_array)
        mask = numpy.any(diff > 0, axis=-1)
        difference_percentage = (numpy.sum(mask) / mask.size) * 100
        return mask, difference_percentage


class ImageDifferencer:
    """Класс для отображения разницы между двумя изображениями"""

    @staticmethod
    def apply_overlay(img, mask):
        result_array = numpy.array(img.copy())
        color_rgb = [255, 255, 0]  # ргб цвета которым будут выделены различия
        result_array[mask] = color_rgb
        return result_array


class DifferenceImageGenerator:
    """Класс для генерации изображения с разницей между ними"""

    def __init__(self, img1, img2, difference_path):
        self.comparer = ImageComparer(img1, img2)
        self.difference_path = difference_path

    def generate_difference_image(self):
        mask, difference_percentage = self.comparer.calculate_difference()
        result_array = ImageDifferencer.apply_overlay(self.comparer.img1, mask)
        result_image = Image.fromarray(result_array)
        result_image.save(self.difference_path)
        return difference_percentage

if __name__ == "__main__":

    expectation_loader = ImageLoader(Config.expectation_path)
    actual_loader = ImageLoader(Config.actual_path)

    expectation_image = expectation_loader.load_image()
    actual_image = actual_loader.load_image()

    difference_generator = DifferenceImageGenerator(
        expectation_image, actual_image, Config.difference_path
    )
    difference_percentage = difference_generator.generate_difference_image()
    print(
        f"\nСгенерировано финальное изображение, разница между ожиданием и фактом = {difference_percentage:.2f}%\n"
    )
