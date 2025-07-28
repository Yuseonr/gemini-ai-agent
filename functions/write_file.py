# 28 Jul 20025

import os

def write_file(working_directory, file_path, content):

    abs_target_path = os.path.abspath(os.path.join(working_directory, file_path))
    abs_work_dpath = os.path.abspath(working_directory)

    # is inside working dir?
    if not os.path.commonpath([abs_target_path, abs_work_dpath]) == abs_work_dpath:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    try :
        # file doesnt exist
        parent_dir = os.path.dirname(abs_target_path)
        if not os.path.exists(parent_dir):
            os.makedirs(parent_dir)
        
        with open(abs_target_path, "w") as f:
            f.write(content)
        
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e :
        return f'Error writing file "{file_path}": {e}'