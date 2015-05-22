from Tkinter import *
import Tkinter as tk
from math import *
import speech
import re

#pip install pykinect
MAX=10
Kmaxg=2
Kmaxb=2
id=0;
size=14*14
rsiz=int(sqrt(size))
flag=1
turn=-1
#print("size",size)
#print("rsiz",rsiz)
mat=[[0 for x in range(rsiz)] for x in range(rsiz)]
for m in range(rsiz):
	for n in range(rsiz):
		
		if n<rsiz/2:
			mat[m][n]=-1
		else :
			mat[m][n]=1
LARGE_FONT= ("Verdana", 12)
dict={'':''}
class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack()#side="top", fill="both", expand = True)

        #container.grid_rowconfigure(0, weight=1)
        #container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

        
class StartPage(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self,parent)
		self.createwindow(controller)


	
	def createwindow(self, controller):
		def callback1(self,phrase):
			print ": %s" % phrase
			global dict 
			p=re.compile('.*Play.*',re.IGNORECASE)
			if p.match(phrase):
				#print "ding ding"
				#listener.stoplistening()
				controller.show_frame(PageOne)
		label = tk.Label(self, text="Welcome to DIGIWAR!!", font=LARGE_FONT)
		label.pack(pady=10,padx=10)

		button = tk.Button(self, text="Play Game",
							command=lambda: controller.show_frame(PageOne))
		button.pack()

		button2 = tk.Button(self, text="Instructions",
							command=lambda: controller.show_frame(PageTwo))
		button2.pack()
		
		
		listener1 = speech.listenforanything(callback1)


class PageOne(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		# label = tk.Label(self, text="Page One!!!", font=LARGE_FONT)
		# label.grid(column=0,row=0)
		self.createWidgets(controller)

	def createWidgets(self,controller):		#arena
		global rsiz
		button1 = tk.Button(self, text="Back to Home",command=lambda: controller.show_frame(StartPage))
		button1.grid(column=rsiz/2,row=rsiz+3,columnspan=4)
		button2 = tk.Button(self, text="Instructions",  command=lambda: controller.show_frame(PageTwo))
		button2.grid(column=rsiz/2,row=rsiz+4,columnspan=4)
		floors = [i for i in range(size)]
		self.buttons = {}
		xPos = 0
		yPos = 0
		global mat
		
		for floor in floors:
			if yPos == rsiz :
				xPos = xPos + 1
				yPos = 0
			if xPos == rsiz :
				yPos = 2
			self.buttons[floor] = tk.Button(self, width=2,bg="white",command = lambda f=floor: self.pressed(f))
			self.buttons[floor].grid(row=xPos, column =yPos)
			yPos = yPos +1
		self.Turn1 = tk.Label(self, text="Turn:", fg="red",width=8).grid(column = rsiz+1, row= 7)
		self.Turn2 = tk.Label(self, bg="green",width=10)
		self.Turn2.grid(column = rsiz+2, row= 7)
		self.stat=tk.Label(self, width=8,text="STATUS:").grid(column=rsiz +1,row=8)
		self.stat1=tk.Label(self,width=10,text="place soldiers")
		self.stat1.grid(column=rsiz+2,row=8)
		#self.QUIT = tk.Button(self, text="QUIT", fg="red",width=3,command=root.destroy).grid(column = rsiz+1, row= 9)
		self.Start=tk.Button(self,text="Attack",width=10,command=self.attack1).grid(column=rsiz+2,row=4)
		self.Stat=tk.Button(self,text="MOVE DOWN",width=10,command=self.movedown).grid(column=rsiz+2,row=6)
		self.Fast=tk.Button(self,text="MOVE UP",width=10,command=self.moveup).grid(column=rsiz+2,row=5)
		global mat
		for m in range(rsiz):
			for n in range(rsiz):
				if n<rsiz/2:
					mat[m][n]=-1
				else :
					mat[m][n]=1	
		for m in range(rsiz):
			for n in range(rsiz):
				if mat[m][n]==2:
					self.buttons[m*rsiz + n].configure(bg="blue")
				elif mat[m][n]==3:
					self.buttons[m*rsiz + n].configure(bg="dark blue")
				elif mat[m][n]==-2:
					self.buttons[m*rsiz + n].configure(bg="green")
				elif mat[m][n]==-3:
					self.buttons[m*rsiz + n].configure(bg="dark green") 
				elif mat[m][n]==5:
					self.buttons[m*rsiz + n].configure(bg="black")
				elif mat[m][n]==-1:
					self.buttons[m*rsiz + n].configure(bg="light green")
				elif mat[m][n]==1:
					self.buttons[m*rsiz + n].configure(bg="light blue")
	def callback(self,phrase, listener):
		#print ": %s" % phrase
		global dict
		p=re.compile('.*attack.*',re.IGNORECASE)
		if p.match(phrase):
			#print "ding ding"
			listener.stoplistening()
			self.attack1()
			return
		q=re.compile('.*up.*',re.IGNORECASE)
		if q.match(phrase):
			#print "ding dong"
			listener.stoplistening()
			self.moveup()
			return
		s=re.compile('.*down.*',re.IGNORECASE)
		if s.match(phrase):
			#print "ding dang1"
			listener.stoplistening()
			self.movedown()
			return
		#dig=re.compile('[0-9]|[oO]ne|[tT]wo|[tT]hree|[fF]our|[fF]ive|[sS]ix|[sS]even|[eE]ight|[nN]ine|[tT]en')
		dig=re.compile('.*one.*|.*two.*|.*to.*|.*three.*|.*four.*|.*for.*|.*full.*|.*five.*|.*six.*|.*seven.*|.*eight.*|.*nine.*|.*ten.*|.*then.*|.*they.*',re.IGNORECASE)
		if dig.match(phrase):
			#d=int(phrase)
			if phrase.lower()=="one":
				d=1;
				speech.say("One")
			if phrase.lower()=="two" or phrase.lower()=="to":
				d=2;
				speech.say("Two")
			if phrase.lower()=="three":
				d=3;
				speech.say("Three")
			if phrase.lower()=="four" or phrase.lower()=="full" or phrase.lower()=="for":
				d=4;
				speech.say("Four")
			if phrase.lower()=="five":
				d=5;
				speech.say("Five")
			if phrase.lower()=="six":
				d=6;
				speech.say("Six")
			if phrase.lower()=="seven":
				d=7;
				speech.say("Seven")
			if phrase.lower()=="eight":
				d=8;
				speech.say("")
			if phrase.lower()=="nine":
				d=9;
				speech.say("")
			if phrase.lower()=="ten" or phrase.lower()=="then" or phrase.lower()=="they":
				d=10;
				speech.say("")
			#print "d= " , d
			#print dict[d]
			self.pressed(dict[d])
			return
		if phrase=="instructions".lower():
			#print "ahaha"
			listener.stoplistening()
			PageTwo.sayit()
	def pressed(self, index):
		global flag,dict
		global mat,turn,MAX
		mat2=[x[:] for x in mat]
		if flag==1 :
			#print("number pressed", index)
			global id,Kmaxg,Kmaxb
			#print(mat[index/rsiz][index%rsiz],index/rsiz,index%rsiz)
			#print("\n ",mat)
			if mat[index/rsiz][index%rsiz]== -2 and turn==-1 and Kmaxg:
				mat2[index/rsiz][index%rsiz]= -3
				turn=1
				Kmaxg=Kmaxg-1
				self.buttons[index].configure(bg = "dark green")
			elif mat[index/rsiz][index%rsiz]== 2 and turn==1 and Kmaxb:
				mat2[index/rsiz][index%rsiz]= 3
				turn=-1
				Kmaxb=Kmaxb-1
				self.buttons[index].configure(bg = "dark blue")
			elif mat[index/rsiz][index%rsiz]==-1 and turn==-1 and id<MAX:
				id=id+1
				mat2[index/rsiz][index%rsiz]= -2
				turn=1
				self.buttons[index].configure(bg = "green",text=id)
				dict[id]=index
			elif mat[index/rsiz][index%rsiz]==1 and turn==1 and id<MAX:
				id=id+1
				mat2[index/rsiz][index%rsiz]= 2
				turn=-1
				self.buttons[index].configure(bg = "blue",text=id)
				dict[id]=index
			mat=[row[:] for row in mat2]
			#print("\n ",mat)
		elif flag==0 :
			if mat[index/rsiz][index%rsiz]!=5 or mat[index/rsiz][index%rsiz]!=-1 or mat[index/rsiz][index%rsiz]!=1 :
				#print("flag =0 number pressed", index)
				#print("\n ",mat)
				row_num=index/rsiz
				if mat[index/rsiz][index%rsiz]== -2 and turn==-1:					
					#print("green soldier clicked!! \n")
					while mat[index/rsiz][index%rsiz]==-1 or mat[index/rsiz][index%rsiz]==5 or mat[index/rsiz][index%rsiz]==-2 or mat[index/rsiz][index%rsiz]==-3 :
						index = index + 1
						if(index/rsiz!=row_num):
							index=index-1
							break
						#print("rn=",row_num,"i/rs=",index/rsiz)
					#print("green side ",index,index/rsiz,index%rsiz)
					turn=1
					mat2[index/rsiz][index%rsiz]=5
				elif mat[index/rsiz][index%rsiz]==2 and turn==1:
					while mat[index/rsiz][index%rsiz]==1 or mat[index/rsiz][index%rsiz]==5 or mat[index/rsiz][index%rsiz]==2 or mat[index/rsiz][index%rsiz]==3:
						index = index - 1
						if(index/rsiz!=row_num):
							index=index+1
							break
						#print("rn=",row_num,"i/rs=",index/rsiz)
					turn=-1
					#print("blue side",index,index/rsiz,index%rsiz)
					mat2[index/rsiz][index%rsiz]=5
				elif mat[index/rsiz][index%rsiz]== -3 and turn==-1:					
					#print("green soldier clicked!! \n")
					# index = index + 1
					while any([mat[index/rsiz][index%rsiz]==-1,mat[index/rsiz][index%rsiz]==5,mat[index/rsiz][index%rsiz]==-2,mat[index/rsiz][index%rsiz]==-3]):
						index = index + 1
						if(index/rsiz!=row_num):
							index=index-1
							break
						#print("rn=",row_num,"i/rs=",index/rsiz)
					#print("green side ",index,index/rsiz,index%rsiz)
					turn=1
					mat2[index/rsiz][index%rsiz]=5
					mat2[index/rsiz+1][index%rsiz]=5
					mat2[index/rsiz-1][index%rsiz]=5
				elif mat[index/rsiz][index%rsiz]==3 and turn==1:
					#index = index - 1
					while any([mat[index/rsiz][index%rsiz]==1,mat[index/rsiz][index%rsiz]==5,mat[index/rsiz][index%rsiz]==2,mat[index/rsiz][index%rsiz]==3]) :
						index = index - 1
						if(index/rsiz!=row_num):
							index=index+1
							break
						#print("rn=",row_num,"i/rs=",index/rsiz)
					turn=-1
					#print("blue side",index,index/rsiz,index%rsiz)
					mat2[index/rsiz][index%rsiz]=5
					mat2[index/rsiz+1][index%rsiz]=5
					mat2[index/rsiz-1][index%rsiz]=5
		elif flag==2 :
			if mat[index/rsiz][index%rsiz]!=5 or mat[index/rsiz][index%rsiz]!=-1 or mat[index/rsiz][index%rsiz]!=1 :
				#print("move up number pressed", index)
				#print("\n ",mat)
				if any([mat[index/rsiz][index%rsiz]== -2,mat[index/rsiz][index%rsiz]== -3]) and turn==-1:					
					#print("green soldier clicked!! \n")
					t=self.buttons[index].cget("text")
					t_up=self.buttons[index-rsiz%size].cget("text")
					self.buttons[index-rsiz%size].configure(text=t)
					del dict[t]
					dict[t]=index+rsiz % size
					self.buttons[index].configure(text=t_up)
					tex=mat[index/rsiz-1][index%rsiz];
					mat2[index/rsiz-1][index%rsiz]=mat[index/rsiz][index%rsiz];
					mat2[index/rsiz][index%rsiz]=tex;
					turn=1;
					#print(t)
					#print("green side ",index,index/rsiz,index%rsiz)
					
				elif any([mat[index/rsiz][index%rsiz]==2, mat[index/rsiz][index%rsiz]== 3]) and turn==1:					
					#print("blue soldier clicked!! \n")
					t=self.buttons[index].cget("text")
					t_up=self.buttons[index-rsiz%size].cget("text")
					self.buttons[index-rsiz%size].configure(text=t)
					del dict[t]
					dict[t]=index+rsiz % size
					self.buttons[index].configure(text=t_up)
					tex=mat[index/rsiz-1][index%rsiz];
					mat2[index/rsiz-1][index%rsiz]=mat[index/rsiz][index%rsiz];
					mat2[index/rsiz][index%rsiz]=tex;
					turn=-1;
					#print(tex)
					#print("blue side ",index,index/rsiz,index%rsiz)
					
		elif flag==3 :
			if mat[index/rsiz][index%rsiz]!=5 or mat[index/rsiz][index%rsiz]!=-1 or mat[index/rsiz][index%rsiz]!=1 :
				#print("move down number pressed", index)
				#print("\n ",mat)
				if any([mat[index/rsiz][index%rsiz]== -2, mat[index/rsiz][index%rsiz]== -3]) and turn==-1:					
					#print("green soldier clicked!! \n")
					t=self.buttons[index].cget("text")
					t_dn=self.buttons[index+rsiz % size].cget("text")
					self.buttons[index+rsiz %size].configure(text=t)
					del dict[t]
					dict[t]=index+rsiz % size
					self.buttons[index].configure(text=t_dn)
					tex=mat[index/rsiz+1][index%rsiz];
					mat2[index/rsiz+1][index%rsiz]=mat[index/rsiz][index%rsiz];
					mat2[index/rsiz][index%rsiz]=tex;
					turn=1;
					#print(tex)
					#print("green side ",index,index/rsiz,index%rsiz)
					
				elif any([mat[index/rsiz][index%rsiz]==2, mat[index/rsiz][index%rsiz]== 3]) and turn==1:					
					#print("blue soldier clicked!! \n")
					t=self.buttons[index].cget("text")
					t_dn=self.buttons[index+rsiz % size].cget("text")
					self.buttons[index+rsiz%size].configure(text=t)
					del dict[t]
					dict[t]=index+rsiz % size
					self.buttons[index].configure(text=t_dn)
					tex=mat[index/rsiz+1][index%rsiz];
					mat2[index/rsiz+1][index%rsiz]=mat[index/rsiz][index%rsiz];
					mat2[index/rsiz][index%rsiz]=tex;
					turn=-1;
					#print(tex)
					#print("blue side ",index,index/rsiz,index%rsiz)
		mat=[row[:] for row in mat2]
		#print dict
		#print("\n ",mat)
		for m in range(rsiz):
			for n in range(rsiz):
			#listener = speech.listenforanything(callback)
				if mat[m][n]==2:
					self.buttons[m*rsiz + n].configure(bg="blue")
				elif mat[m][n]==3:
					self.buttons[m*rsiz + n].configure(bg="dark blue")
				elif mat[m][n]==-2:
					self.buttons[m*rsiz + n].configure(bg="green")
				elif mat[m][n]==-3:
					self.buttons[m*rsiz + n].configure(bg="dark green") 
				elif mat[m][n]==5:
					self.buttons[m*rsiz + n].configure(bg="black")
				elif mat[m][n]==-1:
					self.buttons[m*rsiz + n].configure(bg="light green")
				elif mat[m][n]==1:
					self.buttons[m*rsiz + n].configure(bg="light blue")
		if turn ==-1:
			self.Turn2.configure(bg="green")
		elif turn==1:
			self.Turn2.configure(bg="blue")
		listener = speech.listenforanything(self.callback)
	def sayit(self):
		speech.say("hi")	

	def attack1(self):
		#print("ping pong")
		global flag
		flag = 0
		speech.say("ATTACK MODE ON")
		self.stat1.configure(text="Attack")
	def moveup(self):
		#print("")
		global flag
		flag = 2
		speech.say("MOVE UP MODE ON")
		self.stat1.configure(text="Move Up")
	def movedown(self):
		#print("")
		global flag
		flag = 3
		speech.say("MOVE DOWN MODE ON")
		self.stat1.configure(text="Move Down")
class PageTwo(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		# inst="dnskjf"
		self.txt=""" 1. Each player gets an alternative chance to Place their soldiers. 
					\n 		Player can either place a soldier on an empty cell or place it on another solider to upgrade him to KING.
					\n 2. After done placing them, Choose any mode: ATTACK, MOVEUP or MOVEDOWN.
					\n 		then select your king or soldier to do the corresponding task.
					\n 3. Working of Attack Mode : 
					\n 	  	- Soldier can attack 1 cell of opponent's arena present in the same horizontal line of the soldier.          
					\n 		- King can attack 3 cell of opponent's arena : one present in the same horizontal line of the king and the other cells 
					\n		  present above and below it.
					\n 4. The GAME Ends when there are no moves left for any of the players and 
					\n 		player whose arena is destroyed the most, loses and his/her opponent wins"""
		self.inst= """ 1.... Each player gets an alternative chance to Place their soldiers.
				   Player can either place a soldier on an empty cell or place it on another solider to upgrade him to KING.
				2.... After done placing them, Choose any mode: ATTACK, MOVE UP or MOVEDOWN.
					then select your king or soldier to do the corresponding task.
				 3.... Working of Attack Mode : 
					Soldier can attack 1 cell of opponent's arena present in the same horizontal line of the soldier.          
					King can attack 3 cells of opponent's arena : one present in the same horizontal line of the king and the other cells present above and below it.
				4.... the GAME Ends when there are no moves left for any of the players and player whose arena is destroyed the most loses and his or her opponent wins"""
		label = tk.Label(self, text="Instructions!!!", font=LARGE_FONT)
		label.grid(column=0,row=0)
		label1 = tk.Label(self, text=self.txt, justify=LEFT,font=LARGE_FONT)
		label1.grid(column=0,row=1)
		#self.sayit()
		button21 = tk.Button(self, text="SAY IT",
							command=self.sayit)
		button21.grid(column=0,row=2)

		button1 = tk.Button(self, text="Back to Home",
							command=lambda: controller.show_frame(StartPage))
		button1.grid(column=0,row=3)

		button2 = tk.Button(self, text="Continue Game",
							command=lambda: controller.show_frame(PageOne))
		button2.grid(column=0,row=4)
		
	def sayit(self):
		speech.stoplistening()
		speech.say(self.inst)
		#speech.say("hey hey")


app = SeaofBTCapp()
app.geometry("1200x500")
app.mainloop()
