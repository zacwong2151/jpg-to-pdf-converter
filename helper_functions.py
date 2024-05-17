import glob
import os

def find_file_in_downloads(filename):
    # Construct the path to the Downloads folder in WSL
    downloads_path = '/mnt/c/Users/zacwo/Downloads'
    
    # Use glob to search for the file
    search_pattern = os.path.join(downloads_path, '**', filename)
    found_files = glob.glob(search_pattern, recursive=True)
    
    if found_files:
        return found_files[0]  # Return the first match
    else:
        return None
    
def scale_down(width, height, max_width, max_height):
    width_ratio = width / max_width
    height_ratio = height / max_height
    if width_ratio <= 1 and height_ratio <= 1:
        return width, height
    elif width_ratio > height_ratio:
        return width / width_ratio, height / width_ratio
    elif height_ratio > width_ratio: 
        return width / height_ratio, height / height_ratio