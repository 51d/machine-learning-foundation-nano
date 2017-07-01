#In this program we have renamed all files in a directory
#by removing the nos.  in there namee and the order of pictures in
#the directory now shows message
import os
def rename_files():
    #getting file name from a drectory
    file_list = os.listdir(r"C:\udacity\python my work\prank")
    print file_list
    cur_dir = os.getcwd()
    print cur_dir
    os.chdir(r"C:\udacity\python my work\prank")
    #renaming files
    for file_name in file_list:
        os.rename(file_name,file_name.translate(None, "0123456789"))
    os.chdir(cur_dir)
rename_files()    
