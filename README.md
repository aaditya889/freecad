To install freeCAD on windows or Linux:
  -
-  Install FreeCAD software normally.
- `pip3 install freecad-stubs`: to find `import FreeCAD` module in Python (but not use it)
- To run a FreeCAD code in python (like a macro), run `freecadcmd filename.py` instead of `python3 filename.py`

Example Macro/Code:
  -

```
import FreeCAD as App
import os
import sys

model_name = "final_quadcopter_2.FCStd"
current_path = os.path.join(os.path.abspath((os.path.dirname(__file__))), "models")
model_path = os.path.join(current_path, model_name)

App.ActiveDocument = App.openDocument(model_path)
doc = App.ActiveDocument
```

> Run this code: `freecadcmd filename.py`

Problems
  -
- freecadcmd is not available
  - find freecadcmd (lol)  
