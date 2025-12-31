let my_example =
  
  EAdd (EMul (EInt 2, EInt 2), EMul(EInt 3, EInt 3))
  
let rec eval e =
  match e with
  | EInt x -> x 
  | EAdd (l, r) -> eval (l) + eval (r)
  | EMul(l,r) -> eval (l) * eval(r) 
                     
let factorize (e:exp) : exp =
  match e with
  | EInt p -> EInt p
                
                
    
  | EMul(x,y) -> EMul(x,y)
          

let expand e =
  "Replace this string with your implementation." ;;

let simplify e =
  "Replace this string with your implementation." ;;
