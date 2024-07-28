import FreeCAD
# # import FreeCAD as App
# import FreeCADGui
import FreeCADGui as Gui
import Start as StartPage
# from Sketcher import *
# import Part
# from FreeCAD import Vector
# import Start
# from StartPage import StartPage

# if(App.activeDocument() == None):App.newDocument('yoyo')
#
# f = App.activeDocument().addObject("Sketcher::SketchObject","Sketch")
# f.addGeometry(Part.LineSegment(Vector(0,0,0),Vector(2,20,0)))
# f.addGeometry(Part.LineSegment(Vector(0,0,0),Vector(20,2,0)))
# f.Constraints = [Constraint('Vertical',0),Constraint('Horizontal',1)]
# print(App.activeDocument().recompute())
Gui.showMainWindow()
# Gui.getMainWindow()

Gui.runCommand('Std_Workbench',18)
Gui.runCommand('Std_ViewStatusBar',1)
# Gui.activateWorkbench("NoneWorkbench")
# print(FreeCADGui.listWorkbenches())

MRU="0"
with open('/usr/share/freecad/Mod/Start/StartPage/LoadMRU.py') as file:
	exec(file.read())
FreeCAD.openDocument('/home/aaditya/atelier/synchronous/aaditya/freecad/final_quadcopter.FCStd')
# App.setActiveDocument("final_quadcopter")
# App.ActiveDocument=App.getDocument("final_quadcopter")
# Gui.ActiveDocument=Gui.getDocument("final_quadcopter")