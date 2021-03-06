  <h1>Calculo Numerico</h1>

<h3>1. Considere um sistema linear AX = B de n equações e n variáveis. A matriz A = (aij )n×n pode ser escrita como uma lista</h3><br /><br/>
                        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; A = [[a11, a12, ..., a1n], [a21, a22, ..., a2n], ..., [an1, an2, ..., ann]],<br /> <br />
onde cada elemento da lista é uma lista dos elementos de uma linha de A.<br/> A matriz B = (bi)n×1 pode ser vista como uma lista B = [b1, b2, ..., bn]. Já a matriz aumentada do sistema é uma matriz M de tamanho n × (n + 1) que também pode ser vista como uma lista<br /> <br />
                        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; M = [[a11, ..., a1n, b1], [a21, ..., a2n, b2], ..., [an1, ..., ann, bn]]<br /><br /> 

(a) Implemente uma função em python, definida como Gauss(M), que recebe uma matriz M de tamanho n×(n+ 1) e retorna uma matriz M˜ de um sistema triangular, obtida pelo processo de eliminação de Gauss com pivoteamento parcial.<br /> <br />
(b) Dado um sistema AX = B, n×n, implemente uma função em python, definida como sol(A, B), que recebe como parâmetros uma matriz A, n × n, e uma matriz B, n × 1, e que retorna a solução do sitema linear X = [x1, x2, ..., xn]. Para tanto, você deve obter a matriz aumentada M, usar o item anterior para obter a forma triângular do sistema e, então, usar o método de substituição retroativa. Caso o sistema não apresente solução única, o retorno da função deve ser a mensagem "sistema sem solução determinada". 

<h3>2. Considere o sistema linear</h3>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;9x1 − 2x2 + x3 + 3x4 + x5 = 0<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x1 − 1x2 + 2x3 + 6x4 + x5 = 2<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2x1 − 3x2 + 7x3 + x4 = 1<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x1 + 6x2 − x3 + 4x4 + 2x5 = 1<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x1 − 2x2 + 2x3 + x4 + 8x5 = 2<br />

Encontre uma solução aproximada do sistema pelo método de Gauss-Seidel até obter a distância relativa das
soluções dr(k) < 10−4.<br />

<h3>3. Considere o sistema</h3><br />

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x² + xy + z² − 12 = 0<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x − yz − 10 = 0<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2x² − y² + z² + 5 = 0<br />

Encontre uma solução aproximada X(k) do sistema pelo método de Newton até obter ||F(X(k))||∞ < 10−4
