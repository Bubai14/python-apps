import glob


def capture():
    all_images = glob.glob("images/*.png")
    index = int(len(all_images) / 2)
    image_with_object = all_images[index]
    print("Image captured!!")
