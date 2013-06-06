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

    def __call__(self, ulx, uly, lrx, lry, imw=0):
        if imw is 0:
            scale_factor = 1
        else:
            scale_factor = float(self.ncols) / float(imw)

        #added '- 1' to lower right point coordinates because gamera subimage goes 1 pixel over.
        arg_ulx = scale_factor * ulx
        arg_uly = scale_factor * uly
        arg_lrx = scale_factor * lrx - 1
        arg_lry = scale_factor * lry - 1

        if arg_ulx < 0:
            arg_ulx = 0
        if arg_ulx > self.ncols:
            arg_ulx = self.ncols

        if arg_lrx < 0:
            arg_lrx = 0
        if arg_lrx > (self.ncols - 1):
            arg_lrx = self.ncols - 1

        if arg_uly < 0:
            arg_uly = 0
        if arg_uly > self.nrows:
            arg_uly = self.nrows

        if arg_lry < 0:
            arg_lry = 0
        if arg_lry > (self.nrows - 1):
            arg_lry = self.nrows - 1

        return self.subimage((arg_ulx, arg_uly), (arg_lrx, arg_lry))

    __call__ = staticmethod(__call__)


class RodanCropPluginGenerator(PluginModule):
    category = "Cropping"
    cpp_headers = []
    functions = [rdn_crop]
    author = "Andrew Hankinson"
    url = "http://ddmal.music.mcgill.ca"

module = RodanCropPluginGenerator()
