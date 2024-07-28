from freecad_library.configuration import *
from freecad_library.curved_parts import *
from freecad_library.plane_parts import *


freecad_file_format = "FCStd"
model_name = "hcsr04_ultrasonic_case"
current_document = initialise_document_object(model_name = f"{model_name}.{freecad_file_format}", is_exists=False)

mic_diameter_mm = 15.9
mic_inner_shell_separation_mm = 1.6
mic_height_mm = 12
mic_separation_mm = 10
body_length_mm = 45
body_width_mm = 20.5
body_height_mm = 2.5
pin_start_mm = 17.5
pin_header_width_mm = 10.2
pin_height_mm = 4.5
overall_case_thickness_mm = 0.5

# Fill these values!
crystal_length_mm = 10.6
crystal_width_mm = 4.3
crystal_height_mm = 3.5
pin_header_thickness_mm = 1.5
crystal_placement_vector_mm = ((mic_separation_mm + mic_diameter_mm)/2, 15.6 - body_width_mm/2 + crystal_width_mm/2, 0)


mic_case_object_1 = create_cylinder_object((mic_diameter_mm/2) + overall_case_thickness_mm, mic_height_mm + overall_case_thickness_mm, is_hollow=True, shell_thickness=mic_inner_shell_separation_mm)
mic_case_object_2 = create_cylinder_object((mic_diameter_mm/2) + overall_case_thickness_mm, mic_height_mm + overall_case_thickness_mm, is_hollow=True, shell_thickness=mic_inner_shell_separation_mm, base_center_position=(mic_separation_mm + mic_diameter_mm, 0, 0))
mic_object_1 = create_cylinder_object(mic_diameter_mm/2, mic_height_mm - overall_case_thickness_mm, is_hollow=True, shell_thickness=mic_inner_shell_separation_mm)
mic_object_2 = create_cylinder_object(mic_diameter_mm/2, mic_height_mm - overall_case_thickness_mm, is_hollow=True, shell_thickness=mic_inner_shell_separation_mm, base_center_position=(mic_separation_mm + mic_diameter_mm, 0, 0))
# Part.show(mic_case_object_1, 'mic_case_object_1')
# Part.show(mic_case_object_2, 'mic_case_object_2')
# Part.show(mic_object_1, 'mic_object_1')
# Part.show(mic_object_2, 'mic_object_2')
mic_case_object_1 = mic_case_object_1.cut(mic_object_1)
mic_case_object_2 = mic_case_object_2.cut(mic_object_2)
mic_hole_1 = create_cylinder_object(mic_diameter_mm/2, body_height_mm, base_center_position=(0, 0, -body_height_mm))
mic_hole_2 = create_cylinder_object(mic_diameter_mm/2, body_height_mm, base_center_position=(mic_separation_mm + mic_diameter_mm, 0, -body_height_mm))

# Part.show(mic_hole_1, 'mic_hole_1')
# Part.show(mic_hole_2, 'mic_hole_2')
chip_case_object = create_box_object(body_length_mm, body_width_mm, body_height_mm, is_hollow=True, shell_thickness=overall_case_thickness_mm, base_center=((mic_separation_mm + mic_diameter_mm)/2, 0, -body_height_mm))
# Part.show(chip_case_object, 'chip_case_object')
crystal_case_object = create_box_object(crystal_length_mm + overall_case_thickness_mm, crystal_width_mm + overall_case_thickness_mm, 
                                        crystal_height_mm + overall_case_thickness_mm,
                                        is_hollow=True, shell_thickness=overall_case_thickness_mm,
                                        base_center=crystal_placement_vector_mm)
crystal_hole_object = create_box_object(crystal_length_mm - overall_case_thickness_mm, crystal_width_mm - overall_case_thickness_mm, body_height_mm, base_center=(crystal_placement_vector_mm[0], crystal_placement_vector_mm[1], -body_height_mm))
# pin_header_object = create_box_object(pin_header_width_mm, overall_case_thickness_mm, pin_header_thickness_mm, base_center=(pin_start_mm - pin_header_width_mm/2 + overall_case_thickness_mm, -body_width_mm/2 + overall_case_thickness_mm/2, -body_height_mm))

# Part.show(pin_header_object, 'pin_header_object')

mics = mic_case_object_1.fuse(mic_case_object_2)
case = chip_case_object.fuse([mics, crystal_case_object])
case = case.cut([mic_hole_1, 
                 mic_hole_2, 
                 crystal_hole_object, 
                #  pin_header_object
                 ])
Part.show(case, 'case')
# Part.show(mics, 'mics')
# Part.show(mic_hole_1, 'mics_hole1')
# Part.show(mic_hole_2, 'mics_hole2')
current_document.save()
