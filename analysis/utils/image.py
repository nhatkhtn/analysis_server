import numpy as np
from PIL import Image

import matplotlib.path as mplPath

def CalcAveragesInROI(image: Image.Image, r: tuple[tuple[int, int], tuple[int, int]]):
    """Calculate the average image intensity in a rectangle.

    From `notebooks/polygon_analysis_avg.ipynb`

    Args:
        image: PIL image
        r: pair of xy coordinates of the corners of a rectangle
    Returns: 
        A tuple of the average intensity for each channel
    """
    R = G = B = cnt = 0
    
    minX = min(r[0][0], r[1][0], r[2][0], r[3][0])
    maxX = max(r[0][0], r[1][0], r[2][0], r[3][0])
    minY = min(r[0][1], r[1][1], r[2][1], r[3][1])
    maxY = max(r[0][1], r[1][1], r[2][1], r[3][1])
    
    poly_path = mplPath.Path(np.array(r))

    for y in range(minY, maxY):
        for x in range(minX, maxX):
            if poly_path.contains_points([(x, y)]):
                pix = image.getpixel((x, y))
                R += pix[0]
                G += pix[1]
                B += pix[2]
                cnt += 1
                image.putpixel((x, y), (255, 255, 255)) # for testing
    
    return R/cnt, G/cnt, B/cnt