# -*- coding: utf-8 -*-

# Macro Begin: C:\Users\aadit\atelier_windows\freecad_models\macros\automation_t1.FCMacro +++++++++++++++++++++++++++++++++++++++++++++++++
import FreeCAD as App
import os
import PartDesign 

import Sketcher


model_name = "automation_t2.FCStd"
freecad_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(f"freecad dir: {freecad_directory}...")
# freecad_directory = os.path.dirname(current_directory)
model_directory = os.path.join(freecad_directory, "models")
model_path = os.path.abspath(os.path.join(model_directory, model_name))
print(f"Model path:: {model_path}")

# App.ActiveDocument = App.openDocument(model_path)
App.ActiveDocument = App.newDocument()

doc = App.ActiveDocument
doc.FileName = model_path

App.activeDocument().addObject('PartDesign::Body','Body')
App.ActiveDocument.getObject('Body').Label = 'Body'

App.ActiveDocument.recompute()

doc.getObject('Body').newObject('Sketcher::SketchObject','Sketch')
doc.getObject('Sketch').Support = (doc.getObject('XY_Plane'),[''])
doc.getObject('Sketch').MapMode = 'FlatFace'
App.ActiveDocument.recompute()
print(Part.LineSegment())
print(App.ActiveDocument)
geoList = []
geoList.append(Part.LineSegment(App.Vector(-34.213100,23.998047,0),App.Vector(33.822094,23.998047,0)))
geoList.append(Part.LineSegment(App.Vector(33.822094,23.998047,0),App.Vector(33.822094,-20.087975,0)))
geoList.append(Part.LineSegment(App.Vector(33.822094,-20.087975,0),App.Vector(-34.213100,-20.087975,0)))
geoList.append(Part.LineSegment(App.Vector(-34.213100,-20.087975,0),App.Vector(-34.213100,23.998047,0)))
doc.getObject('Sketch').addGeometry(geoList, False)
conList = []
conList.append(Sketcher.Constraint('Coincident',0,2,1,1))
conList.append(Sketcher.Constraint('Coincident',1,2,2,1))
conList.append(Sketcher.Constraint('Coincident',2,2,3,1))
conList.append(Sketcher.Constraint('Coincident',3,2,0,1))
conList.append(Sketcher.Constraint('Horizontal',0))
conList.append(Sketcher.Constraint('Horizontal',2))
conList.append(Sketcher.Constraint('Vertical',1))
conList.append(Sketcher.Constraint('Vertical',3))
doc.getObject('Sketch').addConstraint(conList)
del geoList, conList

doc.getObject('Sketch').addConstraint(Sketcher.Constraint('DistanceX',0,1,0,2,68.035194))
doc.getObject('Sketch').renameConstraint(8, u'lr1')

# doc.getObject('Sketch').addConstraint(Sketcher.Constraint('DistanceY',1,2,1,1,44.086022))
# doc.getObject('Sketch').setDatum(9,App.Units.Quantity('22.000000 mm'))
# doc.getObject('Sketch').renameConstraint(9, u'wr1')

# doc.getObject('Sketch').addConstraint(Sketcher.Constraint('DistanceY',1,2,1,1,44.086022))
# doc.getObject('Sketch').setDatum(8,App.Units.Quantity('21.000000 mm'))
# doc.getObject('Sketch').renameConstraint(8, u'lr1')

doc.getObject('Sketch').addConstraint(Sketcher.Constraint('DistanceY',1,2,1,1,44.086022))
doc.getObject('Sketch').setDatum(8,App.Units.Quantity('21.000000 mm'))
doc.getObject('Sketch').renameConstraint(8, u'wr1')

def DELETE():
  print(f"Deleting constraint!!")
  doc.getObject('Sketch').delConstraint(9)
  doc.getObject('Sketch').delConstraint(8)
  doc.getObject('Sketch').delConstraint(7)
  doc.recompute()
from PySide import QtCore

# DELETE()
# timer = QtCore.QTimer()
# timer.timeout.connect(DELETE)
# timer.start(10)

# doc.getObject('Sketch').addConstraint(Sketcher.Constraint('DistanceX',0,1,0,2,68.035194))
# doc.getObject('Sketch').setDatum(9,App.Units.Quantity('22.000000 mm'))
# doc.getObject('Sketch').renameConstraint(9, u'lr1')

# doc.getObject('Sketch').addConstraint(Sketcher.Constraint('Symmetric',1,1,1,2,-1,1))

# doc.getObject('Sketch').addConstraint(Sketcher.Constraint('Symmetric',3,1,3,2,-1,1))

# doc.getObject('Sketch').addConstraint(Sketcher.Constraint('Symmetric',0,1,0,2,-1,1))

# doc.getObject('Sketch').addConstraint(Sketcher.Constraint('Symmetric',-1,1,0,2,2))

# doc.getObject('Sketch').addConstraint(Sketcher.Constraint('Symmetric',1,1,1,2,0,1))

# doc.getObject('Sketch').addConstraint(Sketcher.Constraint('Symmetric',0,1,0,2,-1,1))

# doc.getObject('Sketch').addConstraint(Sketcher.Constraint('Symmetric',0,2,2,2,-1,1))

doc.getObject('Sketch').addConstraint(Sketcher.Constraint('Symmetric',0,2,2,2,-1,1))

doc.save()
