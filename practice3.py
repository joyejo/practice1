#creating a file
tx=open("firstfiles.txt","x")
#tx=open("firstfile.txt","w")
#tx.write("this is my first file")
#tx.close()
#tx=open("firstfile.txt","r")
#info=tx.read()
#print(info)
#tx.close()
#append 
#tx=open("firstfile.txt","a")
#tx.write("""
#in real world there are so many challenages
#that we face thenm whenever we deal with them so that is so hard         
 ##        """)
#tx.close()
#tx=open("firstfile.txt","r")
##info=tx.read(30 )
#print(info)
#tx.close()
tx=open("firtsfiles.txt","w")
tx.write("my name is nuredin aman kedir and iam from hawassa university collague")
tx=open("firstfiles.txt","r")
tx.read()
print(tx.read())
tx.close()
tx=open("firstfile.txt","r+")
info=tx.read()
print(info)
tx.close()
tx=open("firstfile.txt","a")
tx.write("something is added")
tx.close()
tx=open("firstfile.txt","r")
info=tx.read()
print(info)

