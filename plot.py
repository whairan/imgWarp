import numpy as np

from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool

N = 1500

x = np.linspace(0, 4, N)
y = np.linspace(0, 5, N)

xx, yy = np.meshgrid(x, y)
d = np.sin(xx)*np.cos(yy)

p = figure(x_range=(0, 10), y_range=(0, 10),
           tools=[HoverTool(tooltips=[("x", "$x"), ("y", "$y"), ("value", "@image")])])

# must give a vector of image data for image parameter
p.image(image=[d], x=5, y=5, dw=5, dh=5, palette="Spectral11")

output_file("image.html", title="image.py example")

show(p)  # open a browser