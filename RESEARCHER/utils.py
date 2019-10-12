import os
import secrets
from RESEARCHER import app
from PIL import Image


def save_file(file, path):

	#if image_file:
	
	# create a random name
	random_hex = secrets.token_hex(20)

	# get file extention via os module
	_, extention = os.path.splitext(file.filename)

	# create image name
	filename = random_hex + extention

	# specify image path
	image_path = os.path.join(app.root_path, path, filename)

	# resize image with pillow and save it 
	new_size = (600, 600)
	image = Image.open(image_file)
	image.thumbnail(new_size)
	image.save(image_path)

	## image_file.save(image_path)

	return image_filename

	#return None