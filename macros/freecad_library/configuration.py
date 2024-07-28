import FreeCAD as App
import os
import PartDesign 
import Sketcher



def __fetch_model_directory_path():
  freecad_directory = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
  model_directory = os.path.join(freecad_directory, "models")
  print(f"Model directory path:: {model_directory}")
  return model_directory
  

def initialise_document_object(model_name, is_exists=True):
  model_path = os.path.join(os.path.abspath(__fetch_model_directory_path()), model_name)
  print(f"Model Path:: {model_path}")
  if not is_exists:
    App.ActiveDocument = App.newDocument()
  else:
    App.ActiveDocument = App.openDocument(model_path)
  doc = App.ActiveDocument
  doc.FileName = model_path
  doc.recompute()
  doc.save()
  
  return doc


def initialise_body_object(current_document, body_name="Body", body_label="Body", is_exists=False):
  assert body_label == body_name
  
  if not is_exists:
    current_document.addObject("PartDesign::Body", body_name)
    
  body_object = current_document.getObject(body_name)
  body_object.Label = body_label
  current_document.recompute()
  
  return current_document.getObject(body_name)
