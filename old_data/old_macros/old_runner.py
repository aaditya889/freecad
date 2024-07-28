import PartDesign 
from FreeCAD import Placement, Rotation, Vector
from freecad_library.configuration import *
from freecad_library.utilities import *
from freecad_library.curved_parts import *
from freecad_library.part_utilities import *
from freecad_library.plane_parts import *

freecad_file_format = "FCStd"
model_name = "pp"
current_document = initialise_document_object(model_name = f"{model_name}.{freecad_file_format}", is_exists=False)
# current_body = initialise_body_object(current_document)

pp_len = 10.0
pp_diameter = 3.0
b_diameter = 5.0
glan_diameter = 3.0

s = create_cylinder_object(pp_diameter/2, 360, pp_len)
b1 = create_sphere_object(b_diameter/2, (0, (pp_diameter*(-1)), 0))
b2 = create_sphere_object(b_diameter/2, (0, (pp_diameter), 0))
g = create_sphere_object(glan_diameter/2, (0, 0, pp_len))


current_document.recompute()

bt = b2.fuse([s, b1, g])
Part.show(bt, 'fused')
# f1 = fuse_union_parts_object(current_document, 'f1', [b2, s])
# f2 = fuse_union_parts_object(current_document, 'f2', [b1, s])
# f3 = fuse_union_parts_object(current_document, 'f3', [f1, f2])
# f4 = fuse_union_parts_object(current_document, 'f4', [g, f3])
# fused_t = s.fuse(b1) 
# fused = fuse_union_parts_object(current_document, 'fused_pp', [b1, s])
current_document.recompute()

current_document.save()
