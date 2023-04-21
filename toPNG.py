import sys
import os
from PIL import Image

image_folder = sys.argv[1] #folder name
output_folder = sys.argv[2] #new folder name

# check if new/ exists, if not create
if not os.path.exists(output_folder):
    os.mkdir(output_folder)

# iterate through pokedex/ files
# change file type to png
# save to new/ file
for filename in os.listdir(image_folder):
    if filename.endswith('.jpg'):
        clean_name = os.path.splitext(filename)[0]
        img = Image.open(f'{image_folder}{filename}')
        img.save(f'{output_folder}{clean_name}.png', 'png')
print('All done')


