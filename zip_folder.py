import shutil
folder_path = "ABC" #here you will provide the file path for the folder which you want to zip
zipped_filename = "result_file" #here you will provide the name for the zip file
shutil.make_archive(zipped_filename,'zip',folder_path)
