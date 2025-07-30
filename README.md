
# Gemini AI Agent Project

## I/O Example : 

```bash
uv run main.py "can write a .py file called test/robot.py, the content will be for _ in range (0,100): print('IM A ROBOT)"

Warning: there are non-text parts in the response: ['function_call'],returning concatenated text result from text parts,check out the non text parts for full response from model.
 - Calling function: write_file({'file_path': 'test/robot.py', 'content': "for _ in range (0,100): print('IM A ROBOT')"})
{'result': 'Successfully wrote to "test/robot.py" (43 characters written)'}

uv run main.py "can u run robot.py?" --verbose                                                                            


Hello from gemini-ai-agent ALICE!

User prompt: can u run robot.py?
Your model : gemini-2.0-flash-001
Generating response ...


Warning: there are non-text parts in the response: ['function_call'],returning concatenated text result from text parts,check out the non text parts for full response from model.
Calling function: run_python_file({'file_path': 'robot.py'})
{'result': 'Error: File "robot.py" not found.'}
-> {'result': 'Error: File "robot.py" not found.'}

Prompt tokens: 324
Response tokens: 11

uv run main.py "can u run robot.py inside test directory?" 

Warning: there are non-text parts in the response: ['function_call'],returning concatenated text result from text parts,check out the non text parts for full response from model.
 - Calling function: run_python_file({'file_path': 'test/robot.py'})
{'result': 'STDOUT:\n IM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\nIM A ROBOT\n'}

uv run main.py "can u show me the content of  robot.py inside test directory?"

Warning: there are non-text parts in the response: ['function_call'],returning concatenated text result from text parts,check out the non text parts for full response from model.
 - Calling function: get_file_content({'file_path': 'test/robot.py'})
{'result': "for _ in range (0,100): print('IM A ROBOT')"}

uv run main.py "can u list me all the file inside test directory?"

Warning: there are non-text parts in the response: ['function_call'],returning concatenated text result from text parts,check out the non text parts for full response from model.
 - Calling function: get_files_info({'directory': 'test'})
{'result': '- robot.py: file_size=43 bytes, is_dir=False'}
```

