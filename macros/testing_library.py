from freecad_library.configuration import *
from freecad_library.part_utilities import *


freecad_file_format = "FCStd"
model_name = "testing_library"
current_document = initialise_document_object(model_name = f"{model_name}.{freecad_file_format}", is_exists=False)

part_object = CreateNewPart("box")
part_object.assign_sphere_part(10)
faces = part_object.fetch_part_faces()

for face in faces:
  vertices = face.Vertexes
  for vertex in vertices:
    print(vertex.Point)