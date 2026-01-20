#TO MAKE A FUNCTION ABOUT THE VIRUS SCAN
#TO GET THE ALL THE STUFF FROM THE ROUTER INTO THE LIST
#THEN CHECK EVERY ITEM FROM THE ROUTER AND CHECK IF ITS A FILE OR A FOLDER
#AT THE END MAKE A DIFFRENT OUTCOMER FOR EACH ITEM
import os


def virus_scan(items):
    folder_file_list=os.listdir(items)
    for path in folder_file_list:
     if os.path.isdir(path):
      print(path+"its a folder")
      read_folder_func(path)
     elif os.path.isfile(path):
       print(path+"its a file")
def read_folder_func(path):
  folders=os.scandir(path)
  
  
  

  
  
  


    
