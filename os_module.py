import os 

# print(os.getcwd())  # Prints the current working directory

# print(os.listdir())  # Lists all files and directories in the current directory

# print(os.chdir("data"))  # Changes the current working directory to "data"
# print(os.getcwd())  # Prints the new current working directory

# if not os.path.exists('data2'):
#     os.mkdir('data2')
# os.chdir('data2')
# print(os.getcwd())  # Prints the new current working directory

# os.makedirs("data2/data3/data4" ,exist_ok=True)  # Creates nested directories "data2/data3"
# os.rmdir("data2")  # Removes the directory "data2/data3/data4"
# os.removedirs("data2/data3/data4")  # Removes the directory "data2/data3/data4" and its parent directories if they are empty

# create  txt file
# os.rename("data2.txt","data3.txt")  # Renames the file "data.txt" to "data2.txt"

# os.remove("data3.txt")  # Removes the file "data2.txt"

# info = os.stat("data2.txt")  # Gets the status of the file "data2.txt"
# print(info)  # Prints the status information of the file "data2.txt"

# print(os.path.exists("data2.txt"))  # Checks if the file "data2.txt" exists

# path = os.path.join("data2", "data3", "data4" ,"file.txt")
# os.makedirs(path, exist_ok=True)
# print(path)   
# print(os.path.isfile(path))
# print(os.path.isdir("data"))
# print(os.path.basename(path))
# print(os.path.dirname(path))
# create path on window using forward slash and on linux 
# data2/data3/data4/file.txt
#data2\data3\data4\file.txt

db_url = os.getenv("DATA_PATH" )
print(db_url)

db_path = os.environ.get("DATA_PATH")
print(db_path)

# os.environ["DEBUG"] ="True"
# print(os.getenv("DEBUG"))
from dotenv import load_dotenv

load_dotenv()

db_url = os.getenv("DATA_PATH" )
print(db_url)

db_path = os.environ.get("DEBUG")
print(db_path)