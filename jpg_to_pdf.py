from PIL import Image
from fpdf import FPDF
import sys
from helper_functions import find_file_in_downloads
from helper_functions import scale_down


def jpg_to_pdf(images, pdf_path):
    # Create a PDF object
    pdf = FPDF(unit="pt")

    for image_name in images:
        image_path = find_file_in_downloads(image_name)
        if image_path:
            print(f'File found: {image_path}\n')
        else:
            print(f'File not found in Downloads folder.\n')
        # Open the image file
        open_image = Image.open(image_path)

        # Convert the image to RGB mode if it's not already
        if open_image.mode != 'RGB':
            open_image = open_image.convert('RGB')

        # Get the dimensions of the image
        width, height = open_image.size

        # scale image down to max size of A4 if its too big
        width, height = scale_down(width, height, 595, 842)
        
        # Add a page with the custom width and height
        pdf.add_page(orientation="P")

        # Insert the image into the PDF
        pdf.image(image_path, 0, 0, width, height)
        
    # Save the PDF to the specified path
    pdf.output(pdf_path)







def main():
    command_line_args = sys.argv[1:]
    print(command_line_args)
    images = []
    pdf_path = ''
    for string in command_line_args:
        if string.endswith('pdf') and pdf_path != '':
            raise Exception('only can have 1 pdf path')
        
        if string.endswith('jpg'):
            images.append(string)
        elif string.endswith('pdf'):
            pdf_path = string
        else:
            raise Exception('only accept files that end with jpg or pdf')
        
    jpg_to_pdf(images, '../../../Downloads/' + pdf_path)

if __name__=="__main__": 
    main() 
