
try:
    fin = open('the_file', 'r')
except:
    fin = open('the_file', 'w')
print(fin.close())
