#!/usr/bin/python

import sys
import urllib.request
import json

if len(sys.argv) != 2:
    print('Need exactly one argument.')
    sys.exit(0)

file_content = urllib.request.urlopen("https://raw.githubusercontent.com/HashOS/"+sys.argv[1]+"/master/hash.dependencies")
json_object = json.load(file_content)

print("\n\n<device>\n	<name></name>\n	<code></code>\n	<repos>")
print("		<git name=\"" + sys.argv[1] + "\" />")

for dependency in json_object:
    print("		<git name=\"" + dependency["repository"] + "\" />")

print("	</repos>\n</device>")
