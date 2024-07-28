import Part
from FreeCAD import Placement, Rotation, Vector


def create_sphere_object(radius, center_position=None):
  if center_position:
    position_vector = Vector(center_position)
  else:
    position_vector = Vector(0, 0, 0)

  sphere_part_object = Part.makeSphere(radius, position_vector)
  # sphere_part_object = current_document.addObject("Part::Sphere", name)
  # sphere_part_object.Radius = radius
  # sphere_part_object.Placement = Placement(position_vector, Rotation(0, 0, 0), Vector(0, 0, 0))
  # current_document.recompute()

  return sphere_part_object
  

def create_cylinder_object(radius, height, is_hollow=False, shell_thickness=0.0, base_center_position=(0,0,0), zdirection=(0,0,1)):
  # if base_center_position:
  #   position_vector = Vector(base_center_position)
  # else:
  #   position_vector = Vector(0, 0, 0)
  # if euler_angles:
  #   rotation_vector = Rotation(euler_angles)
  # else:
  #   rotation_vector = Rotation(0, 0, 0)
  # cylinder_part_object = current_document.addObject("Part::Cylinder", name)
  cylinder_part_object = Part.makeCylinder(radius, height, Vector(base_center_position), Vector(zdirection))
  # cylinder_part_object.Radius = radius
  # cylinder_part_object.Height = height
  # cylinder_part_object.Angle = angle
  # cylinder_part_object.Placement = Placement(position_vector, Rotation(rotation_vector), Vector(0, 0, 0))
  # current_document.recompute()
  if is_hollow:
    # cylinder_part_object = cylinder_part_object.makeThickness(cylinder_part_object, shell_thickness, 0.1)
    hollow_cylinder_part_object = Part.makeCylinder(radius - shell_thickness, height, Vector(base_center_position), Vector(zdirection))
    cylinder_part_object = cylinder_part_object.cut(hollow_cylinder_part_object)

  return cylinder_part_object
  
