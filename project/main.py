from tkinter import *
import tkinter.messagebox
import MentalysisMainAlgo
import matplotlib.pyplot as plt

root = Tk()
root.title("mentalysis")
mainframe = Frame(root)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
mainframe.pack(pady=100, padx=100)

# Create a Tkinter variable
tkvar = StringVar(root)

# Dictionary with options
choices = {'Product Review', 'Customer Service Feedback', 'Swachh Bharat Abhiyan', 'Education System in India'}
tkvar.set('Product Review')  # set the default option

popupMenu = OptionMenu(mainframe, tkvar, *choices)
Label(mainframe, text="Choose  your topic").grid(row=1, column=1)
popupMenu.grid(row=2, column=1)

#Making Object of Mentalysis Class
clf = MentalysisMainAlgo.Mentalsis()


#Function to analyse comment
def main_op(rfile,opt):

    newwin1 = Toplevel(root)
    newwin1.title(opt+" Analysis")

    positive = 0
    wpositive = 0
    spositive = 0
    negative = 0
    wnegative = 0
    snegative = 0
    neutral = 0
    NoOfTerms = 0

    fetchedcomments = rfile.read()

    for comment in fetchedcomments.split("-*-*-*-"):    #To fetch individual comment
        if(comment != ""):

            NoOfTerms+=1
            sentiment_value = clf.calculatingSentiment(comment)
            if (sentiment_value == 0):
                sent=("Neutral")
                neutral+=1
            elif (sentiment_value > 0 and sentiment_value <= 0.3):
                sent=("Weakly positive")
                wpositive+=1
            elif (sentiment_value > 0.3 and sentiment_value <= 0.6):
                sent=("Positive")
                positive+=1
            elif (sentiment_value > 0.6 and sentiment_value <= 1):
                sent=("Strongly positive")
                spositive+=1
            elif (sentiment_value > -0.3 and sentiment_value <= 0):
                sent=("Weakly negative")
                wnegative+=1
            elif (sentiment_value > -0.6 and sentiment_value <= -0.3):
                sent=("Negative")
                negative+=1
            elif (sentiment_value > -1 and sentiment_value <= -0.6):
                sent=("Strongly negative")
                snegative+=1

            d = ("The Sentiment of the Review is " + (sent) + "\n")
            l1 = Label(newwin1, text=str(NoOfTerms) + ". " + comment, font="arial 12")
            l1.pack()
            l2 = Label(newwin1, text=d, font="arial 12")
            l2.pack()

    #Function to calculate percentage of comments
    def percentage(part, whole):
            temp = 100 * float(part) / float(whole)
            return format(temp, '.2f')


    positive = percentage(positive, NoOfTerms)
    wpositive = percentage(wpositive, NoOfTerms)
    spositive = percentage(spositive, NoOfTerms)
    negative = percentage(negative, NoOfTerms)
    wnegative = percentage(wnegative, NoOfTerms)
    snegative = percentage(snegative, NoOfTerms)
    neutral = percentage(neutral, NoOfTerms)

    #Function to plot pie chart
    def plotPieChart(positive, wpositive, spositive, negative, wnegative, snegative, neutral, opt, NoOfTerms):
        labels = ['Positive [' + str(positive) + '%]', 'Weakly Positive [' + str(wpositive) + '%]',
                  'Strongly Positive [' + str(spositive) + '%]', 'Neutral [' + str(neutral) + '%]',
                  'Negative [' + str(negative) + '%]', 'Weakly Negative [' + str(wnegative) + '%]',
                  'Strongly Negative [' + str(snegative) + '%]']
        sizes = [positive, wpositive, spositive, neutral, negative, wnegative, snegative]
        colors = ['yellowgreen', 'lightgreen', 'darkgreen', 'gold', 'red', 'lightsalmon', 'darkred']
        patches, texts = plt.pie(sizes, colors=colors, startangle=90)
        plt.legend(patches, labels, loc="best")
        plt.title('How people are reacting on ' + opt + ' by analyzing various comments')
        plt.axis('equal')
        plt.tight_layout()
        plt.show()

    #Function call
    plotPieChart(positive, wpositive, spositive, negative, wnegative, snegative,neutral, opt,NoOfTerms)



#Function for topic 1
def opt_1(comment):
    wfile = open("myfile1.txt", "a")
    wfile.write(comment)
    wfile.write("-*-*-*-")
    wfile.close()

#Function for topic 2
def opt_2(comment):
    wfile = open("myfile2.txt", "a")
    wfile.write(comment)
    wfile.write("-*-*-*-")
    wfile.close()

#Function for topic 3
def opt_3(comment):
    wfile = open("myfile3.txt", "a")
    wfile.write(comment)
    wfile.write("-*-*-*-")
    wfile.close()

#Function for topic 4
def opt_4(comment):
    wfile = open("myfile4.txt", "a")
    wfile.write(comment)
    wfile.write("-*-*-*-")
    wfile.close()


# on change dropdown value
def change_dropdown(*args):
    print(tkvar.get())
    opt = tkvar.get()
    newwin = Toplevel(root)
    display = Label(newwin, text="Write your comment")
    w = Text(newwin, width=40, height=20)
    w.pack(side=BOTTOM)

    #Function to read the file
    def read_data():
        if (opt == "Product Review"):
            rfile = open("myfile1.txt","r")
        elif (opt == "Customer Service Feedback"):
            rfile = open("myfile2.txt", "r")
        elif (opt == "Swachh Bharat Abhiyan"):
            rfile = open("myfile3.txt", "r")
        elif (opt == "Education System in India"):
            rfile = open("myfile4.txt", "r")
        main_op(rfile,opt)

    button = Button(newwin, text='Analyse', fg="green",command= read_data)
    button.pack(side=LEFT)

    #Function to save the comment in file
    def save_data():
        comment = w.get("1.0", END)
        print(comment)
        if (opt == "Product Review"):
            opt_1(comment)
        elif (opt == "Customer Service Feedback"):
            opt_2(comment)
        elif (opt == "Swachh Bharat Abhiyan"):
            opt_3(comment)
        elif (opt == "Education System in India"):
            opt_4(comment)
        tkinter.messagebox.showinfo("Submitted","Successfully submitted your comment.")

    button = Button(newwin, text="Save", fg="green", command=save_data)
    button.pack(side=RIGHT)
    display.pack()


# link function to change dropdown
tkvar.trace('w', change_dropdown)

root.mainloop()

