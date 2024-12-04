EMPTY = 'ε'

PARSING_TABLE = {
    ('S', 'a'): ['a', 'S', 'b'],
    ('S', 'b'): [],
    ('S', '$'): []
}

TERMINALS = {'a', 'b', '$'}

w = "aabb"

def parser(w, parsingTable):

  # variável para guardar os elementos em que ocorreu match
  #matchList = list()

  # Prepara buffer com string de texto + $ ao final
  buffer = list(w)
  buffer.append("$")
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

      
      #matchList.append(a)

      #remove X da pilha
      stack.pop() 

      # a = próximo símbolo de W
      currentSymbolIndex += 1
      a = buffer[currentSymbolIndex]

      

    # Se X é um terminal
    elif X in TERMINALS:
      
      # É terminal, mas não corresponde ao input
      return "Erro"
  
    # M[X, a] é uma entrada de erro
    elif (X, a) not in parsingTable:
      return "Erro"

    # X não é terminal, aciona a produção em M
    elif ((X, a) in parsingTable):
      production = parsingTable[(X, a)]

      # Imprime a produção
      print(f"Produção: {X} → {''.join(production)}")
      
      #remove X da pilha
      stack.pop()

      # Empilha a produção
      stack.extend(reversed(production))
    
    X = stack[-1]
    print(f"Pilha: {stack}")
    #print(f"Match: {matchList}" )
  

  
parser(w, PARSING_TABLE)

