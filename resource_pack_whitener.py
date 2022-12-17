from PIL import Image
import os
  
def main():
    path = input("\nEnter the absolute path to the resource pack directory (the pack must be in extracted form, not in ZIP form): ") # Input the path to the resource pack directory.
    response = "" # Set a blank response.
    while response != "y" and response != "Y" and response != "n" and response != "N": # Repeat the prompt after an invalid response.
        response = input("\nWarning: This script will attempt to modify every image file with the file extension \".png\" in the target directory and all of its subdirectories. The target directory which you have identified is:\n\n" + path + "\n\nDo you wish to continue? Y/N: ") # Prompt the user for a yes/no response.
    if response == "n" or response == "N": # Exit if the user responds in the negative.
        print("\nNo files have been modified. The program will exit.")
        exit()
    elif response == "y" or response == "Y": # Continue if the user responds in the positive.
        global fileCount 
        fileCount = 0 # Create a counter for modified files.
        scan(os.scandir(path))
        print("\nSuccessfully modified " + str(fileCount) + " files.") # Print the number of files modified.

def scan(directory): # Scan the target directory and its subdirectories for PNG files.
    for entry in directory: 
        if entry.is_dir():
            scan(os.scandir(entry.path)) # Scan through subdirectories for files.
        elif entry.is_file():
            if entry.name.endswith(".png"): # Modify a file if its file extension is ".png".
                modify(entry)

def modify(file): # Modify the image to be white.
    print("Modifying " + file.name)
    image = Image.open(file.path).convert("RGBA")
    modified = Image.new("LA", size = image.size, color= (255,0))
    modified.paste((255,255), mask = image)
    modified.save(file.path)
    global fileCount
    fileCount += 1 # Increment the file counter.

main()
