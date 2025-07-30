# 28/07/2025

import os
from config import CHARACTER_LIMIT

def get_file_content(working_directory, file_path):
    
    abs_target_path = os.path.abspath(os.path.join(working_directory, file_path))
    abs_work_dpath = os.path.abspath(working_directory)

    # is inside working dir?
    if not os.path.commonpath([abs_target_path, abs_work_dpath]) == abs_work_dpath:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    # is file?
    if not os.path.isfile(abs_target_path) :
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    try :
        # read file
        file_text = ''
        with open (abs_target_path) as f:
            file_text = f.read(CHARACTER_LIMIT)
            # file > CHARACTER_LIMIT
            if os.path.getsize(abs_target_path) > CHARACTER_LIMIT :
                file_text += f'...File "{file_path}" truncated at {CHARACTER_LIMIT} characters'
        return file_text
        
    except Exception as e:
        return f'Error reading file "{file_path}": {e}'



