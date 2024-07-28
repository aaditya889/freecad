import Part


def initialise_part_object(current_body, part_name):
  
  part_object = current_body.addObject("Part::Feature", part_name)
  return part_object 
