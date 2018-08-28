import numpy as np
import multiprocessing as mp

import imageio
from tkinter import *
from PIL import Image, ImageTk as itk

class Fractal(object):
	def __init__(self,
		     mode = 'julia',
		     width = 320, 
		     height = 240,
		     radius = 10,
		     duration = 0.2,
		     frames = 10):
		self.mode = mode
		self.width = width
		self.height = height
		self.radius = radius
		self.duration = duration

		if mode == 'mandelbrot':
			self.frames = 1
		else:
			self.frames = frames

	def display_anim(self, image_list):
		root = Tk()
		title = '{} Fractal'.format(self.mode)
		root.title(title)

		frames = [Image.fromarray(img) for img in image_list]
		count = len(frames)
		def update(idx):
			photo = itk.PhotoImage(frames[idx])
			label.configure(image = photo)
			label.image = photo
			idx += 1
			root.after(200, update, idx % count)

		label = Label(root, width = self.width, height = self.height)
		label.pack()
		root.after(0, update, 0)
		root.mainloop()

	def save_anim(self, image_list, extension = 'gif'):
		name = self.mode
		save_name = '{0}.{1}'.format(name, extension)
		imageio.mimsave(save_name, image_list, duration = self.duration)

	def compute_pixel(self, z, c):
		intensity = 255
		if self.mode != 'julia':
			c = z
			z = 0
		while abs(z) < self.radius and intensity > 0:
			z = z**2 + c
			intensity -= 5
		return intensity

	def compute_row(self, imag, c_real, c_imag):
		row = []
		for real in np.linspace(-2., 2., self.width):
			z = complex(real, imag)
			c = complex(c_real, c_imag)
			row.append(self.compute_pixel(z, c))
		return row

	def generate_img(self, c_real, c_imag):
		pool = mp.Pool(mp.cpu_count() - 1)
		ps_list = []
		for imag in np.linspace(-2., 2., self.height):
			ps_list.append(pool.apply_async(self.compute_row, [imag, c_real, c_imag]))
		img = np.vstack([ps.get() for ps in ps_list])
		img = img.astype(np.uint8)
		return img


	def plot_fractal(self, c_real = -0.7):
		steps = self.frames

		image_list = []	
		for c_imag in np.linspace(0., 1., steps):
			image_list.append(self.generate_img(c_real, c_imag))
		self.display_anim(image_list)
		self.save_anim(image_list)

def main():
	mode = 'julia'
	width = 640
	height = 480
	frames = 20

	c_real = -0.7

	fractal = Fractal(mode = mode,
			  width = width, 
			  height = height,
			  frames = frames)
	fractal.plot_fractal(c_real = c_real)

if __name__ == '__main__':
	main()
