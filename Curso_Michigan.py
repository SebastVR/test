Link importantes de cursos
https://online.umich.edu/subject/data-science/

2.3 Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
Use 35 hours and a rate of 2.75 per hour to test the program (the pay should be 96.25). 
You should use input to read a string and float() to convert the string to a number. 
Do not worry about error checking or bad user data.

xh = input("Enter Hours: ") #35
xr = input("Enter Rate: ") #2.75
xp = float(xh)*float(xr)
print("Pay:",xp)
 
fh = open("/home/sebastian/Documentos/Python Michigan/code3/romeo.txt", "r")

count = 0
for line in fh:
    print(line.strip())
    count = count + 1

print(count,"Lines")

astr = "Bob"
try:
	print("hello")
	istr = int(astr)
	print("there")
except:
	istr =-1
print("done",istr)	


rawstr = input("enter a number: ")
try:
	ival=int(rawtr)
except:
	ival=-1

if ival>0:
	print("nice work")
else:
	print("not a number")
	

a=12	
if a>0:
	
astr = 'Hello Bob'
istr = int(astr)
print('First', istr)
astr = '123'
istr = int(astr)
print('Second', istr)

#----------------------------------------------------------------------
3.1 Escriba un programa para pedirle al usuario las horas y la tarifa 
por hora usando la entrada para calcular el salario bruto. 
Paga la tarifa por hora por las horas hasta 40 y 1.5 veces la tarifa por hora 
para todas las horas Trabajó por encima de las 40 horas. 
Use 45 horas y una tasa de 10.50 por hora para probar el programa (la paga debe ser 498.75). 
Debes utilizar input para lee una cadena y float () para convertir la cadena en un número. 
No se preocupe por la comprobación de errores en la entrada del usuario: 
suponga que el usuario escribe los números correctamente.

hrs = input("Enter Hours:") #45
h = float(hrs)
taf = input("Enter Tarifa:") #10.5
t = float(taf)

if h<40:
	tb=h*t
	print(tb)
else:
		
	tb=40*t+1.5*(h-40)*t
	print(tb)

#----------------------------------------------------------------------		
3.3	Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, 
print an error. If the score is between 0.0 and 1.0, print a grade using the following table:
If the user enters a value out of range, print a suitable error message and exit. For the test, 
enter a score of 0.85

score1=float(input("Emnter Score: ")) #0.85
if score1 >= 0 and score1 <0.6:
	print("F")
elif score1 >= 0.6 and score1 <=0.69:
	print("D")
elif score1 >= 0.7 and score1 <=0.79:
	print("C")
elif score1 >= 0.8 and score1 <=0.89:
	print("B")
elif score1 >= 0.9 and score1 <=1:
	print("A")
else:
	try:
		score1/0
	except ZeroDivisionError:
		print("Division por cero")

def thing():
    print('Hello')
print('There')

x = 'banana'
y = max(x)
print(y)

def stuff():
    print('Hello')
    return
    print('World')
stuff()

def addtwo(a, b):
    added = a + b
    return a
x = addtwo(2, 7)
print(x)

#----------------------------------------------------------------------
4.6 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
Pay should be the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours 
worked above 40 hours. Put the logic to do the computation of pay in a function called computepay() 
and use the function to do the computation. The function should return a value. Use 45 hours and a 
rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a 
string and float() to convert the string to a number. Do not worry about error checking the user input 
unless you want to - you can assume the user types numbers properly. Do not name your variable sum or 
use the sum() function.

hrs = input("Enter Hours:") #45
h = float(hrs)
taf = input("Enter Tarifa:") #
t = float(taf)

def computepay(h,t):
	if h<40:
		tb=h*t
		
	else:
		tb=40*t+1.5*(h-40)*t		
	return tb

p = computepay(h,t)
print('Pay', p)

#----------------------------------------------------------------------
5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. 
Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything 
other than a valid number catch it with a try/except and put out an appropriate message and ignore the 
number. Enter 7, 2, bob, 10, and 4 and match the output below.

largest = None
smallest = None

while True:
	num = input("Enter a number: ")
	if num  == 'done':
		print("Maximum is", largest)
		print("Minimum is", smallest)
		break
	try:
		num1 = int(num)
	except:
		print("Invalid input")	
		continue
	if smallest is None or num1 < smallest:
		smallest = num1
	if largest is None or num1 > largest:
		largest = num1

#----------------------------------------------------------------------
6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end
of the line below. Convert the extracted value to a floating point number and print it out.		
	
text = "X-DSPAM-Confidence:    0.8475";
for i in text:
	if i == '0':
		position = text.find(i)
		number = float(text[position:])
print(number)

#----------------------------------------------------------------------
7.1 Write a program that prompts for a file name, then opens that file and reads through the file,
and print the contents of the file in upper case. Use the file words.txt to produce the output below.

/home/sebastian/Documentos/Python Michigan/code3/words.txt
name = input('Enter file:')
fh = open(name)
ff = fh.read().upper().rstrip()
print(ff)

#----------------------------------------------------------------------
7.2 Write a program that prompts for a file name, then opens that file and reads through the file,
looking for lines of the form: X-DSPAM-Confidence:    0.8475 Count these lines and extract the floating
point values from each of the lines and compute the average of those values and produce an output as
shown below. Do not use the sum() function or a variable named sum in your solution.

/home/sebastian/Documentos/Python Michigan/code3/mbox-short.txt
fname = input("Enter file name: ")
fh = open(fname)
cont = 0
acum = 0
l = []
for line in fh:
	line = line.rstrip()
	if line.startswith('X-DSPAM-Confidence: '):
		l.append(float(line[20:26]))
		cont += float(line[20:26])
		acum += 1
print ('Average spam confidence: ' + str(cont/acum))

#----------------------------------------------------------------------
8.4 Open the file romeo.txt and read it line by line.
For each line, split the line into a list of words using the split() method.
The program should build a list of words.
For each word on each line check to see if the word is already in the list and if not append
it to the list. When the program completes, sort and print the resulting words in alphabetical order.	

/home/sebastian/Documentos/Python Michigan/code3/romeo.txt
##### SHAPE 1 #####
fname = input("Enter file name: ")
fh = open(fname)
result =[]
for line in fh:
	result.extend([i for i in line.split() if i not in result])
print(sorted(result))

##### SHAPE 2 #####
fname = input("Enter file name: ")
fh = open(fname)
result =[]
for line in fh:
	for i in line.split():
		if i not in result:
			result.append(i)
print(sorted(result))

#----------------------------------------------------------------------
8.5 Open the file mbox-short.txt and read it line by line. 
When you find a line that starts with 'From ' like the following line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
You will parse the From line using split() and print out the second word in the line
(i.e. the entire address of the person who sent the message).Then print out a count at the end.
Hint: make sure not to include the lines that start with 'From:'.

##### SHAPE 1 #####
/home/sebastian/Documentos/Python Michigan/code3/mbox-short.txt
fname = input("Enter file name: ")
fh = open(fname)
result = []
cont = 0
for line in fh:
	line = line.rstrip()
	if line.startswith('From: '):
		for i in line.split():
			if i != 'From:':
				result.append(i)
				print (result[cont])
				cont += 1
print("There were", cont, "lines in the file with From as the first word")

##### SHAPE 2 #####
fname = input("Enter file name: ")
if len(fname) < 1 : fname = '/home/sebastian/Documentos/Python Michigan/code3/mbox-short.txt'
#When the code solicite the input oprimir enter
fh = open(fname)
result = []
cont = 0
for line in fh:
	line = line.rstrip()
	if line.startswith('From: '):
		for i in line.split():
			if i != 'From:':
				result.append(i)
				print (result[cont])
				cont += 1
print("There were", cont, "lines in the file with From as the first word")

#----------------------------------------------------------------------
9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number
of mail messages.The program looks for 'From ' lines and takes the second word of those lines as the
person who sent the mail. The program creates a Python dictionary that maps the
sender's mail address to a count of the number of times they appear in the file. 
After the dictionary is produced, the program reads through the dictionary using a maximum loopto find
the most prolific committer.

/home/sebastian/Documentos/Python Michigan/code3/mbox-short.txt
fname = input("Enter file name: ")
fh = open(fname)
counts = {}
for line in fh:
	line = line.rstrip()
	if line.startswith('From: '):
		for i in line.split():
			if i != 'From:':
				counts[i] = counts.get(i,0) + 1
print(counts)

largest = -1
thewords = None
for k , v in counts.items():
	if v > largest:
		largest = v
		thewords = k
print(thewords,largest)

	
10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the 
day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and 
then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008 Once you have accumulated the counts for 
each hour, print out the counts, sorted by hour as shown below.


name = '/home/sebastian/Documentos/Python Michigan/code3/mbox-short.txt'

with open(name) as file:
	#l2 = [line.startswith('From') and len(line.split()) >=5 for line in file if line.startswith('From')]
	#l = [line.split()[5] for line in file if (line.startswith('From') and len(line.split()) >= 5)]
	#print(l, l2)
	#d = {key: value for key, value in enumerate(file) if }
	l = []
	for line in file:
		if line.startswith('From'):
			x = line.split()
			if len(x) >= 5:
				l.append(x[5][:2])
	l= sorted(l)
	my_dict = {i: l.count(i) for i in l}
	for key, value in my_dict.items():
		print(key, value)

#------ Chapter 11 -----------------------------------------------------------------
#------ Regular expressions --------------------------------------------------------

Codigo que extrae los numeros enteros de un archivo txt y los suma 
import re
name = '/home/sebastian/Documentos/Python Michigan/code3/regex_sum_405573(2).txt'

with open(name) as file:
	lis = []
	for line in file:
		line = line.rstrip()
		for i in line.split():
			x = re.findall('^[0-9]+',i)    #^
			if x != []:
				i = int(i)
				lis.append(i)
	print(lis)
	print('suma = ',sum(lis))

x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y =re.findall('\S+?@\S+',x) y #['stephen.marquard@uct.ac.za']                                                                                                               


#------ Chapter 12 -------------------------------------------------------
#------ Networked programs -----------------------------------------------
import socket
#import time

Host = 'data.pr4e.org'
Port = 80
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((Host,Port))
mysock.sendall(b'GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n')
count = 0
picture = b""

while True:
	data = mysock.recv(5120)
	if len(data) < 1 : 
		break
	count = count + len(data)
	print(len(data), count)
	picture = picture +data
mysock.close()

#Look fpr the end of the header
pos = picture.find(b'\r\n\r\n')
print('Header length', pos)
print(picture[:pos].decode())

#Skip past the header and the picture data
picture = picture[pos+4:]
fhand = open('stuff.jpg', 'wb')
fhand.write(picture)
fhand.close()

#--------------------------------------------------------
import socket
Host = 'data.pr4e.org'
Port = 80
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((Host,Port))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)
count = 0

while True:
	data = mysock.recv(512)
	if len(data) < 1 : 
		break
	count = count + len(data)
	print(data.decode(),end='')
mysock.close()

#--------------------------------------------------------
import socket
Host = 'data.pr4e.org'
Port = 80
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((Host,Port))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)
count = 0

while True:
	data = mysock.recv(512)
	if len(data) < 1 : 
		break
	count = count + len(data)
	print(data.decode(),end='')
mysock.close()

#--------------------------------------------------------
import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
counts = {}
for line in fhand:
	words = line.decode().split()
	for word in words:
		counts[word] = counts.get(word, 0) + 1
print(counts)

#--------------------------------------------------------
import urllib.request, urllib.parse, urllib.error

img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg').read()
fhand = open('cover3.jpg', 'wb')
fhand.write(img) #230210
fhand.close()

#--------------------------------------------------------
img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg')
fhand = open('cover3.jpg', 'wb')
size = 0
while True:
	info = img.read(100000)
	if len(info) < 1:
		break
	size = size + len(info)
	fhand.write(info)
print(size, 'characters copied.') #230210 characters copied.
fhand.close()

#--------------------------------------------------------
import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
counts = []
for line in fhand:
	words = line.decode().split()
	for word in words:
		counts.append(word)
print(counts)

#--------------------------------------------------------
import urllib.request, urllib.parse, urllib.error
import re
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

https://docs.python.org
url = input('Enter - ')
html = urllib.request.urlopen(url).read()
links = re.findall(b'href="(http[s]?://.*?)"', html)
for link in links:
	print(link.decode())

#--------------------------------------------------------
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

https://docs.python.org
url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('a')
for tag in tags:
	print(tag.get('href', None))

#--------------------------------------------------------
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_405575.html'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
count = 0
for tag in tags:
    # Look at the parts of a tag
	print('TAG:', tag)
	print('URL:', tag.get('href', None))
	print('Contents:', tag.contents[0])
	print('Attrs:', tag.attrs)
	count += float(tag.contents[0])
print(count)

#--------------------------------------------------------
 To run this, download the BeautifulSoup zip file
# and unzip it in the same directory as this file
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

counter = 0
url = 'http://py4e-data.dr-chuck.net/known_by_Sharona.html'
while counter < 7:
	html = urllib.request.urlopen(url, context=ctx).read()
	soup = BeautifulSoup(html, 'html.parser')
	tags = soup('a')
	url = tags[17].get('href', None)
	print (url)
	counter += 1


#------ Chapter 13 -------------------------------------------------------
#------ Using Web Services -----------------------------------------------
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_405577.xml'
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
print('Retrieved', len(data), 'characters')
print(data.decode())
tree = ET.fromstring(data)
print (tree)
counters = tree.findall('.//count')
print (counters)

cont = 0
for count in counters:
	cont += int(count.text) 
print(cont)
  
#--------------------------------------------------------
import urllib.request, urllib.parse, urllib.error
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_405578.json'
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
info = json.loads(data)

cont = 0
sum = 0
for count in info['comments']:
	counts = info['comments'][cont]['count']
	sum += counts
	cont += 1
print(sum)
	
#--------------------------------------------------------
import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = 'Western Governors University'
parms = dict()
parms['address'] = address
parms['key'] = api_key
url = serviceurl + urllib.parse.urlencode(parms)
print(url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
print(data)
print(len(data))
js = json.loads(data)

for count in js['results'][0]:
	if count == 'place_id':
		print(js['results'][0][count])

#--------------------------------------------------------
import pandas as pd
df = pd.read_excel (r'/home/sebastian/Descargas/Ejercicios(3).xlsx', header=None,index_col=None,
names=['A','B','C','D','E'])

df['B'] = df['A'].str.split(',').apply(lambda x: x[0].replace(',',''))
df['C'] = df['A'].str.split(',').apply(lambda x: x[1].replace(',',''))
df['D'] = df['A'].str.split().apply(lambda x: x[-2].replace(',',''))
df['E'] = df['A'].str.split().apply(lambda x: x[-1].replace(',',''))
print(df)
df.to_excel('/home/sebastian/Descargas/Ejercicios(4).xlsx',index=False,header=False) #Save the file
#https://www.regextester.com/

#------ Chapter 15 ---------------------------------------------------------------------
#------ Using Databases and SQL --------------------------------------------------------

import sqlite3

conn = sqlite3.connect('music.sqlite')
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS Tracks')
cur.execute('CREATE TABLE Tracks (title TEXT, plays INTEGER)')
conn.close()

#--------------------------------------------------------
import sqlite3
conn = sqlite3.connect('music.sqlite')
cur = conn.cursor()

cur.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)', ('Thunderstruck', 20))
cur.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)', ('My Way', 15))
conn.commit()

cur.execute('SELECT title, plays FROM Tracks')
for row in cur:
	print(row)

#--------------------------------------------------------
import sqlite3
import pandas as pd
conn = sqlite3.connect('Ages.sqlite')
cur = conn.cursor()

#cur.execute('CREATE TABLE Ages (name VARCHAR(128), age INTEGER)')
cur.execute("INSERT INTO Ages (name, age) VALUES ('Hallie', 16)")
cur.execute("INSERT INTO Ages (name, age) VALUES ('Bret', 26)")
cur.execute("INSERT INTO Ages (name, age) VALUES ('Karyss', 14)")
cur.execute("INSERT INTO Ages (name, age) VALUES ('Pele', 20)")
conn.commit()

cur.execute('SELECT hex(name || age) AS X FROM Ages ORDER BY X')
for row in cur:
	print(row)

df = pd.read_sql('select * from Ages', conn)
df = pd.read_sql('select name from Ages where age>22', conn)
df = pd.read_sql('SELECT hex(name || age) AS X FROM Ages ORDER BY X', conn)

#--------------------------------------------------------
import sqlite3
import pandas as pd
import re

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS Counts")
cur.execute("CREATE TABLE Counts (org TEXT, count INTEGER)")
fname = '/home/sebastian/Documentos/Python Michigan/code3/mbox.txt'
org = {}
fh = open(fname)
for line in fh:
	line = line.rstrip()
	if line.startswith('From:'):
		print (line)
		l = re.search('(?P<org>[^@]*$)', line).group() 
		print (l)
		org[l] = org.get(l, 0) + 1

for o, count in org.items():
	print(o, count)
	cur.execute("INSERT INTO Counts (org, count) VALUES ('{}', {})".format(o, count))
conn.commit()

df = pd.read_sql('select * from Counts', conn)

#---------------------------------------------------------------------------
import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect('Trackdb.sqlite')
cur = conn.cursor()

cur.executescript('''
CREATE TABLE Artist (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, Artist TEXT UNIQUE);
CREATE TABLE Album (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, Album TEXT UNIQUE);
CREATE TABLE Genre (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, Genre TEXT UNIQUE);
CREATE TABLE Track (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, 
Track TEXT UNIQUE, Artist INTEGER, Album INTEGER, Genre INTEGER)''')

fname = '/home/sebastian/Documentos/Python Michigan/code3/tracks/Library.xml'
stuff = ET.parse(fname)
all = stuff.findall('dict/dict/dict')

def lookup(d, key):
	found = False
	for child in d:
		print(child.tag, child.text)
		if found : return child.text
		if child.tag == 'key' and child.text == key:
			found = True
	return None

for entry in all:
	if (lookup(entry, 'Track ID') is None): continue
	track = lookup(entry, 'Name') 
	genre = lookup(entry, 'Genre')
	artist = lookup(entry, 'Artist')
	album = lookup(entry, 'Album')

	if genre is None or artist is None or album is None: continue

	print(genre, artist, album, track)

	cur.execute('''INSERT OR IGNORE INTO Artist (Artist) VALUES ( ? )''',(artist,))
	cur.execute('SELECT id FROM Artist WHERE  Artist = ? ', (artist, ))
	artist_id = cur.fetchone()[0]

	cur.execute('''INSERT OR IGNORE INTO Album (Album) VALUES ( ? )''',(album,))
	cur.execute('SELECT id FROM Album WHERE Album = ? ', (album, ))
	album_id = cur.fetchone()[0]

	cur.execute('''INSERT OR IGNORE INTO Genre (Genre) VALUES ( ? )''',(genre,))
	cur.execute('SELECT id FROM Genre WHERE Genre = ? ', (genre, ))
	genre_id = cur.fetchone()[0]

	cur.execute('''INSERT OR REPLACE INTO Track (Track, Album, Artist, Genre) VALUES ( ?, ?, ?, ?)''', 
	(track, artist_id, album_id, genre_id,))

	conn.commit()
#---------------------------------------------------------------------------
#-------------------Example Cap 15 JOIN-------------------------------------
import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()

# Make some fresh tables using executescript()
#cur.executescript('DROP TABLE IF EXISTS Artis')
#cur.executescript('DROP TABLE IF EXISTS Album')
#cur.executescript('DROP TABLE IF EXISTS Genre')
#cur.executescript('DROP TABLE IF EXISTS Track')

cur.executescript('''
CREATE TABLE Artist (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, name TEXT UNIQUE);
CREATE TABLE Genre (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, name TEXT UNIQUE);
CREATE TABLE Album (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, artist_id  INTEGER, 
title TEXT UNIQUE);
CREATE TABLE Track (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, 
title TEXT  UNIQUE, album_id  INTEGER, genre_id  INTEGER)''')

def lookup(d, key):
	found = False
	for child in d:
		print(child.tag, child.text)
		if found : return child.text
		if child.tag == 'key' and child.text == key:
			found = True
	return None

fname = '/home/sebastian/Documentos/Python Michigan/code3/tracks/Library.xml'	
stuff = ET.parse(fname)
all = stuff.findall('dict/dict/dict')

for entry in all:
	if ( lookup(entry, 'Track ID') is None ) : continue

	name = lookup(entry, 'Name')
	artist = lookup(entry, 'Artist')
	album = lookup(entry, 'Album')
	genre = lookup(entry, 'Genre')
	count = lookup(entry, 'Play Count')   #Be can clear
	rating = lookup(entry, 'Rating')      #Be can clear
	length = lookup(entry, 'Total Time')  #Be can clear

	if name is None or artist is None or genre is None or album is None: continue

	print (name, artist, album, genre, count, rating, length)

	cur.execute('''INSERT OR IGNORE INTO Artist (name) VALUES ( ? )''', ( artist,))
	cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
	artist_id = cur.fetchone()[0]

	cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) VALUES ( ?, ? )''', 
	(album, artist_id,))
	cur.execute('SELECT id FROM Album WHERE title = ? ', (album,))
	album_id = cur.fetchone()[0]

	cur.execute('''INSERT OR IGNORE INTO Genre (name) VALUES ( ? )''', ( genre,))
	cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre,))
	genre_id = cur.fetchone()[0]

	cur.execute('''INSERT OR REPLACE INTO Track (title, album_id, genre_id ) VALUES ( ?, ?, ?)''', 
	(name, album_id, genre_id,))

	conn.commit()
#-----------------------Execute SQL-----------------------------------------
SELECT Track.title, Artist.name, Album.title, Genre.name 
    FROM Track JOIN Genre JOIN Album JOIN Artist 
    ON Track.genre_id = Genre.ID and Track.album_id = Album.id 
        AND Album.artist_id = Artist.id
    ORDER BY Artist.name LIMIT 3
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
import json
import sqlite3

conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

# Do some setup
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;
CREATE TABLE User (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, name TEXT UNIQUE);
CREATE TABLE Course (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, title TEXT UNIQUE);
CREATE TABLE Member (user_id INTEGER,ncourse_id INTEGER, role INTEGER, PRIMARY KEY (user_id, course_id))
''')
fname = '/home/sebastian/Documentos/Python Michigan/code3/roster/roster_data.json'

str_data = open(fname).read()
json_data = json.loads(str_data)

for entry in json_data:
	name = entry[0];
	title = entry[1];
	role = entry[2];

	print((name, title, role))

	cur.execute('''INSERT OR IGNORE INTO User (name) VALUES ( ? )''', ( name, ) )
	cur.execute('SELECT id FROM User WHERE name = ? ', (name, ))
	user_id = cur.fetchone()[0]

	cur.execute('''INSERT OR IGNORE INTO Course (title) VALUES ( ? )''', ( title, ) )
	cur.execute('SELECT id FROM Course WHERE title = ? ', (title, ))
	course_id = cur.fetchone()[0]

	cur.execute('''INSERT OR REPLACE INTO Member
	(user_id, course_id, role) VALUES ( ?, ?, ? )''', ( user_id, course_id, role ) )

	conn.commit()

#-----------------------Execute SQL-----------------------------------------
SELECT hex(User.name || Course.title || Member.role ) AS X FROM 
    User JOIN Member JOIN Course 
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY X
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import ssl
import sqlite3
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://desarrolloweb.com/home/html'
html = urllib.request.urlopen(url, context=ctx)
data = html.read().decode()

soup = BeautifulSoup(data, 'html.parser')
tags = soup('a')

conn = sqlite3.connect('Week7.sqlite')
cur = conn.cursor()	

cur.execute('''CREATE TABLE dictionary (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT 
UNIQUE, keys TEXT, result TEXT)''')


cont = 1
group = {}
for tag in tags:
	keys = tag
	values = tag.get('href')
	group[tag] = tag.get('href')
	cur.execute('''INSERT OR IGNORE INTO dictionary (id, keys, result) 
			VALUES ( ?, ?, ? )''', (cont, str(keys), str(values)  ) )
	cont += 1
	conn.commit()

#---------------------------------------------------------------------
#---------------------------------------------------------------------
######## Applied Data Science with Python Specialization ########
#---------------------------------------------------------------------
#---------------------------------------------------------------------

#-----------------------------WEEK 1----------------------------------
import csv
rute= '/home/sebastian/Documentos/Python Michigan/course1_downloads/course1_downloads/mpg.csv'
%precision 2
with open(rute) as csvfile:
	mpg = list(csv.DictReader(csvfile))

mpg[:3]
len(mpg)
mpg[0].keys()
sum(float(d['cty']) for d in mpg) / len(mpg)

#---------------------------------------------------------------------
cont=0
lis=[]
for i in mpg:
	lis.append(float(i['cty']))
	cont+=1
print(sum(lis))
print(cont)
print(sum(lis)/cont)

cylinders = set(d['cyl'] for d in mpg)
cylinders

#---------------------------------------------------------------------
kind = input('añade un mensaje: ')
def do_math(a, b,kind = kind): 
	if (kind=='add'): 
		return a+b 
	else: 
		return a-b
do_math(2,3,kind)

#---------------------------------------------------------------------
people = [
'Dr. Christopher Brooks', 
'Dr. Kevyn Collins-Thompson', 
'Dr. VG Vinod Vydiswaran',
'Dr. Daniel Romero']
#---------------------------------------------------------------------
def split_title_and_name(person):
	title = person.split()[0]
	lastname = person.split()[-1]
	return '{} {}'.format(title, lastname)

lis = map(split_title_and_name, people)

#---------------------------------------------------------------------
people = [
'Dr. Christopher Brooks', 
'Dr. Kevyn Collins-Thompson', 
'Dr. VG Vinod Vydiswaran', 
'Dr. Daniel Romero']

def split_title_and_name(person):
	return person.split()[0] + ' ' + person.split()[-1]

#option 1
for person in people:
    print(split_title_and_name(person) == (lambda x: x.split()[0] + ' ' + x.split()[-1])(person))

#option 2
list(map(split_title_and_name, people)) == list(map(lambda person: person.split()[0] + ' ' + person.split()[-1], people))

#-----------------------------WEEK 2-----------------------------------------
#----------------------------------------------------------------------------
purchase_1 = pd.Series({'Name': 'Chris','Item Purchased': 'Dog Food','Cost': 22.50})
purchase_2 = pd.Series({'Name': 'Kevyn','Item Purchased': 'Kitty Litter','Cost': 2.50})
purchase_3 = pd.Series({'Name': 'Vinod','Item Purchased': 'Bird Seed','Cost': 5.00})

df = pd.DataFrame([purchase_1, purchase_2, purchase_3], 
index=['Store 1', 'Store 1', 'Store 2'])

'''For the purchase records from the pet store, how would you get a list of all items which 
had been purchased (regardless of where they might have been purchased, or by whom)?'''

df['Item Purchased']

'''For the purchase records from the pet store, how would you update the DataFrame, 
applying a discount of 20% across all the values in the 'Cost' column?'''

#---------Shape1------------------------
df['Cost'] = df['Cost']- df['Cost']*0.2
#---------Shape2------------------------
df['Cost'] *= 0.8
print(df['Cost'])

'''Write a query to return all of the names of people who bought products worth 
more than $3.00'''

df['Name'][df['Cost']>3]

'''Reindex the purchase records DataFrame to be indexed hierarchically, first by store, 
then by person. Name these indexes 'Location' and 'Name'. Then add a new entry to it with 
the value of:
Name: 'Kevyn', Item Purchased: 'Kitty Food', Cost: 3.00 Location: 'Store 2'.'''

df = df.set_index([df.index, 'Name'])
df.index.names = ['Location', 'Name']
df = df.append(pd.Series(data={'Cost': 3.00, 'Item Purchased': 'Kitty Food'}, 
name=('Store 2', 'Kevyn')))
df
#-----------------------------------------------------------------------------
import pandas as pd
import csv
rute= '/home/sebastian/Documentos/Python Michigan/course1_downloads/course1_downloads/olympics.csv'

df = pd.read_csv(rute, index_col=0, skiprows=1)
for col in df.columns:
	if col[:2]=='01':
		df.rename(columns={col:'Gold'+col[4:]}, inplace=True) #si no se pone el inplace=True no cambia el titulo del dataframe 
	if col[:2]=='02':
		df.rename(columns={col:'Silver'+col[4:]}, inplace=True)
	if col[:2]=='03':
		df.rename(columns={col:'Bronze'+col[4:]}, inplace=True)
	if col[:1]=='№':
		df.rename(columns={col:'#'+col[1:]}, inplace=True)

names_ids = df.index.str.split('\s\(') # split the index by '('
df.index = names_ids.str[0] # the [0] element is the country name (new index) 
df['ID'] = names_ids.str[1].str[:3] # the [1] element is the abbreviation or ID (take first 3 characters from that)

df = df.drop('Totals')
df.head()

'''What is the first country in df? This function should return a Series.'''
def answer_zero():
	return df.iloc[0]
answer_zero()

'''Which country has won the most gold medals in summer games?
This function should return a single string value.'''

#---------Shape1------------------------
def answer_one():
	return df['Gold'].idxmax()
answer_one()

#---------Shape2------------------------
def answer_one():
	return df.iloc[df['Gold'].argmax()].name
answer_one()

'''Which country had the biggest difference between their summer and winter gold medal 
counts? This function should return a single string value'''

#---------Shape1------------------------
def answer_two():
	return ((df['Gold'] - df['Gold.1']).idxmax())
answer_two()
#---------Shape2------------------------
df['difference'] = df['Gold']-df['Gold.1']
def answer_two():
	return df.iloc[df['difference'].argmax()].name
answer_two()

'''Which country has the biggest difference between their summer gold medal counts and 
winter gold medal counts relative to their total gold medal count?
Only include countries that have won at least 1 gold in both summer and winter.
This function should return a single string value.'''

#---------Shape1------------------------
def answer_three():
	only_gold = df.where((df['Gold'] > 0) & (df['Gold.1'] > 0))
	only_gold = only_gold.dropna()
	return (abs((only_gold['Gold'] - only_gold['Gold.1']) / only_gold['Gold.2'])).idxmax()
answer_three()

'''Write a function that creates a Series called "Points" which is a weighted value where 
each gold medal (Gold.2) counts for 3 points, silver medals (Silver.2) for 2 points, 
and bronze medals (Bronze.2) for 1 point. The function should return only the 
column (a Series object) which you created, with the country names as indices.'''

def answer_for():
	df['Points'] = (df['Gold.2']*3 + df['Silver.2']*2 + df['Bronze.2']*1)
	return df['Points']
answer_for()

'''Which state has the most counties in it? (hint: consider the sumlevel key carefully! 
You'll need this for future questions too...) This function should return a single string 
value. '''

#------------------------Part 2------------------------------------------------------
#------------------------------------------------------------------------------------

census_df = pd.read_csv('/home/sebastian/Documentos/Python Michigan/course1_downloads/course1_downloads/census.csv')
census_df.head()

def answer_five():
	new_df = census_df[census_df['SUMLEV'] == 50]
	return new_df.groupby('STNAME').count()['SUMLEV'].idxmax()
answer_five()

'''Only looking at the three most populous counties for each state, what are the three
most populous states (in order of highest population to lowest population)? 
Use CENSUS2010POP This function should return a list of string values'''

def answer_six():
	new_df = census_df[census_df['SUMLEV'] == 50]
	most_populous_counties = new_df.sort_values('CENSUS2010POP', ascending=False).groupby('STNAME').head(3)
	return most_populous_counties.groupby('STNAME').sum().sort_values('CENSUS2010POP', ascending=False).head(3).index.tolist()
answer_six()

'''Which county has had the largest absolute change in population within the 
period 2010-2015? (Hint: population values are stored in columns POPESTIMATE2010 through 
POPESTIMATE2015, you need to consider all six columns.)
e.g. If County Population in the 5 year period is 100, 120, 80, 105, 100, 130, then its 
largest change in the period would be |130-80| = 50.
This function should return a single string value.'''

DUDA
def answer_seven():
	new_df = census_df[census_df['SUMLEV'] == 50][[6, 9, 10, 11, 12, 13, 14]]
	new_df["MaxDiff"] = abs(new_df.max(axis=1) - new_df.min(axis=1))
	most_change = new_df.sort_values(by=["MaxDiff"], ascending = False)
	return most_change.iloc[0][0]
answer_seven()

'''In this datafile, the United States is broken up into four regions using the "REGION" 
column. Create a query that finds the counties that belong to regions 1 or 2, whose name 
starts with 'Washington', and whose POPESTIMATE2015 was greater than their POPESTIMATE 2014.
This function should return a 5x2 DataFrame with the columns = ['STNAME', 'CTYNAME'] and 
the same index ID as the census_df (sorted ascending by index)'''

def answer_eight():
	counties = census_df[census_df['SUMLEV'] == 50]
	region = counties[(counties['REGION'] == 1) | (counties['REGION'] == 2)]
	washington = region[region['CTYNAME'].str.startswith("Washington")]
	grew = washington[washington['POPESTIMATE2015'] > washington['POPESTIMATE2014']]
	return grew[['STNAME', 'CTYNAME']]
answer_eight()

#-----------------------------WEEK 3-----------------------------------------
#----------------------------------------------------------------------------
'''Here are two DataFrames, products and invoices. The product DataFrame has an identifier 
and a sticker price. The invoices DataFrame lists the people, product identifiers, 
and quantity. Assuming that we want to generate totals, how do we join these 
two DataFrames together so that we have one which lists all of the information we need?
products DataFrame'''

products_df = pd.DataFrame([{'Product ID':4109, 'Price':5.0, 'Product':'Sushi Roll'},
{'Product ID':1412, 'Price':0.5, 'Product':'Egg'},
{'Product ID':8931, 'Price':1.5, 'Product':'Bagel'}])
products_df = products_df.set_index('Product ID')

invoices_df = pd.DataFrame([{'Customer':'Ali', 'Product ID':4109, 'Quantity':1},
{'Customer':'Eric', 'Product ID':1412, 'Quantity':12},
{'Customer':'Ande', 'Product ID':8931, 'Quantity':6},
{'Customer':'Sam', 'Product ID':4109, 'Quantity':2}])

print(pd.merge(products_df, invoices_df, left_index=True, right_on='Product ID'))

'''Suppose we are working on a DataFrame that holds information on our equipment for an 
upcoming backpacking trip. Can you use method chaining to modify the DataFrame df in one 
statement to drop any entries where 'Quantity' is 0 and rename the column 
'Weight' to 'Weight (oz.)'?'''

print(df.drop(df[df['Quantity'] == 0].index).rename(columns={'Weight': 'Weight (oz.)'}))

'''Looking at our backpacking equipment DataFrame, suppose we are interested in finding our 
total weight for each category. Use groupby to group the dataframe, and apply a function 
to calculate the total weight (Weight x Quantity) by category.'''

#---------Shape1------------------------
def totalweight(df, w, q):
	return sum(df[w] * df[q])

#---------Shape2------------------------
print(df.groupby('Category').apply(lambda df,a,b: sum(df[a] * df[b]), 'Weight (oz.)', 'Quantity'))

#--------------------------------------------------------------------
'''Try casting this series to categorical with the ordering Low < Medium < High.'''

s = pd.Series(['Low', 'Low', 'High', 'Medium', 'Low', 'High', 'Low'])

s.astype('category', CategoricalDtype(categories=['Low', 'Medium', 'High']))

#----------------------------------------------------------------------
'''Suppose we have a series that holds height data for jacket wearers. Use pd.cut to bin 
this data into 3 bins.'''

s = pd.Series([168, 180, 174, 190, 170, 185, 179, 181, 175, 169, 182, 177, 180, 171])

pd.cut(s, 3)
pd.cut(s, 3, labels=['Small', 'Medium', 'Large'])

'''Suppose we have a DataFrame with price and ratings for different bikes, broken down by 
manufacturer and type of bicycle. Create a pivot table that shows the mean price and mean 
rating for every 'Manufacturer' / 'Bike Type' combination.'''

print(pd.pivot_table(Bikes, index=['Manufacturer','Bike Type']))

#--------------------------------------------------------------------
#--------------------Assignment 3 - More Pandas----------------------

#-------Shape1-----------------
def answer_one():
	import pandas as pd
	import numpy as np
	energy = pd.read_excel(
		'/home/sebastian/Documentos/Python Michigan/course1_downloads/course1_downloads/Energy Indicators.xls',
		skiprows = 17, 
		skip_footer = (38), 
		usecols = [2,3,4,5],
		names = ['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable'],
		na_values = ['...']
	) 

	energy['Energy Supply'] = energy['Energy Supply']*10**6
	energy['Country'] = energy['Country'].str.replace(r" *\(.*\)","")
	energy['Country'] = energy['Country'].str.replace(r"([0-9]+)","")
	energy.loc[energy['Country'] == 'Republic of Korea', 'Country'] = "South Korea"
	energy.loc[energy['Country'] == 'United States of America', 'Country'] = "United States"
	energy.loc[energy['Country'] == 'United Kingdom of Great Britain and Northern Ireland', 'Country'] = "United Kingdom"
	energy.loc[energy['Country'] == 'China, Hong Kong Special Administrative Region', 'Country'] = "Hong Kong"

	GPD = pd.read_csv(
		'/home/sebastian/Documentos/Python Michigan/course1_downloads/course1_downloads/world_bank.csv', 
		skiprows=4
	)
	GPD.loc[GPD['Country Name'] == 'Korea, Rep.', 'Country Name'] = "South Korea"
	GPD.loc[GPD['Country Name'] == 'Iran, Islamic Rep.', 'Country Name'] = "Iran"
	GPD.loc[GPD['Country Name'] == 'Hong Kong SAR, China', 'Country Name'] = "Hong Kong"

	GPD.rename(columns={'Country Name':'Country'}, inplace = True)
	GPD = GPD[['Country','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015']] 
	GPD.dropna(how='all', inplace=True)

	ScimEn = pd.read_excel('/home/sebastian/Documentos/Python Michigan/course1_downloads/course1_downloads/scimagojr-3.xlsx')
	ScimEn.dropna(how='all', inplace=True)
	ScimEn = ScimEn.loc[ScimEn['Rank']<=15]

	firt_merge = GPD.merge(
		energy,
		on = 'Country',
		how = 'inner')

	result = firt_merge.merge(
		ScimEn,
		on = 'Country',
		how = 'inner')	

	result = result.loc[ScimEn['Rank']<=15]
	result = result.set_index('Country')
	return result	
answer_one()

#-----------Shape2-----------------
'''Question 1 (20%)
Load the energy data from the file Energy Indicators.xls, which is a list of indicators of energy supply 
and renewable electricity production from the United Nations for the year 2013, and should be put into a 
DataFrame with the variable name of energy.
Keep in mind that this is an Excel file, and not a comma separated values file. Also, make sure to exclude 
the footer and header information from the datafile. The first two columns are unneccessary, so you should 
get rid of them, and you should change the column labels so that the columns are:
['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']
Convert Energy Supply to gigajoules (there are 1,000,000 gigajoules in a petajoule). For all countries which 
have missing data (e.g. data with "...") make sure this is reflected as np.NaN values.
Rename the following list of countries (for use in later questions):
"Republic of Korea": "South Korea",
"United States of America": "United States",
"United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
"China, Hong Kong Special Administrative Region": "Hong Kong"
There are also several countries with numbers and/or parenthesis in their name. Be sure to remove these,
e.g.
'Bolivia (Plurinational State of)' should be 'Bolivia',
'Switzerland17' should be 'Switzerland'.
Next, load the GDP data from the file world_bank.csv, which is a csv containing countries' GDP from 1960 to 
2015 from World Bank. Call this DataFrame GDP.
Make sure to skip the header, and rename the following list of countries:
"Korea, Rep.": "South Korea", 
"Iran, Islamic Rep.": "Iran",
"Hong Kong SAR, China": "Hong Kong"
Finally, load the Sciamgo Journal and Country Rank data for Energy Engineering and Power Technology from 
the file scimagojr-3.xlsx, which ranks countries based on their journal contributions in the aforementioned 
area. Call this DataFrame ScimEn.
Join the three datasets: GDP, Energy, and ScimEn into a new dataset (using the intersection of country names). 
Use only the last 10 years (2006-2015) of GDP data and only the top 15 countries by Scimagojr 
'Rank' (Rank 1 through 15).
The index of this DataFrame should be the name of the country, and the columns should be 
['Rank', 'Documents', 'Citable documents', 'Citations', 'Self-citations', 'Citations per document', 
'H index', 'Energy Supply', 'Energy Supply per Capita', '% Renewable', '2006', '2007', '2008', '2009', 
'2010', '2011', '2012', '2013', '2014', '2015'].
This function should return a DataFrame with 20 columns and 15 entries.'''

import pandas as pd
def Energy():
	energy = pd.read_excel(
		'PythonMichigan/course1_downloads/course1_downloads/Energy Indicators.xls',
		skiprows = 17, 
		skip_footer = (38), 
		usecols = [2,3,4,5],
		names = ['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable'],
		na_values = ['...']
	) 

	energy['Energy Supply'] = energy['Energy Supply']*10**6
	energy['Country'] = energy['Country'].str.replace(r" *\(.*\)","")
	energy['Country'] = energy['Country'].str.replace(r"([0-9]+)","")
	energy.loc[energy['Country'] == 'Republic of Korea', 'Country'] = "South Korea"
	energy.loc[energy['Country'] == 'United States of America', 'Country'] = "United States"
	energy.loc[energy['Country'] == 'United Kingdom of Great Britain and Northern Ireland', 'Country'] = "United Kingdom"
	energy.loc[energy['Country'] == 'China, Hong Kong Special Administrative Region', 'Country'] = "Hong Kong"
	energy.dropna(how='all',inplace=True)
	return energy

def Gpd():
	GPD = pd.read_csv(
		'PythonMichigan/course1_downloads/course1_downloads/world_bank.csv', 
		skiprows=4)
	GPD.loc[GPD['Country Name'] == 'Korea, Rep.', 'Country Name'] = "South Korea"
	GPD.loc[GPD['Country Name'] == 'Iran, Islamic Rep.', 'Country Name'] = "Iran"
	GPD.loc[GPD['Country Name'] == 'Hong Kong SAR, China', 'Country Name'] = "Hong Kong"

	GPD.rename(columns={'Country Name':'Country'}, inplace = True)
	GPD = GPD[['Country','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015']] 
	GPD.dropna(how='all', inplace=True)
	return GPD

def Scimen():
	ScimEn = pd.read_excel('PythonMichigan/course1_downloads/course1_downloads/scimagojr-3.xlsx')
	ScimEn.dropna(how='all', inplace=True)
	return ScimEn

def answer_one():
	energy, GPD, ScimEn = Energy(), Gpd(), Scimen()

	result = pd.merge(ScimEn, energy, how='inner', left_on='Country', right_on='Country')
	result = pd.merge(result, GPD, how='inner', left_on='Country', right_on='Country')
	
	result = result[result['Rank']<=15]
	result.set_index('Country', inplace=True)
	return result	
answer_one()

'''The previous question joined three datasets then reduced this to just the top 15 entries. When you joined
 the datasets, but before you reduced this to the top 15 items, how many entries did you lose? This function 
 should return a single number.'''
	
def answer_two():
	energy, GPD, ScimEn = Energy(), Gpd(), Scimen()

	inner = pd.merge(ScimEn, energy, how='inner', left_on='Country', right_on='Country')
	inner = pd.merge(inner, GPD, how='inner', left_on='Country', right_on='Country')

	outer = pd.merge(ScimEn, energy, how='outer', left_on='Country', right_on='Country')
	outer = pd.merge(outer, GPD, how='outer', left_on='Country', right_on='Country')

	return  len(outer) -len(inner)
answer_two()

'''What is the average GDP over the last 10 years for each country? (exclude missing values from this 
calculation.) This function should return a Series named avgGDP with 15 countries and their average GDP 
sorted in descending order.'''

def answer_three():
	import numpy as np
	Top15 = answer_one()
	Top15['avgGDP'] = Top15[np.arange(2006, 2016).astype(str)].mean(axis=1)
	Top15.sort_values(by='avgGDP',ascending=False,inplace=True)
	return Top15['avgGDP']
answer_three()

'''By how much had the GDP changed over the 10 year span for the country with the 6th largest average GDP?
This function should return a single number.'''

def answer_four():
	index = answer_three().index[5]
	Top15 = answer_one()
	return Top15.loc[index, '2015'] - Top15.loc[index, '2006']
answer_four()	

'''What is the mean Energy Supply per Capita? This function should return a single number'''

def answer_five():
	Top15 = answer_one()['Energy Supply per Capita'].mean()
	return Top15
answer_five()

'''What country has the maximum % Renewable and what is the percentage? 
This function should return a tuple with the name of the country and the percentage'''

def answer_six():
	Top15 = answer_one()
	maxR = Top15['% Renewable'].max()
	country = Top15[Top15['% Renewable']==maxR].index[0]
	return country, maxR
answer_six()

'''Create a new column that is the ratio of Self-Citations to Total Citations. What is the maximum value 
for this new column, and what country has the highest ratio? This function should return a tuple with the 
name of the country and the ratio.'''
  
def answer_seven():
	Top15 = answer_one()
	Top15['ratio'] = Top15['Self-citations'] / Top15['Citations']
	maxR = Top15['ratio'].max()
	country = Top15[Top15['ratio']==maxR].index[0]
	return country, maxR
answer_seven()

'''Create a column that estimates the population using Energy Supply and Energy Supply per capita. What is 
the third most populous country according to this estimate? This function should return a single string value.'''

def answer_eight():
	Top15 = answer_one()
	Top15['Population'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
	Top15.sort_values(by='Population',ascending=False, inplace=True)
	return Top15.index[2]
answer_eight()

'''Create a column that estimates the number of citable documents per person. What is the correlation
between the number of citable documents per capita and the energy supply per capita? Use the .corr() method,
(Pearson's correlation). This function should return a single number.
(Optional: Use the built-in function plot9() to visualize the relationship between Energy Supply per Capita
vs. Citable docs per Capita)'''

def answer_nine():
	Top15 = answer_one()
	Top15['Population'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
	Top15['Citable docs per Capita'] = Top15['Citable documents'] / Top15['Population']
	corr = Top15[['Citable docs per Capita','Energy Supply per Capita']].corr()
	#data = Top15[['Citable docs per Capita','Energy Supply per Capita']]
	#correlation = data.corr(method='pearson')
	return corr.iloc[0,1]
answer_nine()

def plot9():
	import matplotlib
	#%matplotlib inline
	#matplotlib.use('TkAgg')
	import matplotlib.pyplot as plt
	plt.style.use('dark_background')
	Top15 = answer_one()
	Top15['PopEst'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
	Top15['Citable docs per Capita'] = Top15['Citable documents'] / Top15['PopEst']
	Top15.plot(x='Citable docs per Capita', y='Energy Supply per Capita', kind='scatter', 
	s=100,c=10, xlim=[0, 0.0006])
	plt.show()
	#plt.savefig('/mnt/d/SebasUbuntu/Documentos/Graficas/plot.png')
	plt.savefig('/mnt/d/SebasUbuntu/Documentos/Graficas/plot1.pdf')
	return Top15.index[2]
plot9()

'''Create a new column with a 1 if the country's % Renewable value is at or above the median for all 
countries in the top 15, and a 0 if the country's % Renewable value is below the median.
This function should return a series named HighRenew whose index is the country name sorted in ascending 
order of rank.'''

def answer_ten():
	Top15 = answer_one()
	Top15['HighRenew'] = 0 
	Top15.loc[Top15['% Renewable']>=Top15['% Renewable'].median(),'HighRenew'] = 1 
	return Top15['HighRenew']

answer_ten()

'''Use the following dictionary to group the Countries by Continent, then create a dateframe that displays 
the sample size 
(the number of countries in each continent bin), and the sum, mean, and std deviation for the estimated
 population of 
each country.'''

ContinentDict  = {'China':'Asia', 'United States':'North America', 'Japan':'Asia', 'United Kingdom':'Europe', 
'Russian Federation':'Europe', 
'Canada':'North America', 'Germany':'Europe', 'India':'Asia','France':'Europe', 'South Korea':'Asia', 'Italy':'Europe', 
'Spain':'Europe', 'Iran':'Asia','Australia':'Australia', 'Brazil':'South America'}
This function should return a DataFrame with index named Continent ['Asia', 'Australia', 'Europe', 'North America',
'South America'] and columns ['size', 'sum', 'mean', 'std']

def answer_eleven():
	import pandas as pd
	import numpy as np
	Top15 = answer_one()
	Top15['PopEst'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
	continent = pd.Series({'China':'Asia', 
					'United States':'North America', 
					'Japan':'Asia', 
					'United Kingdom':'Europe', 
					'Russian Federation':'Europe', 
					'Canada':'North America', 
					'Germany':'Europe', 
					'India':'Asia',
					'France':'Europe', 
					'South Korea':'Asia', 
					'Italy':'Europe', 
					'Spain':'Europe', 
					'Iran':'Asia',
					'Australia':'Australia', 
					'Brazil':'South America'}, name='Continent').to_frame()

	df = pd.merge(Top15, continent, how='inner', left_index=True, right_index=True)
	group = df.groupby('Continent')['PopEst'].agg({'sum': np.sum,'mean': np.mean, 'std':np.std})
	group['size'] = df.groupby('Continent')['Rank'].count()
	group = group.astype(np.float64)
	return group

answer_eleven()

'''Cut % Renewable into 5 bins. Group Top15 by the Continent, as well as these new % Renewable bins. 
How many countries are in each of these groups?
This function should return a Series with a MultiIndex of Continent, then the bins for % Renewable. 
Do not include groups with no countries.'''

def answer_twelve():
	import pandas as pd
	Top15 = answer_one()

	Top15['bin'] = pd.cut(Top15['% Renewable'], 5)

	continent = pd.Series({'China':'Asia', 
					'United States':'North America', 
					'Japan':'Asia', 
					'United Kingdom':'Europe', 
					'Russian Federation':'Europe', 
					'Canada':'North America', 
					'Germany':'Europe', 
					'India':'Asia',
					'France':'Europe', 
					'South Korea':'Asia', 
					'Italy':'Europe', 
					'Spain':'Europe', 
					'Iran':'Asia',
					'Australia':'Australia', 
					'Brazil':'South America'}, name='Continent').to_frame()


	df = pd.merge(Top15, continent, how='inner', left_index=True, right_index=True)
	df['bin']= pd.Categorical(df['bin'],categories=[
		'(2.212, 15.753]','(15.753, 29.227]','(29.227, 42.701]','(56.174, 69.648]' 
	], ordered=True)
	group = df.groupby(['Continent','bin'])['Rank'].count().dropna()
	return group

answer_twelve()

'''Convert the Population Estimate series to a string with thousands separator (using commas). Do not round 
the results.e.g. 317615384.61538464 -> 317,615,384.61538464
This function should return a Series PopEst whose index is the country name and whose values are the 
population estimate string.'''

def answer_thirteen():
	Top15 = answer_one()
	Top15['PopEst'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
	Top15['PopEst'] = Top15['PopEst'].map('{:,}'.format)
	return Top15['PopEst']

answer_thirteen()

'''Use the built in function plot_optional() to see an example visualization.'''
def plot_optional():
	import matplotlib as plt
	import matplotlib.pyplot as plt
	#%matplotlib inline
	Top15 = answer_one()
	plt.style.use('bmh')
	ax = Top15.plot(x='Rank', y='% Renewable', kind='scatter', 
					c=['#e41a1c','#377eb8','#e41a1c','#4daf4a','#4daf4a','#377eb8','#4daf4a','#e41a1c',
						'#4daf4a','#e41a1c','#4daf4a','#4daf4a','#e41a1c','#dede00','#ff7f00'], 
					xticks=range(1,16), s=6*Top15['2014']/10**10, alpha=1, figsize=[16,6]);
	
	for i, txt in enumerate(Top15.index):
		ax.annotate(txt, [Top15['Rank'][i], Top15['% Renewable'][i]], ha='center')

	print("This is an example of a visualization that can be created to help understand the data. \
	This is a bubble chart showing % Renewable vs. Rank. The size of the bubble corresponds to the countries' \
	2014 GDP, and the color corresponds to the continent.")
	plt.savefig('/mnt/d/SebasUbuntu/Documentos/Graficas/plot2.pdf')
plot_optional()

result.loc[result['Country'].isna()]   

result.loc[result['Country'].isna()]
result.loc[result['Country'].isna()]
result['Country'].isna().any() 
result['Country'].isna().all()
result.loc[~result['Country'].duplicated()]
result.loc[~result['Country'].isna()] 


import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://www.scimagojr.com/countryrank.php?category=2102'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('body')
	
with open('/home/sebastian/Documentos/Python Michigan/course1_downloads/course1_downloads/table.html', 'w') as file:
	file.write(str(tags[0]))

t = pd.read_html('/home/sebastian/Documentos/Python Michigan/course1_downloads/course1_downloads/table.html')

#-----------------------------WEEK 4-----------------------------------------
#----------------------------------------------------------------------------
Suppose we want to simulate the probability of flipping a fair coin 20 times, and getting a number greater than or equal 
to 15. Use np.random.binomial(n, p, size) to do 10000 simulations of flipping a fair coin 20 times, then see what 
proportion of the simulations are 15 or greater.

'''Returns a DataFrame of towns and the states they are in from the 
university_towns.txt list. The format of the DataFrame should be:
DataFrame( [ ["Michigan", "Ann Arbor"], ["Michigan", "Yipsilanti"] ], 
columns=["State", "RegionName"]  )
    
The following cleaning needs to be done:

1. For "State", removing characters from "[" to the end.
2. For "RegionName", when applicable, removing every character from " (" to the end.
3. Depending on how you read the data, you may need to remove newline character '\n'. '''
    
def get_list_of_university_towns():
	import pandas as pd
	import re
	rute = 'PythonMichigan/course1_downloads/course1_downloads/university_towns.txt'	
	with open(rute) as file:
		townslist = file.readlines()
	townslist = [x.rstrip() for x in townslist]
	townslist2 =[]
	for i in townslist:
		if '[edit]' in i:
			state_string = re.sub(r" *\(.*\)| *\[.*\]","",i)
		else:
			region_string  = re.sub(r" *\(.*\)| *\[.*\]","",i)
			townslist2.append([state_string,region_string])
	df = pd.DataFrame(townslist2, columns=['State','RegionName'])
	return df

get_list_of_university_towns()

######## Shape 2 ########
def get_list_of_university_towns():
	State = []
	RegionName = []

	with open ('PythonMichigan/course1_downloads/course1_downloads/university_towns.txt', "r") as fileObj:
		line = fileObj.readline().strip()

		while line != '':

			if line[-6:] == '[edit]':
				st = line[:-6]
			else:
				State.append(st)
				RegionName.append(line)

			line = fileObj.readline().strip()

	ut = pd.DataFrame(list(zip(State,RegionName)),columns=['State','RegionName'])
	ut.RegionName.replace(r" \([^(]*|\([^(]*","", inplace=True,regex = True) 

	return ut

get_list_of_university_towns()

'''Returns the year and quarter of the recession start time as a string value in a format such as 2005q3'''

def get_recession_start():
	import pandas as pd
	gdp = pd.read_excel(
		'PythonMichigan/course1_downloads/course1_downloads/gdplev.xls', 
		skiprows= 219)
	gdp = gdp[['1999q4', 12323.3]]
	gdp = gdp.rename(columns={'1999q4':'Quarter', 12323.3:'GDP in billions'})
	for i in range(0,gdp.shape[0]-1):
		if (gdp.iloc[i-2][1]> gdp.iloc[i-1][1]) and (gdp.iloc[i-1][1]> gdp.iloc[i][1]):
			startdate = gdp.iloc[i-3][0]
	return  startdate

get_recession_start()

def GDP():
	import pandas as pd
	gdp = pd.read_excel(
				io='PythonMichigan/course1_downloads/course1_downloads/gdplev.xls',
				header = None,
				names = ['Quater','GDP'],
				usecols = [4,6],
				skiprows = 8,
			)
    
	gdp['GDP change'] = gdp['GDP'].diff()
	gdp['change'] = 'increase' 
	gdp.loc[gdp['GDP change']<=0,'change'] = 'decline'
	gdp = gdp[gdp['Quater']>='2000q1']

	return gdp
gdp = GDP()

gdp[gdp.change=='decline']

'''Returns the year and quarter of the recession end time as a string value in a format such as 2005q3'''

def get_recession_end():
	import pandas as pd
	gdplev = pd.ExcelFile('PythonMichigan/course1_downloads/course1_downloads/gdplev.xls')
	gdplev = gdplev.parse("Sheet1", skiprows=219)
	gdplev = gdplev[['1999q4', 9926.1]]
	gdplev.columns = ['Quarter','GDP']
	start = get_recession_start()
	start_index = gdplev[gdplev['Quarter'] == start].index.tolist()[0]
	gdplev = gdplev.iloc[start_index:]
	for i in range(2, len(gdplev)):
		if (gdplev.iloc[i-2][1] < gdplev.iloc[i-1][1]) and (gdplev.iloc[i-1][1] < gdplev.iloc[i][1]):
			return gdplev.iloc[i][0]

get_recession_end()

'''Returns the year and quarter of the recession bottom time as a string value in a format such as 2005q3'''

def get_recession_bottom():
	import pandas as pd
	gdplev = pd.ExcelFile('PythonMichigan/course1_downloads/course1_downloads/gdplev.xls')
	gdplev = gdplev.parse("Sheet1", skiprows=219)
	gdplev = gdplev[['1999q4', 9926.1]]
	gdplev.columns = ['Quarter','GDP']
	start = get_recession_start()
	start_index = gdplev[gdplev['Quarter'] == start].index.tolist()[0]

	end = get_recession_end()
	end_index = gdplev[gdplev['Quarter'] == end].index.tolist()[0]

	gdp = gdplev.iloc[start_index:end_index+1]
	bottom = gdp['GDP'].min()
	bottom_index = gdp[gdp["GDP"]== bottom].index.tolist()[0]-start_index

	return gdp.iloc[bottom_index]['Quarter']

get_recession_bottom()

'''Converts the housing data to quarters and returns it as mean 
values in a dataframe. This dataframe should be a dataframe with
columns for 2000q1 through 2016q3, and should have a multi-index
in the shape of ["State","RegionName"].

Note: Quarters are defined in the assignment description, they are
not arbitrary three month periods.

The resulting dataframe should have 67 columns, and 10,730 rows.'''

def convert_housing_data_to_quarters():
	import pandas as pd 
	house = pd.read_csv(
		'PythonMichigan/course1_downloads/course1_downloads/City_Zhvi_AllHomes.csv',header = 0)

	a = list(range(3,51))
	house.drop(house.columns[a],axis=1,inplace=True)
	house.drop(house.columns[0],axis=1,inplace=True)

	states = {'OH': 'Ohio', 'KY': 'Kentucky', 'AS': 'American Samoa', 'NV': 'Nevada', 'WY': 'Wyoming', 'NA': 'National', 
	'AL': 'Alabama', 'MD': 'Maryland', 'AK': 'Alaska', 'UT': 'Utah', 'OR': 'Oregon', 'MT': 'Montana', 'IL': 'Illinois', 
	'TN': 'Tennessee', 'DC': 'District of Columbia', 'VT': 'Vermont', 'ID': 'Idaho', 'AR': 'Arkansas', 'ME': 'Maine', 
	'WA': 'Washington', 'HI': 'Hawaii', 'WI': 'Wisconsin', 'MI': 'Michigan', 'IN': 'Indiana', 'NJ': 'New Jersey', 
	'AZ': 'Arizona', 'GU': 'Guam', 'MS': 'Mississippi', 'PR': 'Puerto Rico', 'NC': 'North Carolina', 'TX': 'Texas', 
	'SD': 'South Dakota', 'MP': 'Northern Mariana Islands', 'IA': 'Iowa', 'MO': 'Missouri', 'CT': 'Connecticut', 
	'WV': 'West Virginia', 'SC': 'South Carolina', 'LA': 'Louisiana', 'KS': 'Kansas', 'NY': 'New York', 'NE': 'Nebraska', 
	'OK': 'Oklahoma', 'FL': 'Florida', 'CA': 'California', 'CO': 'Colorado', 'PA': 'Pennsylvania', 'DE': 'Delaware', 
	'NM': 'New Mexico', 'RI': 'Rhode Island', 'MN': 'Minnesota', 'VI': 'Virgin Islands', 'NH': 'New Hampshire', 
	'MA': 'Massachusetts', 'GA': 'Georgia', 'ND': 'North Dakota', 'VA': 'Virginia'}

	house.replace({'State':states}, inplace = True)
	house.set_index(['State','RegionName'],inplace = True)
	house = house.groupby(pd.PeriodIndex(house.columns, freq='Q'), axis=1).mean()

	return house
convert_housing_data_to_quarters()

'''First creates new data showing the decline or growth of housing prices
between the recession start and the recession bottom. Then runs a ttest
comparing the university town values to the non-university towns values, 
return whether the alternative hypothesis (that the two groups are the same)
is true or not as well as the p-value of the confidence. 

Return the tuple (different, p, better) where different=True if the t-test is
True at a p<0.01 (we reject the null hypothesis), or different=False if 
otherwise (we cannot reject the null hypothesis). The variable p should
be equal to the exact p value returned from scipy.stats.ttest_ind(). The
value for better should be either "university town" or "non-university town"
depending on which has a lower mean price ratio (which is equivilent to a
reduced market loss).'''

def run_ttest():
	import numpy as np
	from scipy import stats
	start = pd.Period(get_recession_start())
	bottom = pd.Period(get_recession_bottom())
	house = convert_housing_data_to_quarters().loc[:,[start,bottom]]
	house.columns = ["Start","Bottom"]
	house["Ratio"] = house.Start / house.Bottom #NAN不用处理，反正数据不使用
	house = house.dropna(axis = 0, how = "any")
	collage = get_list_of_university_towns().set_index(["State","RegionName"])
	collage["isUnv"] = "Yes"
	res = pd.merge(house,collage,how="left",left_index=True,right_index=True)
	res.isUnv = res.isUnv.fillna("No")

	res_u = res[res.isUnv == "Yes"].Ratio
	res_n = res[res.isUnv == "No"].Ratio
	#print(res_n)
	_,p = stats.ttest_ind(res_u,res_n)
	different = (True if p < 0.01 else False)
	better = ("university town" if np.nanmean(res_u) < np.nanmean(res_n) else "non-university town")
	return different, p, better
run_ttest()

#---------------------------------------------------------------------
#---------------------------------------------------------------------
##### Applied Plotting, Charting & Data Representation in Python  ####
#---------------------------------------------------------------------
#---------------------------------------------------------------------

'''Applied Plotting, Charting & Data Representation in Python'''

Language	% Popularity
Python	      56
SQL	          39
Java          34
C++	          34
JavaScript	  29

#---------------------------------------------------------------------
'''Here's some sample code which has the ticks, can you figure out how to remove them?
Press run to see the generated image, and press continue to see my solution.
Task: Remove all the ticks (both axes), and tick labels on the Y axis.'''

import matplotlib.pyplot as plt
import numpy as np

plt.figure()
languages =['Python', 'SQL', 'Java', 'C++', 'JavaScript']
pos = np.arange(len(languages))
popularity = [56, 39, 34, 34, 29]
plt.bar(pos, popularity, align='center')
plt.xticks(pos, languages)
plt.ylabel('% Popularity')
plt.title('Top 5 Languages for Math & Data \nby % popularity on Stack Overflow', alpha=0.8)
#TODO: remove all the ticks (both axes), and tick labels on the Y axis
plt.savefig('/mnt/d/SebasUbuntu/Documentos/Graficas/LanguagesP.png')
#plt.show()

############ SOLUTION #############

import matplotlib.pyplot as plt
import numpy as np

plt.figure()

languages =['Python', 'SQL', 'Java', 'C++', 'JavaScript']
pos = np.arange(len(languages))
popularity = [56, 39, 34, 34, 29]
plt.bar(pos, popularity, align='center')
plt.xticks(pos, languages)
plt.ylabel('% Popularity')
plt.title('Top 5 Languages for Math & Data \nby % popularity on Stack Overflow', alpha=0.8)
# remove all the ticks (both axes), and tick labels on the Y axis
plt.tick_params(top=False, bottom=False, left=False, right=False, labelleft=False, labelbottom=False)
plt.savefig('/mnt/d/SebasUbuntu/Documentos/Graficas/LanguagesP(S).png')
#plt.show()

#---------------------------------------------------------------------
'''Task: Remove the frame of the chart.'''

############ SOLUTION #############
import matplotlib.pyplot as plt
import numpy as np

plt.figure()

languages =['Python', 'SQL', 'Java', 'C++', 'JavaScript']
pos = np.arange(len(languages))
popularity = [56, 39, 34, 34, 29]
plt.bar(pos, popularity, align='center')
plt.xticks(pos, languages)
plt.ylabel('% Popularity')
plt.title('Top 5 Languages for Math & Data \nby % popularity on Stack Overflow', alpha=0.8)
# remove all the ticks (both axes), and tick labels on the Y axis
plt.tick_params(top=False, bottom=False, left=False, right=False, labelleft=False, labelbottom=False)
#Remove the frame of the chart.
for spine in plt.gca().spines.values():
	spine.set_visible(False)
plt.savefig('/mnt/d/SebasUbuntu/Documentos/Graficas/LanguagesP(chart).png')
#plt.show()

#---------------------------------------------------------------------
'''Task: Change the bar colors to be less bright blue, make one bar, the python bar, a contrasting color, 
soften all labels by turning grey.'''

############ SOLUTION #############
import matplotlib.pyplot as plt
import numpy as np

plt.figure()

languages =['Python', 'SQL', 'Java', 'C++', 'JavaScript']
pos = np.arange(len(languages))
popularity = [56, 39, 34, 34, 29]
#color = ['#43053c', '#ffcb32', '#3932ff', '#dec79b', '#dec79b']
plt.bar(pos, popularity, align='center', color=['#43053c', '#ffcb32', '#3932ff', '#dec79b', '#35756a'] )
plt.xticks(pos, languages, color='grey')
plt.ylabel('% Popularity', color='grey')
plt.title('Top 5 Languages for Math & Data \nby % popularity on Stack Overflow', alpha=0.8, color='grey')
# remove all the ticks (both axes), and tick labels on the Y axis
plt.tick_params(top=False, bottom=False, left=False, right=False, labelleft=True, labelbottom=True)
#Remove the frame of the chart.
for spine in plt.gca().spines.values():
	spine.set_visible(False)
plt.savefig('/mnt/d/SebasUbuntu/Documentos/Graficas/LanguagesP(color).png')
#plt.show()


######## Shape 2 ########
import matplotlib.pyplot as plt
import numpy as np 

plt.figure()

languages =['Python', 'SQL', 'Java', 'C++', 'JavaScript']
pos = np.arange(len(languages))
popularity = [56, 39, 34, 34, 29]

# change the bar colors to be less bright blue
bars = plt.bar(pos, popularity, align='center', linewidth=0, color='lightslategrey')
# make one bar, the python bar, a contrasting color
bars[0].set_color('#1F77B4')

# soften all labels by turning grey
plt.xticks(pos, languages, alpha=0.8)
plt.ylabel('% Popularity', alpha=0.8)
plt.title('Top 5 Languages for Math & Data \nby % popularity on Stack Overflow', alpha=0.8)

# remove all the ticks (both axes), and tick labels on the Y axis
plt.tick_params(top=False, bottom=False, left=False, right=False, labelleft=True, labelbottom=True)
# remove the frame of the chart
for spine in plt.gca().spines.values():
	spine.set_visible(False)
plt.show()

plt.savefig('/mnt/d/SebasUbuntu/Documentos/Graficas/LanguagesP(color2).png')
#plt.show()

#---------------------------------------------------------------------
'''Task: Directly label each bar with Y axis values, and remove the Y label since bars are directly 
labeled.'''
import matplotlib.pyplot as plt
import numpy as np

plt.figure()

languages =['Python', 'SQL', 'Java', 'C++', 'JavaScript']
pos = np.arange(len(languages))
popularity = [56, 39, 34, 34, 29]

# change the bar color to be less bright blue
bars = plt.bar(pos, popularity, align='center', linewidth=0, color='lightslategrey')
# make one bar, the python bar, a contrasting color
bars[0].set_color('#1F77B4')

# soften all labels by turning grey
plt.xticks(pos, languages, alpha=0.8)
# remove the Y label since bars are directly labeled
#plt.ylabel('% Popularity', alpha=0.8)
plt.title('Top 5 Languages for Math & Data \nby % popularity on Stack Overflow', alpha=0.8)

# remove all the ticks (both axes), and tick labels on the Y axis
plt.tick_params(top=False, bottom=False, left=False, right=False, labelleft=False, labelbottom=True)

# remove the frame of the chart
for spine in plt.gca().spines.values():
	spine.set_visible(False)

# direct label each bar with Y axis values
for bar in bars:
	plt.gca().text(bar.get_x() + bar.get_width()/2, bar.get_height() - 5, str(int(bar.get_height())) + '%', 
	ha='center', color='w', fontsize=11)

plt.savefig('/mnt/d/SebasUbuntu/Documentos/Graficas/LanguagesP(%porcentaje2).png')
#plt.show()

#---------------------------------------------------------------------
'''Assignment 2
Before working on this assignment please read these instructions fully. In the submission area, you will notice that you can click the link to Preview the Grading for each step of the assignment. This is the criteria that will be used for peer grading. Please familiarize yourself with the criteria before beginning the assignment.

An NOAA dataset has been stored in the file data/C2A2_data/BinnedCsvs_d400/fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89.csv. This is the dataset to use for this assignment. Note: The data for this assignment comes from a subset of The National Centers for Environmental Information (NCEI) Daily Global Historical Climatology Network (GHCN-Daily). The GHCN-Daily is comprised of daily climate records from thousands of land surface stations across the globe.

Each row in the assignment datafile corresponds to a single observation.

The following variables are provided to you:

id : station identification code
date : date in YYYY-MM-DD format (e.g. 2012-01-24 = January 24, 2012)
element : indicator of element type
TMAX : Maximum temperature (tenths of degrees C)
TMIN : Minimum temperature (tenths of degrees C)
value : data value for element (tenths of degrees C)
For this assignment, you must:

Read the documentation and familiarize yourself with the dataset, then write some python code which returns a line graph of the record high and record low temperatures by day of the year over the period 2005-2014. The area between the record high and record low temperatures for each day should be shaded.
Overlay a scatter of the 2015 data for any points (highs and lows) for which the ten year record (2005-2014) record high or record low was broken in 2015.
Watch out for leap days (i.e. February 29th), it is reasonable to remove these points from the dataset for the purpose of this visualization.
Make the visual nice! Leverage principles from the first module in this course when developing your solution. Consider issues such as legends, labels, and chart junk.
The data you have been given is near Ann Arbor, Michigan, United States, and the stations the data comes from are shown on the map below.'''