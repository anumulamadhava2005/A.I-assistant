import webbrowser
import time

time.sleep(1)
while 1:
    a = input('search : ')
    if a == "google":
        print("opening google")
        url = 'https://www.google.com/'
        webbrowser.get().open(url)

    if a == "facebook":
        print("opening facebook")
        url = "https://www.facebook.com/"
        webbrowser.get().open(url)

    if a == "instagram":
        print("opening instagram")
        url = "https://www.instagram.com/"
        webbrowser.get().open(url)

    if a == "youtube":
        b = input("select an option (open, search): ")
        if b == "open":
            print("opening youtube")
            url = "https://www.youtube.com/"
            webbrowser.get().open(url)
        if b == "search":
            c = input("Search: ")
            url = "https://www.youtube.com/results?search_query=" + c
            webbrowser.get().open(url)

    if a == "mail" :
        b = input("select an option (open, send mail)")
        if b == "open":
            print("opening mail")
            url = "https://mail.google.com/mail/u/0/#inbox"
            webbrowser.get().open(url)
        if b == "send mail":
            print("opening mail")
            url = "https://mail.google.com/mail/u/0/#inbox?compose=new"
            webbrowser.get().open(url)
    if a == "twitter" :
        print("opeing twitter")            
        url = "https://www.twitter.com/"
        webbrowser.get().open(url)