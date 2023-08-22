from PIL import Image, ImageDraw, ImageFont


class PhotoWatermark:
    def add_photo_watermark(self, path, watermark_image_path, size_option):
        img = Image.open(path)
        watermark_image = Image.open(watermark_image_path)
        watermark_image = watermark_image.resize((int(watermark_image.width / (size_option / 3)), int(watermark_image.height / (size_option / 3))))

        img = img.copy()
        img.paste(watermark_image, (int((img.width // 2) - watermark_image.width // 2), int((img.height // 2) - watermark_image.height // 2)))
        return img
