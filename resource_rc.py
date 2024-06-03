# Resource object code (Python 3)
# Created by: object code
# Created by: The Resource Compiler for Qt version 6.7.0
# WARNING! All changes made in this file will be lost!

from PySide6 import QtCore

qt_resource_data = b"\
\x00\x00\x09\xb4\
<\
!DOCTYPE html>\x0a<\
html>\x0a  <head>\x0a \
   <meta http-eq\
uiv=\x22Content-Typ\
e\x22 content=\x22text\
/html; charset=u\
tf-8\x22 />\x0a    <sc\
ript type=\x22text/\
javascript\x22 src=\
\x22./qwebchannel.j\
s\x22></script>\x0a   \
 <script type=\x22t\
ext/javascript\x22>\
\x0a      //BEGIN S\
ETUP\x0a      funct\
ion output(messa\
ge) {\x0a        va\
r output = docum\
ent.getElementBy\
Id(\x22output\x22);\x0a  \
      output.inn\
erHTML = output.\
innerHTML + mess\
age + \x22\x5cn\x22;\x0a    \
  }\x0a      window\
.onload = functi\
on () {\x0a        \
if (location.sea\
rch != \x22\x22)\x0a     \
     var baseUrl\
 = /[?&]webChann\
elBaseUrl=([A-Za\
-z0-9\x5c-:/\x5c.]+)/.\
exec(\x0a          \
  location.searc\
h\x0a          )[1]\
;\x0a        else v\
ar baseUrl = \x22ws\
://localhost:123\
45\x22;\x0a\x0a        ou\
tput(\x22Connecting\
 to WebSocket se\
rver at \x22 + base\
Url + \x22.\x22);\x0a    \
    var socket =\
 new WebSocket(b\
aseUrl);\x0a\x0a      \
  socket.onclose\
 = function () {\
\x0a          conso\
le.error(\x22web ch\
annel closed\x22);\x0a\
        };\x0a     \
   socket.onerro\
r = function (er\
ror) {\x0a         \
 console.error(\x22\
web channel erro\
r: \x22 + error);\x0a \
       };\x0a      \
  socket.onopen \
= function () {\x0a\
          output\
(\x22WebSocket conn\
ected, setting u\
p QWebChannel.\x22)\
;\x0a          new \
QWebChannel(sock\
et, function (ch\
annel) {\x0a       \
     // make cor\
e object accessi\
ble globally\x0a   \
         window.\
core = channel.o\
bjects.core;\x0a\x0a  \
          docume\
nt.getElementByI\
d(\x22send\x22).onclic\
k = function () \
{\x0a              \
var input = docu\
ment.getElementB\
yId(\x22input\x22);\x0a  \
            var \
text = input.val\
ue;\x0a            \
  if (!text) {\x0a \
               r\
eturn;\x0a         \
     }\x0a\x0a        \
      output(\x22Se\
nt message: \x22 + \
text);\x0a         \
     input.value\
 = \x22\x22;\x0a         \
     core.receiv\
eText(text);\x0a   \
         };\x0a\x0a   \
         core.se\
ndText.connect(f\
unction (message\
) {\x0a            \
  output(\x22Receiv\
ed message: \x22 + \
message);\x0a      \
      });\x0a\x0a     \
       core.rece\
iveText(\x0a       \
       \x22Client c\
onnected, ready \
to send/receive \
messages!\x22\x0a     \
       );\x0a      \
      output(\x22Co\
nnected to WebCh\
annel, ready to \
send/receive mes\
sages!\x22);\x0a      \
    });\x0a        \
};\x0a      };\x0a    \
  //END SETUP\x0a  \
  </script>\x0a    \
<style type=\x22tex\
t/css\x22>\x0a      ht\
ml {\x0a        hei\
ght: 100%;\x0a     \
   width: 100%;\x0a\
      }\x0a      #i\
nput {\x0a        w\
idth: 400px;\x0a   \
     margin: 0 1\
0px 0 0;\x0a      }\
\x0a      #send {\x0a \
       width: 90\
px;\x0a        marg\
in: 0;\x0a      }\x0a \
     #output {\x0a \
       width: 50\
0px;\x0a        hei\
ght: 300px;\x0a    \
  }\x0a    </style>\
\x0a  </head>\x0a  <bo\
dy>\x0a    <textare\
a id=\x22output\x22></\
textarea><br />\x0a\
    <input id=\x22i\
nput\x22 /><input\x0a \
     type=\x22submi\
t\x22\x0a      id=\x22sen\
d\x22\x0a      value=\x22\
Send\x22\x0a      oncl\
ick=\x22javascript:\
click();\x22\x0a    />\
\x0a  </body>\x0a</htm\
l>\x0a\
"

qt_resource_name = b"\
\x00\x05\
\x00t\xf8p\
\x00m\
\x00y\x00a\x00p\x00p\
\x00\x0a\
\x0c\xba\xf2|\
\x00i\
\x00n\x00d\x00e\x00x\x00.\x00h\x00t\x00m\x00l\
"

qt_resource_struct = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x02\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x10\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x01\x8f\xdf\x8d\xdd\xfc\
"

def qInitResources():
    QtCore.qRegisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
