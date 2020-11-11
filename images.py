import cgi
import pymysql

db = pymysql.connect(host = 'localhost', user = 'gallery', passwd = 'eecs118',
                     db = 'gallery')
cur = db.cursor()
form = cgi.FieldStorage()
a = form.getvalue("i_id")
b = form.getvalue("i_t")
c = form.getvalue("i_l")
d = form.getvalue("gid")
e = form.getvalue("a_id")
f = form.getvalue("d_id")
g = form.getvalue("d_year")
h = form.getvalue("d_type")
i = form.getvalue("d_width")
j = form.getvalue("d_height")
k = form.getvalue("d_location")
l = form.getvalue("d_description")
m = form.getvalue("c_aid")
n = form.getvalue("c_aname")
o = form.getvalue("c_ayear")
p = form.getvalue("c_acountry")
q = form.getvalue("c_adescription")


if ((a!=None) and (b!=None) and (c!=None) and (d!=None) and (e!=None) and (f!=None)):
    sql = "INSERT IGNORE INTO image VALUES (%s, %s, %s, %s, %s, %s)"
    cur.execute(sql, (a,b,c,d,e,f))
    db.commit()
if ((g!=None) and (h!=None) and (i!=None) and (j!=None) and (k!=None) and (l!=None) and (form.getvalue("modify")== None)):
    sql = "INSERT IGNORE INTO detail VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    cur.execute(sql, (f,a,g,h,i,j,k,l))
    db.commit()
if ((m!=None) and (n!=None) and (o!=None) and (p!=None) and (q!=None)):
    sql = "INSERT IGNORE INTO artist VALUES (%s, %s, %s, %s, %s)"
    cur.execute(sql, (m, n, o, p, q))
    db.commit()
if((a!= None) and (form.getvalue("delete") != None)):
    sql = "SELECT detail_id FROM image WHERE image_id="+str(a)
    cur.execute(sql)
    row = cur.fetchone()
    detail = row[0]
    sql = "DELETE FROM image WHERE image_id="+str(a)
    cur.execute(sql)
    db.commit()
    sql = "DELETE FROM detail WHERE detail_id="+str(detail)
    cur.execute(sql)
    db.commit()
if((a != None) and (form.getvalue("modify") !=None)):
    sql = "SELECT detail_id FROM image WHERE image_id="+str(a)
    cur.execute(sql)
    row = cur.fetchone()
    detail = row[0]
##    sql = "UPDATE image SET title = "+str(b)+" link = "+str(c)+" WHERE image_id="+str(a)
##    cur.execute(sql)
##    db.commit()
##    sql = "UPDATE detail SET year = "+str(g)+" type="+str(h)+" width = "+str(i)+" height = "+str(j)+" location = "+str(k)+" description = "+str(l)+", WHERE detail_id = "+str(detail)
##    cur.execute(sql)
##    db.commit()

    sql = "UPDATE image SET title ='"+str(b)+"' WHERE image_id="+str(a)
    cur.execute(sql)
    
    sql = "UPDATE image SET link='"+str(c)+"' WHERE image_id="+str(a)
    cur.execute(sql)

    sql = "UPDATE detail SET year='"+str(g)+"' WHERE detail_id="+str(detail)
    cur.execute(sql)

    sql = "UPDATE detail SET type='"+str(h)+"' WHERE detail_id="+str(detail)
    cur.execute(sql)

    sql = "UPDATE detail SET width='"+str(i)+"' WHERE detail_id="+str(detail)
    cur.execute(sql)

    sql = "UPDATE detail SET height='"+str(j)+"' WHERE detail_id="+str(detail)
    cur.execute(sql)

    sql = "UPDATE detail SET location='"+str(k)+"' WHERE detail_id="+str(detail)
    cur.execute(sql)

    sql = "UPDATE detail SET description='"+str(l)+"' WHERE detail_id="+str(detail)
    cur.execute(sql)
    db.commit()

print("Content-Type: text/html\n\n")
print("""
<html>
<title>Images of a Gallery</title>
<head>
    <style>
    body{
        font-family: "Lucida Console", serif;
    }
    h5{
        text-decoration: underline;
        font-size: 18px;
    }
    #form{
        float: right;
        font-size: 14px;
        position: absolute;
        top: 10px;
        right: 10px;
    }
    #form2{
        float: right;
        font-size: 14px;
        position: absolute;
        top: 450px;
        right: 10px;
    }
    #form3{
        float: right;
        font-size: 14px;
        position: absolute;
        top: 750px;
        right: 300px;
    }
    #form4{
        float: right;
        font-size: 14px;
        position: absolute;
        top: 930px;
        right: 10px;
    }
    input{
        margin-bottom: 3px;
    }
    div.gallery{
        margin: 10px;
        border: 1px solid
        float: left;
    }
    </style>
</head>
<body>
""")
print("<h1 id='top'>Images(GalleryID: "+str(d)+")</h1>")
sql = "SELECT COUNT(image_id) FROM image WHERE gallery_id=" + str(d)
cur.execute(sql)
result = cur.fetchone()
print("<h2>There are " + str(result[0]) + " images in this gallery.</h2>")
print("""
<div id='form'>
    <h5>Add a new image here!</h5>
    <form id='add' action='/test/cgi-bin/images.py' method='post'>
""")
print("<input name='gid' type='hidden' size='11' value='"+str(d)+"'><br>")
print("""
        Image ID: <input name='i_id' type='text' size='11'><br>
        Image Title: <input name='i_t' type='text' size='11'><br>
        Image Link: <input name='i_l' type='text' size='40'><br>
        Artist ID: <input name='a_id' type='text' size='11'><br>
        Detail ID: <input name='d_id' type='text' size='11'><br>
        Image Year: <input name='d_year' type='text' size='11'><br>
        Image Type: <input name='d_type' type='text' size='45'><br>
        Image Width: <input name='d_width' type='text' size='11'><br>
        Image Height: <input name='d_height' type='text' size='11'><br>
        Image Location: <input name='d_location' type='text' size='45'><br>
        Image Description <input name='d_description' type='text' size='45'><br>
        <input type='submit' value='Add Image'>
    </form>
</div>
<div id='form2'>
    <h5>Add a new artist here!</h5>
    <form id='add2' action='/test/cgi-bin/images.py' method='post'>
""")
print("<input name='gid' type='hidden' size='11' value='"+str(d)+"'><br>")
print("""
        Artist ID: <input name='c_aid' type='text' size='11'><br>
        Artist Name: <input name='c_aname' type='text' size='11'><br>
        Artist Birth Year: <input name='c_ayear' type='text' size='11'><br>
        Artist Country: <input name='c_acountry' type='text' size='11'><br>
        Artist Description: <input name='c_adescription' type='text' size='45'><br>
        <input type='submit' value='Create Artist'>
    </form>
</div>
""")
print("""
<div id='form3'>
    <h5>Delete an image here!</h5>
    <form id='add3' action='/test/cgi-bin/images.py' method='post'>
""")
print("<input name='gid' type='hidden' size='11' value='"+str(d)+"'><br>")
print("""
        <input name='delete' type='hidden' value='yes'><br>
        Image ID: <input name='i_id' type='text' size='11'><br>
        <input type='submit' value='Delete Image'>
    </form>
</div>
""")

print("""
<div id='form4'>
    <h5>Modify image details here!</h5>
    <form id='add4' action='/test/cgi-bin/images.py' method='post'>
""")
print("<input name='gid' type='hidden' size='11' value='"+str(d)+"'><br>")
print("""
        <input name='modify' type='hidden' value='yes'><br>
        Image ID(used to select which image to modify): <input name='i_id' type='text' size='11'><br>
        Below are the parameters to change!<br>
        Image Title: <input name='i_t' type='text' size='11'><br>
        Image Link: <input name='i_l' type='text' size='40'><br>
        Image Year: <input name='d_year' type='text' size='11'><br>
        Image Type: <input name='d_type' type='text' size='45'><br>
        Image Width: <input name='d_width' type='text' size='11'><br>
        Image Height: <input name='d_height' type='text' size='11'><br>
        Image Location: <input name='d_location' type='text' size='45'><br>
        Image Description <input name='d_description' type='text' size='45'><br>
        <input type='submit' value='Modify Image'>
    </form>
</div>

""")
if (d != None):
    print("<script>")
    print("localStorage.gallery_id = '" + str(d) + "';")
    print("</script>")

sql = "SELECT * FROM image WHERE gallery_id=" + str(d)
cur.execute(sql)
for row in cur.fetchall():
    print("<div class='gallery'>")
    print("<a target='_blank' href='/test/cgi-bin/details.py?d_id="+str(row[5])+"&a_id="+str(row[4])+"&i_link="+str(row[2])+"'>")
    print("Title: '" + str(row[1]) + "'")
    print("</a><br>")
    print("Image ID: '" + str(row[0]) +"'")
    print("<br>")
    print("<a target='_blank' href='" + str(row[2]) +"'>")
    print("<img src='" + str(row[2]) +"' alt='oof' width='300' height='200'>")
    print("</a>")
    print("</div>")

print("""

</body>
</html>
""")
