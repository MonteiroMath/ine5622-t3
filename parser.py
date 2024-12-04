PARSING_TABLE = {('S', '$'): ['MAIN'],
 ('S', 'def'): ['MAIN'],
 ('S', '{'): ['MAIN'],
 ('S', 'int'): ['MAIN'],
 ('S', 'id'): ['MAIN'],
 ('S', ';'): ['MAIN'],
 ('S', 'print'): ['MAIN'],
 ('S', 'return'): ['MAIN'],
 ('S', 'if'): ['MAIN'],
 ('MAIN', '$'): [],
 ('MAIN', 'def'): ['FLIST'],
 ('MAIN', '{'): ['STMT'],
 ('MAIN', 'int'): ['STMT'],
 ('MAIN', 'id'): ['STMT'],
 ('MAIN', ';'): ['STMT'],
 ('MAIN', 'print'): ['STMT'],
 ('MAIN', 'return'): ['STMT'],
 ('MAIN', 'if'): ['STMT'],
 ('FLIST', 'def'): ['FDEF', 'FLIST’'],
 ('FLIST’', '$'): [],
 ('FLIST’', 'def'): ['FLIST'],
 ('FDEF', 'def'): ['def', 'id(', 'PARLIST', ')', '{', 'STMTLIST', '}'],
 ('PARLIST', ')'): [],
 ('PARLIST', 'int'): ['int', 'id', 'PARLIST’'],
 ('PARLIST’', ')'): [],
 ('PARLIST’', ','): [',', 'PARLIST'],
 ('VARLIST', 'id'): ['id', 'VARLIST’'],
 ('VARLIST’', ','): [',', 'VARLIST'],
 ('VARLIST’', ';'): [],
 ('STMT', '{'): ['{', 'STMTLIST', '}'],
 ('STMT', 'int'): ['int', 'VARLIST', ';'],
 ('STMT', 'id'): ['ATRIBST', ';'],
 ('STMT', ';'): [';'],
 ('STMT', 'print'): ['PRINTST', ';'],
 ('STMT', 'return'): ['RETURNST', ';'],
 ('STMT', 'if'): ['IFSTMT'],
 ('ATRIBST', 'id'): ['id', ':=', 'ATRIBST’'],
 ('ATRIBST’', 'id('): ['FCALL'],
 ('ATRIBST’', 'id'): ['EXPR'],
 ('ATRIBST’', '('): ['EXPR'],
 ('ATRIBST’', 'num'): ['EXPR'],
 ('FCALL', 'id('): ['id(', 'PARLISTCALL', ')'],
 ('PARLISTCALL', ')'): [],
 ('PARLISTCALL', 'id'): ['id', 'PARLISTCALL’'],
 ('PARLISTCALL’', ')'): [],
 ('PARLISTCALL’', ','): [',', 'PARLISTCALL'],
 ('PRINTST', 'print'): ['print', 'EXPR'],
 ('RETURNST', 'return'): ['return', 'RETURNST’'],
 ('RETURNST’', 'id'): ['id'],
 ('RETURNST’', ';'): [],
 ('IFSTMT', 'if'): ['if', '(', 'EXPR', ')', 'STMT', 'IFSTMT’'],
 ('IFSTMT’', '$'): [],
 ('IFSTMT’', '{'): [],
 ('IFSTMT’', '}'): [],
 ('IFSTMT’', 'int'): [],
 ('IFSTMT’', 'id'): [],
 ('IFSTMT’', ';'): [],
 ('IFSTMT’', 'print'): [],
 ('IFSTMT’', 'return'): [],
 ('IFSTMT’', 'if'): [],
 ('IFSTMT’', 'else'): ['else', 'STMT', 'IFSTMT’', 'ε'],
 ('STMTLIST', '{'): ['STMT', 'STMTLIST’'],
 ('STMTLIST', 'int'): ['STMT', 'STMTLIST’'],
 ('STMTLIST', 'id'): ['STMT', 'STMTLIST’'],
 ('STMTLIST', ';'): ['STMT', 'STMTLIST’'],
 ('STMTLIST', 'print'): ['STMT', 'STMTLIST’'],
 ('STMTLIST', 'return'): ['STMT', 'STMTLIST’'],
 ('STMTLIST', 'if'): ['STMT', 'STMTLIST’'],
 ('STMTLIST’', '{'): ['STMTLIST'],
 ('STMTLIST’', '}'): [],
 ('STMTLIST’', 'int'): ['STMTLIST'],
 ('STMTLIST’', 'id'): ['STMTLIST'],
 ('STMTLIST’', ';'): ['STMTLIST'],
 ('STMTLIST’', 'print'): ['STMTLIST'],
 ('STMTLIST’', 'return'): ['STMTLIST'],
 ('STMTLIST’', 'if'): ['STMTLIST'],
 ('EXPR', 'id'): ['NUMEXPR', 'EXPR’'],
 ('EXPR', '('): ['NUMEXPR', 'EXPR’'],
 ('EXPR', 'num'): ['NUMEXPR', 'EXPR’'],
 ('EXPR’', ')'): [],
 ('EXPR’', ';'): [],
 ('EXPR’', '<'): ['<', 'NUMEXPR'],
 ('EXPR’', '<='): ['<=', 'NUMEXPR'],
 ('EXPR’', '>'): ['>', 'NUMEXPR'],
 ('EXPR’', '>='): ['>=', 'NUMEXPR'],
 ('EXPR’', '=='): ['==', 'NUMEXPR'],
 ('EXPR’', '<>'): ['<>', 'NUMEXPR'],
 ('NUMEXPR', 'id'): ['TERM', 'NUMEXPR′'],
 ('NUMEXPR', '('): ['TERM', 'NUMEXPR′'],
 ('NUMEXPR', 'num'): ['TERM', 'NUMEXPR′'],
 ('NUMEXPR′', ')'): [],
 ('NUMEXPR′', ';'): [],
 ('NUMEXPR′', '<'): [],
 ('NUMEXPR′', '<='): [],
 ('NUMEXPR′', '>'): [],
 ('NUMEXPR′', '>='): [],
 ('NUMEXPR′', '=='): [],
 ('NUMEXPR′', '<>'): [],
 ('NUMEXPR′', '+'): ['+', 'TERM', 'NUMEXPR′'],
 ('NUMEXPR′', '-'): ['-', 'TERM', 'NUMEXPR′'],
 ('TERM', 'id'): ['FACTOR', 'TERM′'],
 ('TERM', '('): ['FACTOR', 'TERM′'],
 ('TERM', 'num'): ['FACTOR', 'TERM′'],
 ('TERM′', ')'): [],
 ('TERM′', ';'): [],
 ('TERM′', '<'): [],
 ('TERM′', '<='): [],
 ('TERM′', '>'): [],
 ('TERM′', '>='): [],
 ('TERM′', '=='): [],
 ('TERM′', '<>'): [],
 ('TERM′', '+'): [],
 ('TERM′', '-'): [],
 ('TERM′', '*'): ['*', 'FACTOR', 'TERM′'],
 ('TERM′', '/'): ['/', 'FACTOR', 'TERM′'],
 ('FACTOR', 'id'): ['id'],
 ('FACTOR', '('): ['(', 'NUMEXPR', ')'],
 ('FACTOR', 'num'): ['num']}

TERMINALS = [
    "id", "num",
    "<", ">", "<=", ">=", "<>", "=",
    "int", "if", "else", "def", "print", "return",
    "+", "-", "*", "/", ":=", "(", ")", "{", "}", ",", ";",
    "id("
]

w = '''def id( int id , int id ) {
    int id , id , id ;
    id := id + id ;
    id := id + id * id ;
    id := id - id ;
    return id ;
 }
'''

def parser(w, parsingTable):

  
  # variável para guardar os elementos em que ocorreu match
  matchList = list()

  # Prepara buffer com string de texto + $ ao final
  w = w.replace("\n", "") # substitui caracteres de linha nova por vazios
  buffer = w.split(" ")
  buffer.append("$")
  buffer = [el for el in buffer if el != ""] #remove elementos vazios
  print(buffer)

  currentSymbolIndex = 0

  #prepara a pilha com S$
  stack = ['$'] + ["S"]

  # a = primeiro símbolo de W
  a = buffer[currentSymbolIndex]
  # X = símbolo do topo da pilha
  X = stack[-1]

  # Enquanto a pilha não estiver fazia
  
  while X != "$":
    
    # Se X == a, realiza o match
    if X == a:

      
      matchList.append(a)

      #remove X da pilha
      stack.pop() 

      # a = próximo símbolo de W
      currentSymbolIndex += 1
      a = buffer[currentSymbolIndex]

      

    # Se X é um terminal
    elif X in TERMINALS:
      
      # É terminal, mas não corresponde ao input
      print("Terminal incorreto")
      print(len(X))
      print(len(a))
      print(X == a)
      return "Erro"
  
    # M[X, a] é uma entrada de erro
    elif (X, a) not in parsingTable:
      
      print("Produção não encontrada")
      print(X)
      print(a)
      return "Erro"

    # X não é terminal, aciona a produção em M
    elif ((X, a) in parsingTable):
      production = parsingTable[(X, a)]

      # Imprime a produção
      print(f"Produção: {X} → {''.join(production) if production else 'ε'}")
      
      #remove X da pilha
      stack.pop()

      # Empilha a produção
      stack.extend(reversed(production))
    
    X = stack[-1]
    print("Sucesso")
    print(f"Pilha: {stack}")
    print(f"Match: {matchList}" )
  

  
parser(w, PARSING_TABLE)

