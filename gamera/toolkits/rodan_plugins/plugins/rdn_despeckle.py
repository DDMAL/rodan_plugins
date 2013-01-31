from gamera.plugin import PluginFunction, PluginModule
from gamera.args import ImageType, Args, Int
from gamera.enums import ONEBIT


class rdn_despeckle(PluginFunction):
    """
        A thin wrapper around despeckle() to get the
        desired despeckling behaviour for Rodan.

        Desired behaviour involves returning a gamera Image, rather
        just applying it to the image that is passed in and returning nothing.
    """
    pure_python = 1
    self_type = ImageType(ONEBIT)
    return_type = ImageType(ONEBIT)
    args = Args([Int('cc_size', range=(1, 100))])

    def __call__(self, cc_size):
        self.despeckle(cc_size)
        return self

    __call__ = staticmethod(__call__)


class RodanDespecklePluginGenerator(PluginModule):
    category = "Despeckling"
    cpp_headers = []
    functions = [rdn_despeckle]
    author = "Anton Khelou"
    url = "http://ddmal.music.mcgill.ca"

module = RodanDespecklePluginGenerator()
