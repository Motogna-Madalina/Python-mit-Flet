from models.data_all_tasks import all_tasks
import json

def save_data(all_tasks):
    
    with open('data/tasks.json', 'w', encoding='utf-8') as file:
        json.dump(all_tasks, file, ensure_ascii=False, indent=4)

#json.dump() is a function that converts a Python object into a
# JSON string and writes it to a file.

#all_tasks is the Python object that we want to convert into a JSON string.
#file is the file object that we want to write the JSON string to.
#ensure_ascii=False is an argument that tells json.dump()
# to allow non-ASCII characters in the JSON string. 
#indent=4 is an argument that tells json.dump() to format the JSON string with an indentation 
#of 4 spaces for better readability.
#w - stands for "write" mode, which means that if the file already exists,
#  it will be overwritten.
#encoding='utf-8' is an argument that specifies the encoding of the file.