from bs4 import BeautifulSoup
import re
import sys
import requests

readmePath = sys.argv[3]
with open(readmePath, "w") as readme:
    readme.write("test")
