import Part
from FreeCAD import Placement, Rotation, Vector

class BoxFaces:
  top_face = None
  bottom_face = None
  front_face = None
  back_face = None
  left_face = None
  right_face = None
  
  def __init__(self, part_object):
    self.part_object = part_object
    self.faces = part_object.Faces
    self.top_face = self.faces[0]
    self.bottom_face = self.faces[1]
    self.front_face = self.faces[2]
    self.back_face = self.faces[3]
    self.left_face = self.faces[4]
    self.right_face = self.faces[5]

class CylinderFaces:
  top_face = None
  bottom_face = None
  curved_face = None
  
  def __init__(self, part_object):
    self.part_object = part_object
    self.faces = part_object.Faces
    self.top_face = self.faces[0]
    self.bottom_face = self.faces[1]
    self.curved_face = self.faces[2]


class CreateNewPart:
  name = None
  part_object = None
  faces = None
  protruded_objects = []
  
  def __init__(self, name):
    self.name = name
    
  def assign_box_part(self, length, width, height, base_center=(0,0,0)):
    self.part_object = Part.makeBox(length, width, height, Vector(base_center))
    self.faces = BoxFaces(self.part_object)
  
  def assign_cylinder_part(self, radius, height, base_center=(0,0,0), zdirection=(0,0,1)):
    self.part_object = Part.makeCylinder(radius, height, Vector(base_center), Vector(zdirection))
    self.faces = CylinderFaces(self.part_object)
    
  def assign_sphere_part(self, radius, center_position=(0,0,0)):
    self.part_object = Part.makeSphere(radius, Vector(center_position))
    # self.part_object.Faces[0].
    
  def assign_torus_part(self, radius1, radius2, center_position=(0,0,0), axis=(0,0,1)):
    self.part_object = Part.makeTorus(radius1, radius2, Vector(center_position), Vector(axis))
    
  def assign_cone_part(self, radius1, radius2, height, base_center=(0,0,0), zdirection=(0,0,1)):
    self.part_object = Part.makeCone(radius1, radius2, height, Vector(base_center), Vector(zdirection))
    
  def assign_wedge_part(self, length, width, height, center_position=(0,0,0), zdirection=(0,0,1)):
    self.part_object = Part.makeWedge(length, width, height, Vector(center_position), Vector(zdirection))
    
  def assign_tube_part(self, radius1, radius2, height, base_center=(0,0,0), zdirection=(0,0,1)):
    self.part_object = Part.makeTube(radius1, radius2, height, Vector(base_center), Vector(zdirection))
    
  def assign_cone_frustum_part(self, radius1, radius2, height, base_center=(0,0,0), zdirection=(0,0,1)):
    self.part_object = Part.makeCone(radius1, radius2, height, Vector(base_center), Vector(zdirection))
  
  def fetch_part_faces(self):
    return self.part_object.Faces
  
  def protrude_out_box(self, name, length, width, height, face, relative_location):
    new_box = CreateNewPart(name)
    new_box.assign_box_part(length, width, height, relative_location)
  
  # def protrude_part(self, length, direction=(0,0,1)):
  #   self.part_object = self.part_object.extrude(Vector(direction), length)