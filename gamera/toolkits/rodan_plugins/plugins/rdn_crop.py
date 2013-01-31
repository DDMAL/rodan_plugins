from gamera.plugin import PluginFunction, PluginModule
from gamera.args import ImageType, Args, Int
from gamera.enums import ALL


class rdn_crop(PluginFunction):
    """
        A thin wrapper around subimage() to get the
        desired cropping behaviour for Rodan.

        See http://gamera.sourceforge.net/doc/html/utility.html#subimage
        for more info on why this is necessary.
    """
    pure_python = 1
    self_type = ImageType(ALL)
    return_type = ImageType(ALL)
    args = Args([Int("ulx"), Int("uly"), Int("lrx"), Int("lry")])

    def __call__(self, ulx, uly, lrx, lry):
        #added '- 1' to lower right point coordinates because gamera subimage goes 1 pixel over.
        return self.subimage((ulx, uly), (lrx - 1, lry - 1))

    __call__ = staticmethod(__call__)


class RodanCropPluginGenerator(PluginModule):
    category = "cropping"
    cpp_headers = []
    functions = [rdn_crop]
    author = "Andrew Hankinson"
    url = "http://ddmal.music.mcgill.ca"

module = RodanCropPluginGenerator()
