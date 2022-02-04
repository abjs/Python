from asyncore import poll3
from os.path import exists,join,isdir,isfile
from os import makedirs,listdir,system
from sys import modules
input_file_path = "/home/abjs/Music/Audio nots/3"
out_file_path = "/home/abjs/Music/Audio nots/audio_nots"
subjects = listdir(input_file_path)
for subject in subjects:
    subject_input_path = join(input_file_path,subject)
    subject_output_path = join(out_file_path,subject)
    if not isfile(subject_input_path):
        # print(subject_input_path)
        if not exists(subject_output_path):
            print(f"{subject} does not exist")
            makedirs(subject_output_path)

        modules_or_file = listdir(subject_input_path)
        for mf in modules_or_file:
            mf_path = join(subject_input_path,mf)
            if isfile(mf_path):
                out_path = join(subject_output_path,mf.replace(".m4a",".wav"))
                print(out_path)
                command = 'ffmpeg -i "%s" "%s" -y' % (mf_path, out_path)
                system(command)
            elif isdir(mf_path):
                # print(mf_path)
                modules_path = join(subject_output_path,mf)
                if not exists(modules_path):
                    makedirs(modules_path)
                module_files = listdir(mf_path)
                print(module_files)
                for f in module_files:
                    input_f = join(mf_path,f)
                    out_f =join(modules_path,f.replace(".m4a",".wav"))
                    command = 'ffmpeg -i "%s" "%s" -y' % (input_f, out_f)
                    system(command)

                    # if not isfile(mf_path):
                    # print(input_file_path)
                    # print(out_file_path)

                    # print(f)
        #         # if not exists(subject_output_path):
        #         #     print(f"{subject} does not exist")
        #         #     makedirs(subject_output_path)
        #         # print(f"{subject} dir {mf}")



# out_file_path = join(input_file_path , "output")
# if not exists(out_file_path):
#     print(out_file_path)
#     makedirs(out_file_path)

# if not exists(input_file_path):
#     print(f"{input_file_path} does not exist")
# files_in_dir = listdir(input_file_path)
# if not files_in_dir:
#     print("Input folder is empty add files to input folder")
# for i in files_in_dir:
#     input_file =join(input_file_path,i)
#     name_and_format = i.split(".")
#     if(len(name_and_format) == 2):
#         file_name =  name_and_format[0]
#         file_fromat =  name_and_format[1]
#         if(file_fromat == "webm"):
#             out_file_name = f"{file_name}.wav"
#             out_file = (out_file_path + "/" + out_file_name)
#             command = 'ffmpeg -i "%s" "%s" ' % (input_file, out_file)
#             command = 'ffmpeg -i "%s" -ac 1 -ab 64000 -ar 22050  "%s"' % (input_file, out_file) 
#             print(command)
#             system(command 