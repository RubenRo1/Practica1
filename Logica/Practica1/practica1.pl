% Rubén Rodríguez Catrufo ruben.rodriguez.catrufo@udc.es
% Iago Núñez Lourés iago.nunez.loures@udc.es

meta([1,2,3,4,5,6,7,8,0]). %Meta final

%Estados iniciales
initial1([1,2,3,7,4,6,5,0,8]). %Longitud 5
initial2([4,1,3,7,2,5,0,8,6]). %Longitud 6
initial3([1,6,2,3,0,8,4,7,5]). %Longitud 12
initial4([7,2,1,8,0,3,5,4,6]). %Longitud 20


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

%remplazar_elemento(Lista, Indice, Elemento, Resultado) -> Sustituye un elemento en una posicion por un nuevo elemento

%Caso base
%Si el índice es igual a 0 devuelve el nuevo elemento(C) más lo que queda de la lista 
remplazar_elemento([_|Tail],0, C, [C|Tail]) :- !.

% %Caso recursivo
% %Mientras el índice sea mayor que 0, se conserva la cabeza actual (Head) en la 
% %lista resultante y se busca la posición en la cola (Tail) restando 1 al índice.
remplazar_elemento([Head|Tail],I, C, [Head|Result]) :-
    I > 0,
    I2 is I - 1,
    remplazar_elemento(Tail,I2,C,Result).

% %expandir() ->Se llaman a los predicados correspondientes para realizar un cambio en las posiciones, y mostrar todos los movimientos
expandir(S0, A, S1) :-
    nth0(Pos,S0,0), %Buscamos el 0
    ady(Pos,A,R), %Miramos si pude ir a la dirección A(norte, sur, este, oeste)
    nth0(R,S0,ElementoCambio), %Obtiene el número q hay en R 
    remplazar_elemento(S0,Pos,ElementoCambio,S), %Sustituir la posición Pos(Posición del 0) por ElementoCambio.
    remplazar_elemento(S,R,0,S1).   %Sustituir la posición R(Posición del elemento) por 0
    
%buscar(Modo,nodo([],S0),[],Plan).

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
    
    
busca_limite(_,_,S,Plan,Plan) :-
    meta(S), !. %Si la lista actual(S) es igual a la meta, devuelve el plan actual
    
busca_limite(N,Max,S0,Plan0,Plan) :-
    N < Max, %Comprueba q N sea menor q Max
    N2 is N + 1, %Suma 1 a N(Creando N2)
    expandir(S0,P,S1), %Llamamos a expandir para generar un nuevo estado del 8 puzle(S1), y guardar el Plna(P)
    busca_limite(N2,Max,S1,[P|Plan0],Plan). %Volvemos a llamar busca_limite pero añadiendo P al Plan0(plan actual)
    
plan(iter,S0,Plan):- %Predicado plan para llamar a busca_limite(itera)
    !,itera(0,S0,Plan).

plan(Modo,S0,Plan):- %Predicado plan para llamar a buscar
    buscar(Modo,[nodo([],S0)],[],PlanR),
    reverse(PlanR,Plan).

itera(Max,S0,Plan) :- %Llama a busca_limite y devuelve el plan final
    busca_limite(0,Max,S0,[],PlanR),
     !,
     reverse(PlanR,Plan).
    
itera(Max,S0,Plan) :- %Si la anterior llamada da false suma 1 a Max(contador) y vuelve a llamarse
    Max2 is Max + 1,
    itera(Max2,S0,Plan).