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

Would be :

[![synchronization][1]][1]


The product of A and B is the automaton : 
$A \times B := Ac⟨Q_A \times Q_B, \sum A \bigcap \sum B, \delta, i_A.i_B, M_A \times M_B⟩$

where $Q_A \times Q_B$ is the combination of all states. If $QA = \{a_1, a2\}$ and QB = {b1, b2}
then QA × QB = {a1.b1, a1.b2, a2.b1, a2.b2}
δ(qA.qB, e) := {
δA(qA, e).δB(qB, e) if δA(qA, e) and δB(qB, e) defined
undefined otherwise


  [1]: https://i.stack.imgur.com/1blWq.png
