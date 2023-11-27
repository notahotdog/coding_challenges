'''
    Implement wc tool 
    - name it as ccwc 
    - add command option -c -> outputs the number of bytes in a file

   Steps Completed:
   - 1 : simple version of wc - current issue with the number of bytes in a file
    
'''
import sys, os

file_name = sys.argv[2]

def read_file(file_name: str)->str:
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def get_n_bytes(string:str) -> int:
    return sys.getsizeof(string)

def get_size_of_file(file_name: str) -> int:
    return os.path.getsize(file_name)

# print("File name:", file_name)
# file_str = read_file(file_name)
# n  = get_n_bytes(file_str)
# print(n)

file_size = get_size_of_file(file_name)
print(file_size)