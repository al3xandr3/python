
# pip install wordcloud
# https://github.com/amueller/word_cloud

from os import path
import matplotlib.pyplot as plt
import sys
from wordcloud import WordCloud


def cloudy(text):
    # Read the whole text
    
    wordc = WordCloud().generate(text)
    # Open a plot of the generated image.
    plt.imshow(wordc)
    plt.axis("off")
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("Use: python textcloud.py text.txt")
    
    text = open(sys.argv[1]).read()
    cloudy ( text )