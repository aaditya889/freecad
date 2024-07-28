import Part
from FreeCAD import Placement, Rotation, Vector


def create_sphere_object(radius, center_position=None):
  if center_position:
    position_vector = Vector(center_position)
  else:
    position_vector = Vector(0, 0, 0)

  sphere_part_object = Part.makeSphere(radius, position_vector)
  return sphere_part_object
  

def create_cylinder_object(radius, height, is_hollow=False, shell_thickness=0.0, base_center_position=(0,0,0), zdirection=(0,0,1)):
  cylinder_part_object = Part.makeCylinder(radius, height, Vector(base_center_position), Vector(zdirection))
  if is_hollow:
    hollow_cylinder_part_object = Part.makeCylinder(radius - shell_thickness, height, Vector(base_center_position), Vector(zdirection))
    cylinder_part_object = cylinder_part_object.cut(hollow_cylinder_part_object)

  return cylinder_part_object
  
