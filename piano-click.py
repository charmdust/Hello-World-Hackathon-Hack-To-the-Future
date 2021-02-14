from tkinter import *
import time 
import datetime
import pygame

from PIL import ImageTk, Image 

pygame.init()
root = Tk()
root .title('Piano')
root.geometry('1300x900+0+0')
root .configure(background = 'white')

ABC = Frame(root, bg = "blue", bd=20, relief = RIDGE)
ABC.grid()
ABC1 = Frame(root, bg = "blue", bd=20, relief = RIDGE)
ABC1.grid()
ABC2 = Frame(root, bg = "blue", bd=0, relief = RIDGE)
ABC2.grid()
ABC3 = Frame(root, bg = "blue", bd=0, relief = RIDGE)
ABC3.grid()
##################



#########################################################################

##canvas = Canvas(root, width = 300, height = 300)
#canvas.pack()
#happy_cat = ImageTk.PhotoImage(Image.open("C:/Users/laura/Downloads/cat_happy.png"))
#canvas.create_image(20,20,anchor=NW, image=happy_cat)

#Trying to see if we can import happy cat here
happy_cat = ImageTk.PhotoImage(Image.open("C:/Users/laura/Downloads/cat_happy.png"))
sad_cat = ImageTk.PhotoImage(Image.open("C:/Users/laura/Downloads/kawaii-cat-sad.png"))

label = Label(root, image=happy_cat)
label2 = Label(root, image=sad_cat)
##label.grid(row=1, column=2, columnspan=11)
##label2.grid(row=2, column=2, columnspan=11)




###########################################################################


#Label with title
Label(ABC1, text= "Cat Piano", font = ('arial',25,'bold'), padx = 8,pady=8,bd=4,bg='blue',fg='white').grid(row=0,column=0,columnspan=11)
Label(ABC1, text= "Note to play", font = ('arial',25,'bold'), padx = 8,pady=8,bd=34,bg='blue',fg='white',justify = RIGHT).grid(row=0,column=4,columnspan=11)





#Note display
note = StringVar()
note.set('Note Played goes here')
NoteDisplay = Entry(ABC1, text = note, font = ('arial',18,'bold'), bd = 34, bg = 'red', fg = 'blue', width = 28, justify =  CENTER).grid(row=1,column=0,pady=1)

noteToPlay = StringVar()
# happy birthday - first part: 
happyBirthday = ['C','C','D','C', 'F','E',
        'C','C','D','C','G', 'F',
        'C', 'C', 'C1', 'A', 'F', 'E', 'D',
        'A#', 'A#', 'A', 'F', 'G', 'F']
twinkleTwinkle = ['C', 'C', 'G', 'G', 'A', 'A', 'G', 'F', 'F', 'E', 'E', 'D', 'D', 'C',
          'G', 'G', 'F', 'F', 'E', 'E', 'D','G', 'G', 'F', 'F', 'E', 'E', 'D',
          'C', 'C', 'G', 'G', 'A', 'A', 'G', 'F', 'F', 'E', 'E', 'D', 'D', 'C']
maryLamb = ['E', 'D', 'C', 'D', 'E', 'E', 'E', 'D', 'D', 'D', 'E', 'G', 'G', 'G',
         'E', 'D', 'C', 'D', 'E', 'E', 'E', 'E, ' 'D', 'D',  'E', 'D', 'C']
jingleBells = ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'G', 'C', 'D', 'E',
        'F', 'F', 'F', 'F', 'F', 'E', 'E', 'E', 'E', 'E', 'D', 'D', 'E', 'D', 'G',
        'E', 'E', 'E', 'E', 'E', 'E', 'E',  'G', 'C', 'D', 'E',
        'F', 'F', 'F', 'F', 'F', 'E', 'E', 'E', 'E', 'E', 'G', 'G', 'F', 'D', 'C']
odeToJoy = ['E', 'E', 'F', 'G', 'G', 'F', 'E', 'D', 'C', 'C', 'D', 'E', 'E', 'D', 'D',
        'E', 'E', 'F', 'G', 'G', 'F', 'E', 'D', 'C', 'C', 'D', 'E', 'D', 'C', 'C',
        'D', 'D', 'E', 'C', 'D', 'E', 'F', 'E', 'C', 
        'D', 'E', 'F', 'E', 'D', 'C', 'D', 'G',
        'E', 'E', 'F', 'G', 'G', 'F', 'E', 'D', 'C', 'C', 'D', 'E', 'D', 'C', 'C']

listOfSongs = [happyBirthday,twinkleTwinkle,maryLamb,jingleBells,odeToJoy]
currentSong = listOfSongs[0]


def setNoteToPlay(song, index):
  print(song)
  print(index.get())
  if index.get() < len(song):
    noteToPlay.set(song[index.get()])
  else:
    noteToPlay.set('Congratulations')
  


indexSong = IntVar()
indexSong.set(0)
index = IntVar()
label.grid(row=1, column=2, columnspan=11)
index.set(0)
setNoteToPlay(currentSong,index)
NoteDisplay = Entry(ABC1, text = noteToPlay, font = ('arial',18,'bold'), bd = 34, bg = 'red', fg = 'blue', width = 28, justify =  CENTER).grid(row=1,column=4,pady=1)

def checkNoteToPlay(key):
  if (noteToPlay.get() == key):
  	label.config(image=happy_cat)
  	index.set(index.get()+1)
  	setNoteToPlay(currentSong,index)
  else:
    label.config(image=sad_cat)

  
#functions for buttons

def valueCs():
  note.set('C#')
  checkNoteToPlay('C#') 	
  sound = pygame.mixer.Sound("C:/Users/laura/Downloads/Z_Music_Notes/Music_Notes/C_s.wav")
  sound.play()

def valueDs():
  note.set('D#')
  checkNoteToPlay('D#') 
  sound = pygame.mixer.Sound("C:/Users/laura/Downloads/Z_Music_Notes/Music_Notes/D_s.wav")
  sound.play()

def valueFs():
  note.set('F#')
  checkNoteToPlay('F#') 
  sound = pygame.mixer.Sound("C:/Users/laura/Downloads/Z_Music_Notes/Music_Notes/F_s.wav")
  sound.play()

def valueGs():
   note.set('G#')
   checkNoteToPlay('G#') 
   sound = pygame.mixer.Sound("C:/Users/laura/Downloads/Z_Music_Notes/Music_Notes/G_s.wav")
   sound.play()

def valueAs():
   note.set('A#')
   checkNoteToPlay('A#') 
   sound = pygame.mixer.Sound("C:/Users/laura/Downloads/Z_Music_Notes/Music_Notes/Bb.wav")
   sound.play()

def valueC():
  note.set('C')
  checkNoteToPlay('C') 
  sound = pygame.mixer.Sound("C:/Users/laura/Downloads/Z_Music_Notes/Music_Notes/C.wav")
  sound.play()

def valueD():
  note.set('D')
  checkNoteToPlay('D') 
  sound = pygame.mixer.Sound("C:/Users/laura/Downloads/Z_Music_Notes/Music_Notes/D.wav")
  sound.play()

def valueE():
  note.set('E')
  checkNoteToPlay('E') 
  sound = pygame.mixer.Sound("C:/Users/laura/Downloads/Z_Music_Notes/Music_Notes/E.wav")
  sound.play()


def valueF():
  note.set('F')
  checkNoteToPlay('F') 
  sound = pygame.mixer.Sound("C:/Users/laura/Downloads/Z_Music_Notes/Music_Notes/F.wav")
  sound.play()

def valueG():
   note.set('G')
   checkNoteToPlay('G') 
   sound = pygame.mixer.Sound("C:/Users/laura/Downloads/Z_Music_Notes/Music_Notes/G.wav")
   sound.play()

def valueA():
   note.set('A')
   checkNoteToPlay('A') 
   sound = pygame.mixer.Sound("C:/Users/laura/Downloads/Z_Music_Notes/Music_Notes/A.wav")
   sound.play()

def valueB():
  note.set('B')
  checkNoteToPlay('B') 
  sound = pygame.mixer.Sound("C:/Users/laura/Downloads/Z_Music_Notes/Music_Notes/B.wav")
  sound.play()

def valueC1():
  note.set('C1')
  checkNoteToPlay('C1') 
  sound = pygame.mixer.Sound("C:/Users/laura/Downloads/Z_Music_Notes/Music_Notes/C1.wav")
  sound.play()

   

#Black keys

btnspace = Button(ABC2,state = DISABLED, height = 4, width = 8, relief = FLAT,bg = 'blue')
btnspace.grid(row=0,column = 0,padx=0,pady=0)

btnCs = Button(ABC2,height = 4,width = 5,bd = 4, text = "C#",font = ('arial',25,'bold'), bg='black',fg='white', command = valueCs)
btnCs.grid(row=0,column=1,padx = 5, pady = 5)

btnDs = Button(ABC2,height = 4,width = 5,bd = 4, text = "D#",font = ('arial',25,'bold'), bg='black',fg='white',justify = CENTER, command = valueDs)
btnDs.grid(row=0,column=2,padx = 5, pady = 5)

btnspace1 = Button(ABC2,state = DISABLED, height = 4, width = 16, relief = FLAT,bg = 'blue')
btnspace1.grid(row=0,column = 3,padx=0,pady=0)

btnFs = Button(ABC2,height = 4,width = 5,bd = 4, text = "F#",font = ('arial',25,'bold'), bg='black',fg='white',justify = CENTER, command = valueFs)
btnFs.grid(row=0,column=4,padx = 5, pady = 5)

btnGs = Button(ABC2,height = 4,width = 5,bd = 4, text = "G#",font = ('arial',25,'bold'), bg='black',fg='white',justify = CENTER,command = valueGs)
btnGs.grid(row=0,column=5,padx = 5, pady = 5)

btnAs = Button(ABC2,height = 4,width = 5,bd = 4, text = "A#",font = ('arial',25,'bold'), bg='black',fg='white',justify = CENTER, command = valueAs)
btnAs.grid(row=0,column=6,padx = 5, pady = 5)

btnspace3 = Button(ABC2,state = DISABLED, height = 4, width = 25, relief = FLAT,bg = 'blue')
btnspace3.grid(row=0,column = 7,padx=0,pady=0)

#white keys

btnC = Button(ABC3,height = 4,width = 5,bd = 4, text = "C",font = ('arial',25,'bold'), bg='white',fg='black',justify = CENTER, command = valueC)
btnC.grid(row=1,column=0,padx = 5, pady = 5) 

btnD = Button(ABC3,height = 4,width = 5,bd = 4, text = "D",font = ('arial',25,'bold'), bg='white',fg='black',justify = CENTER, command = valueD)
btnD.grid(row=1,column=1,padx = 5, pady = 5) 

btnE = Button(ABC3,height = 4,width = 5,bd = 4, text = "E",font = ('arial',25,'bold'), bg='white',fg='black',justify = CENTER, command = valueE)
btnE.grid(row=1,column=2,padx = 5, pady = 5) 

btnF = Button(ABC3,height = 4,width = 5,bd = 4, text = "F",font = ('arial',25,'bold'), bg='white',fg='black',justify = CENTER, command = valueF)
btnF.grid(row=1,column=3,padx = 5, pady = 5)

btnG = Button(ABC3,height = 4,width = 5,bd = 4, text = "G",font = ('arial',25,'bold'), bg='white',fg='black',justify = CENTER, command = valueG)
btnG.grid(row=1,column=4,padx = 5, pady = 5)

btnA = Button(ABC3,height = 4,width = 5,bd = 4, text = "A",font = ('arial',25,'bold'), bg='white',fg='black',justify = CENTER, command = valueA)
btnA.grid(row=1,column=5,padx = 5, pady = 5)

btnB = Button(ABC3,height = 4,width = 5,bd = 4, text = "B",font = ('arial',25,'bold'), bg='white',fg='black',justify = CENTER, command = valueB)
btnB.grid(row=1,column=6,padx = 5, pady = 5)

btnC1 = Button(ABC3,height = 4,width = 5,bd = 4, text = "C1",font = ('arial',25,'bold'), bg='white',fg='black',justify = CENTER, command = valueC1)
btnC1.grid(row=1,column=7,padx = 5, pady = 5)

def displayNewSong():
  global currentSong
  index.set(0)
  indexSong.set((indexSong.get()+1)%len(listOfSongs))
  currentSong = listOfSongs[indexSong.get()]
  setNoteToPlay(currentSong,index)

btnNewSong = Button(ABC1,height = 2,width = 5,bd = 4, text = "New \nsong",font = ('arial',25,'bold'), bg='white',fg='black',justify = CENTER, command = displayNewSong)
btnNewSong.grid(row=1,column=5,padx = 5, pady = 5)





root.mainloop()