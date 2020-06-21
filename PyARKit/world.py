import ui
from .material import Material
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


class World:
    def __init__(self, frame=None,):
        self.frame = frame or (0, 0, 100, 100)
        self.width = self.frame[2]
        self.height = self.frame[3]
        self.ui_view = ui.View()
        flex_width, flex_height = (1 << 1), (1 << 4)
        self.instance = ObjCInstance(self.ui_view)
        self.rect = CGRect(CGPoint(0, 0), CGSize(self.width, self.height))
        self.scn_view = ARSCNView.alloc().initWithFrame_options_(self.rect, None).autorelease()
        self.scn_view.setAutoresizingMask_(flex_width|flex_height)

        self.scene = SCNScene.scene()
        self.ui_view.scene = self.scene
        self.ui_view.showsStatistics = 1

        self.ar_configuration = ARWorldTrackingConfiguration.new()
        self.ar_session = ARSession.new()
        self.ar_session.delegate = self.ui_view
        self.ar_session.runWithConfiguration_(self.ar_configuration)
        self.scn_view.setSession_(self.ar_session)
        
        self.instance.addSubview_(self.scn_view)

    def add_childmaterial(self, material):
        if not isinstance(material, Material):
            raise ValueError('It is not material instance')
        self.scene.rootNode().addChildNode_(material.node)

    def present(self):
        self.ui_view.present()


if __name__ == '__main__':
    w = World()
    w.present()
