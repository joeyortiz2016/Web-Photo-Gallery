import cgi
import pymysql

db = pymysql.connect(host = 'localhost', user = 'gallery', passwd = 'eecs118',
                     db = 'gallery')
cur = db.cursor()
form = cgi.FieldStorage()

artist = form.getvalue("a_id")
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
        #top{
            text-decoration: underline;
        }
        #add{
            position: absolute;
            top: 175px;
        }
        h3{
            text-decoration: underline;
        }
    </style>
</head>
<body>
<h1 id='top'>Artist Details</h1>
""")

if (form.getvalue("modify") != None):
    sql = "UPDATE artist SET name ='"+str(form.getvalue("a_name"))+"' WHERE artist_id="+str(artist)
    cur.execute(sql)
    sql = "UPDATE artist SET birth_year ='"+str(form.getvalue("a_year"))+"' WHERE artist_id="+str(artist)
    cur.execute(sql)
    sql = "UPDATE artist SET country ='"+str(form.getvalue("a_country"))+"' WHERE artist_id="+str(artist)
    cur.execute(sql)
    sql = "UPDATE artist SET description ='"+str(form.getvalue("a_description"))+"' WHERE artist_id="+str(artist)
    cur.execute(sql)
    db.commit()
    


sql = "SELECT * FROM artist WHERE artist_id="+str(artist)
cur.execute(sql)
print("<p>")
for row in cur.fetchall():
    print("Artist ID: "+str(row[0]) +"<br>")
    print("Artist Name: "+str(row[1]) +"<br>")
    print("Artist Birth Year: "+str(row[2]) +"<br>")
    print("Artist Country: "+str(row[3]) +"<br>")
    print("Artist Description: "+str(row[4]) +"<br>")

print("</p")

print("""
<div id='form'>
    <h3>Modify Artist details here!</h3>
    <form id='add' action='/test/cgi-bin/artist.py' method='post'>
""")
print("<input name='a_id' type='hidden' size='11' value='"+str(artist)+"'><br>")
print("""
        <input name='modify' type='hidden' value='yes'><br>
        Name :<input name='a_name' type='text' size='45'><br>
        Birth Year :<input name='a_year' type='text' size='11'><br>
        Country :<input name='a_country' type='text' size='45'><br>
        Description :<input name='a_description' type='text' size='45'><br>
        <input type='submit' value='Modify Artist'>
    </form>
</div>

""")


print("</body")
print("</html")
