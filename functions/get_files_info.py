# 28/Jul/2025

import os
from google.genai import types

def get_files_info(working_directory, directory="."):
    try : 
        # constructing abs path
        dir_path = os.path.join(working_directory, directory)
        abs_target_path = os.path.abspath(dir_path)
        abs_work_dpath = os.path.abspath(working_directory)

        # # Debug
        # print(dir_path)
        # print(abs_target_path)
        # print(abs_work_dpath)

        # is inside working dir?
        if not os.path.commonpath([abs_target_path, abs_work_dpath]) == abs_work_dpath:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        # is directory?
        if not os.path.isdir(abs_target_path) :
            return f'Error: "{directory}" is not a directory'
        
        # get all files and dir metadata inside target dir
        contents = []
        for content in os.listdir(abs_target_path) :
            content_abs_path = os.path.join(abs_target_path,content)
            file_size = os.path.getsize(content_abs_path)
            is_dir = os.path.isdir(content_abs_path)
            format = f'- {content}: file_size={file_size} bytes, is_dir={is_dir}'
            contents.append(format)
        return '\n'.join(contents)

    except Exception as e : 
        return f'Error getting files info at {directory}: {e}'
    
# Schemas    

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)
    


