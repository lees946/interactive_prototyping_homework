import imaplib 
import time as t

while True:
	obj = imaplib.IMAP4_SSL('imap.gmail.com','993')
	obj.login('testseunglee','test0001')
	inbox = obj.select('Inbox')
	print "The inbox contains a tatal of:", inbox
	unreadIds = obj.search(None,'UnSeen')
	print "raw unread:", unreadIds
	unread = unreadIds[1][0].split()
	print "///////"
	print "Unread Array:", unread
	unreadCount = len(unread)
	print unreadCount
		