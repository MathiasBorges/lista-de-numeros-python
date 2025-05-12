def analisar_lista(lista:list):
 
    media=sum(lista.copy())/(len(lista.copy()))
    print(f"Média: {media:.2f}")
    
    maior_n=max(lista.copy())
    print("Maior número: ",maior_n)
    
    menor_n=min(lista.copy())
    print("Menor número: ",menor_n)
    
    qtd_n_pares=0
    
    for i in lista:
        if i%2==0:
            qtd_n_pares+=1
    
    print("Quantidade de números pares: ",qtd_n_pares)

    return ""
    
    