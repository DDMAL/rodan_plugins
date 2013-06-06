from gamera.plugin import PluginFunction, PluginModule
from gamera.args import ImageType, Args, Int
from gamera.enums import ONEBIT


class rdn_despeckle(PluginFunction):
    """
        A thin wrapper around despeckle() to get the
        desired despeckling behaviour for Rodan.

        Desired behaviour involves returning a gamera Image, rather
        just applying it to the image that is passed in and returning nothingm,
        and also scaling the cc_size, although I'm (Deepanjan) not sure if this works.
    """
    pure_python = 1
    self_type = ImageType(ONEBIT)
    return_type = ImageType(ONEBIT)
    args = Args([Int('cc_size', range=(1, 100)), Int('image_width')])

    def __call__(self, cc_size, image_width=0):

        if image_width == 0:
            scale_factor = 1
        else:
            scale_factor = float(self.ncols) / float(image_width)

        print "effective cc size = " + str(int(cc_size*scale_factor))
        self.despeckle(int(cc_size*scale_factor))
        return self

    __call__ = staticmethod(__call__)


class RodanDespecklePluginGenerator(PluginModule):
    category = "Despeckling"
    cpp_headers = []
    functions = [rdn_despeckle]
    author = "Anton Khelou"
    url = "http://ddmal.music.mcgill.ca"

module = RodanDespecklePluginGenerator()
