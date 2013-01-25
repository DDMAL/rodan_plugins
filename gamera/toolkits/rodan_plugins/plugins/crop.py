from gamera.plugin import PluginFunction, PluginModule
from gamera.args import ImageType, Args, Int
from gamera.enums import ALL


class crop(PluginFunction):
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
        return self.subimage((ulx, uly), (lrx, lry))

    __call__ = staticmethod(__call__)


class CropPluginGenerator(PluginModule):
    category = "Cropping"
    cpp_headers = []
    functions = [crop]
    author = "Andrew Hankinson"
    url = "http://ddmal.music.mcgill.ca"

module = CropPluginGenerator()
