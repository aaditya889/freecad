import Part
from FreeCAD import Placement, Rotation, Vector
import math


def create_box_object(length, width, height, is_hollow=False, shell_thickness=0.0, base_center=None, figure_center=None, euler_angles=None):
  assert not (base_center and figure_center)
  if base_center:
    position_vector = Vector(length*(-0.5), width*(-0.5), 0)
    position_vector = position_vector.add(Vector(base_center))
  elif figure_center:
    position_vector = Vector(length*(-0.5), width*(-0.5), height*(-0.5))
    position_vector = position_vector.add(Vector(figure_center))
  else:
    position_vector = Vector(0, 0, 0)
  if euler_angles:
    rotation_vector = Rotation(euler_angles)
  else:
    rotation_vector = Rotation(0, 0, 0)
    
  box_part_object = Part.makeBox(length, width, height, position_vector)
  if is_hollow:
    hollow_box_part_object = Part.makeBox(length - (shell_thickness*2), width - (shell_thickness*2), height - shell_thickness, position_vector.add(Vector(shell_thickness, shell_thickness, 0)))
    box_part_object = box_part_object.cut(hollow_box_part_object)
    
  return box_part_object


def create_wedge_object(length, width, height, wedge_angle_degrees):
  ymin = 0
  ymax = width
  xmin = zmin = 0
  xmax = length
  zmax = height
  x2min = 0
  z2min = 0
  x2max = length
  z2max = height - (width*math.tan(wedge_angle_degrees*math.pi/180))
  wedge_part_object = Part.makeWedge(xmin, ymin, zmin, z2min, x2min, xmax, ymax, zmax, z2max, x2max)
  return wedge_part_object
