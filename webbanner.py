#!/usr/bin/env python3

# takes user input and throws it into an html file
# to be displayed in a browser as a sort of banner

import os
import webbrowser
import time
import sys

cwd = os.getcwd()

FILENAME = "banner_output.tmp.html"

TOO_MANY_TEMPFILES_ERR_TEXT = """
Found too many banner_output{1-9}.tmp.html files.
You should get rid of them.
"""

bannertext = input("Enter banner text:\n>")

banner_html = f"""
<div id='spacer' style='height: 60px;'></div>
<h1 style='text-align: center; font-size: 48px;'>{bannertext}</h1>
"""

file_exists_count = 0
def check_filename():
	# recursively check if file exists.
	# if so, increment a suffix and try again.
	# stop after 10 tries to prevent accidental infinite loops.
	if file_exists_count <=9:

		if (os.path.isfile(f"{cwd}/{FILENAME}")):
			file_exists_count+=1
			FILENAME = f"banner_output{file_exists_count}.tmp.html"
			check_filename()
	else:
		print(TOO_MANY_TEMPFILES_ERR_TEXT)
		sys.exit(1)

check_filename()

with open(FILENAME, "w+") as f:
	f.write(banner_html)

# turns out webbrowser is part of the standard lib? python is cool.
webbrowser.open_new(f"file:///{cwd}/{FILENAME}")

# wait 1 second before deleting. firefox got mad at me if i didn't.
time.sleep(1)
os.remove(f"{cwd}/{FILENAME}")
