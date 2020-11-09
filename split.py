import glob
import os
import Tkinter
import Tkconstants
import tkFileDialog
while True:
    print("Please select your image directory.")
    current_dir = tkFileDialog.askdirectory()
    if current_dir == None or current_dir == "":
        print("You must select a directory.")
        continue
    break
# Percentage of images to be used for the test set
percentage_test = 10
# Create and/or truncate train.txt and test.txt
file_train = open('train7.txt', 'w')
file_test = open('test7.txt', 'w')
image_list = open('image7.list','w')
label_list = open('label7.list','w')
# Populate train.txt and test.txt
counter = 1
index_test = round(100 / percentage_test)
print(current_dir)
for pathAndFilename in glob.iglob(os.path.join(current_dir, "*.jpg")):
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))
    if counter == index_test:
        counter = 1
        file_test.write(current_dir + "/" + title + '.jpg' + "\n")
        image_list.write(title + '.jpg' + "\n")
        label_list.write(title + '.txt' + "\n") 
    else:
        file_train.write(current_dir + "/" + title + '.jpg' + "\n")
        image_list.write(title + '.jpg' + "\n")
        label_list.write(title + '.txt' + "\n")
        counter = counter + 1
