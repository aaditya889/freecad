from freecad_library.configuration import *
from freecad_library.utilities import *
from freecad_library.curved_parts import *
from freecad_library.part_utilities import *
from freecad_library.plane_parts import *
import math
from freecad_library.parts.wedge import get_sink_wedge


freecad_file_format = "FCStd"
model_name = "sink_drainer"
current_document = initialise_document_object(model_name = f"{model_name}.{freecad_file_format}", is_exists=False)
drainer_body_length = 230
drainer_body_width = 90
drainer_body_wall_height = 180
drainer_body_sink_height = 120
ridge_radius = 8
ridge_distance=8
null_width = 10

drainer_body_angle_degrees = (math.atan((drainer_body_wall_height-drainer_body_sink_height)/drainer_body_width)*180/math.pi)
drainer = get_sink_wedge(drainer_body_length, drainer_body_width, drainer_body_wall_height, drainer_body_sink_height, num_wedges=1, 
                          dist_between_wedges=null_width, is_ridged=True, ridge_radius=ridge_radius, ridge_distance=ridge_distance)

Part.show(drainer, 'drainer')
current_document.save()


