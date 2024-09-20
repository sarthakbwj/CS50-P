import sys
from os.path import splitext
from PIL import Image, ImageOps


def main():
    check_command_line_arg()
    #open the image
    try:
        imagefile = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist.")
    #open the shirt
    shirtfile = Image.open("shirt.png")
    #get the size
    size = shirtfile.size
    #resize muppet image to fit shirt 
    muppet = ImageOps.fit(imagefile, size)
    #paste shirt on muppet
    muppet.paste(shirtfile, shirtfile)
    #create output image 
    muppet.save(sys.argv[2])
    
#check how many elements in command line. 
def check_command_line_arg():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments.")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments.")
    file1 = splitext(sys.argv[1])
    file2 = splitext(sys.argv[2])

    #check if image file
    if(check_extension(file1[1])) == False:
        sys.exit("Invalid input")
    if check_extension(file2[1]) == False:
        sys.exit("Invalid output")
    
    #check if extensions of both files is same
    if file1[1].lower() != file2[1].lower():
        sys.exit("Input and output have different extensions. ")

def check_extension(file):
    if file in [".jpg", ".png", ".jpeg"]:
        return True
    return False 
    

if __name__ == "__main__":
    main()
