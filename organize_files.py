import os
import shutil
source_directory = r'C:\djangostock\stocks\stocks'
file_type_folders={
    'Images':['.jpg','.jpeg','.png','.gif','.bmp'],
    'Documents':['.pdf','.docx','.txt','.xls','.xlsx','.pptx'],
    'Videos':['.mp4','.avi','.mov','.mkv'],
    'Music':['.mp3','.wav','.flac'],
    'Archives':['.zip','.rar','.tar','.gz'],
    'Scripts':['.py','.js','.htmml','.css']
}
for folder in file_type_folders.keys():
    folder_path=os.path.join(source_directory,folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

for filename in os.listdir(source_directory):
    file_path=os.path.join(source_directory,filename)
    if os.path.isfile(file_path):
        file_extension=os.path.splitext(filename)[1].lower()
        for folder,extensions in file_type_folders.items():
            if file_extension in extensions:
                destination_path = os.path.join(source_directory,folder,filename)
                shutil.move(file_path, destination_path)
                print("Moved file: {filename} to folder : {folder}")
                break


print("Files have been organized successfully.")