from gamera.plugin import PluginFunction, PluginModule
from gamera.args import ImageType, Args, Int
from gamera.enums import ALL


class rdn_rotate(PluginFunction):
    """
        A thin wrapper around subimage() to get the
        desired cropping behaviour for Rodan.

        See http://gamera.sourceforge.net/doc/html/utility.html#subimage
        for more info on why this is necessary.
    """
    pure_python = 1
    self_type = ImageType(ALL)
    return_type = ImageType(ALL)
    args = Args([Int("angle")])

    def __call__(self, angle):
        if angle != 0:
            output_image = self.rotate(angle)
        else:
            output_image = self
        return output_image

    __call__ = staticmethod(__call__)


class RodanRotatePluginGenerator(PluginModule):
    category = "rotating"
    cpp_headers = []
    functions = [rdn_rotate]
    author = "Anton Khelou"
    url = "http://ddmal.music.mcgill.ca"

module = RodanRotatePluginGenerator()
