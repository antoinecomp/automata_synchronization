# automata_synchronization

Here is an attempt to construct something that would do the synchronized product between two automata. For instance with the following automatas :

```
(Etat : S4, [Transition : (S4,S1,[Evenement : e1, Evenement : e2, Evenement : e3])])
(Etat : S1, [Transition : (S1,S2,[Evenement : e1, Evenement : e3]), Transition : (S1,S4,[Evenement : s1, Evenement : s2, Evenement : s3])])
(Etat : S2, [Transition : (S2,S1,[Evenement : s1, Evenement : s2, Evenement : s3])])
``` 

and

```
(Etat : S0, [Transition : (S0,S1,[Evenement : e1, Evenement : e2, Evenement : e3])])
(Etat : S1, [Transition : (S1,S2,[Evenement : e1, Evenement : e2, Evenement : e3]), Transition : (S1,S0,[Evenement : s1, Evenement : s2, Evenement : s3])])
(Etat : S2, [Transition : (S2,S1,[Evenement : s1, Evenement : s2, Evenement : s3])])
``` 

Would be, if I'm correct :

[![synchronization][1]][1]


  [1]: https://i.stack.imgur.com/iZCZV.png
