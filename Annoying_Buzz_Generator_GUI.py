import random
import tkinter
from tkinter import*


class BuzzGeneratorGUI:
    
    def __init__(self):

        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.prompt_label1 = tkinter.Label(self.top_frame, \
                                          text='Welcome to the business Catchphrase Generator!')
        self.prompt_label2 = tkinter.Label(self.top_frame, \
                                           text='For all those awkward pauses in long meetings.')

        self.prompt_label1.pack(side='left')
        self.prompt_label2.pack(side='left')
        
        self.buzzPhrase_button=tkinter.Button(self.bottom_frame, \
                                       text='Give me a phrase!', \
                                       command=self.phrase)
        self.quit_button = tkinter.Button(self.bottom_frame, \
                                          text='Quit', \
                                          command=self.main_window.destroy)

        self.buzzPhrase_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()




    
    def phrase(self):

        listA=["We are going to ",
            "Let's ",
            "Moving forward, we should ",
            "Get off your high horse and ",
            "Silos are for corn and our team should ",
            "I'd like to ",
            "From now on ",
            "We should put our heads together and "]

        listB=["go ahead and address the elephant in the room ... Phil?",
            "interface our faces off. Or have a face-off.",
            "dive deeper on this issue. Like Flipper, only deeper.",
            "speak only in acronyms. SOIA. SMH. LOL.",
            "cascade relevant information; but don't go chasing waterfalls. Please stick to the rivers and the lakes that you're used to.",
            "put all hands on deck. Last one on the deck gets to swab it!",
            "go on the customer journey. Which means ordering things online at 2 a.m.",
            "move the needle. Except when you are getting blood drawn. That's bad.",
            "leverage our position for a quick win; because slow wins are for losers.",
            "admit that's not in our wheelhouse. Wheels are in our wheelhouse.",
            "focus on customer retention. It's better than water retention.",
            "be gamechangers. Let's play Yahtzee.",
            "admit this project has no legs. Ever since the accident.",
            "understand that takeaways do not include restaurant centerpieces and office supplies!"]

        master=Tk()
        
        buzz = Message(master, text=(random.choice(listA)+random.choice(listB)),width=250)
        buzz.pack()
        #tkMessageBox.showinfo(random.choice(listA)+random.choice(listB))

       
buzz_gen = BuzzGeneratorGUI()   
