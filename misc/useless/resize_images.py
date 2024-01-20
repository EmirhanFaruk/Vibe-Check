
# Modification date: Sat Jun 11 14:21:18 2022

# Production date: Sun Sep  3 15:44:21 2023

from PIL import Image

"""
for i in range(6):
    image = Image.open(f'shadow_palm{i + 1}.png')
    image.thumbnail((150, 150))
    image.save(f'shadow_palm{i + 1}edit.png')
"""
image = Image.open(f'shadow_palm6.png')
da_img = image.resize((32, 32))
da_img.save(f'icon.png')
