import os
import sys
import pathlib

path = pathlib.Path(sys.argv[1])
files = path.iterdir()

files = [x for x in files if not pathlib.Path(os.fspath(x)).is_dir()]

extensions = set()

for f in files:
    extensions.add(os.path.splitext(os.fspath(f))[1][1:])
for extension in extensions:
    if not os.path.exists(path / extension):
        os.mkdir(path / extension)

for f in files:
    extension = os.path.splitext(os.fspath(f))[1][1:]
    os.rename(os.fspath(f), os.fspath(path) + "/" + extension+"/"+f.parts[-1])
