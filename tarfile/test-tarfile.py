#!/usr/bin/python

# This script checks if a file is a tar file or not.
# It also checks for a valid tar file

import tarfile


file_list = ['Readme.txt', 'example.tar', 'bad_exmaple.tar']

for filename in file_list:
	try:
		print filename, " ", tarfile.is_tarfile(filename)
	except Exception, err:
		print filename, " ", err
