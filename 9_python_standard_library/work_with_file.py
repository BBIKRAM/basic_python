from pathlib import Path
from time import ctime
import shutil
path=Path("sample1/__init__.py")
# path.exists()
# path.rename("init.txt")
# path.unlink()
# print(path.stat())
# print(ctime(path.stat().st_mtime())
print(path.read_text())
path.write_text("hfsdh")


source = Path("sample1/__init__.py")
target = Path() / "__init__.py"
target.write_text(source.read_text())
#shutil we can easily copy from wource to target
shutil.copy(source,target)