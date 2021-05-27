import urllib.request

urls = open("sites.txt","r")

print ("<!DOCTYPE html>")
print ("<html lang='"'pt-br'"'>")
print ("   <head>")
print ("      <meta charset='"'UTF-8'"'>")
print ("      <title>MONITORAÇÃO MIDDLEWARE</title>")
print ("   </head>")
print ("   <body align='"'center'"'>")
print ("      <font size='"'5'"' face='"'Tahoma, Verdana, Arial, Helvetica, sans-serif'"' color='"'red'"'>")
print ("         <h3>Validações de WebSites</h3>")
print ("      </font>")
print ("      <div align='"'center'"'>")
print ("        <Table border=0 cellpadding=0 cellspacing=8>")
print ("            <TR bgcolor=red align=center>")
print ("                    <TD><FONT COLOR=white>WEBSITE</TD>")
print ("                    <TD><FONT COLOR=white>STATUS</TD>")
print ("                </TR>")

for url in urls:
    try:    
        get = urllib.request.urlopen(url).getcode()

        if get == 200 :
            print ("                <TD align=center>",url,"</TD>")
            print ("                <TD align=center bgcolor=gree><FONT COLOR=white>",get,"</TD>")
            print ("                </TR>")

        else :
            print ("                <TD align=center>",url,"</TD>")
            print ("                <TD align=center bgcolor=red><FONT COLOR=white>",get,"</TD>")
            print ("                </TR>")
            

    except Exception as e:
        print ("                <TD align=center>",url,"</TD>")
        print ("                <TD align=center bgcolor=red><FONT COLOR=white>ERROR</TD>")
        print ("                </TR>")

print("            </TR>")
print("        </Table>")
print("      </div>")
print("   </body>")
print("</html>")
urls.close()
