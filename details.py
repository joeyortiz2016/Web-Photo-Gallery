import cgi
import pymysql

db = pymysql.connect(host = 'localhost', user = 'gallery', passwd = 'eecs118',
                     db = 'gallery')
cur = db.cursor()
form = cgi.FieldStorage()

image = form.getvalue("i_link")
artist = form.getvalue("a_id")
detail = form.getvalue("d_id")


print("Content-Type: text/html\n\n")
print("""
<html>
<title>Image Details</title>
<head>
    <style>
        title{
            font-family: "Lucida Console", serif;
        }
        body{
            font-family: "Lucida Console", serif;
        }
    </style>
</head>
<body>
<h1 id='top'>Image Details</h1>
""")

print("<a target='_blank' href='"+str(image)+"'>")
print("<img src='"+str(image)+"' alt='oof' width='900' height='750'>")
print("</a>")
print("<br>")
sql = "SELECT * FROM detail WHERE detail_id="+str(detail)
cur.execute(sql)
print("<p>")
row = cur.fetchone()
print("Year: "+str(row[2]) + "<br>")
print("Type: "+str(row[3]) + "<br>")
print("Width: "+str(row[4]) + "<br>")
print("Height: "+str(row[5]) + "<br>")
print("Location: "+str(row[6]) + "<br>")
print("Description: "+str(row[7]) + "<br>")
sql = "SELECT name FROM artist WHERE artist_id="+str(artist)
cur.execute(sql)
row = cur.fetchone()
print("<a target='_blank' href='/test/cgi-bin/artist.py?a_id="+str(artist)+"'>")
print("Artist: " + str(row[0]) + "<br>")
print("</a>")
print("</p>")
print("""
</body>
</html>
""")
