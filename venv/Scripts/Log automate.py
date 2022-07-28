import re
import sys

file_name = "log.txt"
lines = open(file_name, "r")
i=0
iv =0
iw =0
ie=0
#print("Start of the line")


# for line in lines:
#     #print(line)
#     #x=re.findall(r"\[(.*?)\]", line)
#     x = re.search("Application launched", line)
#     v= re.search("Software version", line)
#     if x != None:
#         #print(x)
#         i+=1
#     if v !=None:
#         print(v)
#         #v.split(":")
#         iv +=1

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
        print("Software version", v[-1])
        iv=1

    w= re.search("Warning", line)
    e=re.search("Error", line)
    c=re.search("Error: Application exit due to critical failure", line)

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
        # print("Application crashed " , c)
        # print("Error message is:", e[-1])
        # print("Application crashed on %s, at %s hours, %s minutes "  %{c[1], c[2], c[3]})
        print("Application crashed on day %s, at %s hours, %s minutes" % (c[0], c[1], c[2]))
    #print(type(v))

    # if v[-2] ==" Software version":
    #     # print("line containing software version")
    #     print("Software version is", v[-1])


    # print(v)

print("The application launched %s times" %i )
print("End of the line")

