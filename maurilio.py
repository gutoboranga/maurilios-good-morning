
def calculate_maurilio_size((background_w, background_h), (maurilio_w, maurilio_h)):
    if maurilio_w > maurilio_h:
        ratio = float(maurilio_h) / float(maurilio_w)
        new_width = background_w / 2
        
        size = (new_width, int(new_width * ratio))
    else:
        ratio = float(maurilio_w) / float(maurilio_h)
        new_height = (background_h / 4) * 3
        
        size = (int(new_height * ratio), new_height)
        
    return size

def calculate_maurilio_position((background_w, background_h), (maurilio_w, maurilio_h)):
    x = background_w - maurilio_w
    y = background_h - maurilio_h
    
    return (x,y)
