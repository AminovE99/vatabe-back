from PIL import Image
import io


def compress_image(instance_image):
    img_io = io.BytesIO()

    image = Image.open(instance_image)
    exif_orientation_tag = 274
    if (
            hasattr(image, "_getexif")
            and isinstance(image._getexif(), dict)
            and exif_orientation_tag in image._getexif()
    ):
        orientation = image._getexif()[exif_orientation_tag]

        if orientation == 1:
            pass
        elif orientation == 2:
            image = image.transpose(Image.FLIP_LEFT_RIGHT)
        elif orientation == 3:
            image = image.rotate(180)
        elif orientation == 4:
            image = image.rotate(180).transpose(Image.FLIP_LEFT_RIGHT)
        elif orientation == 5:
            image = image.rotate(-90, expand=True).transpose(Image.FLIP_LEFT_RIGHT)
        elif orientation == 6:
            image = image.rotate(-90, expand=True)
        elif orientation == 7:
            image = image.rotate(90, expand=True).transpose(Image.FLIP_LEFT_RIGHT)
        elif orientation == 8:
            image = image.rotate(90, expand=True)

    width = 320
    width_percent = width / float(image.size[0])
    height = int((float(image.size[1]) * float(width_percent)))
    final_image = image.resize((width, height), Image.ANTIALIAS)

    final_image.convert("RGB").save(img_io, format="JPEG", quality=90)

    return img_io


def compress_user_avatar(instance):
    image_io = compress_image(instance.avatar)
    instance.avatar.save(
        f"user-{instance.pk}.jpg", content=image_io, save=False,
    )
