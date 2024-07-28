import FreeCAD as App
import os
import PartDesign
import Sketcher
import Part


# def create_constrained_straight_line(current_document, current_body, start_point, end_point, line_name="Line"):
#   line_object = Part.LineSegment()
#   line_object.StartPoint = start_point
#   line_object.EndPoint = end_point
#   line_document_object = current_body.addObject(line_object)

#   # line_document_object.Shape = line_object.toShape()
#   # current_body.addObject(line_name)




def create_constrained_straight_line(current_document, part_object, start_point, end_point):
  line_object = Part.LineSegment()
  line_object.StartPoint = start_point
  line_object.EndPoint = end_point
  part_object.Shape = line_object.toShape()
  current_document.recompute()
  return line_object
  
