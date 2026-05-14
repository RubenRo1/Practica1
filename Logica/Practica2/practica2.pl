:- op(1060, yfx, <->). %doble implicación
:- op(1050, yfx, <-). %implicación hacia la izquierda
:- op(600, yfx, v). %disyunción
:- op(400, yfx, &). %conjunción
                    %negación usamos el '-'
:- op(200, fx, forall). %universal
:- op(200, fx, exists). %existencial
:- op(300, xfy, ::). %separador para cuantificadores

% subs(X/T,F,G) Remplaza var X by term T on formula or term F to produce G
% subs_list(L,F,G) replaces a list of pairs X/T in F to get G

%Variable
%Si F es X, el resultado G es directamente el término T.
subs(X/T, X, T) :- !.

%forall/exits
%Si intentamos sustituir X, pero X está ligada por un forall/exists, NO tocamos nada.
subs(X/_, forall X :: F, forall X :: F) :- !.
subs(X/_, exists X :: F, exists X :: F) :- !.


%Si el cuantificador es sobre otra variable (Y), entramos a sustituir en la fórmula F.
subs(X/T, forall Y :: F, forall Y :: G) :- !,
    subs(X/T, F, G).

subs(X/T, exists Y :: F, exists Y :: G) :- !,
    subs(X/T, F, G).

%Usamos el operador (=..) para separar el nombre del predicado (p/f...) de sus argumentos(x, x v y...).
subs(X/T, F, G) :-
    F =.. [Pred|Argum], %Separamos el nombre del predicado
    recorrer_subs(X/T,Argum, Argum2), %Recorremos la lista de argumentos
    G =.. [Pred|Argum2]. %Devolvemos el nombre del predicado + los nuevos argumentos
    
%Lista de argumentos
%Caso base: la lista vacía se queda vacía.
recorrer_subs(_, [], []).

%Caso recursivo: procesamos la cabeza (H) y seguimos con el resto (Tail).
recorrer_subs(X/T, [H|Tail], [H1|T1]) :-
    subs(X/T, H, H1), 
    recorrer_subs(X/T, Tail, T1).
    

%Caso base: si no hay más sustituciones, la fórmula no cambia.
subs_list([], F , F).

%Caso recursivo: aplicamos la primera sustitución (H) a F obteniendo G,
%y usamos ese G como entrada para el resto de la lista (T).
subs_list([H|T], F, G1) :-
    subs(H, F, G),
    !,
    subs_list(T, G, G1).

