from pdf2image import convert_from_path
from PIL import Image 
import PIL
import sys

def main():
    fname = "paper.pdf"
    if len(sys.argv) > 1:
        fname = sys.argv[1]
    pil_image_lst = convert_from_path(fname) # This returns a list even for a 1 page pdf
    first_page = pil_image_lst[0]
    num_pages = len(pil_image_lst)
    num_rows = (num_pages + 3) // 4
    canvas_width = first_page.width * 4
    canvas_height = first_page.height * num_rows
    canvas = Image.new('RGB', (canvas_width, canvas_height), (255, 255, 255))
    
    for i, page in enumerate(pil_image_lst):
        x = (i % 4) * first_page.width
        y = (i // 4) * first_page.height
        
        rectangle = Image.new('RGB', (first_page.width, first_page.height), (0, 0, 0))

        left = first_page.width * 0.3
        top = first_page.height * 0.25
        right = first_page.width * 0.7
        bottom = first_page.height * 0.75

        rectangle = rectangle.crop((left, top, right, bottom))

        page.paste(rectangle, (int(left), int(top)))
        canvas.paste(page, (x,y))

    # Jank way of removing file extension
    fname_no_ext = ('.').join(fname.split('.')[:-1])

    canvas = canvas.save("[PREVIEW] " + fname_no_ext + ".jpg")

if __name__ == "__main__":
    main()
