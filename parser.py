PARSING_TABLE = {
    ('S', 'a'): ['a', 'S', 'b'],
    ('S', 'b'): [],
    ('S', '$'): []
}

w = "aabb"

def parser(w, parsingTable):

  # Prepara buffer com string de texto + $ ao final
  buffer = list(w)
  buffer.append("$")

  #prepara a pilha com S$
  stack = ['$'] + ["S"]

  print(buffer)

parser(w, PARSING_TABLE)