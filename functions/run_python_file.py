# 29/06/2025

import os
import subprocess
import time

def run_python_file(working_directory, file_path, args=[]):
    abs_target_path = os.path.abspath(os.path.join(working_directory, file_path))
    abs_work_dpath = os.path.abspath(working_directory)

    # is inside working dir?
    if not os.path.commonpath([abs_target_path, abs_work_dpath]) == abs_work_dpath:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(abs_target_path):
        return f'Error: File "{file_path}" not found.'
    if not abs_target_path.endswith('.py'):
        return f'Error: "{file_path}" is not a python file'
    
    # Run logic 
    try :
        run_object = subprocess.run(['python3', abs_target_path] + args, timeout=30, capture_output=True, text=True,cwd=abs_work_dpath)
        components = []
        if run_object.stdout :
            components.append(f"STDOUT:\n {run_object.stdout}")
        if run_object.stderr:
            components.append(f"STDERR:\n {run_object.stderr}")
        if run_object.returncode != 0:
            components.append(f"Process exited with code  {run_object.returncode}")
        return "\n".join(components) if components else "No output produced."
    except Exception as e:
        return f"Error: executing Python file: {e}"

    
#         return_code = f"Process exited with code {run_object.returncode}" if run_object.returncode != 0 else ''

#         if run_object.stdout == None :
#             stdout = f"STDOUT: No output produced."
#         else :
#             stdout = 

#         stderr = f"STDERR:\n {run_object.stderr}"

#         components = [stdout, stderr]
#         if return_code:
#             components.append(return_code)

#         return '\n'.join(components)