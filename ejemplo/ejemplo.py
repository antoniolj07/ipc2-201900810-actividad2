from xml.dom import minidom

xmldoc = minidom.parse('familia.xml')

# doc.getElementsByTagName returns NodeList
name = xmldoc.getElementsByTagName('apellido')[0]
print(name.firstChild.data)

familia = xmldoc.getElementsByTagName('familiar')
for familiar in familia:
        sid = familiar.getAttribute('id')
        nombre = familiar.getElementsByTagName('nombre')[0]
        edad = familiar.getElementsByTagName('edad')[0]
        print("id:%s, nombre:%s, edad:%s" %
              (sid, nombre.firstChild.data, edad.firstChild.data))