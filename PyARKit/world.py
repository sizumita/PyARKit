import ui
from material import Material, Light
from color import Color
from objc_util import ObjCClass, ObjCInstance, CGRect, CGPoint, CGSize, load_framework

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

ARWorldTrackingConfiguration = ObjCClass('ARWorldTrackingConfiguration')
ARSCNView = ObjCClass('ARSCNView')
ARSession = ObjCClass('ARSession')


class World(ui.View):
    def __init__(self, frame=None,):
        self.frame = frame or (0, 0, 100, 100)
        self.width = self.frame[2]
        self.height = self.frame[3]
        flex_width, flex_height = (1 << 1), (1 << 4)
        self.instance = ObjCInstance(self)
        self.rect = CGRect(CGPoint(0, 0), CGSize(self.width, self.height))
        self.scn_view = ARSCNView.alloc().initWithFrame_options_(self.rect, None).autorelease()
        self.scn_view.setAutoresizingMask_(flex_width|flex_height)

        self.scene = SCNScene.scene()
        self.scn_view.showsStatistics = 1
        self.scn_view.scene = self.scene
        
        self.ar_configuration = ARWorldTrackingConfiguration.new()
        self.ar_session = ARSession.new()
        self.ar_session.delegate = self
        self.ar_session.runWithConfiguration_(self.ar_configuration)
        self.scn_view.setSession_(self.ar_session)
        
        self.instance.addSubview_(self.scn_view)

    def add_material(self, material):
        if not isinstance(material, Material):
            self.scene.rootNode().addChildNode_(material)
            return

        self.scene.rootNode().addChildNode_(material.node)

    def add_light(self, light):
        if not isinstance(light, Light):
            self.scene.rootNode().addChildNode_(light)
            return

        self.scene.rootNode().addChildNode_(light.node)


if __name__ == '__main__':
    w = World()
    m = Material.Box(height=0.1, width=0.1, length=0.1, chamferRadius=0.05, position=(0, 0, -0.2))
    
    l = Light((-40,40,60), color=Color.blue())
    l2 = Light(light_type='ambient', color=Color.purple())

    w.add_material(m)
    w.add_light(l)
    w.add_light(l2)
    w.present()
