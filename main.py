from PIL import Image, ImageDraw
import random

def generate_abstract_image(width, height):
    image = Image.new('RGB', (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(image)

    num_shapes = 100

    for _ in range(num_shapes):
        shape_type = random.choice(['circle', 'rectangle', 'line'])

        x1, y1 = random.randint(0, width), random.randint(0, height)
        x2, y2 = random.randint(0, width), random.randint(0, height)
        fill_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        outline_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        x1, x2 = min(x1, x2), max(x1, x2)
        y1, y2 = min(y1, y2), max(y1, y2)

        if shape_type == 'circle':
            draw.ellipse([x1, y1, x2, y2], fill=fill_color, outline=outline_color)
        elif shape_type == 'rectangle':
            draw.rectangle([x1, y1, x2, y2], fill=fill_color, outline=outline_color)
        elif shape_type == 'line':
            draw.line([x1, y1, x2, y2], fill=outline_color, width=random.randint(1, 10))

    return image

width, height = 3840, 2160
abstract_image = generate_abstract_image(width, height)

abstract_image.save('abstract_4k.png')
