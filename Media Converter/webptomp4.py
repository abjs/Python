from os.path import exists,join
from os import makedirs,listdir,system
input_file_path = "/home/abjs/Videos/s7/csa"
out_file_path = join(input_file_path , "csa")
if not exists(out_file_path):
    print(out_file_path)
    makedirs(out_file_path)

if not exists(input_file_path):
    print(f"{input_file_path} does not exist")
files_in_dir = listdir(input_file_path)
if not files_in_dir:
    print("Input folder is empty add files to input folder")
for i in files_in_dir:
    input_file =join(input_file_path,i)
    name_and_format = i.split(".")
    if(len(name_and_format) == 2):
        file_name =  name_and_format[0]
        file_fromat =  name_and_format[1]
        if(file_fromat == "webm"):
            out_file_name = f"{file_name}.wav"
            out_file = (out_file_path + "/" + out_file_name)
            # command = 'ffmpeg -i "%s" "%s" -f wav -bitexact -acodec pcm_s16le -ar 22050 -ac 1 -y' % (input_file, out_file) 
            command = 'ffmpeg -i "%s" "%s" -ar 8000 -acodec pcm_s16le  -y' % (input_file, out_file) 
            print(command)
            system(command) 

            # print(file_name , file_fromat)
            # thumbnail_file = f"{file_name}.webp"
            # thumbnail_path = join(input_file_path,thumbnail_file)
            # if exists(thumbnail_path):
            #     print(input_file)
            #     out_file_name = f"{file_name}.mp3"
            #     out_file = (out_file_path + "/" + out_file_name)
            #     command = 'ffmpeg -i "%s" "%s"' % (input_file, out_file) 
            #     system(command)      
         
