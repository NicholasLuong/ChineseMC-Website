import codecs
import Tkinter
import tkFileDialog
import os

def prerequisite():
    title= '<h1><b>' + raw_input("What is the title of your article?") + '</b></h1>'
    
    

def remove(x):
    y = htmlCode.replace(htmlCode[removeStart(x):removeEnd(x)], "") #Replaces the second post with a blank
    y =  y.replace("<!-- Start -->", "<!-- Start2 -->")
    y = y.replace("<!-- End -->", "<!-- End2 -->")
    return y

def add(x):
    h3 = "<h3>" + raw_input("Title?") + "</h3>"
    paragraph = "<p>" + raw_input("Para?") + "</p>"
    block = "<!-- Start -->" + "\n" + "<li class='feed-article'>" +  "\n" + h3 + "\n" + paragraph + "\n"  + "</li>" + "\n"  + "<!-- End -->"

    return  x[:removeStart(x)] + "\n" +  block + "\n" + x[removeEnd(x):13] + "\n"  + x[htmlCode.find("<!-- Start2 -->"):]
    
def linkArticle(x):
    link = raw_input("What is the name of the file you want to link?")
    readMore = '<p class="read-more">' + "\n" + '<a href="' + link + '.html'

    
#Opens window to browse for file
root = Tkinter.Tk()
root.withdraw() #use to hide tkinter window

currdir = os.getcwd()
htmldir = tkFileDialog.askopenfilename(filetypes = (("Open the Template File", "*.php"),("All files", "*")))

    
f = codecs.open(htmldir, 'r')
htmlCode = f.read()
f.close()
htmlCode = remove(htmlCode)
htmlCode = add(htmlCode)
target = codecs.open(htmldir, 'w+')
target.write(htmlCode)
target.close()








