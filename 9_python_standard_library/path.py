from pathlib import Path

# # path("C:\\program files\\ microsoft")
# path(r"C:\ program files\ microsoft")
# path("ecommerce/__init__.py")
# path() / "ecommerce" /"__init__.py"
# path.home()
# path.exists()
# path.is_file()
# path.is_dir()
# print(path.name)
# print(path.stem)
# print(path.suffix)
# print(path.parent)
# path = path.with_name("file.txt")
# print(path.abslute())
# print(path)

#WORKING WITH DIRECTORIES

path = Path("classes")
#path.exists()
# path.mkdir()
# path.rmdir()
# path.rename("ecommerce2")
# print(path.iterdir())
# for p in path.iterdir():
#     print(p)
paths=[p for p in path.iterdir() if p.is_dir()]
py_files = [p for p in path.rglob("*.py")]
print(py_files)