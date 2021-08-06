import os
path_now  =   os.getcwd()
if not os.path.exists('input'):
    print("Add files to input folder for converting to mp3")
    os.makedirs('input')
input_file_path = os.path.join(path_now,"input")
if not os.path.exists('out'):
    os.makedirs('out')
out_file_path = os.path.join(path_now,"out")
files_in_dir = os.listdir(input_file_path)
if not files_in_dir:
    print("Input folder is empty add files to input folder")
for i in files_in_dir:
    input_file = os.path.join(input_file_path,i)
    out_file = os.path.join(out_file_path,i)
    out_file = out_file.split(".")[0]+".mp3"
    command = 'ffmpeg -i "%s" "%s" ' % (input_file, out_file)
    print(command)
    os.system(command)
