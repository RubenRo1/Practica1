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

%Remplazo sobre las apariciones libres solo
%subs(y/f(a), forall x :: p(x,y), G).
% G = forall x :: p(x, f(a))
% subs(X/T, A & B, A1 & B1) :- subs(X/T, A, A1), subs(X/T,B,B1).

%Caso F es un atomo
% subs(_/_, F, T) :- 
%     F =..[_|T].

% %Variable
subs(X/T, X, T) :- !.


%Caso F es un and y or
subs(X/T, A & B, A1 & B1) :- 
    !,
    subs(X/T, A, A1), 
    subs(X/T,B,B1).

subs(X/T, A v B, A1 v B1) :- 
    !,
    subs(X/T, A, A1), 
    subs(X/T, B, B1).

subs(X/T, F, G) :-
    X == F, !,
    G = T.

subs(_/_, F, F).






% subs(X/T, A v B, A) :- !.
    % subs(X/T, A, A1), 
    % subs(X/T, B, B1).


% subs_arg(_,[],[]).
% subs_arg(X/T,[Head|Tail],[Head1|Tail1]) :-
%     subs(X/T, Head, Head1),
%     subs_arg(X/T, Tail, Tail1).

% subs(X/T, A & B, T) :-
% F =..[A|T1],
% A == X,!.




