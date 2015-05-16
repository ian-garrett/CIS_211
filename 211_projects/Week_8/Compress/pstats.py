"""
pstats.py: CIS 211 assignment 8.3, Spring 2014
author: Ian Garrett, igarrett@uoregon.edu

pulls the number of chapters, sections, lines, and words from all text files in a directory
"""
import sys
from os import walk
from os import path
from os import popen

if len(sys.argv) < 2:
    raise Exception("enter a directory")
source = sys.argv[1]
chapt_count = 0
sect_count = 0
line_count = 0
word_count = 0
for directory in walk(source):
	for file in directory[2]:
		if path.splitext(file)[1] == '.tex':
			chapt_cmd = r"grep '\\chapter' {}".format(directory[0]+"/"+file)
			chapt_count += (len(popen(chapt_cmd).readlines()))
			sect_cmd = r"grep '\\section' {}".format(directory[0]+"/"+file)
			sect_count += (len(popen(sect_cmd).readlines()))
			wc_cmd = 'wc '+(directory[0]+"/"+file)
			wc_total = str(list(popen(wc_cmd))).split()
			line_count += int(wc_total[1])
			word_count += int(wc_total[2])

print ("\t",chapt_count,"\t",sect_count,"\t",line_count,"\t",word_count,"\t",source)