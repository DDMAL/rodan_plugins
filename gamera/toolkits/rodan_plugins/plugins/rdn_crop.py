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
    args = Args([Int("ulx"), Int("uly"), Int("lrx"), Int("lry"), Int("imw")])

    def __call__(self, ulx, uly, lrx, lry, imw=None):
        if imw is None:
            scale_factor = 1
        else:
            scale_factor = self.ncols / imw

        #added '- 1' to lower right point coordinates because gamera subimage goes 1 pixel over.
        return self.subimage((scale_factor * ulx, scale_factor * uly), (scale_factor * lrx - 1, scale_factor * lry - 1))

    __call__ = staticmethod(__call__)


class RodanCropPluginGenerator(PluginModule):
    category = "Cropping"
    cpp_headers = []
    functions = [rdn_crop]
    author = "Andrew Hankinson"
    url = "http://ddmal.music.mcgill.ca"

module = RodanCropPluginGenerator()
