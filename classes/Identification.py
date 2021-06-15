from tkinter import Tk, Frame, Label, Button, Entry, IntVar, RIGHT, LEFT, BOTTOM, Checkbutton, Text
from tkinter.messagebox import showerror
from classes.Tribu import Tribu


class Identification:
    def __init__(self, fenetre):
        self.fen = fenetre
        self.Fenetre = self.fen
        self.Fenetre.title("identification PROG FJU")
        self.Fenetre.iconbitmap("./images/FJU_Lyon.ico")
        self.Fenetre.geometry('+400+300')
        self.Fenetre.resizable(width=False, height=False)
        self.Fenetre.configure(bg='LightCyan2')

        self.loadFentre()

        self.Fenetre.mainloop()

    def loadFentre(self):
        self.divPrincipale = Frame(self.Fenetre, bg='LightCyan2')
        self.divPrincipale.pack()

        Label(self.divPrincipale, text='Utilisateur', bg='LightCyan2',
              font='calibri 12 bold italic').pack(side=LEFT, padx=5, pady=5)
        Label(self.divPrincipale, text='Mot de passe ', bg='LightCyan2',
              font='calibri 12 bold italic').pack(side=LEFT, padx=5, pady=5)

        self.Utillisateur = Entry(self.divPrincipale, bg='bisque',
                                  fg='maroon', font='calibri 12 bold italic')
        self.Motdepasse = Entry(self.divPrincipale, show='*', bg='bisque',
                                fg='maroon', font='calibri 12 bold italic')
        self.Motdepasse.pack(side=RIGHT, padx=5, pady=5)
        self.Utillisateur.pack(side=RIGHT, padx=5, pady=5)

        self.divOptions = Frame(self.Fenetre, bg='LightCyan2')
        self.divOptions.pack()

        self.val = IntVar()
        Checkbutton(self.divOptions, text='Afficher Mot de passe', variable=self.val, command=self.AfficherMp,
                    bg='LightCyan2', font='calibri 10 bold italic').pack(side=LEFT)

        self.divValider = Frame(self.Fenetre, bg='LightCyan2')
        self.divValider.pack()

        Button(self.divValider, text='Valider', bg='bisque', command=self.ValiderIdentification,
               padx=5, font='calibri 12 bold italic').pack(side=BOTTOM, pady=5, padx=10)

        self.Fenetre.bind("<Key>", self.clavier)

    def clavier(self, event):
        touche = event.keysym
        if touche == "Return":
            self.ValiderIdentification()

    def detruireLoadInit(self):
        self.divPrincipale.destroy()
        self.divOptions.destroy()
        self.divValider.destroy()

    def AfficherMp(self):
        if self.val.get() == 0:
            self.Motdepasse.config(show="*")
        if self.val.get() == 1:
            self.Motdepasse.config(show="")

    def ValiderIdentification(self):
        if (self.Utillisateur.get() != "FJULyon.," and self.Motdepasse.get() != "Fju69007Lyon"):
            showerror("IDENTIFIANT INCORRECTE !",
                      "les identifiants sont incorrect")
        else:
            self.detruireLoadInit()
            self.getGroupes()

    def getGroupes(self):
        Label(self.Fenetre, text="Ajouter les noms des groupe une par une !",
              font="calibri 12 normal italic", bg="LightCyan2").pack()
        self.divPrincipale = Frame(self.Fenetre, bg='LightCyan2')
        self.divPrincipale.pack(padx=10, pady=5)
        Label(self.divPrincipale, text="Nom du groupe", bg='LightCyan2', font='calibri 12 bold italic').pack(
            side=LEFT, padx=5, pady=5)
        self.donnee = Entry(self.divPrincipale, bg='bisque',
                            fg='maroon', font='calibri 12 bold italic')
        self.donnee.pack(side=RIGHT, padx=5, pady=5)

        divValider = Frame(self.Fenetre, bg='LightCyan2')
        divValider.pack()

        self.validerTribu = Button(divValider, text='Valider', bg='bisque', command="",
                                   padx=5, font='calibri 12 bold italic').pack(pady=5, padx=10)
