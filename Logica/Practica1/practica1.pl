
meta([1,2,3,4,5,6,7,8,0]). %Meta final

%Estados iniciales
initial1([1,2,3,7,4,6,5,0,8]).
initial2([4,1,3,7,2,5,0,8,6]).
initial3([1,6,2,3,0,8,4,7,5]).


%Dice el elemento Norte(R) al numero X
ady(X,n,R) :-
    R is X - 3,
    R >=0.
   
%Dice el elemento Sur(R) al numero X
ady(X,s,R) :-
    R is X + 3,
    R =< 8.

%Dice el elemento Este(R) al numero X
ady(X,e,R) :-
    R is X + 1,
    X mod 3 < 2.

%Dice el elemento Oeste(R) al numero X
ady(X,w,R) :-
    R is X - 1,
    X mod 3 > 0.


%localizar_pos() -> Localiza la posicion del cero

%Caso base 
%Si el primer elemento de la lista es un 0 devuelve la posición
localizar_pos([0|_], C, C) :- !.

%Caso recursivo
%Creamos un contador(C1) inicializado en C(0) y llamamos recursivamente a la funcion eliminando el 1 elemento de la lista
localizar_pos([_|Tail],C,Pos) :-
    C1 is C + 1,
    localizar_pos(Tail,C1,Pos).

%obtener_elemento() -> Obtiene el valor numerico de la posicion que se le pase como argumento

%Caso base
%Una vez el contador llegue a 0, devuelve el 1º elemento de la lista
obtener_elemento([Head|_],0,Head) :- !.

%Caso recursivo
%Se crea un contador(C1) inicializado en la posicion que queremos obtener(C) se resta uno y llama recursivamente a la funcion eliminando el 1 elemento de la lista
obtener_elemento([_|Tail],C,X) :-
    C1 is C - 1,
    obtener_elemento(Tail,C1,X).

%remplazar_elemento() -> Sstutiye un elemento en una posicion por un nuevo elemento

%Caso base
%Si el índice es igual a 0 devuelve el nuevo elemento(C) más lo que queda de la lista 
remplazar_elemento([_|Tail],0, C, [C|Tail]) :- !.

%Caso recursivo
%Mientras el índice sea mayor que 0, se conserva la cabeza actual (Head) en la 
%lista resultante y se busca la posición en la cola (Tail) restando 1 al índice.
remplazar_elemento([Head|Tail],I, C, [Head|Result]) :-
    I2 is I - 1,
    remplazar_elemento(Tail,I2,C,Result).

%Se llaman a los predicados correspondientes para realizar un cambio en las posiciones,
%0 a todas las posibles
expandir(S0, A, S1) :-
    localizar_pos(S0,0,Pos), %Buscamos el 0
    ady(Pos,A,R), %Miramos si pude ir a la dirección A(norte, sur, este, oeste)
    obtener_elemento(S0,R,ElementoCambio), %Obtenemos el elemento de la posicion A
    remplazar_elemento(S0,Pos,ElementoCambio,S), %Sustituir la posición Pos(Posición del 0) por PosCambio(Elemento A).
    remplazar_elemento(S,R,0,S1).   %Sustituir la posición R(Posición del elemento) por 0

%buscar(Modo,nodo([],S0),[],Plan).

%Busacar
%Si el estado S(lista) del nodo es igual a la meta devolvemos P(pasos necesarios para llegar a S)
buscar(_,[nodo(P,S)|_],_,P):-
meta(S), !. %meta(S) devuelve true si S es igual a [1,2,3,4,5,6,7,8,0]

buscar(Modo,[nodo(_,S)|Tail],Visitados,Plan) :-
    member(S, Visitados), !, %este member se usa para ver si S esta en Visitados
    buscar(Modo,Tail,Visitados,Plan). %En ese caso volvemos a llamar a buscar pero sin el 1º elemento en nodos

buscar(profund,[nodo(P,S)|Tail],Visitados,Plan) :-
    findall(nodo([M | P],S1),expandir(S,M,S1),Expandidos), %findall supongo xd
    append(Expandidos,Tail, Nodos2), %creamos una nueva lista Nodos2, Expandidos se añadirá a la cabeza de la de Nodos
    buscar(profund, Nodos2, [S|Visitados], Plan). %Volvemos a llamar a buscar pero con Nodos2 y añadiendo S a la lista de Visitados

buscar(anchura,[nodo(P,S)|Tail],Visitados,Plan) :-
    findall(nodo([M | P],S1),expandir(S,M,S1),Expandidos),%findall por segunda vez supongo xd
    append(Tail, Expandidos, Nodos2),%creamos una nueva lista Nodos2, Expandidos se añadirá al cfinal de la de Nodos
    buscar(anchura, Nodos2, [S|Visitados], Plan).%Volvemos a llamar a buscar pero con Nodos2 y añadiendo S a la lista de Visitados
    
plan(Modo,S0,Plan):- %Predicado plan para llamar a buscar
    buscar(Modo,[nodo([],S0)],[],Plan).

