# List
def print_list(l):
    for i in l:
        print(i)


l=[1,2,"N",5.5,"Tech_Tribe"]

print_list(l)

l[1]=99.36

print_list(l)

# Important to deal wiht MongoDB
# Same format as JSon -> Javascript object notation

a=[1,2,3,4,5]
dict={
    "Name":"Minato",
    "Nick-name":"Yellow Flash",
    "post":"Hokage",
    "Missons":999,
    "stars":a
}
print(dict)