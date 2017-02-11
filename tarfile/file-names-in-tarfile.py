# Program to list the files compressed inside the tarfile 
# Returns the list of files which are compressed inside tart file
import tarfile
t = tarfile.open("example.tar", "r")
print t.getnames()
