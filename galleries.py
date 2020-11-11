import cgi
import cgitb
import pymysql
import datetime

now = datetime.datetime.now()
hour = now.hour
minute = str(now.minute)
if ((hour >= 0) and (hour <= 11)):
    time = "Good Morning! "
elif ((hour >= 12)  and (hour <= 16)):
    time = "Good Afternoon!  "
elif ((hour >= 17) and (hour <= 20)):
    time = "Good Evening!  "
else:
    time = "Good Night!  "

hour = str(now.hour)
number = hour+":"+minute


db = pymysql.connect(host = 'localhost', user = 'gallery', passwd = 'eecs118',
                     db = 'gallery')
cur = db.cursor()

cgitb.enable()
form = cgi.FieldStorage()
x = form.getvalue("g_id")
y = form.getvalue("g_n")
z = form.getvalue("g_d")

if ((x != None) and (y != None) and (z != None) and(form.getvalue("modify")==None)):
    sql = "INSERT IGNORE INTO gallery VALUES (%s, %s, %s)"
    cur.execute(sql,(x,y,z))
    db.commit()

if (form.getvalue("modify") != None):
    sql = "UPDATE gallery SET name='"+str(y)+"' WHERE gallery_id="+str(x)
    cur.execute(sql)
    sql = "UPDATE gallery SET description='"+str(z)+"' WHERE gallery_id="+str(x)
    cur.execute(sql)
##for row in rows:
##    count += 1
##    name = row[0]
##    description = row[1]
##    
    

print("Content-Type: text/html\n\n")
print("""
<html>
<title>Galleries</title>
<head>
    <style>
        body{
            font-family: "Lucida Console", serif;
        }
        p{
            float: left;
            max-width: 1000px
        }
        #form{
            float: right;
            font-size: 18px;
            position: absolute;
            top: 250px;
            right: 380px;
        }
        #form2{
            float: right;
            font-size: 18px;
            position: absolute;
            top: 550px;
            right: 20px;
        }
        h3{
            text-decoration: underline;
        }
        input{
            margin-bottom: 20px
        }
        #form_next{
            float: right;
            margin-bottom: 200px;
            position: absolute;
            right: 50px;
        }
        textarea{
            width: 200px;
        }
        #list{
            float:left;
        }
    </style>
</head>

<body>
<h1 id='top'>Galleries</h1>
""")
print("<h2>"+time+"The time is "+number+"</h2>")
print("<a target='_blank' href='/test/cgi-bin/search.py'>Click here for search functions!</a>")

print("""<div id='galleries'>""")
print("""<p id='list'>""")

print("""</p>""")

print("""
<div id='form_next'>
    <h3>Type in gallery id for accessing the specific gallery:</h3>
    <form id='next' action='/test/cgi-bin/images.py' method='post' target='_blank'>
        <input name = 'gid' type='text' size='4'><br>
        <input type='submit' value='Access Gallery'>
    </form>
</div>
""")

print("<script>")
sql = "SELECT name, description, gallery_id FROM gallery"
cur.execute(sql)
for row in cur.fetchall():
    print("document.getElementById('list').innerHTML += 'Gallery Name: " + str(row[0]) + "  ';")
    print("document.getElementById('list').innerHTML += '<br>'")
    print("document.getElementById('list').innerHTML += 'Gallery ID: " + str(row[2]) + "';")
    print("document.getElementById('list').innerHTML += '<br>'")
    print("document.getElementById('list').innerHTML += 'Gallery Description: " + str(row[1]) + "';")
    print("document.getElementById('list').innerHTML += '<br><br><br>'")
print("</script>")

print("""</div>""")


print("""
<div id='form'>
    <h3>Add a new gallery here!</h3>
    <form id='add' action='/test/cgi-bin/galleries.py' method='post'>
        Gallery ID: <input name='g_id' type='text' size='11'><br>
        Gallery Name: <input name='g_n' type='text' size='11'><br>
        Gallery Description: <br><textarea name='g_d' cols='60' rows='5' wrap='soft'>Enter description here...</textarea>
        <input type='submit' value='Submit'>
    </form>
</div>
""")

print("""
<div id='form2'>
    <h3>Modify Gallery details here!</h3>
    <form id='add' action='/test/cgi-bin/galleries.py' method='post'>
        <input name='modify' type='hidden' value='yes'><br>
        Gallery ID(used to select which gallery to modify) :<input name='g_id' type='text' size='11'><br>
        Gallery Name :<input name='g_n' type='text' size='11'><br>
        Gallery Description: <br><textarea name='g_d' cols='60' rows='5' wrap='soft'>Enter description here...</textarea>
        <input type='submit' value='Modify Gallery'>
    </form>
</div>

""")


print("""
</body>
""")
