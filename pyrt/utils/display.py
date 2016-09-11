"""
This is a display utility for IPython / Jupyter Notebook

It also uses PIL (Pillow) to encode images
This code is not essential for pyRT, it just simplifies displaying stuff in Jupyter.
"""



try:
    from IPython.core.display import HTML
    g_hasIPython = True
except:
    g_hasIPython = False

try:
    from PIL import Image as PILImage
    g_hasPIL = True
except:
    g_hasPIL = False

import base64
from io import BytesIO


def display(imagedata, w, h):
    """
    This is the display function - use only with a running Jupyter notebook.

    :param imagedata: list containing rgb values
    :param w: width of the image
    :param h: height of the image
    :return: HTML object representing the image or None if PIL/Jupyter unavailable.
    """
    if g_hasIPython and g_hasPIL:
        im = PILImage.new("RGB", (w, h))
        im.putdata(imagedata)
        buffer = BytesIO()
        im.save(buffer, format="PNG")
        img_str = str(base64.b64encode(buffer.getvalue()), encoding="ascii")
        return HTML('<img src="data:image/png;base64,' + img_str + '"></img>')
    else:
        print("WARNING: display function needs Jupyter notebook and PIL")
        return None