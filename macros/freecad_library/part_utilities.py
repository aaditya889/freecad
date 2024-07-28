import Part


def fuse_union_parts_object(current_document, name, part_objects):
  fused_part_object = current_document.addObject("Part::MultiFuse", name)
  fused_part_object.Shapes = part_objects
  fused_part_object.Refine = True
  current_document.recompute() 
  
  return fused_part_object
