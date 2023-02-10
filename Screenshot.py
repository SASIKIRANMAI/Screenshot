from PIL import ImageGrab

import random

import time

while True:
	
	random_time = random.randint(1, 5)

	
	time.sleep(random_time)

	
	snapshot = ImageGrab.grab()

	
	file_name = str(time.time())+".png"
	snapshot.save(file_name)
