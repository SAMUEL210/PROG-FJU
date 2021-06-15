# @ FJU de Lyon // 
# @ FJU (Force Jeune Universelle ) LYON  //===>
# @ CAU (Centre D'acceuil Universel) LYON @ 101 Rue D'envers Jean Mace Lyon

#
# Nov 2017 by ==>
# Samuel Ibou Marone // @SAMI, @THe_CHoOSen_One // @SAMI, @ThE_HAckEr_One
# 

# ----------------------------------------------------------------- #
#   @ Script Graphique des activites du Samedi de La FJU de Lyon    #
#                        tous les Samedi a 13h 30                   #
#                               @ By S@MI                           #
# ----------------------------------------------------------------- #

from tkinter import *
from tkinter.messagebox import *
from turtle import *
from pygame import *
from datetime import datetime
import math, random, time

class Tribu(): 
    def __init__(self):
        self.CODE = ['²','~','\n',' ', 'i', 'U','§','j', '[','©', '}','k', '(','P', 'l', ']','D', 'm', 'S', 'n', 'o', '-', '|', '&', 'p', 'q', 'C','{', 'a', 'b', 'c', 'd', 'e','E', 'H', 'F','_', 'é', 'ç', 'ê','ô', 'â', 'J', 'K', '8', 'L', '^', 'M', '\'', 'N','\"', 'O', 'Y', 'Z', 'f', 'g', 'h', 'r', 's', 't', 'u', 'v', 'w', 'x', '0', 'y', 'z' , '1', '2','A', '4', 'W', '5','G', '6', 'I','7', ",", '@', '!', '.', '?', ';', ':', '/', "'", '*', '+', 'T', '3', 'V', 'B', '#', 'Q', 'R', 'X', ')', 'î', '9']
        self.fen1 = Tk()
        self.w, self.h = self.fen1.winfo_screenwidth(), self.fen1.winfo_screenheight()
        self.fen1.overrideredirect(1)
        self.fen1.geometry("%dx%d+0+0" % (self.w, self.h))
        self.fen1.title('FJU LYON')
        self.fen1.iconbitmap('images/FJU_Lyon.ico')
        self.fen1.configure(bg = "light sea green")

        with open('fichiers/app.fju', 'r') as f:
            val = self.decryptbin(f.read())
        self.variablement = StringVar()
        self.variablement.set('???')
        
        menubar = Menu(self.fen1)
        
        menu1 = Menu(menubar, tearoff=0)
        if val == 'TheChoosenOne':
            menu1.add_command(label='Controler', command=self.controler)
            menu1.add_separator()
        menu1.add_command(label='Terminer', command=self.Terminer)
        menu1.add_separator()
        menu1.add_command(label='Quitter', command=self.Quitter)
        menubar.add_cascade(label='FENETRE', menu=menu1)

        menu2 = Menu(menubar, tearoff=0)
        menu2.add_command(label='Afficher Point', command=self.afficherPoint)
        menu2.add_separator()
        menu2.add_command(label='Masquer Point', command=self.masquerPoint)
        menubar.add_cascade(label='AFFICHAGE', menu=menu2)

        menu3 = Menu(menubar, tearoff=0)
        menu3.add_separator()
        menu3.add_command(label='Changer Temps', command=self.ChangerTemps)
        menubar.add_cascade(label='TEMPS', menu=menu3)

        menu4 = Menu(menubar, tearoff=0)
        menu4.add_separator()
        menu4.add_command(label='Demarrer son (alarme)', command=self.Demarreralarme)
        menu4.add_separator()
        menu4.add_command(label='Stop son (alarme)', command=self.Stopalarme)
        menu4.add_separator()
        menu4.add_command(label='Activer son Fin de Temps', command=self.ActiverSonTemps)
        menu4.add_separator()
        menu4.add_command(label='Stoper son Fin de Temps', command=self.StopperSonTemps)
        menu4.add_separator()
        menu4.add_command(label='Lire une Musique', command=self.LireMusique)
        menubar.add_cascade(label='SONS', menu=menu4)

        menu5 = Menu(menubar, tearoff=0)
        menu5.add_separator()
        menu5.add_command(label='Ajouter/Enlever Point', command=self.dempointNephtalie)
        menubar.add_cascade(label='NEPHTALIE', menu=menu5)

        menu6 = Menu(menubar, tearoff=0)
        menu6.add_separator()
        menu6.add_command(label='Ajouter/Enlever Point', command=self.dempointEphraim)
        menubar.add_cascade(label='EPHRAIM', menu=menu6)

        menu7 = Menu(menubar, tearoff=0)
        menu7.add_separator()
        menu7.add_command(label='Ajouter/Enlever Point', command=self.dempointJudah)
        menubar.add_cascade(label='JUDAH', menu=menu7)

        menu8 = Menu(menubar, tearoff=0)
        menu8.add_separator()
        menu8.add_command(label='Ajouter/Enlever Point', command=self.dempointBenjamin)
        menubar.add_cascade(label='BENJAMIN', menu=menu8)

        menu9 = Menu(menubar, tearoff=0)
        menu9.add_command(label='Force Jeune Universel Lyon', command=self.fjuLyon)
        menu9.add_command(label='Info App', command=self.detail_App)
        menubar.add_cascade(label='FJU LYON', menu=menu9)
        
        menu10 = Menu(menubar, tearoff=0)
        menu10.add_command(label='Contacter', command=self.Contact)
        menubar.add_cascade(label='?', menu=menu10)
         
        self.fen1.config(menu=menubar)
        
        fram101 = Frame(self.fen1, width=self.w , height=100, bg='white')
        fram101.pack(side=TOP)
        label1 = Label(fram101, text='FORCE JEUNE UNIVERSELLE LYON', fg='firebrick1', font='Algerian 60 bold', bg='white')
        label1.pack()
        label1.pack_propagate(False)
        
        textverset = StringVar()
        textresultat = StringVar()
        textinfo = StringVar()
        textinfoplus = StringVar()
        textinfoEv = StringVar()
        with open('fichiers/vers.fju', 'r') as self.f:
            textverset.set(self.f.read())
        with open('fichiers/result.fju', 'r') as self.f:
            textresultat.set(self.f.read())
        with open('fichiers/info.fju', 'r') as self.f:
            textinfo.set(self.f.read())
        with open('fichiers/info+.fju', 'r') as self.f:
            textinfoplus.set(self.f.read())
        with open('fichiers/infoEv.fju', 'r') as self.f:
            textinfoEv.set(self.f.read())
        
            
        marquee = Marquee(fram101, text=textverset.get() + '\t\t [SEMAINE PASSE] ' + textresultat.get() + '\t\t ' + textinfo.get() + '\t\t' + textinfoplus.get() + textinfoEv.get(), borderwidth=1, relief="sunken")
        marquee.pack(side=BOTTOM, fill=X)
        marquee.pack_propagate(False)
        
        fram2 = Frame(self.fen1, width =self.w/2-150, height =(self.h-152)/2, bg='steel blue')
        fram2.place(x=0, y=136)
        fram2.pack_propagate(False)
        label2 = Label(fram2, text='NEPHTALIE', font='Algerian 54 bold', bg='steel blue')
        label2.pack(side=TOP)
        self.pointneph = StringVar()
        self.pointneph.set(0)
        self.pointnephtalie = 0
        self.label3 = Label(fram2,textvariable=self.pointneph, font='Algerian 54 bold', bg='steel blue')
        self.label3.pack()
        photo1 = PhotoImage(file='images/Nephtalie.gif')
        item1 = Label(fram2, image=photo1, bg='steel blue')
        item1.photo = photo1
        item1.pack(side=BOTTOM)
      
        fram3 = Frame(self.fen1, width =self.w/2-150, height =(self.h-152)/2, bg='grey99')
        fram3.place(x=self.w/2+150, y=136)
        fram3.pack_propagate(False)
        label4 = Label(fram3, text='EPHRAIM', font='Algerian 54 bold', bg='grey99')
        label4.pack()
        self.pointeph = StringVar()
        self.pointeph.set(0)
        self.pointephraim = 0
        self.label5 = Label(fram3, textvariable=self.pointeph, font='Algerian 54 bold', bg='grey99')
        self.label5.pack()
        photo2 = PhotoImage(file='images/Ephraim.gif')
        item2 = Label(fram3, image=photo2, bg='grey99')
        item2.photo = photo2
        item2.pack(side=BOTTOM)

        fram4 = Frame(self.fen1, width =self.w/2-150, height =(self.h-155)/2, bg='red4')
        fram4.place(x=0, y=135+(self.h-150)/2)
        fram4.pack_propagate(False)
        label6 = Label(fram4, text='JUDAH', font='Algerian 54 bold', bg='red4')
        label6.pack()
        self.pointjud = StringVar()
        self.pointjud.set(0)
        self.pointjudah = 0
        self.label7 = Label(fram4, textvariable=self.pointjud, font='Algerian 54 bold', bg='red4')
        self.label7.pack()
        photo3 = PhotoImage(file='images/Judah.gif')
        item3 = Label(fram4, image=photo3, bg='red4')
        item3.photo = photo3
        item3.pack(side=BOTTOM)

        fram5 = Frame(self.fen1, width =self.w/2-150, height =(self.h-155)/2, bg='green4')
        fram5.place(x=self.w/2+150, y=135+(self.h-150)/2)
        fram5.pack_propagate(False)
        label8 = Label(fram5, text='BENJAMIN', font='Algerian 54 bold', bg='green4')
        label8.pack()
        self.pointbenj = StringVar()
        self.pointbenj.set(0)
        self.pointbenjamin = 0
        self.label9 = Label(fram5, textvariable=self.pointbenj, font='Algerian 54 bold', bg='green4')
        self.label9.pack()
        photo4 = PhotoImage(file='images/Benjamin.gif')
        item4 = Label(fram5, image=photo4, bg='green4')
        item4.photo = photo4
        item4.pack(side=BOTTOM)

        self.fram6 = Frame(self.fen1, width=305, height=(self.h-153)/2, bg='gray60')
        self.fram6.place(x=self.w/2-150,y=136)
        self.fram6.pack_propagate(False)
        self.lab = Label(self.fram6,text='40:00', fg='red', font='algrian 84 bold', bg='gray60')
        self.lab.pack(fill='x')
        self.lab1 = Label(self.fram6,text='00:00', fg='red', font='algrian 66 bold', bg='gray60')
        self.lab1.pack(fill='x')
        
        Button(self.fram6, text='Start', bg='bisque',command=self.lancer_Minuteur1, font='calibri 12 bold italic').pack(side=BOTTOM, anchor='s', pady=3)
        self.can1 = Canvas(self.fen1, width=300, height=(self.h-155)/2)
        self.can1.place(x=self.w/2-150,y=135+(self.h-150)/2)
        
        fram7 = Frame(self.fram6, width=300,bg='gray60')
        fram7.pack(side=BOTTOM)
        fram17 = Frame(self.fram6, bg='gray60')
        fram17.pack(side=BOTTOM)
        
        Label(fram17, text='Minutes', font='calibri 8 italic', bg='gray60').pack(side=LEFT)
        Label(fram17, text='secondes', font='calibri 8 italic', bg='gray60').pack(side=LEFT)
        
        
        
        self.entremins = Spinbox(fram7, from_=0, to=45, width=5, bg='bisque')
        self.entremins.pack(anchor='e', side=LEFT, padx=2, )
        self.entresec = Spinbox(fram7, from_=0, to=59, width=5, bg='bisque')
        self.entresec.pack(anchor='e', side=LEFT, padx=2,)
        
        self.LARGEUR = 300
        self.HAUTEUR = 309
        self.RAYON = 15

        # position initiale au milieu
        self.X = random.randint(0, (self.h-150)/2)
        self.X1 = random.randint(0, (self.h-150)/2)
        self.X2 = random.randint(0, (self.h-150)/2)
        self.X3 = random.randint(0, (self.h-150)/2)
        self.Y = random.randint(0, (self.h-150)/2)
        self.Y1 = random.randint(0, (self.h-150)/2)
        self.Y2 = random.randint(0, (self.h-150)/2)
        self.Y3 = random.randint(0, (self.h-150)/2)

        # direction initiale aléatoire
        vitesse = random.uniform(1.8,2)*5
        angle = random.uniform(random.randint(0,5),random.randint(0,20)*math.pi)
        angle1 = random.uniform(random.randint(0,5),random.randint(0,20)*math.pi)
        angle2 = random.uniform(random.randint(0,5),random.randint(0,20)*math.pi)
        angle3 = random.uniform(random.randint(0,5),random.randint(0,20)*math.pi)
        self.DX = vitesse*math.cos(angle)
        self.DX1 = vitesse*math.cos(angle1)
        self.DX2 = vitesse*math.cos(angle2)
        self.DX3 = vitesse*math.cos(angle3)
        self.DY = vitesse*math.sin(angle)
        self.DY1 = vitesse*math.sin(angle1)
        self.DY2 = vitesse*math.sin(angle2)
        self.DY3 = vitesse*math.sin(angle3)
        
        self.Balle = self.can1.create_oval(self.X-self.RAYON,self.Y-self.RAYON,self.X+self.RAYON,self.Y+self.RAYON,width=1,fill='green4')
        self.Balle1 = self.can1.create_oval(self.X1-self.RAYON,self.Y1-self.RAYON,self.X1+self.RAYON,self.Y1+self.RAYON,width=1,fill='red4')
        self.Balle2 = self.can1.create_oval(self.X2-self.RAYON,self.Y2-self.RAYON,self.X2+self.RAYON,self.Y2+self.RAYON,width=1,fill='steel blue')
        self.Balle3 = self.can1.create_oval(self.X3-self.RAYON,self.Y3-self.RAYON,self.X3+self.RAYON,self.Y3+self.RAYON,width=1,fill='gray60')

        self.lab1.destroy()
        self.lab1 = Label(self.fram6,text='00:00', fg='red', font='algrian 68 bold', bg='gray60')
        self.lab1.pack(fill='x')

        self.deplacement()
        self.deplacement1()
        self.deplacement2()
        self.deplacement3()
        
        self.lancer_Minuteur()

        self.flag1 = 0
        self.depart1 = 0

        self.fen1.mainloop()

    def Terminer(self):
        if self.pointnephtalie == 0 and self.pointephraim ==0 and self.pointjudah == 0 and self.pointbenjamin == 0:
            showinfo('AUCUN POINT COMPTABILISE', 'AUCUN POINT COMPTABILISÉ !!!\n\n VEUILLEZ APPUYER SUR QUITTER !!!')
        elif self.pointnephtalie == self.pointephraim   or self.pointnephtalie == self.pointjudah or self.pointnephtalie == self.pointbenjamin \
        or self.pointephraim == self.pointjudah or self.pointephraim == self.pointbenjamin \
        or self.pointjudah == self.pointbenjamin:
            showinfo('EGALITE','UNE OU PLUSIEURS EGALITEE(S) DETECTEE(S) VEUILLEZ LES DEPARTAGER !!!')
                    
        else:
            self.sons = mixer.init()
            self.sons = mixer.Sound('sons/Eye Of The Tiger .ogg')
            self.sons.set_volume(5)
            self.sons.play()
            self.fen = Toplevel(self.fen1)
            self.fen.geometry('700x650+330+60')
            self.fen.overrideredirect(1)
            self.fen.grab_set()
            self.fen.focus_set()
            self.fen.config(bg='light sea green')
            
            frametitle = Frame(self.fen, width=700, bg='light sea green')
            frametitle.pack(side=TOP, fill=X)
            Label(frametitle, text='FJU LYON', font='algerian 68 bold', bg='light sea green', fg='red4').pack()
            date = datetime.now()
            Label(frametitle, text='%s/%s/%s' % (date.day, date.month, date.year), font='algerian 20 bold', bg='light sea green', fg='red4').pack()
            
            Point = {'NEPHTALIE':self.pointnephtalie, 'EPHRAIM':self.pointephraim, 'JUDAH':self.pointjudah, 'BENJAMIN':self.pointbenjamin}
            Val = [Point['NEPHTALIE'], Point['EPHRAIM'],Point['JUDAH'], Point['BENJAMIN']]
            Val = sorted(Val)
            Premier = Val[3]
            Second = Val[2]
            Trois = Val[1]
            Dernier = Val[0]
            
            for i in Point:
                if Point[i] == Premier:
                    self.Vainqueur = {'NOM':i, 'Point':Premier}
                if Point[i] == Second:
                    self.Deuxieme = {'NOM':i, 'Point':Second}
                if Point[i] == Trois:
                    self.Troisieme = {'NOM':i, 'Point':Trois}
                if Point[i] == Dernier:
                    self.Quatrieme = {'NOM':i, 'Point':Dernier}

        
            fram = Frame(self.fen, bg ='light sea green')
            fram.pack()
            self.labvainqueur = Label(fram, text='Vainqueur est: ???', fg='red4', font='algerian 32 bold', bg='light sea green')
            self.labvainqueur.pack(pady=30)

            self.labsecond = Label(fram, text='Le second est: ???', fg='red4', font='algerian 32 bold', bg='light sea green')
            self.labsecond.pack(pady=30)

            self.labtroisieme = Label(fram, text='Le Troisieme est: ???', fg='red4', font='algerian 32 bold', bg='light sea green')
            self.labtroisieme.pack(pady=30)
            
            self.labquatrieme = Label(fram, text='Le Quatrieme est: ???', fg='red4', font='algerian 32 bold', bg='light sea green')
            self.labquatrieme.pack(pady=30)

            self.labvainqueur.after(21000, self.Vainq)
            self.labsecond.after(20000, self.Second)
            self.labtroisieme.after(16500, self.Trois)
            self.labquatrieme.after(9500, self.Quatr)
            self.fen.after(24000, self.fin)
                          
            try:
                with open('fichiers/result.fju', 'w') as f:
                    f.write('[Vainqueur]: %s\t[Deuxieme]: %s\t[Troisieme]: %s\t[Quatrieme]: %s' % (self.Vainqueur['NOM'], self.Deuxieme['NOM'], self.Troisieme['NOM'], self.Quatrieme['NOM']))
            except:
                with open('fichiers/result.fju', 'x') as f:
                    f.write('[Vainqueur]: %s\t[Deuxieme]: %s\t[Troisieme]: %s\t[Quatrieme]: %s' % (self.Vainqueur['NOM'],self. Deuxieme['NOM'], self.Troisieme['NOM'], self.Quatrieme['NOM']))

            with open('fichiers/log.fju', 'a') as f:
                f.write('%s/%s/%s\t\t%sh %s mins %s sec\t\tSession Ferme !!!\n' % (date.day, date.month, date.year, date.hour, date.minute, date.second))

    def cryptbin (self, chaine):
        liste = list(chaine)
        IN = []
        BIN = []
        for i in liste:
            if i in self.CODE:
                ind = self.CODE.index(i)
                IN.append(ind)
        for i in IN:
            BIN.append(bin(i))
        return "".join(BIN)

    def debin(self, chaine):
        chaine = list(chaine)
        chaine.reverse()
        val = 0
        tot = 0
        for i in chaine:
            if i == '1':
                tot += 2 ** val
            val += 1
        return int(tot)

    def decryptbin(self, chaine):
        valeur = []
        liste  = []
        chaine = chaine.split('0b')
        try:
            chaine.remove('')
        except:
            zero = 0
        for i in chaine:
            valeur.append(self.debin(i))
        for i in valeur:
            liste.append(self.CODE[i])
        return "".join(liste)
    
    def masquerPoint(self):
        self.label3.config(textvariable= self.variablement)
        self.label5.config(textvariable= self.variablement)
        self.label7.config(textvariable= self.variablement)
        self.label9.config(textvariable= self.variablement)

    def afficherPoint(self):
        self.label3.config(textvariable=self.pointneph)
        self.label5.config(textvariable=self.pointeph)
        self.label7.config(textvariable=self.pointjud)
        self.label9.config(textvariable=self.pointbenj)

    def controler(self):
        self.fen = Toplevel(self.fen1)
        self.fen.grab_set()
        self.fen.focus_set()
        self.fen.geometry("600x400+750+50")  
        self.fen.title('Affichage')
        self.fen.iconbitmap('images/FJU_Lyon.ico') 
        self.fen.resizable(width=False,height=False)
        scrollbar = Scrollbar(self.fen)
        textfield = Text(self.fen,yscrollcommand=scrollbar.set)
        scrollbar.config(command=textfield.yview)
        scrollbar.pack(side='right', fill='y')
        textfield.pack(side='left', expand=0, fill='both')
        with open('Fichiers/log.fju', 'r') as self.f:
            for ligne in self.f:
                textfield.insert(0.0, ligne)
        textfield.config(state=DISABLED)
                
        self.fen.mainloop()

    def Vainq(self):
        self.labvainqueur.config(text='Le Vainqueur est: %s' % self.Vainqueur['NOM'])
        
        if self.Vainqueur['NOM'] == 'JUDAH':
            self.label7.config(textvariable=self.pointjud)
        elif self.Vainqueur['NOM'] == 'NEPHTALIE':
            self.label3.config(textvariable=self.pointneph)
        elif self.Vainqueur['NOM'] == 'EPHRAIM':
            self.label5.config(textvariable=self.pointeph)
        else:
            self.label9.config(textvariable=self.pointbenj)
            
    def Second(self):
        self.labsecond.config(text='Le second est: %s' % self.Deuxieme['NOM'])

        if self.Deuxieme['NOM'] == 'JUDAH':
            self.label7.config(textvariable=self.pointjud)
        elif self.Deuxieme['NOM'] == 'NEPHTALIE':
            self.label3.config(textvariable=self.pointneph)
        elif self.Deuxieme['NOM'] == 'EPHRAIM':
            self.label5.config(textvariable=self.pointeph)
        else:
            self.label9.config(textvariable=self.pointbenj)
    
    def Trois(self):
        self.labtroisieme.config(text='Le Troisieme est: %s' % self.Troisieme['NOM'])

        if self.Troisieme['NOM'] == 'JUDAH':
            self.label7.config(textvariable=self.pointjud)
        elif self.Troisieme['NOM'] == 'NEPHTALIE':
            self.label3.config(textvariable=self.pointneph)
        elif self.Troisieme['NOM'] == 'EPHRAIM':
            self.label5.config(textvariable=self.pointeph)
        else:
            self.label9.config(textvariable=self.pointbenj)
    
    def Quatr(self):
        self.labquatrieme.config(text='Le Quatrieme est: %s' % self.Quatrieme['NOM'])

        if self.Quatrieme['NOM'] == 'JUDAH':
            self.label7.config(textvariable=self.pointjud)
        elif self.Quatrieme['NOM'] == 'NEPHTALIE':
            self.label3.config(textvariable=self.pointneph)
        elif self.Quatrieme['NOM'] == 'EPHRAIM':
            self.label5.config(textvariable=self.pointeph)
        else:
            self.label9.config(textvariable=self.pointbenj)

    def fin(self):
        framefin = Frame(self.fen)
        framefin.pack(side=BOTTOM)
        Button(framefin, text='FIN', bg='light sea green',font='calibri 12 italic', padx=10, command=self.finish).pack()
                     
    def finish(self):
        self.fen.destroy()
        self.fen1.destroy()
        try:
            self.sons.stop()
        except:
            rien = 0
            
    def Quitter(self):
        date = datetime.now()
        if self.pointnephtalie != 0 or self.pointephraim != 0 or self.pointjudah != 0 or self.pointbenjamin != 0:
            if askyesno('ATTENTION', ' ETES VOUS SURE DE VOULOIR QUUITTER !!!\n DES POINTS ONT ÉTÉ COMPTABILISÉS !!!'):
                self.fen1.destroy()
            try:
                self.fen.destroy()
                self.verset.destroy()
                self.info.destroy()
            except:
                essai ='Echouer'
        else:
            self.fen1.destroy()
            try:
                self.fen.destroy()
                self.verset.destroy()
                self.info.destroy()
            except:
                essai ='Echouer'
                
        with open('fichiers/log.fju', 'a') as f:
                f.write('%s/%s/%s\t\t%sh %s mins %s sec\t\tSession Ferme !!!\n' % (date.day, date.month, date.year, date.hour, date.minute, date.second))    
        
    def Contact(self):
        showinfo('ME CONTACTER', 'EN CAS DE BUG OU D\'ERREUR DE FONCTIONNEMENT  OU DE CONSEILLE D\'AMELIORATION\n\nVOUS POUVER CONTACTER L\'AUTEUR VIA CET EMAIL: \n\nEMAIL: hiservicesone@gmail.com\n\nCopyright © S MARONE')

    def detail_App(self):
        showinfo('Application', 'FJU  LYON PROG EST UNE APPLICATION DU GROUPE JEUNE LYON \nFORCE JEUNE UNIVERSELLE LYON DU CENTRE D\'ACCEUIL UNIVERSEL LYON\nPOUR LES ACTIVITÉS DU SAMEDI\n\nCopyright © S MARONE')

    def fjuLyon(self):
        showinfo('FJU Lyon', 'ADRESSE: 101 RUE D\'ENVERS JEAN MACE\n JOUR:\nMARDI ::: 20H CONNEXION FUN // SUR FACEBOOK ::: https://www.facebook.com/forcejseunefrance.fjf/  \nSAMEDI 13H 30 ::: ACTIVITE JEUNE')
    
    def LireMusique(self):
        showinfo('PAS ACTIVÉE', 'CETTE OPTION SERA BIENTOT DISPONIBLE !!!')
    
    def deplacement(self):
        #""" Déplacement de la balle """
        
        # rebond à droite
        if self.X+self.RAYON+self.DX > self.LARGEUR:
            self.X = 2*(self.LARGEUR-self.RAYON)-self.X
            self.DX = -self.DX
    
        # rebond à gauche
        if self.X-self.RAYON+self.DX < 0:
            self.X = 2*self.RAYON-self.X
            self.DX = -self.DX
    
        # rebond en bas
        if self.Y+self.RAYON+self.DY > self.HAUTEUR:
            self.Y = 2*(self.HAUTEUR-self.RAYON)-self.Y
            self.DY = -self.DY
        
        # rebond en haut
        if self.Y-self.RAYON+self.DY < 0:
            self.Y = 2*self.RAYON-self.Y
            self.DY = -self.DY
    
        self.X = self.X+self.DX
        self.Y = self.Y+self.DY
    
        # affichage
        self.can1.coords(self.Balle,self.X-self.RAYON,self.Y-self.RAYON,self.X+self.RAYON,self.Y+self.RAYON)

        # mise à jour toutes les 50 ms
        self.fen1.after(50,self.deplacement)

    def deplacement1(self):
        #""" Déplacement de la balle """
        
        # rebond à droite
        if self.X1+self.RAYON+self.DX1 > self.LARGEUR:
            self.X1 = 2*(self.LARGEUR-self.RAYON)-self.X1
            self.DX1 = -self.DX1
        
        # rebond à gauche
        if self.X1-self.RAYON+self.DX1 < 0:
            self.X1 = 2*self.RAYON-self.X1
            self.DX1 = -self.DX1
        
        # rebond en bas
        if self.Y1+self.RAYON+self.DY1 > self.HAUTEUR:
            self.Y1 = 2*(self.HAUTEUR-self.RAYON)-self.Y1
            self.DY1 = -self.DY1
            
        # rebond en haut
        if self.Y1-self.RAYON+self.DY1 < 0:
            self.Y1 = 2*self.RAYON-self.Y1
            self.DY1 = -self.DY1
        
        self.X1 = self.X1+self.DX1
        self.Y1 = self.Y1+self.DY1
        
        # affichage
        self.can1.coords(self.Balle1,self.X1-self.RAYON,self.Y1-self.RAYON,self.X1+self.RAYON,self.Y1+self.RAYON)

        # mise à jour toutes les 50 ms
        self.fen1.after(50,self.deplacement1)

    def deplacement2(self):
        #""" Déplacement de la balle """
    
        # rebond à droite
        if self.X2+self.RAYON+self.DX2 > self.LARGEUR:
            self.X2 = 2*(self.LARGEUR-self.RAYON)-self.X2
            self.DX2 = -self.DX2
    
        # rebond à gauche
        if self.X2-self.RAYON+self.DX2 < 0:
            self.X2 = 2*self.RAYON-self.X2
            self.DX2 = -self.DX2
    
        # rebond en bas
        if self.Y2+self.RAYON+self.DY2 > self.HAUTEUR:
            self.Y2 = 2*(self.HAUTEUR-self.RAYON)-self.Y2
            self.DY2 = -self.DY2
        
        # rebond en haut
        if self.Y2-self.RAYON+self.DY2 < 0:
            self.Y2 = 2*self.RAYON-self.Y2
            self.DY2 = -self.DY2
    
        self.X2 = self.X2+self.DX2
        self.Y2 = self.Y2+self.DY2
    
        # affichage
        self.can1.coords(self.Balle2,self.X2-self.RAYON,self.Y2-self.RAYON,self.X2+self.RAYON,self.Y2+self.RAYON)

        # mise à jour toutes les 50 ms
        self.fen1.after(50,self.deplacement2)

    def deplacement3(self):
        #""" Déplacement de la balle """
    
        # rebond à droite
        if self.X3+self.RAYON+self.DX3 > self.LARGEUR:
            self.X3 = 2*(self.LARGEUR-self.RAYON)-self.X3
            self.DX3 = -self.DX3
    
        # rebond à gauche
        if self.X3-self.RAYON+self.DX3 < 0:
            self.X3 = 2*self.RAYON-self.X3
            self.DX3 = -self.DX3
    
        # rebond en bas
        if self.Y3+self.RAYON+self.DY3 > self.HAUTEUR:
            self.Y3 = 2*(self.HAUTEUR-self.RAYON)-self.Y3
            self.DY3 = -self.DY3
        
        # rebond en haut
        if self.Y3-self.RAYON+self.DY3 < 0:
            self.Y3 = 2*self.RAYON-self.Y3
            self.DY3 = -self.DY3
    
        self.X3 = self.X3+self.DX3
        self.Y3 = self.Y3+self.DY3
    
        # affichage
        self.can1.coords(self.Balle3,self.X3-self.RAYON,self.Y3-self.RAYON,self.X3+self.RAYON,self.Y3+self.RAYON)

        # mise à jour toutes les 50 ms
        self.fen1.after(50,self.deplacement3)
        
    def ChangerTemps(self):
        self.fenv = Toplevel(self.fen1)
        self.fenv.overrideredirect(1)
        self.fenv.grab_set()
        self.fenv.focus_set()
        self.fenv.geometry('400x190+480+340')
        self.fenv.resizable(width=False,height=False)
        self.fenv.title('FJU LYON INFO')
        self.fenv.iconbitmap('images/FJU_Lyon.ico')
        self.fenv.configure(bg='LightCyan2')
		
        Label(self.fenv, text='TEMPS', fg='red2', font='Algerian 45 bold', bg='LightCyan2').pack()
        self.entrtemps = Entry(self.fenv, width=10, font='calibri 12 bold italic', bg='bisque')
        self.entrtemps.pack(pady=10)
        Button(self.fenv, text='Valider', command=self.validerchangertemps, font='calibri 12 bold italic', fg='red2', padx=10, bg='bisque').place(y=130, x=100)
        Button(self.fenv, text = 'Annuler', command=self.fenv.destroy,font='calibri 12 bold italic', fg='red2', padx=10, bg='bisque').place(y=130, x=210)

        self.fenv.bind("<Key>", self.clavierchangertemps)
        
        self.fenv.mainloop()

    def clavierchangertemps(self, event):
        touche = event.keysym
        if touche == "Return":
            self.validerchangertemps()
        
    def validerchangertemps(self):
        self.temps = self.entrtemps.get()
        if self.temps == '':
            showinfo('CHAMPS VIDES', 'LE CHAMPS EST VIDE, VEUILLEZ SAISIR !!!')
        elif self.temps.isdigit() == False:
            showwarning('ERREUR VALEUR',' VEUILLEZ SAISIR DES VALEURS NUMERIQUE')
        elif int(self.temps) > 40 or int(self.temps) < 0:
            showinfo('ERREUR VALEUR', 'LA VALEUR N\'EST PAS PRISE EN COMPTE !!!')
        else:
            self.lancer_changertemps()
            self.fenv.destroy()
            
    def lancer_changertemps(self):
        mixer.init()
        self.son1 = mixer.Sound('sons/Alarm.ogg')
        self.son1.set_volume(2.0)
        self.flag = 1
        self.depart = time.time()
        self.time = int(self.temps)-1
        self.top_horloge()
            
    def lancer_Minuteur(self):
        mixer.init()
        self.son1 = mixer.Sound('sons/Alarm.ogg')
        self.son1.set_volume(2.0)
        self.flag = 1
        self.depart = time.time()
        self.time = 39
        self.top_horloge()

    def top_horloge(self):
        y = time.time()-self.depart    
        minutes = time.localtime(y)[4]
        secondes = time.localtime(y)[5]
        if self.flag == 1:
            if 59 - secondes < 10:
                self.lab.config(text = '%i:0%i' %(self.time - minutes, 59 - secondes))
                self.lab.after(1000, self.top_horloge)
            else:
                self.lab.config(text = "%i:%i" %(self.time - minutes,59 - secondes))
                self.lab.after(1000, self.top_horloge)
            if  self.time - minutes == 0 and 59 - secondes == 30:
                self.son1.play(-1)
            if self.time - minutes == 0 and 59 - secondes == 0:
                self.flag = 0
                self.son1.stop()

    def lancer_Minuteur1(self):
        self.lab1.destroy()
        self.lab1 = Label(self.fram6,text='00:00', fg='red', font='algrian 68 bold', bg='gray60')
        self.lab1.pack(fill='x')
        mixer.init()
        self.son = mixer.Sound('sons/Ring.ogg')
        self.son.set_volume(1.0)
        self.flag1 = 1
        if self.entremins.get().isdigit() == False or self.entresec.get().isdigit() == False:
             showinfo('ERREUR VALEUR MINUTES ET SECONDES', 'DES CARRACTERE NON NUMERIQUE ONT ÉTÉ RENSEIGNÉES DANS LE CHAMPS MINUTE / SECONDE !!!')
        elif int(self.entremins.get()) > 39:
            showinfo('ERREUR DE SAISIE', 'LA VALEUR DES MINUTES N\'EST PAS VALIDE !!!\n\n VÉRIFIEZ LES VALEURS RENSEIGNÉES !!!')
        elif int(self.entresec.get()) > 59:
            showinfo('ERREUR DE SAISIE', 'LA VALEUR DES SECONDES N\'EST PAS VALIDE !!!\n\n VÉRIFIEZ LES VALEURS RENSEIGNÉES !!!')
        else:
            if int(self.entremins.get()) == 0 and int(self.entresec.get()) == 0:
                self.flag1 = 0
            else:
                self.mins = int(self.entremins.get())
                self.s = int(self.entresec.get())
                self.top_horloge1()

    def top_horloge1(self):
        if self.mins  == 0 and self.s == -1:
                self.flag1 = 0
                self.son.play()
        if self.flag1 == 1:
            if self.s == -1:
                self.s = 59
                self.mins = self.mins - 1
            if self.mins < 10:
                self.mins = '0' +str(self.mins)
            if self.s < 10:
                self.s = '0' + str(self.s)
            self.lab1.config(text = '%s:%s' %(self.mins, self.s))
            self.lab1.after(1000, self.top_horloge1)
            self.mins = int(self.mins)
            self.s = int(self.s)
            self.s = self.s - 1

    def Demarreralarme(self):
        mixer.init()
        self.sonalarm = mixer.Sound('sons/Alarm Minuteur.ogg')
        self.sonalarm.set_volume(2.0)
        self.sonalarm.play(-1)

    def Stopalarme(self):
        try:
            self.sonalarm.stop()
        except:
            rien = ''
    def ActiverSonTemps(self):
        mixer.init()
        self.son1 = mixer.Sound('sons/Alarm.ogg')
        self.son1.set_volume(2.0)
        showinfo('SONS', 'SONS TEMPS ACTIVE !!!')

    def StopperSonTemps(self):
        try:
            self.son1.stop()
        except:
            rien = ''
    def affmasqu(self):
        if self.valeur.get() == 0 :
            self.entr1.config(show='*')
        else:
            self.entr1.config(show='')
            
    def dempointNephtalie(self):
        self.fen = Toplevel(self.fen1)
        self.fen.grab_set()
        self.fen.focus_set()
        self.fen.geometry('450x220+450+340')
        self.fen.resizable(width=False,height=False)
        self.fen.overrideredirect(1)
        self.fen.title('AJOUTER/ENLEVER POINT NEPHTALIE')
        self.fen.iconbitmap('images/FJU_Lyon.ico')
        self.fen.configure(bg='LightCyan2')
        
        Label(self.fen, text='NEPHTALIE', bg='LightCyan2', fg='red4', font='algerian 58 bold').pack()
        fram15 = Frame(self.fen, bg='LightCyan2')
        fram15.pack()
        self.value = IntVar(value=0)
        Radiobutton(fram15, text='Ajouter Point', variable=self.value, value=1, bg='LightCyan2', padx=5, command=self.mod1, font='calibri 12 bold italic').pack(side=LEFT,padx=10)
        Radiobutton(fram15, text='Enlever Point', variable=self.value, value=2, bg='LightCyan2', padx=5, command=self.mod2, font='calibri 12 bold italic').pack(side=LEFT)

        
        fram17 = Frame(self.fen, bg='LightCyan2')
        fram17.pack()
        self.entr1 = Entry(fram17, width=20, show='*', bg='bisque', font='calibri 12 bold italic', fg='maroon')
        self.entr1.pack()
        fram18 =Frame(self.fen, bg='LightCyan2')
        fram18.pack()
        self.valeur = IntVar()
        Checkbutton(fram18, text='Afficher/Masquer', font='normal 8 italic bold', variable=self.valeur, onvalue=1,command=self.affmasqu, offvalue=0, bg='LightCyan2').pack(side=LEFT, padx=5)

        fram = Frame(self.fen, bg='LightCyan2')
        fram.pack(side=BOTTOM)
        Button(fram, text='Valider', command=self.ValiderNeph, font='calibri 12 bold italic', bg='bisque', padx=5).pack(side=LEFT, pady=10, padx=10)
        Button(fram, text='Annuler', command=self.fen.destroy , font='calibri 12 bold italic', bg='bisque', padx=5).pack(side=LEFT, pady=10, padx=10)

        self.fen.bind("<Key>", self.clavierNeph)
        
        self.fen.mainloop()

    def dempointEphraim(self):
        self.fen = Toplevel(self.fen1)
        self.fen.grab_set()
        self.fen.focus_set()
        self.fen.geometry('450x220+450+340')
        self.fen.resizable(width=False,height=False)
        self.fen.overrideredirect(1)
        self.fen.title('AJOUTER/ENLEVER POINT EPHRAIM')
        self.fen.iconbitmap('images/FJU_Lyon.ico')
        self.fen.configure(bg='LightCyan2')
        
        Label(self.fen, text='EPHRAIM', bg='LightCyan2', fg='red4', font='algerian 58 bold').pack()
        fram15 = Frame(self.fen, bg='LightCyan2')
        fram15.pack()
        self.value = IntVar(value=0)
        Radiobutton(fram15, text='Ajouter Point', variable=self.value, value=1, bg='LightCyan2', padx=5, command=self.mod1, font='calibri 12 bold italic').pack(side=LEFT,padx=10)
        Radiobutton(fram15, text='Enlever Point', variable=self.value, value=2, bg='LightCyan2', padx=5, command=self.mod2, font='calibri 12 bold italic').pack(side=LEFT)

        
        fram17 = Frame(self.fen, bg='LightCyan2')
        fram17.pack()
        self.entr1 = Entry(fram17, width=20, show='*', bg='bisque', font='calibri 12 bold italic', fg='maroon')
        self.entr1.pack()
        fram18 =Frame(self.fen, bg='LightCyan2')
        fram18.pack()
        self.valeur = IntVar()
        Checkbutton(fram18, text='Afficher/Masquer', font='normal 8 italic bold', variable=self.valeur, onvalue=1,command=self.affmasqu, offvalue=0, bg='LightCyan2').pack(side=LEFT, padx=5)
        
        fram = Frame(self.fen, bg='LightCyan2')
        fram.pack(side=BOTTOM)
       
        Button(fram, text='Valider', command=self.ValiderEph, font='calibri 12 bold italic', bg='bisque', padx=5).pack(side=LEFT, pady=10, padx=10)
        Button(fram, text='Annuler', command=self.fen.destroy , font='calibri 12 bold italic', bg='bisque', padx=5).pack(side=LEFT, pady=10, padx=10)

        self.fen.bind("<Key>", self.clavierEph)
        
        self.fen.mainloop()

    def dempointJudah(self):
        self.fen = Toplevel(self.fen1)
        self.fen.grab_set()
        self.fen.focus_set()
        self.fen.geometry('450x220+450+340')
        self.fen.resizable(width=False,height=False)
        self.fen.overrideredirect(1)
        self.fen.title('AJOUTER/ENLEVER  POINT JUDAH')
        self.fen.iconbitmap('images/FJU_Lyon.ico')
        self.fen.configure(bg='LightCyan2')
        
        Label(self.fen, text='JUDAH', bg='LightCyan2', fg='red4', font='algerian 58 bold').pack()
        fram15 = Frame(self.fen, bg='LightCyan2')
        fram15.pack()
        self.value = IntVar(value=0)
        Radiobutton(fram15, text='Ajouter Point', variable=self.value, value=1, bg='LightCyan2', padx=5, command=self.mod1, font='calibri 12 bold italic').pack(side=LEFT,padx=10)
        Radiobutton(fram15, text='Enlever Point', variable=self.value, value=2, bg='LightCyan2', padx=5, command=self.mod2, font='calibri 12 bold italic').pack(side=LEFT)

        
        fram17 = Frame(self.fen, bg='LightCyan2')
        fram17.pack()
        self.entr1 = Entry(fram17, width=20, show='*', bg='bisque', font='calibri 12 bold italic', fg='maroon')
        self.entr1.pack()
        fram18 =Frame(self.fen, bg='LightCyan2')
        fram18.pack()
        self.valeur = IntVar()
        Checkbutton(fram18, text='Afficher/Masquer', font='normal 8 italic bold', variable=self.valeur, onvalue=1,command=self.affmasqu, offvalue=0, bg='LightCyan2').pack(side=LEFT, padx=5)
        
        fram = Frame(self.fen, bg='LightCyan2')
        fram.pack(side=BOTTOM)
       
        Button(fram, text='Valider', command=self.ValiderJud, font='calibri 12 bold italic', bg='bisque', padx=5).pack(side=LEFT, pady=10, padx=10)
        Button(fram, text='Annuler', command=self.fen.destroy , font='calibri 12 bold italic', bg='bisque', padx=5).pack(side=LEFT, pady=10, padx=10)

        self.fen.bind("<Key>", self.clavierJud)
        
        self.fen.mainloop()

    def dempointBenjamin(self):
        self.fen = Toplevel(self.fen1)
        self.fen.grab_set()
        self.fen.focus_set()
        self.fen.geometry('450x220+450+340')
        self.fen.resizable(width=False,height=False)
        self.fen.overrideredirect(1)
        self.fen.title('AJOUTER/ENLEVER POINT BENJAMIN')
        self.fen.iconbitmap('images/FJU_Lyon.ico')
        self.fen.configure(bg='LightCyan2')
        
        Label(self.fen, text='BENJAMIN', bg='LightCyan2', fg='red4', font='algerian 58 bold').pack()
        fram15 = Frame(self.fen, bg='LightCyan2')
        fram15.pack()
        self.value = IntVar(value=0)
        Radiobutton(fram15, text='Ajouter Point', variable=self.value, value=1, bg='LightCyan2', padx=5, command=self.mod1, font='calibri 12 bold italic').pack(side=LEFT,padx=10)
        Radiobutton(fram15, text='Enlever Point', variable=self.value, value=2, bg='LightCyan2', padx=5, command=self.mod2, font='calibri 12 bold italic').pack(side=LEFT)

        
        fram17 = Frame(self.fen, bg='LightCyan2')
        fram17.pack()
        self.entr1 = Entry(fram17, width=20, show='*', bg='bisque', font='calibri 12 bold italic', fg='maroon')
        self.entr1.pack()
        fram18 =Frame(self.fen, bg='LightCyan2')
        fram18.pack()
        self.valeur = IntVar()
        Checkbutton(fram18, text='Afficher/Masquer', font='normal 8 italic bold', variable=self.valeur, onvalue=1,command=self.affmasqu, offvalue=0,bg='LightCyan2').pack(side=LEFT, padx=5)
        
        fram = Frame(self.fen, bg='LightCyan2')
        fram.pack(side=BOTTOM)
       
        Button(fram, text='Valider', command=self.ValiderBenj, font='calibri 12 bold italic', bg='bisque', padx=5).pack(side=LEFT, pady=10, padx=10)
        Button(fram, text='Annuler', command=self.fen.destroy , font='calibri 12 bold italic', bg='bisque', padx=5).pack(side=LEFT, pady=10, padx=10)

        self.fen.bind("<Key>", self.clavierBenj)
        
        self.fen.mainloop()
        
    def clavierNeph(self, event):
        touche = event.keysym
        if touche == "Return":
            self.ValiderNeph()
            
    def clavierEph(self, event):
        touche = event.keysym
        if touche == "Return":
            self.ValiderEph()

    def clavierJud(self, event):
        touche = event.keysym
        if touche == "Return":
            self.ValiderJud()

    def clavierBenj(self, event):
        touche = event.keysym
        if touche == "Return":
            self.ValiderBenj()
        
    def mod1(self):
        self.value.set(1)

    def mod2(self):
        self.value.set(2)

    def ValiderNeph(self):
        if self.entr1.get() == '':
            showinfo('CHAMPS VIDES', 'LE CHAMPS EST VIDE, VEUILLEZ SAISIR !!!')
        elif self.entr1.get().isdigit() == FALSE:
            showinfo('ERREUR VALEUR', 'ERREUR  DE VALEUR !!!\nLA VALEUR SAISIE N\'EST PAS VALABLE !!!')
        elif int(self.entr1.get()) > 100000 or int(self.entr1.get()) < 0:
            showinfo('ERREUR VALEUR', 'LA VALEUR N\'EST PAS PRISE EN COMPTE LIMITE A 100 000) !!!')
        else:
            val = int(self.entr1.get())
            if self.value.get() == 0:
                showinfo('PAS DE CHOIX', 'PAS DE CHOIX !!! CHOISISSEZ ENTRE AJOUTER OU ENLEVER DES POINTS !!!')
            elif self.value.get() == 1:
                self.pointnephtalie += val
                self.pointneph.set(self.pointnephtalie)
                self.fen.destroy()
            elif self.value.get() == 2:
                self.pointnephtalie -= val
                self.pointneph.set(self.pointnephtalie)
                self.fen.destroy()
                
    def ValiderEph(self):
        if self.entr1.get() == '':
            showinfo('CHAMPS VIDES', 'LE CHAMPS EST VIDE, VEUILLEZ SAISIR !!!')
        elif self.entr1.get().isdigit() == FALSE:
            showinfo('ERREUR VALEUR', 'ERREUR  DE VALEUR !!!\nLA VALEUR SAISIE N\'EST PAS VALABLE !!!')
        elif int(self.entr1.get()) > 100000 or int(self.entr1.get()) < 0:
            showinfo('ERREUR VALEUR', 'LA VALEUR N\'EST PAS PRISE EN COMPTE (LIMITE A 100 000) !!!')
        else:
            val = int(self.entr1.get())
            if self.value.get() == 0:
                showinfo('PAS DE CHOIX', 'PAS DE CHOIX !!! CHOISISSEZ ENTRE AJOUTER OU ENLEVER DES POINTS !!!')
            elif self.value.get() == 1:
                self.pointephraim += val
                self.pointeph.set(self.pointephraim)
                self.fen.destroy()
            elif self.value.get() == 2:
                self.pointephraim -= val
                self.pointeph.set(self.pointephraim)
                self.fen.destroy()   
                    
    def ValiderJud(self):
        if self.entr1.get() == '':
            showinfo('CHAMPS VIDES', 'LE CHAMPS EST VIDE, VEUILLEZ SAISIR !!!')
        elif self.entr1.get().isdigit() == FALSE:
            showinfo('ERREUR VALEUR', 'ERREUR  DE VALEUR !!!\nLA VALEUR SAISIE N\'EST PAS VALABLE !!!')
        elif int(self.entr1.get()) > 100000 or int(self.entr1.get()) < 0:
            showinfo('ERREUR VALEUR', 'LA VALEUR N\'EST PAS PRISE EN COMPTE LIMITE A 100 000) !!!')
        else:
            val = int(self.entr1.get())
            if self.value.get() == 0:
                showinfo('PAS DE CHOIX', 'PAS DE CHOIX !!! CHOISISSEZ ENTRE AJOUTER OU ENLEVER DES POINTS !!!')
            elif self.value.get() == 1:
                self.pointjudah += val
                self.pointjud.set(self.pointjudah)
                self.fen.destroy()
            elif self.value.get() == 2:
                self.pointjudah -= val
                self.pointjud.set(self.pointjudah)
                self.fen.destroy()
        
    def ValiderBenj(self):
        if self.entr1.get() == '':
            showinfo('CHAMPS VIDES', 'LE CHAMPS EST VIDE, VEUILLEZ SAISIR !!!')
        elif self.entr1.get().isdigit() == FALSE:
            showinfo('ERREUR VALEUR', 'ERREUR  DE VALEUR !!!\nLA VALEUR SAISIE N\'EST PAS VALABLE !!!')
        elif int(self.entr1.get()) > 100000 or int(self.entr1.get()) < 0:
            showinfo('ERREUR VALEUR', 'LA VALEUR N\'EST PAS PRISE EN COMPTE LIMITE A 100 000) !!!')
        else:
            val = int(self.entr1.get())
            if self.value.get() == 0:
                showinfo('PAS DE CHOIX', 'PAS DE CHOIX !!! CHOISISSEZ ENTRE AJOUTER OU ENLEVER DES POINTS !!!')
            elif self.value.get() == 1:
                self.pointbenjamin += val
                self.pointbenj.set(self.pointbenjamin)
                self.fen.destroy()
            elif self.value.get() == 2:
                self.pointbenjamin -= val
                self.pointbenj.set(self.pointbenjamin)
                self.fen.destroy()


                
class HomFem():
    def __init__(self):
        self.CODE = ['²','~','\n',' ', 'i', 'U','§','j', '[','©', '}','k', '(','P', 'l', ']','D', 'm', 'S', 'n', 'o', '-', '|', '&', 'p', 'q', 'C','{', 'a', 'b', 'c', 'd', 'e','E', 'H', 'F','_', 'é', 'ç', 'ê','ô', 'â', 'J', 'K', '8', 'L', '^', 'M', '\'', 'N','\"', 'O', 'Y', 'Z', 'f', 'g', 'h', 'r', 's', 't', 'u', 'v', 'w', 'x', '0', 'y', 'z' , '1', '2','A', '4', 'W', '5','G', '6', 'I','7', ",", '@', '!', '.', '?', ';', ':', '/', "'", '*', '+', 'T', '3', 'V', 'B', '#', 'Q', 'R', 'X', ')', 'î', '9']
        self.fen1 = Tk()
        self.w, self.h = self.fen1.winfo_screenwidth(), self.fen1.winfo_screenheight()
        self.fen1.overrideredirect(1)
        self.fen1.geometry("%dx%d+0+0" % (self.w, self.h))
        self.fen1.title('FJU LYON')
        self.fen1.iconbitmap('images/FJU_Lyon.ico')
        self.fen1.configure(bg = "light sea green")

        with open('fichiers/app.fju', 'r') as f:
            val = self.decryptbin(f.read())
        self.variablement = StringVar()
        self.variablement.set('???')
        
        menubar = Menu(self.fen1)
        
        menu1 = Menu(menubar, tearoff=0)
        if val == 'TheChoosenOne':
            menu1.add_command(label='Controler', command=self.controler)
            menu1.add_separator()
        menu1.add_command(label='Terminer', command=self.Terminer)
        menu1.add_separator()
        menu1.add_command(label='Quitter', command=self.Quitter)
        menubar.add_cascade(label='FENETRE', menu=menu1)

        menu2 = Menu(menubar, tearoff=0)
        menu2.add_command(label='Afficher Point', command=self.afficherPoint)
        menu2.add_separator()
        menu2.add_command(label='Masquer Point', command=self.masquerPoint)
        menubar.add_cascade(label='AFFICHAGE', menu=menu2)

        menu3 = Menu(menubar, tearoff=0)
        menu3.add_separator()
        menu3.add_command(label='Changer Temps', command=self.ChangerTemps)
        menubar.add_cascade(label='TEMPS', menu=menu3)

        menu4 = Menu(menubar, tearoff=0)
        menu4.add_separator()
        menu4.add_command(label='Demarrer son (alarme)', command=self.Demarreralarme)
        menu4.add_separator()
        menu4.add_command(label='Stop son (alarme)', command=self.Stopalarme)
        menu4.add_separator()
        menu4.add_command(label='Activer son Fin de Temps', command=self.ActiverSonTemps)
        menu4.add_separator()
        menu4.add_command(label='Stoper son Fin de Temps', command=self.StopperSonTemps)
        menu4.add_separator()
        menu4.add_command(label='Lire une Musique', command=self.LireMusique)
        menubar.add_cascade(label='SONS', menu=menu4)

        menu5 = Menu(menubar, tearoff=0)
        menu5.add_separator()
        menu5.add_command(label='Ajouter/Enlever Point', command=self.dempointHomme)
        menubar.add_cascade(label='HOMME', menu=menu5)

        menu6 = Menu(menubar, tearoff=0)
        menu6.add_separator()
        menu6.add_command(label='Ajouter/Enlever Point', command=self.dempointFemme)
        menubar.add_cascade(label='FEMME', menu=menu6)

        menu7 = Menu(menubar, tearoff=0)
        menu7.add_command(label='Force Jeune Universel Lyon', command=self.fjuLyon)
        menu7.add_command(label='Info App', command=self.detail_App)
        menubar.add_cascade(label='FJU LYON', menu=menu7)
        
        menu8 = Menu(menubar, tearoff=0)
        menu8.add_command(label='Contacter', command=self.Contact)
        menubar.add_cascade(label='?', menu=menu8)
         
        self.fen1.config(menu=menubar)
        
        fram101 = Frame(self.fen1, width=self.w , height=100, bg='white')
        fram101.pack(side=TOP)
        label1 = Label(fram101, text='FORCE JEUNE UNIVERSELLE LYON', fg='firebrick1', font='Algerian 60 bold', bg='white')
        label1.pack()
        label1.pack_propagate(False)
        
        textverset = StringVar()
        textresultat = StringVar()
        textinfo = StringVar()
        textinfoplus = StringVar()
        textinfoEv = StringVar()
        with open('fichiers/vers.fju', 'r') as self.f:
            textverset.set(self.f.read())
        with open('fichiers/result.fju', 'r') as self.f:
            textresultat.set(self.f.read())
        with open('fichiers/info.fju', 'r') as self.f:
            textinfo.set(self.f.read())
        with open('fichiers/info+.fju', 'r') as self.f:
            textinfoplus.set(self.f.read())
        with open('fichiers/infoEv.fju', 'r') as self.f:
            textinfoEv.set(self.f.read())
        
            
        marquee = Marquee(fram101, text=textverset.get() + '\t\t [SEMAINE PASSE] ' + textresultat.get() + '\t\t ' + textinfo.get() + '\t\t' + textinfoplus.get() + textinfoEv.get(), borderwidth=1, relief="sunken")
        marquee.pack(side=BOTTOM, fill=X)
        marquee.pack_propagate(False)
        
        fram2 = Frame(self.fen1, width =self.w/2-150, height =(self.h-152), bg='steel blue')
        fram2.place(x=0, y=136)
        fram2.pack_propagate(False)
        label2 = Label(fram2, text='HOMME', font='Algerian 94 bold', bg='steel blue')
        label2.pack(pady=40)
        self.pointhom = StringVar()
        self.pointhom.set(0)
        self.pointhomme = 0
        self.label3 = Label(fram2,textvariable=self.pointhom, font='Algerian 100 bold', bg='steel blue')
        self.label3.pack()
        photo1 = PhotoImage(file='images/Homme.gif')
        item1 = Label(fram2, image=photo1, bg='steel blue')
        item1.photo = photo1
        item1.pack(side=BOTTOM, pady=10)
      
        fram3 = Frame(self.fen1, width =self.w/2-150, height =(self.h-152), bg='pink')
        fram3.place(x=self.w/2+150, y=136)
        fram3.pack_propagate(False)
        label4 = Label(fram3, text='FEMME', font='Algerian 94 bold', bg='pink')
        label4.pack(pady=40)
        self.pointfem = StringVar()
        self.pointfem.set(0)
        self.pointfemme = 0
        self.label5 = Label(fram3, textvariable=self.pointfem, font='Algerian 100 bold', bg='pink')
        self.label5.pack()
        photo2 = PhotoImage(file='images/Femme.gif')
        item2 = Label(fram3, image=photo2, bg='pink')
        item2.photo = photo2
        item2.pack(side=BOTTOM, pady=10)

        self.fram6 = Frame(self.fen1, width=305, height=(self.h-153)/2, bg='gray60')
        self.fram6.place(x=self.w/2-150,y=136)
        self.fram6.pack_propagate(False)
        self.lab = Label(self.fram6,text='40:00', fg='red', font='algrian 84 bold', bg='gray60')
        self.lab.pack(fill='x')
        self.lab1 = Label(self.fram6,text='00:00', fg='red', font='algrian 64 bold', bg='gray60')
        self.lab1.pack(fill='x')
        
        Button(self.fram6, text='Start', bg='bisque',command=self.lancer_Minuteur1, font='calibri 12 bold italic').pack(side=BOTTOM, anchor='s', pady=3)
        self.can1 = Canvas(self.fen1, width=300, height=(self.h-155)/2)
        self.can1.place(x=self.w/2-150,y=135+(self.h-150)/2)
        
        fram7 = Frame(self.fram6, width=300,bg='gray60')
        fram7.pack(side=BOTTOM)
        fram17 = Frame(self.fram6, bg='gray60')
        fram17.pack(side=BOTTOM)
        
        Label(fram17, text='Minutes', font='calibri 8 italic', bg='gray60').pack(side=LEFT)
        Label(fram17, text='secondes', font='calibri 8 italic', bg='gray60').pack(side=LEFT)
        
        self.entremins = Spinbox(fram7, from_=0, to=45, width=5, bg='bisque')
        self.entremins.pack(anchor='e', side=LEFT, padx=2, )
        self.entresec = Spinbox(fram7, from_=0, to=59, width=5, bg='bisque')
        self.entresec.pack(anchor='e', side=LEFT, padx=2,)
        
        self.LARGEUR = 300
        self.HAUTEUR = 309
        self.RAYON = 15

        # position initiale au milieu
        self.X = random.randint(0, (self.h-150)/2)
        self.X1 = random.randint(0, (self.h-150)/2)
        
        self.Y = random.randint(0, (self.h-150)/2)
        self.Y1 = random.randint(0, (self.h-150)/2)
        

        # direction initiale aléatoire
        vitesse = random.uniform(1.8,2)*5
        angle = random.uniform(random.randint(0,5),random.randint(0,20)*math.pi)
        angle1 = random.uniform(random.randint(0,5),random.randint(0,20)*math.pi)
        
        self.DX = vitesse*math.cos(angle)
        self.DX1 = vitesse*math.cos(angle1)
        
        self.DY = vitesse*math.sin(angle)
        self.DY1 = vitesse*math.sin(angle1)
        
        
        self.Balle = self.can1.create_oval(self.X-self.RAYON,self.Y-self.RAYON,self.X+self.RAYON,self.Y+self.RAYON,width=1,fill='steel blue')
        self.Balle1 = self.can1.create_oval(self.X1-self.RAYON,self.Y1-self.RAYON,self.X1+self.RAYON,self.Y1+self.RAYON,width=1,fill='pink')

        self.lab1.destroy()
        self.lab1 = Label(self.fram6,text='00:00', fg='red', font='algrian 68 bold', bg='gray60')
        self.lab1.pack(fill='x')

        self.deplacement()
        self.deplacement1()
        
        self.lancer_Minuteur()

        self.flag1 = 0
        self.depart1 = 0

        self.fen1.mainloop()
        
    def cryptbin (self, chaine):
        liste = list(chaine)
        IN = []
        BIN = []
        for i in liste:
            if i in self.CODE:
                ind = self.CODE.index(i)
                IN.append(ind)
        for i in IN:
            BIN.append(bin(i))
        return "".join(BIN)

    def debin(self, chaine):
        chaine = list(chaine)
        chaine.reverse()
        val = 0
        tot = 0
        for i in chaine:
            if i == '1':
                tot += 2 ** val
            val += 1
        return int(tot)

    def decryptbin(self, chaine):
        valeur = []
        liste  = []
        chaine = chaine.split('0b')
        try:
            chaine.remove('')
        except:
            zero = 0
        for i in chaine:
            valeur.append(self.debin(i))
        for i in valeur:
            liste.append(self.CODE[i])
        return "".join(liste)

    def masquerPoint(self):
        self.label3.config(textvariable= self.variablement)
        self.label5.config(textvariable= self.variablement)

    def afficherPoint(self):
        self.label3.config(textvariable=self.pointhom)
        self.label5.config(textvariable=self.pointfem)

    def controler(self):
        self.fen = Toplevel(self.fen1)
        self.fen.grab_set()
        self.fen.focus_set()
        self.fen.geometry("600x400+750+50")  
        self.fen.title('Affichage')
        self.fen.iconbitmap('images/FJU_Lyon.ico') 
        self.fen.resizable(width=False,height=False)
        scrollbar = Scrollbar(self.fen)
        textfield = Text(self.fen,yscrollcommand=scrollbar.set)
        scrollbar.config(command=textfield.yview)
        scrollbar.pack(side='right', fill='y')
        textfield.pack(side='left', expand=0, fill='both')
        with open('Fichiers/log.fju', 'r') as self.f:
            for ligne in self.f:
                textfield.insert(0.0, ligne)
        textfield.config(state=DISABLED)
                
        self.fen.mainloop()

    def Contact(self):
        showinfo('ME CONTACTER', 'EN CAS DE BUG OU D\'ERREUR DE FONCTIONNEMENT  OU DE CONSEILLE D\'AMELIORATION\n\nVOUS POUVER CONTACTER L\'AUTEUR VIA CET EMAIL: \n\nEMAIL: hiservicesone@gmail.com\n\nCopyright © S MARONE')

    def detail_App(self):
        showinfo('Application', 'FJU  LYON PROG EST UNE APPLICATION DU GROUPE JEUNE LYON \nFORCE JEUNE UNIVERSELLE LYON DU CENTRE D\'ACCEUIL UNIVERSEL LYON\nPOUR LES ACTIVITÉS DU SAMEDI\n\nCopyright © S MARONE')

    def fjuLyon(self):
        showinfo('FJU Lyon', 'ADRESSE: 101 RUE D\'ENVERS JEAN MACE\n JOUR:\nMARDI ::: 20H CONNEXION FUN // SUR FACEBOOK ::: https://www.facebook.com/forcejseunefrance.fjf/  \nSAMEDI 13H 30 ::: ACTIVITE JEUNE')

    def LireMusique(self):
        showinfo('PAS ACTIVÉE', 'CETTE OPTION SERA BIENTOT DISPONIBLE !!!')
    
    def deplacement(self):
        #""" Déplacement de la balle """
        
        # rebond à droite
        if self.X+self.RAYON+self.DX > self.LARGEUR:
            self.X = 2*(self.LARGEUR-self.RAYON)-self.X
            self.DX = -self.DX
    
        # rebond à gauche
        if self.X-self.RAYON+self.DX < 0:
            self.X = 2*self.RAYON-self.X
            self.DX = -self.DX
    
        # rebond en bas
        if self.Y+self.RAYON+self.DY > self.HAUTEUR:
            self.Y = 2*(self.HAUTEUR-self.RAYON)-self.Y
            self.DY = -self.DY
        
        # rebond en haut
        if self.Y-self.RAYON+self.DY < 0:
            self.Y = 2*self.RAYON-self.Y
            self.DY = -self.DY
    
        self.X = self.X+self.DX
        self.Y = self.Y+self.DY
    
        # affichage
        self.can1.coords(self.Balle,self.X-self.RAYON,self.Y-self.RAYON,self.X+self.RAYON,self.Y+self.RAYON)

        # mise à jour toutes les 50 ms
        self.fen1.after(50,self.deplacement)

    def deplacement1(self):
        #""" Déplacement de la balle """
        
        # rebond à droite
        if self.X1+self.RAYON+self.DX1 > self.LARGEUR:
            self.X1 = 2*(self.LARGEUR-self.RAYON)-self.X1
            self.DX1 = -self.DX1
        
        # rebond à gauche
        if self.X1-self.RAYON+self.DX1 < 0:
            self.X1 = 2*self.RAYON-self.X1
            self.DX1 = -self.DX1
        
        # rebond en bas
        if self.Y1+self.RAYON+self.DY1 > self.HAUTEUR:
            self.Y1 = 2*(self.HAUTEUR-self.RAYON)-self.Y1
            self.DY1 = -self.DY1
            
        # rebond en haut
        if self.Y1-self.RAYON+self.DY1 < 0:
            self.Y1 = 2*self.RAYON-self.Y1
            self.DY1 = -self.DY1
        
        self.X1 = self.X1+self.DX1
        self.Y1 = self.Y1+self.DY1
        
        # affichage
        self.can1.coords(self.Balle1,self.X1-self.RAYON,self.Y1-self.RAYON,self.X1+self.RAYON,self.Y1+self.RAYON)

        # mise à jour toutes les 50 ms
        self.fen1.after(50,self.deplacement1)
    
    def ChangerTemps(self):
        self.fenv = Toplevel(self.fen1)
        self.fenv.overrideredirect(1)
        self.fenv.grab_set()
        self.fenv.focus_set()
        self.fenv.geometry('400x190+480+340')
        self.fenv.resizable(width=False,height=False)
        self.fenv.title('FJU LYON INFO')
        self.fenv.iconbitmap('images/FJU_Lyon.ico')
        self.fenv.configure(bg='LightCyan2')
		
        Label(self.fenv, text='TEMPS', fg='red2', font='Algerian 45 bold', bg='LightCyan2').pack()
        self.entrtemps = Entry(self.fenv, width=10, font='calibri 12 bold italic', bg='bisque')
        self.entrtemps.pack(pady=10)
        Button(self.fenv, text='Valider', command=self.validerchangertemps, font='calibri 12 bold italic', fg='red2', padx=10, bg='bisque').place(y=130, x=100)
        Button(self.fenv, text = 'Annuler', command=self.fenv.destroy,font='calibri 12 bold italic', fg='red2', padx=10, bg='bisque').place(y=130, x=210)

        self.fenv.bind("<Key>", self.clavierchangertemps)
        
        self.fenv.mainloop()

    def clavierchangertemps(self, event):
        touche = event.keysym
        if touche == "Return":
            self.validerchangertemps()
        
    def validerchangertemps(self):
        self.temps = self.entrtemps.get()
        if self.temps == '':
            showinfo('CHAMPS VIDES', 'LE CHAMPS EST VIDE, VEUILLEZ SAISIR !!!')
        elif self.temps.isdigit() == False:
            showwarning('ERREUR VALEUR',' VEUILLEZ SAISIR DES VALEURS NUMERIQUE')
        elif int(self.temps) > 40 or int(self.temps) < 0:
            showinfo('ERREUR VALEUR', 'LA VALEUR N\'EST PAS PRISE EN COMPTE !!!')
        else:
            self.lancer_changertemps()
            self.fenv.destroy()
            
    def lancer_changertemps(self):
        mixer.init()
        self.son1 = mixer.Sound('sons/Alarm.ogg')
        self.son1.set_volume(2.0)
        self.flag = 1
        self.depart = time.time()
        self.time = int(self.temps)-1
        self.top_horloge()
            
    def lancer_Minuteur(self):
        mixer.init()
        self.son1 = mixer.Sound('sons/Alarm.ogg')
        self.son1.set_volume(2.0)
        self.flag = 1
        self.depart = time.time()
        self.time = 39
        self.top_horloge()

    def top_horloge(self):
        y = time.time()-self.depart    
        minutes = time.localtime(y)[4]
        secondes = time.localtime(y)[5]
        if self.flag == 1:
            if 59 - secondes < 10:
                self.lab.config(text = '%i:0%i' %(self.time - minutes, 59 - secondes))
                self.lab.after(1000, self.top_horloge)
            else:
                self.lab.config(text = "%i:%i" %(self.time - minutes,59 - secondes))
                self.lab.after(1000, self.top_horloge)
            if  self.time - minutes == 0 and 59 - secondes == 30:
                self.son1.play(-1)
            if self.time - minutes == 0 and 59 - secondes == 0:
                self.flag = 0
                self.son1.stop()

    def lancer_Minuteur1(self):
        self.lab1.destroy()
        self.lab1 = Label(self.fram6,text='00:00', fg='red', font='algrian 68 bold', bg='gray60')
        self.lab1.pack(fill='x')
        mixer.init()
        self.son = mixer.Sound('sons/Ring.ogg')
        self.son.set_volume(1.0)
        self.flag1 = 1
        if self.entremins.get().isdigit() == False or self.entresec.get().isdigit() == False:
             showinfo('ERREUR VALEUR MINUTES ET SECONDES', 'DES CARRACTERE NON NUMERIQUE ONT ÉTÉ RENSEIGNÉES DANS LE CHAMPS MINUTE / SECONDE !!!')
        elif int(self.entremins.get()) > 39:
            showinfo('ERREUR DE SAISIE', 'LA VALEUR DES MINUTES N\'EST PAS VALIDE !!!\n\n VÉRIFIEZ LES VALEURS RENSEIGNÉES !!!')
        elif int(self.entresec.get()) > 59:
            showinfo('ERREUR DE SAISIE', 'LA VALEUR DES SECONDES N\'EST PAS VALIDE !!!\n\n VÉRIFIEZ LES VALEURS RENSEIGNÉES !!!')
        else:
            if int(self.entremins.get()) == 0 and int(self.entresec.get()) == 0:
                self.flag1 = 0
            else:
                self.mins = int(self.entremins.get())
                self.s = int(self.entresec.get())
                self.top_horloge1()

    def top_horloge1(self):
        if self.mins  == 0 and self.s == -1:
                self.flag1 = 0
                self.son.play()
        if self.flag1 == 1:
            if self.s == -1:
                self.s = 59
                self.mins = self.mins - 1
            if self.s < 10:
                self.lab1.config(text = '%i:0%i' %(self.mins, self.s))
                self.lab1.after(1000, self.top_horloge1)
            else:
                self.lab1.config(text = '%i:%i' %(self.mins, self.s))
                self.lab1.after(1000, self.top_horloge1)
            self.s = self.s - 1

    def Demarreralarme(self):
        mixer.init()
        self.sonalarm = mixer.Sound('sons/Alarm Minuteur.ogg')
        self.sonalarm.set_volume(2.0)
        self.sonalarm.play(-1)

    def Stopalarme(self):
        try:
            self.sonalarm.stop()
        except:
            rien = ''
    def ActiverSonTemps(self):
        mixer.init()
        self.son1 = mixer.Sound('sons/Alarm.ogg')
        self.son1.set_volume(2.0)
        showinfo('SONS', 'SONS TEMPS ACTIVE !!!')

    def StopperSonTemps(self):
        try:
            self.son1.stop()
        except:
            rien = ''

    def affmasqu(self):
        if self.valeur.get() == 0 :
            self.entr1.config(show='*')
        else:
            self.entr1.config(show='')
            
    def dempointHomme(self):
        self.fen = Toplevel(self.fen1)
        self.fen.grab_set()
        self.fen.focus_set()
        self.fen.geometry('450x220+450+340')
        self.fen.resizable(width=False,height=False)
        self.fen.overrideredirect(1)
        self.fen.title('AJOUTER/ENLEVER POINT HOMME')
        self.fen.iconbitmap('images/FJU_Lyon.ico')
        self.fen.configure(bg='LightCyan2')
        
        Label(self.fen, text='HOMME', bg='LightCyan2', fg='red4', font='algerian 58 bold').pack()
        fram15 = Frame(self.fen, bg='LightCyan2')
        fram15.pack()
        self.value = IntVar(value=0)
        Radiobutton(fram15, text='Ajouter Point', variable=self.value, value=1, bg='LightCyan2', padx=5, command=self.mod1, font='calibri 12 bold italic').pack(side=LEFT,padx=10)
        Radiobutton(fram15, text='Enlever Point', variable=self.value, value=2, bg='LightCyan2', padx=5, command=self.mod2, font='calibri 12 bold italic').pack(side=LEFT)

        
        fram17 = Frame(self.fen, bg='LightCyan2')
        fram17.pack()
        self.entr1 = Entry(fram17, width=20, show='*', bg='bisque', font='calibri 12 bold italic', fg='maroon')
        self.entr1.pack()
        fram18 =Frame(self.fen, bg='LightCyan2')
        fram18.pack()
        self.valeur = IntVar()
        Checkbutton(fram18, text='Afficher/Masquer', font='normal 8 italic bold', variable=self.valeur, onvalue=1,command=self.affmasqu, offvalue=0, bg='LightCyan2').pack(side=LEFT, padx=5)
        
        fram = Frame(self.fen, bg='LightCyan2')
        fram.pack(side=BOTTOM)
       
        Button(fram, text='Valider', command=self.ValiderHom, font='calibri 12 bold italic', bg='bisque', padx=5).pack(side=LEFT, pady=10, padx=10)
        Button(fram, text='Annuler', command=self.fen.destroy , font='calibri 12 bold italic', bg='bisque', padx=5).pack(side=LEFT, pady=10, padx=10)

        self.fen.bind("<Key>", self.clavierHom)
        
        self.fen.mainloop()

    def dempointFemme(self):
        self.fen = Toplevel(self.fen1)
        self.fen.grab_set()
        self.fen.focus_set()
        self.fen.geometry('450x220+450+340')
        self.fen.resizable(width=False,height=False)
        self.fen.overrideredirect(1)
        self.fen.title('AJOUTER/ENLEVER POINT FEMME')
        self.fen.iconbitmap('images/FJU_Lyon.ico')
        self.fen.configure(bg='LightCyan2')
        
        Label(self.fen, text='FEMME', bg='LightCyan2', fg='red4', font='algerian 58 bold').pack()
        fram15 = Frame(self.fen, bg='LightCyan2')
        fram15.pack()
        self.value = IntVar(value=0)
        Radiobutton(fram15, text='Ajouter Point', variable=self.value, value=1, bg='LightCyan2', padx=5, command=self.mod1, font='calibri 12 bold italic').pack(side=LEFT,padx=10)
        Radiobutton(fram15, text='Enlever Point', variable=self.value, value=2, bg='LightCyan2', padx=5, command=self.mod2, font='calibri 12 bold italic').pack(side=LEFT)

        
        fram17 = Frame(self.fen, bg='LightCyan2')
        fram17.pack()
        self.entr1 = Entry(fram17, width=20, show='*', bg='bisque', font='calibri 12 bold italic', fg='maroon')
        self.entr1.pack()
        fram18 =Frame(self.fen, bg='LightCyan2')
        fram18.pack()
        self.valeur = IntVar()
        Checkbutton(fram18, text='Afficher/Masquer', font='normal 8 italic bold', variable=self.valeur, onvalue=1,command=self.affmasqu, offvalue=0, bg='LightCyan2').pack(side=LEFT, padx=5)
        
        fram = Frame(self.fen, bg='LightCyan2')
        fram.pack(side=BOTTOM)
       
        Button(fram, text='Valider', command=self.ValiderFem, font='calibri 12 bold italic', bg='bisque', padx=5).pack(side=LEFT, pady=10, padx=10)
        Button(fram, text='Annuler', command=self.fen.destroy , font='calibri 12 bold italic', bg='bisque', padx=5).pack(side=LEFT, pady=10, padx=10)

        self.fen.bind("<Key>", self.clavierFem)
        
        self.fen.mainloop()

    def clavierHom(self, event):
        touche = event.keysym
        if touche == "Return":
            self.ValiderHom()
            
    def clavierFem(self, event):
        touche = event.keysym
        if touche == "Return":
            self.ValiderFem()
            
    def mod1(self):
        self.value.set(1)

    def mod2(self):
        self.value.set(2)

    def ValiderHom(self):
        if self.entr1.get() == '':
            showinfo('CHAMPS VIDES', 'LE CHAMPS EST VIDE, VEUILLEZ SAISIR !!!')
        elif self.entr1.get().isdigit() == FALSE:
            showinfo('ERREUR VALEUR', 'ERREUR  DE VALEUR !!!\nLA VALEUR SAISIE N\'EST PAS VALABLE !!!')
        elif int(self.entr1.get()) > 100000 or int(self.entr1.get()) < 0:
            showinfo('ERREUR VALEUR', 'LA VALEUR N\'EST PAS PRISE EN COMPTE LIMITE A 100 000) !!!')
        else:
            val = int(self.entr1.get())
            if self.value.get() == 0:
                showinfo('PAS DE CHOIX', 'PAS DE CHOIX !!! CHOISISSEZ ENTRE AJOUTER OU ENLEVER DES POINTS !!!')
            elif self.value.get() == 1:
                self.pointhomme += val
                self.pointhom.set(self.pointhomme)
                self.fen.destroy()    
            elif self.value.get() == 2:
                self.pointhomme -= val
                self.pointhom.set(self.pointhomme)
                self.fen.destroy()

    def ValiderFem(self):
        if self.entr1.get() == '':
            showinfo('CHAMPS VIDES', 'LE CHAMPS EST VIDE, VEUILLEZ SAISIR !!!')
        elif self.entr1.get().isdigit() == FALSE:
            showinfo('ERREUR VALEUR', 'ERREUR  DE VALEUR !!!\nLA VALEUR SAISIE N\'EST PAS VALABLE !!!')
        elif int(self.entr1.get()) > 100000 or int(self.entr1.get()) < 0:
            showinfo('ERREUR VALEUR', 'LA VALEUR N\'EST PAS PRISE EN COMPTE LIMITE A 100 000) !!!')
        else:
            val = int(self.entr1.get())
            if self.value.get() == 0:
                showinfo('PAS DE CHOIX', 'PAS DE CHOIX !!! CHOISISSEZ ENTRE AJOUTER OU ENLEVER DES POINTS !!!')
            elif self.value.get() == 1:
                self.pointfemme += val
                self.pointfem.set(self.pointfemme)
                self.fen.destroy()       
            elif self.value.get() == 2:
                self.pointfemme -= val
                self.pointfem.set(self.pointfemme)
                self.fen.destroy()

    def Quitter(self):
        date = datetime.now()
        if self.pointhomme != 0 or self.pointfemme != 0:
            if askyesno('ATTENTION', 'ETES VOUS SURE DE VOULOIR QUITTER !!!\n  DES POINTS ONT ÉTÉ COMPTABILISÉS !!!'):
                self.fen1.destroy()
            try:
                self.fen.destroy()
                self.verset.destroy()
                self.info.destroy()
            except:
                essai ='Echouer'
        else:
            self.fen1.destroy()
            try:
                self.fen.destroy()
                self.verset.destroy()
                self.info.destroy()
            except:
                essai ='Echouer'
                
        with open('fichiers/log.fju', 'a') as f:
                f.write('%s/%s/%s\t\t%sh %s mins %s sec\t\tSession Ferme !!!\n' % (date.day, date.month, date.year, date.hour, date.minute, date.second))

    def Terminer(self):
        if self.pointhomme == 0 and self.pointfemme ==0:
            showinfo('AUCUN POINT COMPTABILISE', 'AUCUN POINT COMPTABILISE !!!\n\n VEUILLEZ APPUYER SUR QUITTER !!!')
        elif self.pointhomme == self.pointfemme:
            showinfo('EGALITE', 'IL SONT A EGALE POINT VEUILLEZ LES DEPARTAGER !!!')
        else:
            self.sons = mixer.init()
            self.sons = mixer.Sound('sons/Eye Of The Tiger .ogg')
            self.sons.set_volume(5)
            self.sons.play()
            self.fen = Toplevel(self.fen1)
            self.fen.geometry('800x450+330+60')
            self.fen.overrideredirect(1)
            self.fen.grab_set()
            self.fen.focus_set()
            self.fen.config(bg='light sea green')
            
            frametitle = Frame(self.fen, width=700, bg='light sea green')
            frametitle.pack(side=TOP, fill=X)
            Label(frametitle, text='FJU LYON', font='algerian 68 bold', bg='light sea green', fg='red4').pack()
            date = datetime.now()
            Label(frametitle, text='%s/%s/%s' % (date.day, date.month, date.year), font='algerian 20 bold', bg='light sea green', fg='red4').pack()
            
            Point = {'HOMME':self.pointhomme, 'FEMME':self.pointfemme}
            Val = [Point['HOMME'], Point['FEMME']]
            Val = sorted(Val)
            Premier = Val[1]
            Second = Val[0]
            
            for i in Point:
                if Point[i] == Premier:
                    self.Vainqueur = {'NOM':i, 'Point':Premier}
                if Point[i] == Second:
                    self.Deuxieme = {'NOM':i, 'Point':Second}

        
            fram = Frame(self.fen, bg ='light sea green')
            fram.pack()
            self.labvainqueur = Label(fram, text='Vainqueur est: ???', fg='red4', font='algerian 62 bold', bg='light sea green')
            self.labvainqueur.pack(pady=50)

            self.labvainqueur.after(4000, self.actu1)
            self.labvainqueur.after(6000, self.actu2)
            self.labvainqueur.after(8000, self.actu3)
            self.labvainqueur.after(10000, self.Vainq)
                          
            try:
                with open('fichiers/result.fju', 'w') as f:
                    f.write('[Vainqueur]: %s\t[Deuxieme]: %s' % (self.Vainqueur['NOM'], self.Deuxieme['NOM']))
            except:
                with open('fichiers/result.fju', 'x') as f:
                    f.write('[Vainqueur]: %s\t[Deuxieme]: %s' % (self.Vainqueur['NOM'],self. Deuxieme['NOM']))

            with open('fichiers/log.fju', 'a') as f:
                f.write('%s/%s/%s\t\t%sh %s mins %s sec\t\tSession Ferme !!!\n' % (date.day, date.month, date.year, date.hour, date.minute, date.second))

    def actu1(self):
        self.labvainqueur.config(text='.', font='algerian 94 bold')
        
    def actu2(self):
        self.labvainqueur.config(text='..', font='algerian 94 bold')
        
    def actu3(self):
        self.labvainqueur.config(text='...', font='algerian 94 bold')
        
    def Vainq(self):
        self.labvainqueur.config(text='%s' % self.Vainqueur['NOM'], font='algerian 94 bold')
        self.fin()

    def fin(self):
        framefin = Frame(self.fen)
        framefin.pack(side=BOTTOM)
        Button(framefin, text='FIN', bg='light sea green',font='calibri 12 italic', padx=10, command=self.finish).pack()
                     
    def finish(self):
        self.fen.destroy()
        self.fen1.destroy()
        try:
            self.sons.stop()
        except:
            rien = 0


class Presentation():
    def __init__(self):
        val = 0
        self.fen = Tk()
        self.fen.iconbitmap('images/FJU_Lyon.ico')
        self.fen.geometry('+300+50')
        self.fen.config(bg='white')
        self.fen.overrideredirect(1)

        self.col = ["red4","grey60","steel blue1", "green4"]
        i = random.randint(0,3)
        
        self.can = Canvas(self.fen, width=700, height=500, bg=self.col[i])
        self.can.pack(side=TOP)
        photo = PhotoImage(file ='images/Logo FJU.gif')
        item = self.can.create_image(0, 0, anchor=NW, image =photo)
        
        char = Canvas(self.fen, width=700, height=50)
        char.pack(side=TOP)
        
        self.col = ["red4","grey60","steel blue1", "green4"]
        
        screen = TurtleScreen(char)
        t = RawTurtle(screen)
        t.hideturtle()
        t.write('Chargement ...')
        t.up()
        t.goto(-340,0)
        t.width(100)
        t.color(self.col[i])
        t.down()
        t.speed('slowest')
        t.forward(700)

        menubar = Menu(self.fen)

        menu1 = Menu(menubar, tearoff=0)
        menu1.add_separator()
        menu1.add_command(label='Mode Homme vs Femme', command=self.Modehomfem)
        menu1.add_separator()
        menu1.add_command(label='Mode Tribu', command=self.Modetribu)
        menu1.add_separator()
        menu1.add_command(label='Quitter', command=self.fen.destroy)
        menubar.add_cascade(label='FENETRE', menu=menu1)
        
        menu2 = Menu(menubar, tearoff=0)
        menu2.add_command(label='Ajouter Verset du Jour', command=self.Verset)
        menubar.add_cascade(label='VERSET', menu=menu2)

        menu3 = Menu(menubar, tearoff=0)
        menu3.add_command(label='Ajouter Information a faire Passer', command=self.Info)
        menubar.add_cascade(label='INFO', menu=menu3)

        menu4 = Menu(menubar, tearoff=0)
        menu4.add_separator()
        menu4.add_command(label='Ajouter infos Evenement', command=self.AjouterInfoEv)
        menu4.add_separator()
        menu4.add_command(label='Enlever infos Evenement', command=self.EnleverEv)
        menubar.add_cascade(label='EVENEMENT', menu=menu4)
    
        self.fen.config(menu=menubar)
        
        self.Start = Button(self.fen, text='COMMENCER', command=self.Commencer, width=10, height=1,font='Calibri 11 bold italic', bg=self.col[i])
        self.Start.pack(side=BOTTOM)

        self.fen.mainloop()    

    def Verset(self):
        self.fenv = Toplevel(self.fen)
        self.fenv.overrideredirect(1)
        self.fenv.grab_set()
        self.fenv.focus_set()
        self.fenv.geometry('500x200+450+340')
        self.fenv.resizable(width=False,height=False)
        self.fenv.title('FJU LYON VERSET DU JOUR')
        self.fenv.iconbitmap('images/FJU_Lyon.ico')
        self.fenv.configure(bg ='LightCyan2')
		
        Label(self.fenv, text='VERSET DU JOUR', fg='brown4', font='Algerian 45 bold', bg='LightCyan2').pack()
        self.entr1verset = Text(self.fenv, width=50, bg='bisque', height=4)
        self.entr1verset.pack(pady=10)
        fram = Frame(self.fenv, bg='LightCyan2')
        fram.pack()
        Button(fram, text='Valider', command=self.validerVerset, font='calibri 12 bold italic', padx=10, bg='bisque').pack(side=LEFT, padx=10)
        Button(fram, text = 'Annuler', command=self.fenv.destroy,font='calibri 12 bold italic', padx=10, bg='bisque').pack(side=LEFT, padx=10)

        self.fenv.bind("<Key>", self.clavierverset)
        
        self.fenv.mainloop()

    def clavierverset(self, event):
        touche = event.keysym
        if touche == "Return":
            self.validerVerset()
        
    def validerVerset(self):
        textverset = self.entr1verset.get(0.0, END)
        try:
            with open('fichiers/vers.fju', 'w') as f:
                f.write(textverset[:-1])
        except:
            with open('fichiers/vers.fju', 'x') as f:
                f.write(textverset[:-1])

        self.fenv.destroy()

    def Info(self):
        self.fenv = Toplevel(self.fen)
        self.fenv.overrideredirect(1)
        self.fenv.grab_set()
        self.fenv.focus_set()
        self.fenv.geometry('500x200+450+340')
        self.fenv.resizable(width=False,height=False)
        self.fenv.title('FJU LYON INFO')
        self.fenv.iconbitmap('images/FJU_Lyon.ico')
        self.fenv.configure(bg = 'LightCyan2')
		
        Label(self.fenv, text='INFORMATION', fg='brown4', font='Algerian 45 bold', bg='LightCyan2').pack()
        self.entr1info = Text(self.fenv, width=50, bg='bisque', height=4)
        self.entr1info.pack(pady=10)
        fram = Frame(self.fenv, bg='LightCyan2')
        fram.pack()
        Button(fram, text='Valider', command=self.validerInfo, font='calibri 12 bold italic', padx=10, bg='bisque').pack(side=LEFT, padx=10)
        Button(fram, text = 'Annuler', command=self.fenv.destroy,font='calibri 12 bold italic', padx=10, bg='bisque').pack(side=LEFT, padx=10)

        self.fenv.bind("<Key>", self.clavierinfo)
        
        self.fenv.mainloop()

    def clavierinfo(self, event):
        touche = event.keysym
        if touche == "Return":
            self.validerInfo()
        
    def validerInfo(self):
        textinfo = self.entr1info.get(0.0, END)
        try:
            with open('fichiers/info+.fju', 'w') as f:
                f.write(textinfo[:-1])
        except:
            with open('fichiers/info+.fju', 'x') as f:
                f.write(textinfo[:-1])
        
        self.fenv.destroy()

    def AjouterInfoEv(self):
        self.fenv = Toplevel(self.fen)
        self.fenv.overrideredirect(1)
        self.fenv.grab_set()
        self.fenv.focus_set()
        self.fenv.geometry('500x200+450+340')
        self.fenv.resizable(width=False,height=False)
        self.fenv.title('FJU LYON INFO ÉVÉNEMENT')
        self.fenv.iconbitmap('images/FJU_Lyon.ico')
        self.fenv.configure(bg = 'LightCyan2')
		
        Label(self.fenv, text='EVENEMENT', fg='brown', font='Algerian 45 bold',bg = 'LightCyan2').pack()
        self.entrEv = Text(self.fenv, width=50, bg='bisque', height=4)
        self.entrEv.pack(pady=10)
        fram = Frame(self.fenv, bg='LightCyan2')
        fram.pack()
        Button(fram, text='Valider', command=self.ValiderEv, font='calibri 12 bold italic',bg = 'bisque', padx=10).pack(side=LEFT, padx=10)
        Button(fram, text = 'Annuler', command=self.fenv.destroy,font='calibri 12 bold italic', bg = 'bisque', padx=10).pack(side=LEFT, padx=10)

        self.fenv.bind("<Key>", self.clavierAjouterEv)
        
        self.fenv.mainloop()

    def clavierAjouterEv(self, event):
        touche = event.keysym
        if touche == "Return":
            self.ValiderEv()
            
    def ValiderEv(self):
        infoEv =  self.entrEv.get(0.0, END)
        try:
            with open('fichiers/infoEv.fju', 'w') as f:
                f.write(infoEv[:-1])
        except:
            with open('fichiers/infoEv.fju', 'x') as f:
                f.write(infoEv[:-1])
        self.fenv.destroy()

    def EnleverEv(self):
        if askyesno('ENLEVER ÉVÉNEMENT', 'VOULEZ VOUS ENREGISTRER L\'ÉVÉNEMENT ENREGISTRÉ ?'):
            with open('fichiers/infoEv.fju', 'w') as f:
                f.write('')
        else:
            rien = ''

    def Modehomfem(self):
        self.Start.configure(command=self.SelectHomFem)
        showinfo('MODE', 'MODE HOMME VS FEMME SELECTIONÉ !!!')

    def Modetribu(self):
        self.Start.configure(command=self.SelectTribu)
        showinfo('MODE', 'MODE TRIBU SELECTIONÉ !!!')

    def SelectHomFem(self):
        self.fen.destroy()
        Fentre = HomFem()

    def SelectTribu(self):
        self.fen.destroy()
        Fentre = Tribu()

    def Commencer(self):
        self.fen.destroy()
        Fentre = Tribu()

class Marquee(Canvas):
    def __init__(self, parent, text, margin=2, borderwidth=1, relief='flat', fps=30):
        Canvas.__init__(self, parent, borderwidth=borderwidth, relief=relief)
        self.fps = fps

        text = self.create_text(0, -1000, text=text,font='calibri 18 italic', anchor="w", tags=("text",))
        (x0, y0, x1, y1) = self.bbox("text")
        width = (x1 - x0) + (2*margin) + (2*borderwidth)
        height = (y1 - y0) + (2*margin) + (2*borderwidth)
        self.configure(width=width, height=height)

        self.animate()
        
    def animate(self):
        (x0, y0, x1, y1) = self.bbox("text")
        if x1 < 0 or y0 < 0:
            x0 = self.winfo_width()
            y0 = int(self.winfo_height()/2)
            self.coords("text", x0, y0)
        else:
            self.move("text", -3, 0)

        self.after_id = self.after(int(1000/self.fps), self.animate)
        
class Identification():
    def __init__(self):
        self.CODE = ['²','~','\n',' ', 'i', 'U','§','j', '[','©', '}','k', '(','P', 'l', ']','D', 'm', 'S', 'n', 'o', '-', '|', '&', 'p', 'q', 'C','{', 'a', 'b', 'c', 'd', 'e','E', 'H', 'F','_', 'é', 'ç', 'ê','ô', 'â', 'J', 'K', '8', 'L', '^', 'M', '\'', 'N','\"', 'O', 'Y', 'Z', 'f', 'g', 'h', 'r', 's', 't', 'u', 'v', 'w', 'x', '0', 'y', 'z' , '1', '2','A', '4', 'W', '5','G', '6', 'I','7', ",", '@', '!', '.', '?', ';', ':', '/', "'", '*', '+', 'T', '3', 'V', 'B', '#', 'Q', 'R', 'X', ')', 'î', '9']
        self.fen1 = Tk()
        self.fen1.geometry('+400+300')
        self.fen1.resizable(width=False,height=False)
        self.fen1.title(' FJU LYON Identification')
        self.fen1.iconbitmap('images/FJU_Lyon.ico')
        self.fen1.configure(bg = 'LightCyan2')
            
        fram1 = Frame(self.fen1, bg = 'LightCyan2')
        fram1.pack()
        
        Label(fram1, text = 'Utilisateur',bg = 'LightCyan2', font='calibri 12 bold italic').pack(side = LEFT, padx = 5, pady = 5)
        Label(fram1, text = 'Mot de passe ',bg = 'LightCyan2', font='calibri 12 bold italic').pack(side = LEFT, padx = 5, pady = 5)
    
        self.entre1 = Entry(fram1, bg ='bisque', fg='maroon', font='calibri 12 bold italic')
        self.entre2 = Entry(fram1, show='*', bg ='bisque', fg='maroon', font='calibri 12 bold italic')
        self.entre2.pack(side = RIGHT, padx = 5, pady = 5)
        self.entre1.pack(side = RIGHT, padx = 5, pady = 5)

        framz = Frame(self.fen1, bg='LightCyan2')
        framz.pack()
        
        self.val = IntVar()
        Checkbutton(framz, text='Enregistrer Id & Mp', variable=self.val, bg='LightCyan2', font='calibri 10 bold italic').pack(side=LEFT)

        self.val1 = IntVar()
        Checkbutton(framz, text='Deja !', variable=self.val1, command=self.deja, bg='LightCyan2', font='calibri 10 bold italic').pack(side=LEFT, padx=10) 
        
        self.fram2 = Frame(self.fen1, bg='LightCyan2')
        self.fram2.pack()
        
        Button(self.fram2, text='Valider', bg = 'bisque', command=self.Valider, padx=5, font='calibri 12 bold italic').pack(pady =5, padx=10)

        self.samuel = {'ID':'%s' % self.cryptbin('TheChoosenOne'), 'MP':'%s' % self.cryptbin('Langagecwane2016.:TheoneandonlY')}
        self.cusman = {'ID':'%s' % self.cryptbin('cusman'), 'MP':'%s' % self.cryptbin('OuvrierCusman')}

        self.fen1.bind("<Key>", self.clavier)

        self.fen1.mainloop()
        
    def deja(self):
        try:
            with open('fichiers/etat.fju', 'r') as f:
                self.texttext = self.decryptbin(f.read())
        except:
            f = open('fichiers/etat.fju', 'x')
        
        try:
            with open('fichiers/eng.fju', 'r')  as f:
                text1 = self.decryptbin(f.read())
        except:
            f = open('fichiers/eng.fju', 'x')
            
        try:
            with open('fichiers/eng1.fju', 'r')  as f:
                text2 = self.decryptbin(f.read())
        except:
            f = open('fichiers/eng1.fju', 'x')

        if self.val1.get() == 1:
            self.entre1.insert(0, text1)
            self.entre2.insert(0, text2)
        else:
            self.entre1.delete(0, 100)
            self.entre2.delete(0, 100)
        

    def clavier(self, event):
        touche = event.keysym
        if touche == "Return":
            self.Valider()
            
    def cryptbin (self, chaine):
        liste = list(chaine)
        IN = []
        BIN = []
        for i in liste:
            if i in self.CODE:
                ind = self.CODE.index(i)
                IN.append(ind)
        for i in IN:
            BIN.append(bin(i))
        return "".join(BIN)

    def debin(self, chaine):
        chaine = list(chaine)
        chaine.reverse()
        val = 0
        tot = 0
        for i in chaine:
            if i == '1':
                tot += 2 ** val
            val += 1
        return int(tot)

    def decryptbin(self, chaine):
        valeur = []
        liste  = []
        chaine = chaine.split('0b')
        try:
            chaine.remove('')
        except:
            zero = 0
        for i in chaine:
            valeur.append(self.debin(i))
        for i in valeur:
            liste.append(self.CODE[i])
        return "".join(liste)

    def Valider(self):
        util = self.entre1.get()
        mp = self.entre2.get()
        ID = ''
        MP = ''
        debut = datetime.now()
        liste = [self.samuel,self.cusman]
        for i in liste:
            if util == self.decryptbin(i['ID']) and mp == self.decryptbin(i['MP']):
                ID = self.decryptbin(i['ID'])
                MP = self.decryptbin(i['MP'])

        if util == ''  or mp == '':
            showinfo('CHAMPS VIDES', 'LE CHAMPS EST VIDE, VEUILLEZ SAISIR !!!')
        elif ID == util and MP == mp:
            try:
                with open('fichiers/log.fju', 'a') as self.f:
                    self.f.write('------------------------------------------------------\n%s/%s/%s\t\t' % (debut.day, debut.month, debut.year) + '%sh %s mins %s sec\t\t%s CONNECTE\n' % (debut.hour, debut.minute, debut.second, ID.upper()))
                
            except:
                with open('fichiers/log.fju', 'x') as self.f:
                    self.f.write('------------------------------------------------------\n%s/%s/%s\t\t' % (debut.day, debut.month, debut.year) + '%sh %s mins %s sec\t\t%s CONNECTE\n' % (debut.hour, debut.minute, debut.second, ID.upper()))
            if ID == util and MP == mp:
                try:
                    with open('fichiers/app.fju', 'w') as f:
                        f.write(self.cryptbin(ID))
                except:
                    with open('fichiers/app.fju', 'x') as f:
                        f.write(self.cryptbin(ID))

                
                if self.val.get() == 1:
                    try:
                        with open('fichiers/etat.fju', 'w') as f:
                            f.write(self.cryptbin(str(self.val.get())))
                    except:
                        with open('fichiers/etat.fju', 'x') as f:
                            f.write(self.cryptbin(self.val.get()))
                            
                    try:
                        with open('fichiers/eng.fju', 'w') as f:
                            f.write(self.cryptbin(ID))
                    except:
                        with open('fichiers/eng.fju', 'x') as f:
                            f.write(self.cryptbin(ID))
                            
                    try:
                        with open('fichiers/eng1.fju','w') as f:
                            f.write(self.cryptbin(MP))
                    except:
                        with open('fichiers/eng1.fju','x') as f:
                            f.write(self.cryptbin(MP))
                    

                self.fen1.destroy()
                Pre = Presentation()
        else:
            showwarning('ERROR', 'UTILISATEUR OU MOT DE PASSE NON VALIDE !!!')
                    
Demarrer = Identification()
