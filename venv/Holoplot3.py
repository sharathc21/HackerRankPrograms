import re
import sys
import os
import contextlib


file_name = "log2.txt"

lines = open(file_name, "r")

i=0
iv =0
iw =0
ie=0

for line in lines:
    # print(line)
    #x=re.findall(r"\[(.*?)\]", line)

    x = re.search("Application launched", line)
    if x != None:
        # print(x)
        i+=1
    # print("Splitting the lines")
    v= re.search("Software version", line)
    if v != None and iv!=1:
        v= re.split(":", line)
        print("Software version is", v[-1])
        iv=1
    w= re.search("Warning", line)
    e=re.search("Error", line)
    c=re.search("Error: Application exit", line)

    if w != None  and iw !=1:

        w= re.split(":", line)
        # print("Warning message is:", w[-1])
        print("Yes, there are warnings")
        iw=1

    if e != None and ie != 1:
        e = re.split(":", line)
        # print("Error message is:", e[-1])
        print("Yes, there are errors")
        ie = 1
    if c!= None:
        c = re.split(":", line)

        c1 = re.split(" ", c[0])
        # print("Splitting the first one", c1)
        print("Application crashed on day %s, at %s hours, %s minutes, %s seconds" % (c1[0], c1[1], c[1], c[2]))

print("The application launched %s times" %i )


##### Trying to send the console output to text file

# original_stdout = sys.stdout # Save a reference to the original standard output
#
# with open('logoutput.txt', 'w') as f:
#     sys.stdout = f # Change the standard output to the file we created.
#     #print('This message will be written to a file.')
#     print( file= sys.stderr)
#     sys.stdout = original_stdout # Reset the standard output to its original value

# stdoutOrigin=sys.stdout
# sys.stdout = open("logoutput.txt", "w")
#
# sys.stdout.close()
# sys.stdout=stdoutOrigin

#
# file_path = 'logoutput.txt.txt'
# with open(file_path, "w") as o:
#     with contextlib.redirect_stdout(o):
#         print("This text will be added to the file")