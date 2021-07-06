#Window size 500 350
#width = 20
#heigth = 202
from tkinter import *
from tkinter import Tk, Label, Button, Entry, IntVar, END, W, font
import random
import time
import math
from math import log10, floor
import numpy as np
from model_imp.py import model_imp


def round_sig(x, sig=2):
  return round(x, sig-int(floor(log10(abs(x))))-1)

class GUI:
    
    def __init__(self, master):
        print(font.names())
        self.master = master
        master.title("Network Management System")

        self.numberNodes = 0
        self.powerConsumption = 0
        self.Througput = 0

        self.sfCongestion = [0]*6
        
        #Initializing all the variables
        self.Power = np.array([])
        self.SpreadingFactor = np.array([])
        self.CodingRate = np.array([])


        self.SFallocation = [0]*6
        self.nodesDistance = np.array([])
        self.nodesLos = np.array([])
        self.nodesWall = np.array([])
        self.WIDTH = 1200
        self.HEIGTH = 700
        self.master.geometry("1100x700")
        self.master.configure(background = 'dark slate grey')
        self.lbl = Label(master, text="Welcome")
        Tops = Frame(self.master,bg="black",width = 1600,height=100,relief=SUNKEN)
        Tops.pack(side=TOP)

        
        
        self.informationFrame = Frame(self.master,bg="black",width = 200,height=300,relief=SUNKEN)
        self.informationFrame.place(x=0,y=self.HEIGTH/2-75)
        
        self.bottomFrame = Frame(self.master,bg="black",width = 1600,height=150,relief=SUNKEN)
        self.bottomFrame.place(x=0,y=600)
        #pack(side=BOTTOM)

        ####Creating Canvas
        self.bottomCanvas = Canvas(self.bottomFrame, bg="black", height=200, width=1600,relief=SUNKEN,highlightthickness=0)
        self.bottomCanvas.pack()


        self.centerFrame = Frame(self.master,width = 500,height=500,relief=SUNKEN, bg = 'dark green')
        #self.centerFrame.pack(side=LEFT)
        
        self.buttonFrame = Frame(self.master ,width = 250,height=700,relief=SUNKEN,bg= 'spring green')
        self.buttonFrame.pack(pady = 50)#place(x=self.WIDTH/2,y=self.HEIGTH/2-75)

        self.numberNodes_label = Label(self.informationFrame, font=( 'aria' ,16, 'bold' ),text="Number of Nodes: " + str(self.numberNodes),fg="steel blue",bd=10,width = 20,bg = 'light yellow')
        self.numberNodes_label.grid(column=0,row=0)

        self.powerConsumption_label = Label(self.informationFrame, font=( 'aria' ,16, 'bold' ),text="Power Consumption: " + str(self.powerConsumption),fg="steel blue",bd=10,width = 20,bg = 'light yellow')
        self.powerConsumption_label.grid(column=0,row=1)

        self.Througput_label = Label(self.informationFrame, font=( 'aria' ,16, 'bold' ),text="Througput: " + str(self.Througput),fg="steel blue",bd=10,width = 20,bg = 'light yellow')
        self.Througput_label.grid(column=0,row=3)

        #------------------TIME--------------
        localtime=time.asctime(time.localtime(time.time()))
        #-----------------INFO TOP------------
        lblinfo = Label(Tops, font=( 'TkHeadingFont' ,30, 'bold' ),text="Network Management System",fg="steel blue",bg='black',bd=10,justify = CENTER)
        lblinfo.grid(row=2,column=0,pady = 40)
        lblinfo.configure(text="Network Management System")
        lblinfo = Label(Tops, font=( 'aria' ,20, ),text=localtime,fg="steel blue",anchor=W)
       # lblinfo.grid(row=2,column=0,pady =0)

       # self.lbl.place(x=0, y=1)
        self.lb2 = Label(self.centerFrame, state = "disabled",width = 15)
        self.lb3 = Label(self.centerFrame, state = "disabled",width = 15)
        self.lb4 = Label(self.centerFrame, state = "disabled", width= 15)
        self.lb5 = Label(self.centerFrame,fg = "blue",bg="brown",bd=10,font=( 'aria' ,16, 'bold' ))
        self.lb6 = Label(self.centerFrame,fg = "blue",bg="brown",bd=10,font=( 'aria' ,16, 'bold' ))
        self.lb7 = Label(self.centerFrame, fg = "blue",bg="brown",bd=10,font=( 'aria' ,16, 'bold' ))
        #self.addNodeBtn2 = Button(master, text="Enter", command=secondMenu)

        

        self.addNodeBtn = Button(self.buttonFrame, text="Add Node", command=self.addNode ,height = 5, width = 20,bg = "turquoise1", font=( 'aria' ,20, 'bold' ))
        self.addNodeBtn.grid(column=0,row=0)#,pady = 2, columnspan = 1)

        self.displayInfoBtn = Button(self.buttonFrame, text="Display Info", height = 5, width = 20, command=self.DisplayInfo,bg = "turquoise1",font=( 'aria' ,20, 'bold' ))
        self.displayInfoBtn.grid(column=0,row=1)#,pady = 2, columnspan = 1)
        """ btn_displayInfo = Button(master, text="Display network information", command=displayInfo)
        btn3 = Button(master, text="Enter", command=displayInfo) """

    def all_children (self,window) :
        _list = window.winfo_children() 

        for item in _list :
            if item.winfo_children() :
                _list.extend(item.winfo_children())

        return _list

    def addNode(self):

        self.addNodeBtn.configure(height = 3, width = 10,bg = "turquoise1", font=( 'aria' ,15, 'bold' ),pady=0)
        self.displayInfoBtn.configure(height = 3, width = 10,bg = "turquoise1", font=( 'aria' ,15, 'bold' ))
        self.addNodeBtn2 = Button(self.buttonFrame, text="Enter", command=self.updateInfo, height = 3, width = 10,bg = "turquoise1", font=( 'aria' ,15, 'bold' ))
        self.addNodeBtn2.grid(column=0,row=2)

        self.buttonFrame.pack(side=RIGHT)
        self.centerFrame.place(x=300,y=self.HEIGTH/2-75)

        widget_list = self.all_children(self.centerFrame)
        for item in widget_list:
            item.grid_forget()

        self.Distance = Entry(self.centerFrame,width=15,bd = 5,font=( 'aria' ,20, 'bold' ),bg = 'bisque')
        self.Los = Entry(self.centerFrame,width=15, bd = 5,font=( 'aria' ,20, 'bold' ),bg = 'bisque')
        self.Walls = Entry(self.centerFrame,width=15, bd = 5,font=( 'aria' ,20, 'bold' ),bg = 'bisque')
        self.PRRentry = Entry(self.centerFrame,width=15, bd = 5,font=( 'aria' ,20, 'bold' ),bg = 'bisque')
        #self.centerFrame.place(x=200,y=200)
        self.lbl.configure(text="Please enter the information")
        self.lb2.configure(text ="Distance (m)", state = "active", width = 20, fg = "blue",bg="brown",bd=10,font=( 'aria' ,20, 'bold' ))
        """ txtburger = Entry(centerFrame,font=('ariel' ,16,'bold'), textvariable=Burger , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
        5txtburger.grid(row=3,column=1) """
        self.lb2.grid(row=0, column=0)
        self.Distance.grid(row=0,column=1)
        self.lb3.configure(text ="Line of Sight ", state = "active", width = 20,fg = "blue",bg="brown",bd=10,font=( 'aria' ,20, 'bold' ))
        self.lb3.grid(row=1, column=0)
        self.Los.grid(row=1, column=1)
        self.lb4.configure(text ="Number of Walls ", state = "active", width = 20,fg = "blue",bd=10,font=( 'aria' ,20, 'bold' ))
        self.lb4.grid(row=2, column=0)
        self.Walls.grid(row=2, column=1)
        self.lb5.configure(text ="Required PRR ", state = "active", width = 20,fg = "blue",bd=10,font=( 'aria' ,20, 'bold' ))
        self.lb5.grid(row=3, column=0)
        self.PRRentry.grid(row=3, column=1)
        
    def updateInfo(self):
        w
        self.addNodeBtn2.destroy()
        wrongString = "Incorrect "
        wrongVar = False
        distanceText = int(self.Distance.get())
        Lostext = int(self.Los.get())
        WallText = int(self.Walls.get())
        PRRText = float(self.PRRentry.get())
        #self.addNodeBtn["state"] = "disabled"
        if(distanceText<0):
            wrongVar = True
            wrongString += "Power "
        
       
            

        if(Lostext<0):
            wrongVar = True
            wrongString += "SF "

        else:
            if(Lostext>0):
                Lostext = 1
            
            
            

        if(PRRText < 0 or PRRText > 1):
            wrongVar = True


        if(WallText<0):
            wrongVar = True
            wrongString += "CR "

        else:
            if(WallText>3):
                WallText = 3
            

        if(wrongVar):
            self.lbl.configure(text= wrongString + ".Please re-enter.")
        else:  
            self.lbl.configure(text="Node has been added")
            self.assignParameters(distanceText,Lostext,WallText,PRRText)
            

        self.refreshWindow()

    def assignParameters(self,distance,Los,Walls,PRR):
        #This function assigns parameter using machine learning
        tempPower = np.array([])
        #Predict for each SF
        for x in range(6):
            effectivePRR = PRR*(1-self.sfCongestion[x]*100)
            if(effectivePRR <= 1):
                tempPower = np.append(tempPower,self.predictModel(distance, Los, Walls, effectivePRR, x+7))
            else:
                tempPower = np.append(tempPower,100) #Meaing the setting is not possible. 100 is choosen arbitrary as max power is 27 dB

        #Minimizing the power
        temp = np.min(tempPower)

        if(temp<= 27): #Max power limit is 27dB
            index = np.argmin(tempPower) #Index determines which SF
            self.Power = np.append(self.Power,temp)
            self.SpreadingFactor = np.append(self.SpreadingFactor,index+7)
            self.CodingRate = np.append(self.CodingRate,5) #Using constant coding rate for now 
            self.update_SF_congestion(index+7,10) #Updating congestion

            print(str(temp)+str(index+7))

            #Updating all the variables
            self.numberNodes += 1
            self.nodesWall = np.append(self.nodesWall,Walls)
            self.nodesLos = np.append(self.nodesLos,Los)
            self.nodesDistance = np.append(self.nodesDistance,distance)
            self.SFallocation[index] += 1



        else:
            print("Power allocation not possible")

    #####################################
    def predictModel(self,distance,Los,Walls,SF,PRR):
        
        model_imp()
        
        return int(SF)

    def DisplayInfo(self):
       # self.centerFrame.pack_forget()
        self.addNodeBtn.configure(height = 3, width = 10,bg = "turquoise1", font=( 'aria' ,15, 'bold' ),pady=0)
        self.displayInfoBtn.configure(height = 3, width = 10,bg = "turquoise1", font=( 'aria' ,15, 'bold' ))
        self.addNodeBtn2 = Button(self.buttonFrame, text="Enter", command=self.updateInfo, height = 3, width = 10,bg = "turquoise1", font=( 'aria' ,15, 'bold' ))
        self.addNodeBtn2.grid(column=0,row=2)

        self.buttonFrame.pack(side=RIGHT)
        self.centerFrame.place(x=300,y=self.HEIGTH/2-75)
        
        widget_list = self.all_children(self.centerFrame)
        for item in widget_list:
            item.grid_forget()


        self.centerFrame.place(x=400,y=self.HEIGTH/2-125)
        widget_list = self.all_children(self.centerFrame)
        for item in widget_list:
            item.grid_forget()
        self.centerFrame.grid_forget()
        self.lbl.configure(text="Number of active devices are:" + str(self.numberNodes),width=20, bg = "thistle1")
        self.lb2.configure(text="SF-7: "+ str(self.SFallocation[0]) + " (" + "{:.2f}".format(self.sfCongestion[0]*100) + "%)",width=20,font=( 'aria' ,20, 'bold' ), bg = "thistle1")
        self.lb3.configure(text="SF-8: "+ str(self.SFallocation[1]) + " (" + "{:.2f}".format(self.sfCongestion[1]*100) + "%)",width=20,font=( 'aria' ,20, 'bold' ), bg = "thistle1")
        self.lb4.configure(text="SF-9: "+ str(self.SFallocation[2]) + " (" + "{:.2f}".format(self.sfCongestion[2]*100) + "%)",width=20,font=( 'aria' ,20, 'bold' ), bg = "thistle1")
        self.lb5.configure(text="SF-10: "+ str(self.SFallocation[3]) + " (" + "{:.2f}".format(self.sfCongestion[3]*100) + "%)",width=20,font=( 'aria' ,20, 'bold' ), bg = "thistle1")
        self.lb6.configure(text="SF-11: "+ str(self.SFallocation[4]) + " (" + "{:.2f}".format(self.sfCongestion[4]*100) + "%)",width=20,font=( 'aria' ,20, 'bold' ), bg = "thistle1")
        self.lb7.configure(text="SF-12: "+ str(self.SFallocation[5]) + " (" + "{:.2f}".format(self.sfCongestion[5]*100) + "%)",width=20,font=( 'aria' ,20, 'bold' ), bg = "thistle1",bd=10)
        self.lb2.grid(row=0, column=0)
        self.lb3.grid(row=1, column=0)
        self.lb4.grid(row=2, column=0)
        self.lb5.grid(row=3, column=0)
        self.lb6.grid(row=4, column=0)
        self.lb7.grid(row=5, column=0)
        #self.lb4.grid(row=2, column=0)
    
    def refreshWindow(self):
        self.Througput_label.configure(text="Througput: " + str(self.Througput))
        self.numberNodes_label.configure(text="Number of Nodes: " + str(self.numberNodes))
        self.powerConsumption_label.configure(text = "Power Consumption: " + str(self.powerConsumption))

    def TimeOnAirCal(self,n_size, n_sf, n_bw=125,n_cr=1, n_preamble=8,enable_eh=True, enable_crc=True):

        r_sym = (n_bw*1000.) / math.pow(2,n_sf)
        t_sym = 1000. / r_sym
        t_preamble = (n_preamble + 4.25) * t_sym
        # LDRO
        v_DE = 0
        
        #Auto enable LDRO
        if t_sym > 16:
            v_DE = 1
       
        # IH
        v_IH = 0
        if not enable_eh:
            v_IH = 1
        # CRC
        v_CRC = 1
        if enable_crc == False:
            v_CRC = 0
        #
        a = 8.*n_size - 4.*n_sf + 28 + 16*v_CRC - 20.*v_IH
        b = 4.*(n_sf-2.*v_DE)
        n_payload = 8 + max(math.ceil(a/b)*(n_cr+4), 0)
        t_payload = n_payload * t_sym
        t_packet = t_preamble+ t_payload

        return t_packet

    def update_SF_congestion(self,n_sf,n_size):   
        time = self.TimeOnAirCal(n_sf=n_sf,n_size=n_size)

        #Assuming 60 sec Aloha access
        ratio = time/(60*1000)
        print(ratio)
        
        #Updating the congestion in each of these
        self.sfCongestion[n_sf-7] += ratio
        print(self.sfCongestion[0])
        print(n_sf-7)



master = Tk()
my_gui = GUI(master)
master.mainloop()