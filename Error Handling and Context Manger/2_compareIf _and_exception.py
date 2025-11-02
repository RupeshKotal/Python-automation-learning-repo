import os
filepath = "./1_exceptions.py"

if os.path.exists(filepath):
    if os.access(filepath, os.R_OK):
        with open(filepath, "r") as f:
            print(f)

    else:
        print("Error")
    
else:
    print("Eroor file not present")


#VS

try:
    with open(filepath, "r") as k:
        print(k)

except FileNotFoundError:
    print(f"Fille not found")

except PermissionError:
    print(f"Permisson not fount")


except Exception as e:
    print(f"Erro : {e}")