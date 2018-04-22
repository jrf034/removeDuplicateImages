from PIL import Image
import imagehash
import os

class ImageInfo(object):

	def __init__(self, name, folder):
		self.name = name
		self.hash_val = self.get_hash(name, folder)

	def get_hash(self, name, folder):
		return imagehash.average_hash(Image.open(folder + str(name)))

def make_array(folder):
	directory = os.fsencode(folder)
	ret_arr = []

	for file in os.listdir(directory):
		filename = os.fsdecode(file)
		if filename.endswith(".jpg"): 
			ret_arr.append(ImageInfo(filename, folder))
			continue
		else:
			continue
	return ret_arr

def delete_duplicates(arr, folder):
	x = 0
	for obj_x in arr:
		y = 0
		for obj_y in arr:
			if obj_x.name != obj_y.name: #not comparing it with itself
				if obj_x.hash_val == obj_y.hash_val:
					print("Removing found duplicate: " + obj_x.name + " & " + obj_y.name + ". With hashes: " + str(obj_x.hash_val) + " --- " + str(obj_y.hash_val))
					os.remove(folder + obj_y.name)
					arr.pop(y)
					x += 1
			y += 1
	print("Removed " + str(x) + " duplicate images.")

def remove_small_images(folder):
	directory = os.fsencode(folder)
	x = 0
	for file in os.listdir(directory):
		filename = os.fsdecode(file)
		if filename.endswith(".jpg"):
			width, height = Image.open(folder + filename).size
			if width < 1920:
				os.remove(folder + filename)
				x += 1
			continue
	print("Removed " + str(x) + " images with incorrect dimensions.")

remove_small_images("./wallpapers/")
obj_arr = make_array("./wallpapers/")
delete_duplicates(obj_arr, "./wallpapers/")
