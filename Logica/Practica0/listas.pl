%Rubén Rodríguez Catrufo ruben.rodriguez.catrufo@udc.es
%Iago Núñez Lourés iago.nunez.loures@udc.es

suma([],0).

suma([Head|Tail],Result) :-
    suma(Tail, ResultSuma),
    Result is Head + ResultSuma.


intervalo(X,X,[X]).

intervalo(A,B,[]):-
    A > B.

intervalo(A,B,[A|Tail]) :-
    B > A,
    Siguiente is A + 1,
    intervalo(Siguiente,B,Tail).


inserta(X,[],[X]).

inserta(D,[Head|Tail],[D, Head|Tail]) :-
    D @< Head.

inserta(D,[Head|Tail],[Head|Resto]):-
    D @> Head,
    inserta(D,Tail,Resto).
        



