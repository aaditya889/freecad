from freecad_library.configuration import *
from freecad_library.utilities import *
from freecad_library.curved_parts import *
from freecad_library.part_utilities import *
from freecad_library.plane_parts import *
import PartDesign 
from FreeCAD import Placement, Rotation, Vector
import math

def get_sink_wedge(length, width, back_height, front_height, num_wedges=1, dist_between_wedges=0, is_ridged=False, 
                   ridge_radius=2, ridge_distance=1, is_hollow=True):

  wedge_angle = (math.atan((back_height-front_height)/width)*180/math.pi)
  wedge_slant_length = math.sqrt((back_height-front_height)**2 + width**2)

  wedge = create_wedge_object(length, width, back_height, wedge_angle)

  if is_ridged:
    ridge_direction = (0, 1, -math.tan(wedge_angle*math.pi/180))
    ridge_position = (0, 0, back_height)
    for i in range(1, int(length/(ridge_radius + ridge_distance))):
      ridge = create_cylinder_object(ridge_radius, wedge_slant_length, ridge_position, ridge_direction)
      ridge_position = (i*((ridge_radius + ridge_distance)), 0, back_height)
      ridge = create_cylinder_object(ridge_radius, wedge_slant_length, ridge_position, ridge_direction)
      wedge = wedge.cut([ridge])

  cut_box = create_box_object(length, 10, front_height)
  cut_box.applyTranslation(Vector(0, width-10, 0))
  wedge = wedge.cut(cut_box)
  
  if is_hollow:
    hollow_box = create_box_object(length-3, width-13, front_height-3)
    hollow_box.applyTranslation(Vector(1, 1, 1))
    wedge = wedge.cut(hollow_box)
    
    
  drainer2 = wedge.copy()
  for i in range(1, num_wedges):
    drainer2.applyTranslation(Vector(length + dist_between_wedges, 0, 0))
    wedge = wedge.fuse(drainer2)
  
  # Part.show(hollow_box, 'hollow_box')

  return wedge

