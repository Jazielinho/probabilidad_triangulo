
romper_palillo = function(longitud){
  # Divide un palillo en 3 partes
  x = runif(n = 1, min = 0, max = longitud)
  y = runif(n = 1, min = 0, max = longitud)

  a = min(x, y)
  b = abs(x - y)
  c = longitud - (a + b)

  return(list(a = a, b = b, c = c))
}


es_triangulo = function(a, b, c){
  # Determina si los lados de un triángulo son válidos.
  return(a + b > c & a + c > b & b + c > a)
}


simula_probabilidad = function(longitud = 1.0, num_iter = 1000){
  # Simula la probabilidad de que un palillo se rompa en 3 partes
  num_triangulos_formados = 0
  for (i in seq(1, num_iter)){
    lados = romper_palillo(longitud)
    a = lados$a
    b = lados$b
    c = lados$c

    if (es_triangulo(a, b, c)){
      num_triangulos_formados = num_triangulos_formados + 1
    }
  }
  return(num_triangulos_formados / num_iter)
}


iteraciones = c()
probabilidades = c()

for(i in seq(10000)){
  prob = simula_probabilidad(num_iter = i)
  iteraciones = c(iteraciones, i)
  probabilidades = c(probabilidades, prob)
}


plot(iteraciones, probabilidades, type = 'l')
abline(h = 0.25, col = 'red')
