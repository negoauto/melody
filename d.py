import os
hi nego
if not os.path.isfile("serias.txt"):
    print("created serias.txt")
    with open("serias.txt", "w"):
        pass

if not os.path.isfile("movies.txt"):
    print("created movies.txt")
    with open("movies.txt", "w"):
        pass

if not os.path.isfile("links.txt"):
    print("created links.txt")
    with open("links.txt", "w"):
        pass

if not os.path.isfile("eposit.txt"):
    print("created eposit.txt")
    with open("eposit.txt", "w"):
        pass
print("all files found")
