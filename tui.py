class Tui:
    def get_watermark_size(self):
        size = input('Select text size (S/M/L/XL): ').upper()

        match size:
            case 'S':
                return 24
            case 'M':
                return 20
            case 'L':
                return 14
            case 'XL':
                return 10

    def get_watermark_type(self):
        return input('Watermark type (text/image): ').upper()

    def get_watermark_text(self):
        return input('Watermark text: ')

    def get_watermark_image(self):
        return input('Watermark image path: ')

    def get_image_path(self):
        return input('Image path: ')
