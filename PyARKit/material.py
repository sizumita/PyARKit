from objc_util import ObjCClass, ObjCInstance, CGRect, CGPoint, CGSize, load_framework
from color import Color
load_framework('SceneKit')
load_framework('ARKit')

SCNScene = ObjCClass('SCNScene')
SCNView = ObjCClass('SCNView')
SCNNode = ObjCClass('SCNNode')
SCNCamera = ObjCClass('SCNCamera')
SCNMaterial = ObjCClass('SCNMaterial')
SCNBox = ObjCClass('SCNBox')
UIColor = ObjCClass('UIColor')
SCNLight = ObjCClass('SCNLight')
SCNText = ObjCClass('SCNText')

ARWorldTrackingConfiguration = ObjCClass('ARWorldTrackingConfiguration')
ARSCNView = ObjCClass('ARSCNView')
ARSession = ObjCClass('ARSession')


class Material:
    def __init__(self, obj, position=None, color=None):
        self.obj = obj
        self.position = position or (0, 0, 0)
        self.node = SCNNode.nodeWithGeometry_(self.obj)
        if position is not None:
            self.set_position()
        if color is not None:
            self.set_color(color)

    def set_position(self):
        self.node.setPosition_(self.position)

    def set_color(self, color):
        if not isinstance(color, Color):
            self.obj.setColor_(color)
        self.obj.material().setColor_(color.get())

    @classmethod
    def Box(cls, width=0, height=0, length=0, chamferRadius=0, position=None):
        box_obj = SCNBox.boxWithWidth_height_length_chamferRadius_(width, height, length, chamferRadius).autorelease()
        return cls(box_obj, position)


class Light:
    def __init__(self, position=None, light_type='omni', color=None):
        self.obj = SCNLight.light()
        self.position = position or (0, 0, 0)
        self.obj.setType_(light_type)
        self.node = SCNNode.node()
        self.node.setLight_(self.obj)
        
        if position is not None:
            self.set_position()
        
        if color is not None:
            self.set_color(color)

    def set_position(self):
        self.node.setPosition_(self.position)
    
    def set_color(self, color):
        if not isinstance(color, Color):
            self.obj.setColor_(color)
        self.obj.setColor_(color.get())

