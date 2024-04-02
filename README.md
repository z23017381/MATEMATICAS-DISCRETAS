Teoria de Conjuntos con Python
La teoria de conjuntos es un área fundamental de las matemáticas que trata sobre las propiedades y relaciones entre conjunto, que son colecciones bien detalladas de objetos. Python, como un lenguaje de programación versatíl, ofrece varias formas de trabajar con conjuntos y aplicarconceptos de teoria de conjuntos.

Creacion de conjuntos
En python, puedes crear un conjunto utilizando llaves {} o la función set()

A = {1, 2, 3, 4, 5}
B = {3, 4, 5, 6, 7}
C = set([3, 6, 9, 12, 15])
TABLA

lista = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5}

lista
{1, 2, 3, 4, 5}

conjunto = set(lista)
conjunto
{1, 2, 3, 4, 5}

Operaciones
Python proporciona operaciones y métodos para realizar operaciones básicas de conjuntos como unión, intersección, diferencia y diferencia simétrica.

Unión
Cuando tomamos la unión de dos conjuntos (representada por A ∪ B), los combinamos en un conjunto nuevo que incluye todos los elementos que pertenecen al conjunto A, al conjunto B o a ambos. Imagina que tienes dos conjuntos: Conjunto A = {1, 2, 3} (contiene los números 1, 2 y 3) Conjunto B = {2, 4, 5} (contiene los números 2, 4 y 5) La unión de estos conjuntos (A ∪ B) sería: {1, 2, 3, 4, 5}

El operador | se utiliza para unir dos conjuntos. El resultado de la operación será un nuevo conjunto que contiene todos los elementos que están en uno o en ambos conjuntos originales.

Usando el método union():
El método union() se utiliza para unir dos conjuntos. El resultado de la operación será un nuevo conjunto que contiene todos los elementos que están en uno o en ambos conjuntos originales.

La fórmula LaTex es:
𝐶=𝐴∪𝐵=(𝑥:𝑥∈𝐴𝑜 𝑞𝑢𝑎𝑑𝑥∈𝐵)

A | B
{1, 2, 3, 4, 5, 6, 7}

A.union(B)
{1, 2, 3, 4, 5, 6, 7}

Intersección
la intersección de dos o más conjuntos es una operación que da como resultado un nuevo conjunto que contiene únicamente los elementos que son comunes a todos los conjuntos originales. La intersección de dos conjuntos A y B se denota por A ∩ B.

Ejemplo:

A = {1, 2, 3, 4} B = {2, 3, 5, 6} A ∩ B = {2, 3}

La intersección de conjuntos en Python se puede realizar de dos maneras:

Usando el operador &:
El operador & se utiliza para encontrar la intersección de dos conjuntos. El resultado de la operación será un nuevo conjunto que contiene solo los elementos que están en ambos conjuntos originales.

Usando el método intersection():
El método intersection() se utiliza para encontrar la intersección de dos conjuntos. El resultado de la operación será un nuevo conjunto que contiene solo los elementos que están en ambos conjuntos originales.

La fórmula LaTex es:
𝐶=𝐴∩𝐵={𝑥∈𝐴∧𝑥∈𝐵}

A & B
{3, 4, 5}

A.intersection(B)
{3, 4, 5}

B & A
{3, 4, 5}

B.intersection(A)
{3, 4, 5}

Diferencia
En teoría de conjuntos, la diferencia de dos conjuntos es una operación que da como resultado un nuevo conjunto que contiene todos los elementos del primer conjunto que no están en el segundo conjunto. La diferencia de dos conjuntos A y B se denota por A - B.

Ejemplo:

A = {1, 2, 3, 4} B = {2, 3, 5, 6} A - B = {1, 4}

La diferencia de conjuntos en Python se puede realizar de dos maneras:

Usando el operador -:
El operador - se utiliza para encontrar la diferencia de dos conjuntos. El resultado de la operación será un nuevo conjunto que contiene solo los elementos que están en el primer conjunto pero no en el segundo.

Usando el método difference():
El método difference() se utiliza para encontrar la diferencia de dos conjuntos. El resultado de la operación será un nuevo conjunto que contiene solo los elementos que están en el primer conjunto pero no en el segundo.

Ambas formas de realizar la diferencia de conjuntos son válidas y producen el mismo resultado. La elección de una u otra dependerá de las preferencias del programador o del contexto en el que se esté trabajando.

La fórmula LaTex es:
𝐶=𝐴−𝐵={𝑥∈𝐴∧𝑥∉𝐵}

A - B
{1, 2}

A.difference(B)
{1, 2}

B - A
{6, 7}

B.difference(A)
{6, 7}

Diferencia simétrica
La diferencia simétrica de dos conjuntos es una operación que da como resultado un nuevo conjunto que contiene todos los elementos que pertenecen a uno de los dos conjuntos originales, pero no a ambos a la vez.

Notación: La diferencia simétrica de dos conjuntos A y B se denota por A △ B.

Ejemplo:

A = {1, 2, 3, 4} B = {2, 3, 5, 6} A △ B = {1, 4, 5, 6}

La diferencia simétrica de conjuntos en Python se puede realizar de dos maneras:

1. Usando el operador ^:
El operador ^ se utiliza para encontrar la diferencia simétrica de dos conjuntos. El resultado de la operación será un nuevo conjunto que contiene solo los elementos que están en uno de los dos conjuntos pero no en ambos.

2. Usando el método symmetric_difference():
El método symmetric_difference() se utiliza para encontrar la diferencia simétrica de dos conjuntos. El resultado de la operación será un nuevo conjunto que contiene solo los elementos que están en uno de los dos conjuntos pero no en ambos.

La fórmula LaTex es:

𝐶=𝐴△𝐵={𝑥∈(𝐴∪𝐵)∧𝑥∉(𝐴∩𝐵)}

A ^ B
{1, 2, 6, 7}

A.symmetric_difference(B)
{1, 2, 6, 7}

B ^ A
{1, 2, 6, 7}

B.symmetric_difference(A)
{1, 2, 6, 7}
