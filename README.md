<h1>Explicação do código:</h1>
<br>
<h2>Este é um pequeno projeto feito em Python, para realizar algumas análises básicas em uma lista de números:</h2>
<ol>
    <li>
        <b>Arquivo main.py</b>
        <ol>
            <li>
                É criada uma função "analisar_lista", que tem como parâmetro a variável <code>lista</code>, de tipo <code>list</code> (ou seja, literalmente do tipo de uma lista).
            </li>
            <br>
            <li>
                A função realiza várias operações de análise nos dados dessa lista:
                <ol>
                    <li>
                        Calcula a média dos números da lista.
                    </li>
                    <li>
                        Encontra o maior número da lista.
                    </li>
                    <li>
                        Encontra o menor número da lista.
                    </li>
                    <li>
                        Conta a quantidade de números pares presentes na lista.
                    </li>
                </ol>
            </li>
        </ol>
    </li>
    <br>
    <li>
        A função "analisar_lista" recebe uma lista de números como parâmetro.
    </li>
    <br>
    <li>
        A primeira operação dentro da função é calcular a média dos números da lista:
        <pre>
            media = sum(lista.copy()) / (len(lista.copy()))
            print(f"Média: {media:.2f}")
        </pre>
        O método <code>sum()</code> calcula a soma dos elementos da lista, e o <code>len()</code> retorna a quantidade de elementos. A média é então calculada dividindo a soma pelo número de elementos. O valor da média é impresso com duas casas decimais.
    </li>
    <br>
    <li>
        Após isso, o código encontra o maior número da lista usando a função <code>max()</code>:
        <pre>
            maior_n = max(lista.copy())
            print("Maior número: ", maior_n)
        </pre>
        A função <code>max()</code> retorna o maior valor presente na lista.
    </li>
    <br>
    <li>
        O mesmo processo ocorre para o menor número da lista, mas utilizando a função <code>min()</code>:
        <pre>
            menor_n = min(lista.copy())
            print("Menor número: ", menor_n)
        </pre>
        Aqui, <code>min()</code> retorna o menor número presente na lista.
    </li>
    <br>
    <li>
        Para contar a quantidade de números pares na lista, foi utilizado um loop <code>for</code> que itera sobre cada elemento da lista. Dentro do loop, é feita a verificação de paridade utilizando o operador <code>%</code> (resto da divisão):
        <pre>
            qtd_n_pares = 0
            for i in lista:
                if i % 2 == 0:
                    qtd_n_pares += 1
        </pre>
        Caso o número seja par, ou seja, o resto da divisão por 2 seja zero, a variável <code>qtd_n_pares</code> é incrementada. Ao fim do loop, o número total de números pares é "printado" (impresso).
    </li>
    <li>
        Por fim, a função retorna uma string vazia (<code>return ""</code>), mas como não é usada no código, ela não impacta a execução do programa.
    </li>
</ol>

<h2>Arquivo teste.py</h2>
<ol>
    <li>
        O arquivo <code>teste.py</code> serve para testar a função "analisar_lista". Nesse arquivo, uma lista de números chamada <code>numeros</code> é criada:
        <pre>
            numeros = [10, 23, 5, 8, 12, 33, 42, 7, 19, 28, 3, 16, 9, 50, 21]
        </pre>
    </li>
    <li>
        Em seguida, a função "analisar_lista" é importada do arquivo <code>main.py</code> em:
        <pre>
            from main import analisar_lista as al
        </pre>
    </li>
    <li>
        Finalmente, a função é chamada com a lista <code>numeros</code> como argumento e o resultado é impresso:
        <pre>
            print(al(numeros))
        </pre>
        O código executa todas as operações de análise e exibe as informações solicitadas sobre a lista de números.
    </li>
</ol>
