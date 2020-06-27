from PyQt4 import QtCore, QtGui
import subprocess
import socket
from PIL import Image
import threading
import thread
import time
import pyscreenshot as ImageGrab
from PIL import Image
from threading import Thread
from SocketServer import ThreadingMixIn

ip_address={}
printed={}
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_ScrollArea(object):

    def run(self, path):
        subprocess.call(['pythonw',path])
        
    def setupUi(self, ScrollArea):
        ScrollArea.setObjectName(_fromUtf8("Desktop Sharing"))
        self.title="Desktop Sharing"
        ScrollArea.resize(1125, 805)
        ScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1123, 803))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.label = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label.setGeometry(QtCore.QRect(30, 10, 801, 421))
        self.label.setObjectName(_fromUtf8("label"))
        #self.label.setText(_fromUtf8(""))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        #self.label.setPixmap(QtGui.QPixmap(_fromUtf8("server.png")).scaled(self.label.size(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))
        
        self.pushButton = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton.setGeometry(QtCore.QRect(60, 530, 171, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(self.server_fun)
        self.pushButton_2 = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 530, 171, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_2.clicked.connect(self.start)
        
        self.pushButton_3 = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_3.setGeometry(QtCore.QRect(540, 530, 171, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_3.clicked.connect(self.stop)
        self.pushButton_4 = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_4.setGeometry(QtCore.QRect(770, 530, 171, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setMouseTracking(True)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_4.clicked.connect(self.multi)

        self.pushButton_5 = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_5.setGeometry(QtCore.QRect(1000, 530, 171, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setMouseTracking(True)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_5.clicked.connect(self.refresh_dict)
        
        self.listWidget = QtGui.QListWidget(self.scrollAreaWidgetContents)
        self.listWidget.setGeometry(QtCore.QRect(850, 10, 256, 461))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.listWidget.setFont(font)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        ScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(ScrollArea)
        QtCore.QMetaObject.connectSlotsByName(ScrollArea)
    def refresh_dict(self):
        for d in ip_address:
            if d not in printed:
                self.listWidget.addItem(d)
                printed[d]=ip_address[d]
                ip_address[d]
            else:
                printed[d]=ip_address[d]

    def retranslateUi(self, ScrollArea):
        ScrollArea.setWindowTitle(_translate("ScrollArea", "SERVER", None))
        #self.label.setText(_translate("ScrollArea", "image", None))
        self.pushButton.setText(_translate("ScrollArea", "Connect", None))
        self.pushButton_2.setText(_translate("ScrollArea", "Start", None))
        self.pushButton_3.setText(_translate("ScrollArea", "Stop", None))
        self.pushButton_4.setText(_translate("ScrollArea", "Multi", None))
        self.pushButton_5.setText(_translate("ScrollArea", "Refresh", None))

    def server_fun(self):
        port = 5000
        s = socket.socket()
        while True:
            nam=raw_input("enter the user name")
            if nam in ip_address:
                host = ip_address[nam]
                s.connect((host , port))
                break
            else:
                print "sorry enter proper name"
                

        print "\n Waiting for Image.............."

        f = open("server.png", "wb")

        while True:

            read = s.recv(1)

            if not read:

                break
                
            f.write(read)
                
        f.close()

        print "\n Image Received Successfully"

        image = Image.open('server.png')

        #image.show()

        self.fun()

        s.close()

        
    def fun(self):
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("server.png")).scaled(self.label.size(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))
        #QWidget().resize(QPixmap(_fromUtf8("server.png")).width() , QPixmap(_fromUtf8("server.png")).height())

    def start(self):
        serversock = socket.socket()
        host = socket.gethostname()
        port = 9000
        serversock.bind((host, port))

        serversock.listen(10)
        print("Waiting for a connection.....")
        i=0

        def reader(client,i):
            fle = client.makefile('r')
            filename = fle.readline()
            client.send("Got file {}\n".format(filename))
            file_to_write = open(filename.rstrip(), 'wb')
            client.send("Starting writing {}\n".format(filename))
            file_to_write.write(fle.read())
            file_to_write.close()
            image = Image.open('image%d.png'%(i))
            image.show()
            client.send("Finished writing {}\n".format(filename))


        while True:
            client, addr = serversock.accept()
            print("Got a connection from %s" % str(addr))
            i=i+1
            client_serve_thread = threading.Thread(target=reader, args=tuple((client,i)))
            client_serve_thread.start()
            time.sleep(0.001)

        

    def stop(self):
        serversock.close()

    def multi(self):

        if __name__ == "__main__":
            # fullscreen
           #ImageGrab.grab_to_file('image.png')


           TCP_IP = 'localhost'
           TCP_PORT = 9001
           BUFFER_SIZE = 1024

           class ClientThread(Thread):

               def __init__(self,ip,port,sock):
                   Thread.__init__(self)
                   self.ip = ip
                   self.port = port
                   self.sock = sock
                   time.sleep(3)
                   ImageGrab.grab_to_file('image.png')
                   print " New thread started for "+ip+":"+str(port)
                   
                   

               def run(self):
                   filename='image.png'
                   f = open(filename,'rb')
                   while True:
                       l = f.read(BUFFER_SIZE)
                       while (l):
                           self.sock.send(l)
                           #print('Sent ',repr(l))
                           l = f.read(BUFFER_SIZE)
                       if not l:
                           f.close()
                           self.sock.close()
                           break
                   print "File sent to "+ip+":"+str(port)

           tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
           tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
           tcpsock.bind((TCP_IP, TCP_PORT))
           threads = []

           while True:
               tcpsock.listen(5)
               print "Waiting for incoming connections..."
               (conn, (ip,port)) = tcpsock.accept()
               print 'Got connection from ', (ip,port)
               newthread = ClientThread(ip,port,conn)
               newthread.start()
               threads.append(newthread)

           for t in threads:
               t.join()

        

def communication(threadName,delay):
    if __name__ == "__main__":
        import sys
        app = QtGui.QApplication(sys.argv)
        ScrollArea = QtGui.QScrollArea()
        ui = Ui_ScrollArea()
        ui.setupUi(ScrollArea)
        ScrollArea.show()
        sys.exit(app.exec_())



       
def receive_connection(threadName,delay):
    print "2"
    while True:
         host = socket.gethostname()
         port = 5000
         s = socket.socket()
         s.bind((host, port))
         s.listen(1)
         con , address = s.accept()
         name = con.recv(1024)
         ip_address[name]=address[0]
         print ip_address
         s.close()







thread.start_new_thread(communication,("thread 1",1))
thread.start_new_thread(receive_connection,("thread 2",1))


