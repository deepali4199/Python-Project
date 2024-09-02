from pathlib import Path
import os
import shutil

def createfolder():
    try:
        name = input("please tell your folder name: ")
        if name == "":
            name == "new Folder"
        path = Path(name)
        path.mkdir()
        print(f"folder name {name} successfully created.")

    except Exception as err:
        print(f"Error: folder {name} already exist.")

def readfileandfolder():
    path = Path("")
    items = path.rglob("*")
    for i, v in enumerate(items):
        print(f"{i+1}: {v}")

def updatefolder():
    try:
        readfileandfolder()
        name = input("Which folder you want to update: ")
        path = Path(name)
        if path.exists() and path.is_dir():
            newname = input("please tell your new name: ")
            new_path = Path(newname)
            path.rename(new_path)
            print("done_successfully")

        else:
            print("No such folder exist")

    except Exception as err:
        print("error:", err)

def deletefolder():
    try:
        readfileandfolder()
        name = input("Which folder you want to delete: ")
        path = Path(name)
        if path.exists() and path.is_dir():
            # path.rmdir()
            shutil.rmtree(path)
            print("Deleted")

        else:
            print("folder not exist")
    
    except Exception as err:
        print("error:", err)

def createfile():
    try:
        readfileandfolder()
        name = input("Enter your file name: ")
        path = Path(name)

        if not path.exists():
            with open(name, "w") as fs:
                data = input("What do you want to write in your file: ")
                fs.write(data)

            print(f"file {name} created successfully")


        else:
            print("file already exist.")
    
    except Exception as err:
        print("error:", err)

def readfile():
    try: 
        readfileandfolder()
        name = input("Which file you want to read: ")
        path = Path(name)
        if path.exists():
            with open(name, 'r') as fs:
                data = fs.read()
                print(data)

        else:
            print("this file name does not exist")

    except Exception as err:
        print("error:", err)

def updatefile():
    try:
        readfileandfolder()
        name = input("Which file you want to update")
        path = Path(name)
        if path.exists():
            print("press 1 for changing the name of file")
            print("press 2 for for appending new content")
            print("press 3 for deleting all the content")
            choice = int(input("What you wanna do? "))
            if choice == 1:
                new_name = input("tell your new file name: ")
                newpath = Path(new_name)
                if not newpath.exists():
                    path.rename(newpath)
                    print("name change succuessfully")
                else:
                    print("Sorry this name already exist")
                
            elif choice == 2:
                with open(name, "a") as fs:
                    data = input("What do you want to append: ")
                    fs.write(" " + data)
                print("Content appended successfully")

            elif choice == 3:
                with open(name, "w") as fs:
                    data = input("press enter to skip or write new data")
                    fs.write(data)
                print("done successfully")

            else:
                print("Sorry wrong command")

        else:
            print("file does not exist")
        
    except Exception as err:
        print("error:", err)


def deletefile():
    try: 
        name = input("Which file you want to delete: ")
        path = Path(name)
        if  path.exists() and path.is_file():
            # os.remove(path)
            path.unlink()

        else:
            print("this file does not exist")

    except Exception as err:
        print("error:", err)


print("press 1 for creating a folder")
print("press 2 for readding files and folders")
print("press 3 for updating a folder")
print("press 4 for deleting a folder")
print("press 5 for creating a file")
print("press 6 for reading a file")
print("press 7 for updating a file")
print("press 8 for deleting a file")

check = int(input("What do you want? "))

if check == 1:
    createfolder()

elif check == 2:
    readfileandfolder()

elif check == 3:
    updatefolder()

elif check == 4:
    deletefolder()

elif check == 5:
    createfile()

elif check == 6:
    readfile()

elif check == 7:
    updatefile()

elif check == 8:
    deletefile()

else:
    print("You are entering wrong input")

