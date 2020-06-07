from pathlib import Path 
from zipfile import ZipFile
#IS USED TO OPEN THE ZIP FOLDER OF REQUIRED
# with ZipFile("file.zip","w") as zip:
#     for path in Path("sample1").rglob("*.*"):
#         zip.write(path)

with ZipFile("file.zip") as zip:
    print(zip.namelist())
    info = zip.getinfo("sample1/__init__.py")
    print(info.file_size)
    print(info.compress_size)
    zip.extractall("extract")