import imageio
from pathlib import Path
data_folder = Path("C:/Users/amatos/Desktop/101MSDCF/")
images = []
filenames = [data_folder  / "Alex1a.JPG", 
          data_folder  / "Alex2a.JPG"]
for filename in filenames:
    print(filename)
    imageio.imread(filename)
    images.append(imageio.imread(filename))
imageio.mimsave('C:\\Users\\amatos\\Desktop\\101MSDCF\\movie.gif', images, duration=0.5)