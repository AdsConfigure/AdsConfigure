import sys

readmePath = sys.argv[3]
with open(readmePath, "w") as readme:
    readme.write("test")
