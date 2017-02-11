import tarfile 

out = tarfile.open("hello-compressed.tar.gz", mode="w")
out.add("hello.txt")
out.close()

