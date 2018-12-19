class Etat:
    def __init__(self,nomDonne,initial=False,final=False):
        self.nom=nomDonne
        self.initial=initial
        self.final=final
        self.transitionsSortantes=[]
        

    def __str__(self):
         return'{}'.format(self.nom)
         
    def __repr__(self) :
        return 'Etat : {}'.format(self)
        
    def ajouterTransitionSortante(self,transition):
            self.transitionsSortantes.append(transition) 

class Evenement:
     def __init__(self,nomDonne,controle=False):
         self.nom=nomDonne
         self.controle=controle
     def __str__(self):
         return'{}'.format(self.nom)
     def __repr__(self) :
          return 'Evenement : {}'.format(self)

class Transition:
    def __init__(self,depart,arrivee):
         self.depart=depart
         self.arrivee=arrivee
         self.evenements=[]
         self.depart.ajouterTransitionSortante(self)
         
    def __str__(self):
        return'({},{},{})'.format(self.depart,self.arrivee,self.evenements)
         
    def __repr__(self) :
        return 'Transition : {}'.format(self)
    
    def enregistrerEvt(self,evt):
        self.evenements.append(evt)
     
class Automate:
    def __init__(self,nomDonne,probleme):
        self.nom=nomDonne
        self.probleme=probleme
        self.etats=[]
        self.etatNomme={} # cle : nom, valeur : obj
        self.transitions=[]
        
        
    def __str__(self):
         return'{}'.format(self.nom)
         
    def __repr__(self) :
        return 'Automate : {}'.format(self)
    
    def ajouterEtat(self,nom,initial,final):
        objEtat=Etat(nom,initial,final)
        self.etats.append(objEtat)
        self.etatNomme[nom]=objEtat
    
    def ajouterTransition(self,nomEtatDepart,nomEtatArrivee,listeNomsEvts):
        objEtatDepart=self.etatNomme[nomEtatDepart]
        objEtatArrivee=self.etatNomme[nomEtatArrivee]
        objtrans=Transition(objEtatDepart,objEtatArrivee)
        self.transitions.append(objtrans)
    
        for nom in listeNomsEvts :
            objEvt=self.probleme.evtNomme[nom]
            objtrans.enregistrerEvt(objEvt)
            
    
                           
    def sAfficher(self):
        print(self)
        for etat in self.etats:
            print (etat)
        for etat in self.etats:
            print (etat,etat.transitionsSortantes)
        

class Probleme:
    def __init__(self,nomprob):
        
        self.nom=nomprob
        self.evts=[]
        self.plant=None
        self.spec=None
        self.superviseur=None
        self.plantspec=None
        self.evtNomme={} # cle : nom, valeur : obj
        
        
    def __str__(self):
         return'{}'.format(self.nom)
         
    def __repr__(self) :
        return 'Probleme : {}'.format(self)
    

    def ajouterEvenement(self,nom,controle):
        objEvt=Evenement(nom,controle)
        self.evts.append(objEvt)
        self.evtNomme[nom]=objEvt
    
    
        
    def creerPlant(self,donnees):
        nom,donneesEtats,donneesTransitions=donnees
        self.plant=Automate(nom,self)
        for elt in donneesEtats :
            nom,initial,final=elt
            self.plant.ajouterEtat(nom,initial,final)
          
            
        for elt in donneesTransitions:
            nomDepart,nomArrivee,listeNomsEvt=elt
            self.plant.ajouterTransition(nomDepart,nomArrivee,listeNomsEvt)
            
        
             
    def creerspec(self,donnees):
        nom,donneesEtats,donneesTransitions=donnees
        self.spec=Automate(nom,self)
        for elt in donneesEtats :
            nom,initial,final=elt
            self.spec.ajouterEtat(nom,initial,final)
        for elt in donneesTransitions:
            nomDepart,nomArrivee,listeNomsEvt=elt
            self.spec.ajouterTransition(nomDepart,nomArrivee,listeNomsEvt)
            
    def creerplantspec(self,donnees):
         nom,donneesEtats,donneesTransitions=donnees
         self.plantspec=Automate(nom,self)
         for elt in donneesEtats :
            nom,initial,final=elt
           
            (self.spec+self.plant).ajouterEtat(nom,initial,final)
         for elt in donneesTransitions:
            nomDepart,nomArrivee,listeNomsEvt=elt
            self.spec.ajouterTransition(nomDepart,nomArrivee,listeNomsEvt)
            
         
         
        

donnees=("nomprob",[("e1",True),("e2",True),("e3",True),("s1",False),("s2",False),("s3",False)],
                    ("plant",[("S4",True,False),("S1",False,False),("S2",False,True)],
                              [("S4","S1",["e1","e2","e3"]),("S1","S2",["e1","e3"]),("S1","S4",["s1","s2","s3"]),("S2","S1",["s1","s2","s3"])]),
                    ("spec",[("S0",True,False),("S1",False,False),("S2",False,True)],[("S0","S1",["e1","e2","e3"]),("S1","S2",["e1","e2","e3"]),("S1","S0",["s1","s2","s3"]),("S2","S1",["s1","s2","s3"])]))
 


nom,donneesEvts,donneesPlant,donneesSpec=donnees

monProbleme=Probleme(nom)

for elt in donneesEvts:
    nom,controle=elt
    monProbleme.ajouterEvenement(nom,controle)


monProbleme.creerPlant(donneesPlant)
monProbleme.plant.sAfficher()

monProbleme.creerspec(donneesSpec)
monProbleme.spec.sAfficher()
    
   
