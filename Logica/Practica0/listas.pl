%Rubén Rodríguez Catrufo ruben.rodriguez.catrufo@udc.es
%Iago Núñez Lourés iago.nunez.loures@udc.es

% 1º Crear predicado suma(L,N), que toma cualquier lista de números enteros L y devuelve en N la suma total de todos los elementos de L.
%Caso base 
suma([],0).

%Caso recursivo     
suma([Head|Tail],Result) :-
    suma(Tail, ResultSuma),
    Result is Head + ResultSuma.


% 2º Crear predicado intervalo(A,B,L) que toma como entrada dos números enteros A y B y tiene que generar en L la lista de números
% comprendida entre A y B.
%Casos base 
intervalo(X,X,[X]).

intervalo(A,B,[]):-
    A > B.

%Caso recursivo
intervalo(A,B,[A|Tail]) :-
    B > A,
    Siguiente is A + 1,
    intervalo(Siguiente,B,Tail).

% 3º Crear predicado inserta(X,L1,L2) que inserta un elemento X en una lista L1 que está previamente ordenada (con la relación de orden @<)
% y devuelve la nueva lista L2 ordenada pero conteniendo también el nuevo elemento X.
%Caso base
inserta(X,[],[X]).

%Caso recursivo
inserta(D,[Head|Tail],[D, Head|Tail]) :-
    D @=< Head.

inserta(D,[Head|Tail],[Head|Resto]):-
    D @> Head,
    inserta(D,Tail,Resto).
        

% 4º Crear predicado insercion(L1,L2) que ordena cualquier lista L1 para devolver la lista ordenada L2 con los mismos elementos que L1, 
% utilizando el método de ordenación por inserción. 
%Caso base
insercion([],[]).

%Caso recursivo
insercion([Head|Tail],Res):-
    insercion(Tail,Resto),
    inserta(Head,Resto,Res). 



