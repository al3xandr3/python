
import Image
import sys

# from http://stackoverflow.com/questions/10640114/overlay-two-same-sized-images-in-python

if len(sys.argv) < 3:
	sys.exit("Use: python blendpic.py 1.png 2.png")

background = Image.open(sys.argv[1])
overlay = Image.open(sys.argv[2])

background = background.convert("RGBA")
overlay    = overlay.convert("RGBA")

new_img = Image.blend(background, overlay, 0.5)
new_img.save("blend.png","PNG")
