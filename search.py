import pymysql
import cgi

db = pymysql.connect(host = 'localhost', user = 'gallery', passwd = 'eecs118',
                     db = 'gallery')
cur = db.cursor()

form = cgi.FieldStorage()


print("Content-Type: text/html\n\n")

print("""
<html>
<title>Search Functions</title>
<head>
    <style>
        body{
            font-family: "Lucida Console", serif;
            font-size: 14;
        }
        h3{
            text-decoration:underline;
        }
        div.gallery{
            margin: auto;
            margin-top 15px;
        }
        #form1{
            position: absolute;
            right: 20px;
        }
        #form2{
            position: absolute;
            right: 20px;
            top: 200px;
        }
        #form3{
            position: absolute;
            right: 20px;
            top: 350px;
        }
        #form4{
            position: absolute;
            right: 20px;
            top: 500px;
        }
        #form5{
            position: absolute;
            right: 20px;
            top: 650px;
        }
        #form6{
            position: absolute;
            right: 20px;
            top: 800px;
        }
        
    </style>
</head>

<body>
<h1 id='top'>Search Functions</h1>
""")
print("</body>")
        
    

print("""
<body>
<div id='form1'>
    <h3>Find the images by type:</h3>
    <form action='/test/cgi-bin/search.py' method=post>
        Image Type:<input name='type' type='text' size ='10'><br>
        <input type='submit' value='Search for images'>
    </form>
</div>

<div id='form2'>
    <h3>Find the images by year range:</h3>
    <form action='/test/cgi-bin/search.py' method=post>
        From Year:<input name='f_year' type='text' size ='4'><br>
        To Year:<input name='t_year' type='text' size = '4'><br>
        <input type='submit' value='Search for images'>
    </form>
</div>

<div id='form3'>
    <h3>Find the images by artist name:</h3>
    <form action='/test/cgi-bin/search.py' method=post>
        Artist Name:<input name='a_name' type='text' size ='45'><br>
        <input type='submit' value='Search for images'>
    </form>
</div>

<div id='form4'>
    <h3>Find the images by location:</h3>
    <form action='/test/cgi-bin/search.py' method=post>
        Location:<input name='location' type='text' size ='45'><br>
        <input type='submit' value='Search for images'>
    </form>
</div>

<div id='form5'>
    <h3>Find the artists by country:</h3>
    <form action='/test/cgi-bin/search.py' method=post>
        Artist Country:<input name='a_country' type='text' size ='45'><br>
        <input type='submit' value='Search for artists'>
    </form>
</div>

<div id='form6'>
    <h3>Find the artists by birth year:</h3>
    <form action='/test/cgi-bin/search.py' method=post>
        Artist Birth Year:<input name='a_year' type='text' size ='4'><br>
        <input type='submit' value='Search for artists'>
    </form>
</div>
""")

if(form.getvalue("type") != None):
    sql = "SELECT * FROM image WHERE image_id IN (SELECT image_id FROM detail WHERE type = '"+str(form.getvalue("type"))+"')"
    cur.execute(sql)
    for row in cur.fetchall():
        print("<div class='gallery'>")
        print("<a target='_blank' href='/test/cgi-bin/details.py?d_id="+str(row[5])+"&a_id="+str(row[4])+"&i_link="+str(row[2])+"'>")
        print("Title: '" + str(row[1]) + "'")
        print("</a><br>")
        print("Image ID: '" + str(row[0]) +"'")
        print("<br>")
        print("<a target='_blank' href='" + str(row[2]) +"'>")
        print("<img src='" + str(row[2]) +"' alt='oof' width='600' height='400'>")
        print("</a>")
        print("</div>")

if((form.getvalue('f_year') != None) and (form.getvalue('t_year'))):
    a = "WHERE year >= "+str(form.getvalue('f_year'))+" AND year <= "+str(form.getvalue('t_year'))
    sql = "SELECT * FROM image WHERE image_id IN (SELECT image_id FROM detail "+a+")"
    cur.execute(sql)
    for row in cur.fetchall():
        print("<div class='gallery'>")
        print("<a target='_blank' href='/test/cgi-bin/details.py?d_id="+str(row[5])+"&a_id="+str(row[4])+"&i_link="+str(row[2])+"'>")
        print("Title: '" + str(row[1]) + "'")
        print("</a><br>")
        print("Image ID: '" + str(row[0]) +"'")
        print("<br>")
        print("<a target='_blank' href='" + str(row[2]) +"'>")
        print("<img src='" + str(row[2]) +"' alt='oof' width='600' height='400'>")
        print("</a>")
        print("</div>")
if(form.getvalue('a_name') != None):
    sql = "SELECT * FROM image WHERE artist_id IN (SELECT artist_id FROM artist WHERE name = '"+str(form.getvalue("a_name"))+"')"
    cur.execute(sql)
    for row in cur.fetchall():
        print("<div class='gallery'>")
        print("<a target='_blank' href='/test/cgi-bin/details.py?d_id="+str(row[5])+"&a_id="+str(row[4])+"&i_link="+str(row[2])+"'>")
        print("Title: '" + str(row[1]) + "'")
        print("</a><br>")
        print("Image ID: '" + str(row[0]) +"'")
        print("<br>")
        print("<a target='_blank' href='" + str(row[2]) +"'>")
        print("<img src='" + str(row[2]) +"' alt='oof' width='600' height='400'>")
        print("</a>")
        print("</div>")
if(form.getvalue('location') != None):
    sql = "SELECT * FROM image WHERE image_id IN (SELECT image_id FROM detail WHERE location = '"+str(form.getvalue("location"))+"')"
    cur.execute(sql)
    for row in cur.fetchall():
        print("<div class='gallery'>")
        print("<a target='_blank' href='/test/cgi-bin/details.py?d_id="+str(row[5])+"&a_id="+str(row[4])+"&i_link="+str(row[2])+"'>")
        print("Title: '" + str(row[1]) + "'")
        print("</a><br>")
        print("Image ID: '" + str(row[0]) +"'")
        print("<br>")
        print("<a target='_blank' href='" + str(row[2]) +"'>")
        print("<img src='" + str(row[2]) +"' alt='oof' width='600' height='400'>")
        print("</a>")
        print("</div>")
if(form.getvalue('a_country') != None):
    sql = "SELECT * FROM artist WHERE country = '"+str(form.getvalue('a_country'))+"'"
    cur.execute(sql)
    for row in cur.fetchall():
        print("<div class='gallery'>")
        print("Artist ID: "+str(row[0]) +"<br>")
        print("Artist Name: "+str(row[1]) +"<br>")
        print("Artist Birth Year: "+str(row[2]) +"<br>")
        print("Artist Country: "+str(row[3]) +"<br>")
        print("Artist Description: "+str(row[4]) +"<br>")
        print("<br><br>")
        print("</div>")
if(form.getvalue('a_year') != None):
    sql = "SELECT * FROM artist WHERE birth_year = '"+str(form.getvalue('a_year'))+"'"
    cur.execute(sql)
    for row in cur.fetchall():
        print("<div class='gallery'>")
        print("Artist ID: "+str(row[0]) +"<br>")
        print("Artist Name: "+str(row[1]) +"<br>")
        print("Artist Birth Year: "+str(row[2]) +"<br>")
        print("Artist Country: "+str(row[3]) +"<br>")
        print("Artist Description: "+str(row[4]) +"<br>")
        print("<br><br>")
        print("</div>")
        
    


print("""
</body>
</html>
""")



