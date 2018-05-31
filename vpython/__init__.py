from browser import document, window

GLOWSCRIPT = window.glowscript

from .primitive import box, arrow, cone, curve, pyramid, helix, cylinder, ellipsoid
from .primitive import sphere, ring, attach_trail, compound, extrusion, text
from .utils import create_script_tag
from .vector import vec
import os

project_stdlib = "../stlib/"  # os.path.dirname("../stdlib{}/".format(os.path.abspath(__file__)))

version = "2.7"

create_script_tag(project_stdlib + 'glow.2.7.min.js')


class Glow:
    def __init__(self, container):
        self._id = document.get(id=container)[0]
        setattr(self._id, 'id', '')

        setattr(window, '__context', {})
        setattr(getattr(window, '__context'), 'glowscript_container',
                self._id.elt)


# todo, make canvas its own class
def canvas():
    return window.glowscript.canvas()


def rate(t, func):
    window.glowscript.rate(t, func)


color = window.glowscript.color
