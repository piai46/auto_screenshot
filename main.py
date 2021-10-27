from time import sleep
import pyscreenshot, datetime, os
from PIL import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

SCREENSHOT_EVERY = 2 #Time in seconds

class Screenshot:
    def __init__(self, screenshot_time) -> None:
        self.screenshot_time = screenshot_time

    def take_screenshot(self):
        image = pyscreenshot.grab()
        return image

    def saving_screenshot(self, image, name):
        all_directory = os.listdir()
        if 'screenshots' not in all_directory:
            os.makedirs('screenshots')
        file_compressed = os.listdir('./screenshots/')
        if 'not_compressed' not in file_compressed:
            os.makedirs('./screenshots/not_compressed/')
        image.save(f'./screenshots/not_compressed/{name}.png')
        print('Screenshot saved!')

    def screenshot_name(self):
        return datetime.datetime.today().strftime('%d-%m-%Y_%H-%M-%S')

    def compress_images(self):
        all_directory = os.listdir('./screenshots/')
        if 'compressed' not in all_directory:
            os.makedirs('./screenshots/compressed')
        path_not_compressed = os.listdir('./screenshots/not_compressed')
        for f in path_not_compressed:
            if f.endswith('.png'):
                img = Image.open(f'./screenshots/not_compressed/{f}')
                img = img.resize((1024,768), Image.ANTIALIAS)
                img.save(f'./screenshots/compressed/C_{f}', optmize=True, quality=80)
        print('All images compressed!')
        self.remove_not_compressed()

    def remove_not_compressed(self):
        all_directory = os.listdir('./screenshots/')
        if 'not_compressed' in all_directory:
            not_comp_img = os.listdir('./screenshots/not_compressed')
            for img in not_comp_img:
                os.remove(f'./screenshots/not_compressed/{img}')
            print('Images not compressed was removed!')

    def run(self):
        while True:
            for i in range(10):
                name = self.screenshot_name()
                image = self.take_screenshot()
                self.saving_screenshot(image, name)
                sleep(self.screenshot_time)
            self.compress_images()

if __name__ == '__main__':
    screen = Screenshot(SCREENSHOT_EVERY)
    screen.run()