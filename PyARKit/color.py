from objc_util import ObjCClass

UIColor=ObjCClass('UIColor')


class Color:
    def __init__(self, obj):
        self.obj = obj

    def get(self):
        return self.obj

    @classmethod
    def black(cls):
        return cls(UIColor.blackColor().CGColor())

    @classmethod
    def blue(cls):
        return cls(UIColor.blueColor().CGColor())

    @classmethod
    def brown(cls):
        return cls(UIColor.brownColor().CGColor())

    @classmethod
    def clear(cls):
        return cls(UIColor.clearColor().CGColor())

    @classmethod
    def cyan(cls):
        return cls(UIColor.cyanColor().CGColor())

    @classmethod
    def darkgray(cls):
        return cls(UIColor.darkGrayColor().CGColor())

    @classmethod
    def gray(cls):
        return cls(UIColor.grayColor().CGColor())

    @classmethod
    def green(cls):
        return cls(UIColor.greenColor().CGColor())

    @classmethod
    def lightgray(cls):
        return cls(UIColor.lightGrayColor().CGColor())

    @classmethod
    def magenta(cls):
        return cls(UIColor.magentaColor().CGColor())

    @classmethod
    def orange(cls):
        return cls(UIColor.orangeColor().CGColor())

    @classmethod
    def purple(cls):
        return cls(UIColor.purpleColor().CGColor())

    @classmethod
    def red(cls):
        return cls(UIColor.redColor().CGColor())

    @classmethod
    def white(cls):
        return cls(UIColor.whiteColor().CGColor())

    @classmethod
    def yellow(cls):
        return cls(UIColor.yellowColor().CGColor())
