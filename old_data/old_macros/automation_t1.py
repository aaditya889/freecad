
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
