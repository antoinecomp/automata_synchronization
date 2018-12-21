class Etat:
    """Etat is a class that stands for a state where an automaton can be in the state universe.

    """
    def __init__(self,nomDonne,initial=False,final=False):
        """method to instantiate an Etat object

        Args:
            nomDonne (str): name given to Etat.
            initial (bool): tells if the Etat is the initial state.
            final (bool): tells if the Etat is the final state.
        
        Attributes:
            nom (str): is the name given to the given Etat.
            initial (bool): tells if the Etat is the initial state.
            final (bool): tells if the Etat is the final state.
            transitionsSortantes (array): array of transition from the given Etat.

        """
        self.nom=nomDonne
        self.initial=initial
        self.final=final
        self.transitionsSortantes=[] # Array of transition coming from the given state, intiated as empty
        
    #@property
    def __str__(self):
        """str: give back the name of the Etat"""
        return'{}'.format(self.nom)
         
    def __repr__(self) :
        """str: give back ???"""
        return 'Etat : {}'.format(self)
        
    def ajouterTransitionSortante(self,transition):
        """add Transition going out of the state to the array of transitions.

        Args:
            transition: a transition from the given state to another state. For instance : ("S1","S4",["s1","s2","s3"])
        """
        self.transitionsSortantes.append(transition)

class Evenement:
    """Evenement is a class that stands for an event that is part of the conditions to shift from a state to another.

    """
    def __init__(self,nomDonne,controle=False):
        """method to instantiate an Evenement object

        Args:
            nom (str): name given to Etat.
            controle (bool): ???
            
        Attributes:
            nomDonne (str): is the name given to the given Evenement.
            controle (bool): ???

        """
        self.nom=nomDonne
        self.controle=controle
    def __str__(self):
        """str: give back the name of the Evenement"""
        return'{}'.format(self.nom)
        
    def __repr__(self) :
        """str: give back ???"""
        return 'Evenement : {}'.format(self)

class Transition:
    """Transition is a class that stands for the transitions between states.

    """
    def __init__(self,depart,arrivee):
        """method to instantiate an Etat object

        Args:
            depart (Etat): tells if the Etat is the initial state.
            arrivee (Etat): tells if the Etat is the final state.

        """
        self.depart=depart
        self.arrivee=arrivee
        self.evenements=[]
        self.depart.ajouterTransitionSortante(self)
    
    #@property
    def __str__(self):
        """str: give back ???"""
        return'({},{},{})'.format(self.depart,self.arrivee,self.evenements)

    #6/6666666666666666666@property
    def __repr__(self) :
        """str: give back ???"""
        return 'Transition : {}'.format(self)
    
    def enregistrerEvt(self,evt):
        """record necessary transition to shift from a state to a given state (depart) to another (arrivee)

        Args:
            evt (Evenement): event that link two states.
        """
        self.evenements.append(evt)
     
class Automate:
    def __init__(self,nomDonne,probleme):
        """method to instantiate an Automate object
        
        Args:
            nomDonne (str): the name of the automata.
            probleme (Probleme): ???

        Attributes:
            nom (str): the name of the automata.
            probleme (Probleme): tells if the Etat is the final state.
            etats (:obj:`list` of :obj:`Etat`): 
            etatNomme : 
            transitions : list of transitions of the automata 
        """
        self.nom=nomDonne
        self.probleme=probleme
        self.etats=[]
        self.etatNomme={} # cle : nom, valeur : obj
        self.transitions=[]
        
    #@property    
    def __str__(self):
        """str: give back the name of the automata"""
        return'{}'.format(self.nom)
    
    #@property
    def __repr__(self) :
        """str: give back ???"""
        return 'Automate : {}'.format(self)
    
    def ajouterEtat(self,nom,initial,final):
        """instiate and add an Etat to the automata, precising if it is an initial or a final one.

        Args:
            Etat(nom,initial,final) (Etat): instantiate an Etat
        """
        objEtat=Etat(nom,initial,final)
        self.etats.append(objEtat)
        self.etatNomme[nom]=objEtat
        #print(self.etatNomme[nom])
    
    def ajouterTransition(self,nomEtatDepart,nomEtatArrivee,listeNomsEvts):
        """instiate and add a Transition to the automata, precising where it goes from and to.
            
        Args:
            nomEtatDepart (str): the name of the transition starting point.
            nomEtatArrivee (str): the name of the transition ending point.
            listeNomsEvts (:obj:`list` of :obj:`str`): list of the events required for transitionning from a state to another.
            
        Attributes:
            objEtatDepart (Etat): state from which the Transition starts
            objEtatArrivee(Etat): state towards which the Transition goes
            objtrans (Transition): transition object from the instantiation made from objEtatDepart and objEtatArrivee.
        """
        objEtatDepart=self.etatNomme[nomEtatDepart]
        objEtatArrivee=self.etatNomme[nomEtatArrivee]
        objtrans=Transition(objEtatDepart,objEtatArrivee)
        self.transitions.append(objtrans)
    
        for nom in listeNomsEvts :
            objEvt=self.probleme.evtNomme[nom] # ???
            objtrans.enregistrerEvt(objEvt) 
            
    
                           
    def sAfficher(self):
        """print states and transition of the automata"""
        print(self)
        for etat in self.etats:
            print (etat)
        for etat in self.etats:
            print (etat,etat.transitionsSortantes)
        

class Probleme:
    """Probleme is ???

    """
    def __init__(self,nomprob):
        """method to instantiate an Automate object
        
        Args:
            nomprob (str): the name of the problem.
            
        Attributes:
            nom (str): the name of the automata.
            evts (:obj:`list`): tells if the Etat is the final state.
            plant : ??? 
            spec : ???
            superviseur : ???
            plantspec = ???
            evtNomme = ??? # event that are part of the problem. Are they ordered ?
        """
        
        self.nom=nomprob
        self.evts=[]
        self.plant=None
        self.spec=None
        self.superviseur=None
        self.plantspec=None
        self.evtNomme={} # cle : nom, valeur : obj
        
    
    @property
    def __str__(self):
        """return name of the problem"""
        return'{}'.format(self.nom)

    @property      
    def __repr__(self) :
        """return ???"""
        return 'Probleme : {}'.format(self)
    

    def ajouterEvenement(self,nom,controle):
        """instiate and add an Evenement to the problem, .

        Args:
            nom (str): name of the Evenement to add
            crontrole(???): ???
        
        Attributes :
            objEvt (Evenement): event added to the problem
        """
        objEvt=Evenement(nom,controle)
        self.evts.append(objEvt)
        self.evtNomme[nom]=objEvt
    
    
        
    def creerPlant(self,donnees):
        """method to instiate and add Plant automata.

        Args:
            donnees (:obj:`list` of :obj:`str`): name, events, transition and states.
        
        Attributes :
            plant (Automate): automata we want to create with a given name, events and states
        """
        nom,donneesEtats,donneesTransitions=donnees
        self.plant=Automate(nom,self)
        for elt in donneesEtats :
            nom,initial,final=elt
            self.plant.ajouterEtat(nom,initial,final)
          
            
        for elt in donneesTransitions:
            nomDepart,nomArrivee,listeNomsEvt=elt
            self.plant.ajouterTransition(nomDepart,nomArrivee,listeNomsEvt)
            
        
             
    def creerspec(self,donnees):
        """method to create the specifications automata.

        Args:
            donnees (:obj:`list` of :obj:`str`): name, events, transition and states of the specifications automata we want to create.
        
        Attributes :
            spec (Automate): automata of specifications we want to create with a given name, events and states.
        """
        nom,donneesEtats,donneesTransitions=donnees
        self.spec=Automate(nom,self)
        for elt in donneesEtats :
            nom,initial,final=elt
            self.spec.ajouterEtat(nom,initial,final)
        for elt in donneesTransitions:
            nomDepart,nomArrivee,listeNomsEvt=elt
            self.spec.ajouterTransition(nomDepart,nomArrivee,listeNomsEvt)
            
    def creerplantspec(self,donnees):
        """method to create the synchronised automata.

        Args:
            donnees (:obj:`list` of :obj:`str`): name, events, transition and states of the synchronisation automata.
        
        Attributes :
            plantspec (Automate): automata of specifications we want to create with a given name, events and states.
        """
        nom,donneesEtats,donneesTransitions=donnees
        self.plantspec=Automate(nom,self)
        for elt in donneesEtats :
            nom,initial,final=elt
           
            (self.spec+self.plant).ajouterEtat(nom,initial,final)
        for elt in donneesTransitions:
            nomDepart,nomArrivee,listeNomsEvt=elt
            self.spec.ajouterTransition(nomDepart,nomArrivee,listeNomsEvt)
            
         
         
        

'''donnees=("nomprob", #nom
        [("e1",True),("e2",True),("e3",True),("s1",False),("s2",False),("s3",False)], # donneesEvts
        ("plant", # donneesPlant
            [("S4",True,False),("S1",False,False),("S2",False,True)], # states 
            [("S4","S1",["e1","e2","e3"]),("S1","S2",["e1","e3"]),("S1","S4",["s1","s2","s3"]),("S2","S1",["s1","s2","s3"])] # transitions
        ), 
        ("spec", # donneesSpec
            [("S0",True,False),("S1",False,False),("S2",False,True)],# state
            [("S0","S1",["e1","e2","e3"]),("S1","S2",["e1","e2","e3"]),("S1","S0",["s1","s2","s3"]),("S2","S1",["s1","s2","s3"])] # transitions
        )
    ) 
 '''

donnees=("nomprob", # name of the problem
        [("e1",True),("e2",True),("e3",True),("s1",False),("s2",False),("s3",False)], # events
        ("plant",[("S4",True,False),("S1",False,False),("S2",False,True)], # first automata states
            [("S4","S1",["e1","e2","e3"]),("S1","S2",["e1","e3"]),("S1","S4",["s1","s2","s3"]),("S2","S1",["s1","s2","s3"])]), # first automata transitions
        ("spec",[("S0",True,False),("S1",False,False),("S2",False,True)], #second automata s.t0ates
            [("S0","S1",["e1","e2","e3"]),("S1","S2",["e1","e2","e3"]),("S1","S0",["s1","s2","s3"]),("S2","S1",["s1","s2","s3"])] # second automata transitions
        )
    )
 


nom,donneesEvts,donneesPlant,donneesSpec=donnees

monProbleme=Probleme(nom)

for elt in donneesEvts:
    nom,controle=elt
    monProbleme.ajouterEvenement(nom,controle)


monProbleme.creerPlant(donneesPlant)
monProbleme.plant.sAfficher()

monProbleme.creerspec(donneesSpec)
monProbleme.spec.sAfficher()

# we're going to synchronize
def synchroniserProbleme(probleme):
    # we're saving the states of both
    etat_plant = probleme.plant.etats
    etat_spec = probleme.spec.etats
    # we create the automaton merging  plant and spec automata
    autoSynchro = Automate("synchro",probleme)
    # then we synchronize it with all the states
    for etat_p in etat_plant:
        for etat_s in etat_spec:
            synchroniserEtats(autoSynchro, etat_p, etat_s, probleme) 

    
def synchroniserEtats(automateSynchronise, etat_1, etat_2, probleme):
    # we're adding a new state merging the given ones, we're specifying if it is initial with all and final with any
    print str(etat_1.nom + etat_2.nom)
    automateSynchronise.ajouterEtat(str(etat_1.nom + etat_2.nom), all([etat_1.initial,etat_2.initial]), any([etat_1.final, etat_2.final]))
    
    # 
    for transition_1 in etat_1.transitionsSortantes:
        for transition_2 in etat_2.transitionsSortantes:
            automateSynchronise.ajouterEtat(str(transition_1.arrivee.nom+transition_2.arrivee.nom), all([transition_1.arrivee.nom,transition_2.arrivee.nom]), any([transition_1.arrivee.nom,transition_2.arrivee.nom]))
            # we're going to find the subset of the events that are part of both transitions
            ev = list(set(transition_1.evenements).intersection(transition_2.evenements))
            # we're going to create the transition in the merging automaton
            automateSynchronise.ajouterTransition(str(etat_1.nom+etat_2.nom),str(transition_1.arrivee.nom+transition_2.arrivee.nom), ev)

synchroniserProbleme(monProbleme)
        
    
   
