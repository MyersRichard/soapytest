"""
Makes and saves plots for the SH WFS
"""

import plotly
from plotly.graph_objs import Scatter, Layout
import os

from .. import wfs

SOAPYTEST_DIR = os.path.join(
        os.path.dirname(os.path.realpath(__file__)), "../../")

def plotSHPixelScale():
    print("\nPLOT SH WFS PIXELSCALE\n***")
    ps, mps = wfs.shpixelscale.testPixelScale()

    filename = os.path.join(SOAPYTEST_DIR, 'plots/shpixelscale.html')
    plotly.offline.plot(
            {   "data":[
                    Scatter(x=ps, y=mps, name="Soapy Pixel Scale"),
                    Scatter(x=ps, y=ps, name='Theoretical', line={'dash':'dash'})],
                "layout":Layout(title='Pixel Scale')},
            auto_open=False,
            filename=filename)


if __name__ == '__main__':
    plotSHPixelScale()
