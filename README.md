  <h1>Calculo Numerico</h1>

1. Considere um sistema linear AX = B de n equações e n variáveis. A matriz A = (aij )n×n pode ser escrita como uma lista 
                        A = [[a11, a12, ..., a1n], [a21, a22, ..., a2n], ..., [an1, an2, ..., ann]], 
onde cada elemento da lista é uma lista dos elementos de uma linha de A. A matriz B = (bi)n×1 pode ser vista como uma lista B = [b1, b2, ..., bn]. Já a matriz aumentada do sistema é uma matriz M de tamanho n × (n + 1) que também pode ser vista como uma lista 
                        M = [[a11, ..., a1n, b1], [a21, ..., a2n, b2], ..., [an1, ..., ann, bn]] 
. 
(a) Implemente uma função em python, de nida como Gauss(M), que recebe uma matriz M de tamanho n×(n+ 1) e retorna uma matriz M˜ de um sistema triangular, obtida pelo processo de eliminação de Gauss com pivoteamento parcial. 
(b) Dado um sistema AX = B, n×n, implemente uma função em python, de nida como sol(A, B), que recebe como parâmetros uma matriz A, n × n, e uma matriz B, n × 1, e que retorna a solução do sitema linear X = [x1, x2, ..., xn]. Para tanto, você deve obter a matriz aumentada M, usar o item anterior para obter a forma triângular do sistema e, então, usar o método de substituição retroativa. Caso o sistema não apresente solução única, o retorno da função deve ser a mensagem "sistema sem solução determinada". 
