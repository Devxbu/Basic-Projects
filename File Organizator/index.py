import os

path = 'C:\\Users\\Bahri\\Desktop\\Alet Edevat'

files = os.listdir(path)

file_types = {
    'Images': ['.png', '.jpg', '.jpeg', '.gif', '.svg'],
    'Videos': ['.mp4', '.mkv', '.avi', '.flv', '.wmv'],
    'Documents': ['.doc', '.docx', '.pdf', '.txt', '.xlsx', '.xls', '.ppt', '.pptx'],
    'Compressed': ['.zip', '.rar', '.tar', '.gz', '.7z'],
    'Programs': ['.exe', '.msi'],
    'Music': ['.mp3', '.wav', '.ogg', '.flac', '.wma'],
    'Others': []
}

for file in files:
    file_name, file_ext = os.path.splitext(file)

    for key, value in file_types.items():
        if file_ext in value:
            dir_path = os.path.join(path, key)
            if not os.path.exists(dir_path):
                os.mkdir(dir_path)
            os.rename(os.path.join(path, file), os.path.join(dir_path, file))
            break
    else:
        dir_path = os.path.join(path, 'Others')
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
        os.rename(os.path.join(path, file), os.path.join(dir_path, file))