# import the necessary packages
import pytesseract
import argparse
import cv2
import numpy as np
import re
import pandas as pd
import os
import glob

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--folder", required=True,
                help="path to input folder with images to be OCR'd")
ap.add_argument("-w", "--whitelist", type=str, default="",
                help="list of characters to whitelist")
ap.add_argument("-b", "--blacklist", type=str, default="",
                help="list of characters to blacklist")
args = vars(ap.parse_args())

# getting all files inside of folder argument
folder_path = os.path.join(args["folder"], "*")
images = glob.glob(folder_path)
# construct the lists that contains the names and dni
name_list = []
dni_list = []

# loop over all images
for image_path in images:
    try:
        # load the input image, swap channel ordering, and initialize our
        # Tesseract OCR options as an empty string
        image = cv2.imread(image_path)
        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    except Exception as e:
        print(f"the image path {image_path} was not processed. Error: {e}")
        continue
    options = ""
    # check to see if a set of whitelist characters has been provided,
    # and if so, update our options string
    if len(args["whitelist"]) > 0:
        options += "-c tessedit_char_whitelist={} ".format(
            args["whitelist"])
    # check to see if a set of blacklist characters has been provided,
    # and if so, update our options string
    if len(args["blacklist"]) > 0:
        options += "-c tessedit_char_blacklist={}".format(
            args["blacklist"])

    # OCR the input image using Tesseract
    text = pytesseract.image_to_string(rgb, config=options)
    # Sanity the output text:

    # Split by \n character
    text_list = text.split("\n")
    # Convert to numpy array
    text_list_np = np.array(text_list)
    # delete "" value
    text_list_np = np.delete(text_list_np, np.where(text_list_np == ""))
    # delete " " value
    text_list_np = np.delete(text_list_np, np.where(text_list_np == " "))
    # create the output by image seeking words and numbers
    for text in text_list_np:
        name = re.findall(r'[a-zA-Z]+', text)
        if len(name) > 0:
            final_name = ' '.join(name)
        else:
            final_name = " "
        name_list.append(final_name)

        dni = re.findall(r'\d+', text)
        if len(dni) > 0:
            final_dni = dni[0]
        else:
            final_dni = " "
        dni_list.append(final_dni)
# load a dataframe from the lists
df = pd.DataFrame(list(zip(name_list, dni_list)), columns=["Name", "DNI"])
# export to csv file
df.to_csv("output.csv", index=False)
