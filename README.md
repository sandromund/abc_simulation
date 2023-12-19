# ABC Optimization Algorithm

My implementation and visualisation of the [artificial bee colony (ABC)](https://en.wikipedia.org/wiki/Artificial_bee_colony_algorithm) optimization algorithm.

I left out the evaluation part by adding more bees and was surprised that the optimizations still worked well. 


<p align="center">
    <img src="abc.gif"  width="60%" height="30%">
</p>

To illustrate this, we search for the four local minima of the
def [Himmelblau function](https://en.wikipedia.org/wiki/Himmelblau%27s_function).

````python
f(x, y) == (x ** 2 + y - 11) ** 2 + (x + y ** 2 - 7) ** 2
````

<p align="center">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ad/Himmelblau_function.svg/1280px-Himmelblau_function.svg.png"  width="60%" height="30%">
</p>


# Create a .gif from frames
Useful code form [stack overflow](https://stackoverflow.com/questions/753190/programmatically-generate-video-or-animated-gif-in-python).
Set ``save_frames`` to true in `main.py` and then create a gif from the png images. 
````python
import glob
import contextlib
from PIL import Image

fp_in = "*.png"
fp_out = "abc.gif"

with contextlib.ExitStack() as stack:
    frames = (stack.enter_context(Image.open(f)) for f in sorted(glob.glob(fp_in)))
    img = next(frames)
    img.save(fp=fp_out, format='GIF', append_images=frames, save_all=True, duration=200, loop=0)

````