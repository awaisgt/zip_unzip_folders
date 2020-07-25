import shutil
folder_path = "ABC" # here you will provide the folder path in which you want to unzip the file.
zipped_filename = "result_file" # here you will provide the path for the zip file which you want to unzip
shutil.unpack_archive(zipped_filename,folder_path,zip)
