from bs4 import BeautifulSoup
import requests
import re
import sys

readmePath = sys.argv[3]
with open(readmePath, "w") as readme:
    readme.write("test")
