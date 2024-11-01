from PIL import Image
from numpy import asarray

need_rotate = True
img_count = 8
white = (255, 255, 255)
angels = [0, 5, 10, 15, 20, 25, -5, -10, -15, -20, -25]
folders = ["alpha", "beta", "delta", "epsilon", "eta", "gamma", "kappa", "mu",
           "sigma", "theta"]
ALPHABET = {
    "alpha": "A",
    "beta": "B",
    "delta": "D",
    "epsilon": "E",
    "gamma": "G",
    "sigma": "Sigma",
    "eta": "H",
    "theta": "Theta",
    "kappa": "K",
    "mu": "M",
}
ALPHABET_INV = {
    "A": "alpha",
    "B": "beta",
    "D": "delta",
    "E": "epsilon",
    "G": "gamma",
    "Sigma": "sigma",
    "H": "eta",
    "Theta": "theta",
    "K": "kappa",
    "M": "mu",
}

# rotate part
if need_rotate:
    for folder in folders:
        for img_index in range(img_count):
            im = Image.open(f'dataSet/Learning/{folder}/{ALPHABET[folder]}_{img_index}.png')
            im = Image.open(f'dataSet/{folder}/{ALPHABET[folder]}_{img_index}_{angel}.bmp')

            for angel in angels:
                im_rotate = im.rotate(angel, fillcolor=white)
                im_rotate.save(f'dataSet/{folder}/{ALPHABET[folder]}_{img_index}_{angel}.png', quality=100)

            im.close()

#.csv part
ROOT_PATH = 'dataSet/Learning'
id = 0
csv_annotation = open('dataSet/Test/annotation.csv', 'w')
for folder in folders:
    for img_index in range(8, 11):
        for angel in angels:
            img_path = f'{ROOT_PATH}/{folder}/{ALPHABET[folder]}_{img_index}_{angel}.bmp'
            try:
                im = Image.open(img_path)
                pixels = asarray(im)
                bin_img = ""
                for i in range(im.height):
                    for px in pixels[i]:
                        if px[0] == 255 and px[1] == 255 and px[2] == 255:
                            bin_img += '0; '
                        else:
                            bin_img += '1; '

                bin_img += f'{folder}; {id}; \r'
                csv_annotation.write(bin_img)
                id += 1

                im.close()

            except:
                print(f'Can`t open: {img_path}')

csv_annotation.close()
