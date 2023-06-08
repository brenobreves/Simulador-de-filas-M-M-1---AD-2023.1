import random
import numpy as np
import math
import matplotlib.pyplot as plt

def simulador2zerando(clientes_inicio, lamb, mi):
    #Quantidade de clientes na fila
    clientes_na_fila = clientes_inicio
    #tempo de simulaçao mantido a cada iteração
    tempo_de_simulacao = 0
    #lista de eventos, iniciada com uma chegada.
    lista_de_eventos = [[random.expovariate(lamb),"Chegada"]]
    #lista de tempos para calculo do tempo medio
    lista_tempos = []
    if clientes_inicio > 0:
        prox_saida = random.expovariate(mi) + tempo_de_simulacao
        lista_de_eventos.append([prox_saida,"Saida"])
        lista_de_eventos.sort()
        for i in range(clientes_inicio):
            lista_tempos.append(tempo_de_simulacao)
    #quantidade media de pessoas na fila
    media_clientes_na_fila = 0
    #tempo medio que um cliente leva para ser atendido
    tempo_medio_espera = 0
    #clientes atendidos, para uso no calculo do tempo medio
    clientes_atendidos = 0
    #lista com todos os valores da fila
    lista_clientes_na_fila = []
    lista_clientes_na_fila.append(clientes_na_fila)
    #lista de tempos de espera
    lista_tempos_de_espera = []
    while clientes_na_fila > 0:
        #atualizando o tempo de simulação e calculando o tempo até a proxima chegada e/ou saida. Na maioria das vezes um desses será descartado.
        media_clientes_na_fila += clientes_na_fila*(lista_de_eventos[0][0] - tempo_de_simulacao)
        tempo_de_simulacao = lista_de_eventos[0][0]
        prox_chegada = random.expovariate(lamb) + tempo_de_simulacao
        prox_saida = random.expovariate(mi) + tempo_de_simulacao
        #Se o evento atual é uma chegada, trata o evento e adiciona o próximo evento de chegada na lista de eventos. Se o evento leva de 0 -> 1 cliente na fila, também adiciona o evento de saida para esse cliente.
        if lista_de_eventos[0][1] == "Chegada":
            clientes_na_fila += 1
            lista_clientes_na_fila.append(clientes_na_fila)
            lista_tempos.append(tempo_de_simulacao)
            print(str(tempo_de_simulacao) + ": chegada de cliente, total de clientes na fila é " + str(clientes_na_fila))
            if clientes_na_fila == 1:
                lista_de_eventos.append([prox_chegada,"Chegada"])
                lista_de_eventos.append([prox_saida,"Saida"])
            else:
                lista_de_eventos.append([prox_chegada,"Chegada"])
        #Se o evento atual é uma saida, trata o evento e adiciona o próximo evento de saída, exceto se não há nenhum cliente na fila após a saida.
        elif lista_de_eventos[0][1] == "Saida":
            clientes_na_fila -= 1
            lista_clientes_na_fila.append(clientes_na_fila)
            lista_tempos_de_espera.append(tempo_de_simulacao - lista_tempos[0])
            tempo_medio_espera += tempo_de_simulacao - lista_tempos.pop(0)
            clientes_atendidos += 1
            print(str(tempo_de_simulacao) + ": saida de cliente, total de clientes na fila é " + str(clientes_na_fila))
            if clientes_na_fila != 0:
                lista_de_eventos.append([prox_saida,"Saida"])
        #Remove o evento tratado da lista de eventos e organiza ela em termos de tempo.
        lista_de_eventos.pop(0)
        lista_de_eventos.sort()
    print("\n")
    return tempo_de_simulacao
    
def simulador2ate1(clientes_inicio, lamb, mi):
    #Quantidade de clientes na fila
    clientes_na_fila = clientes_inicio
    #tempo de simulaçao mantido a cada iteração
    tempo_de_simulacao = 0
    #lista de eventos, iniciada com uma chegada.
    lista_de_eventos = [[random.expovariate(lamb),"Chegada"]]
    #lista de tempos para calculo do tempo medio
    lista_tempos = []
    if clientes_inicio > 0:
        prox_saida = random.expovariate(mi) + tempo_de_simulacao
        lista_de_eventos.append([prox_saida,"Saida"])
        lista_de_eventos.sort()
        for i in range(clientes_inicio):
            lista_tempos.append(tempo_de_simulacao)
    #quantidade media de pessoas na fila
    media_clientes_na_fila = 0
    #tempo medio que um cliente leva para ser atendido
    tempo_medio_espera = 0
    #clientes atendidos, para uso no calculo do tempo medio
    clientes_atendidos = 0
    #lista com todos os valores da fila
    lista_clientes_na_fila = []
    lista_clientes_na_fila.append(clientes_na_fila)
    #lista de tempos de espera
    lista_tempos_de_espera = []
    while clientes_na_fila > 1:
        #atualizando o tempo de simulação e calculando o tempo até a proxima chegada e/ou saida. Na maioria das vezes um desses será descartado.
        media_clientes_na_fila += clientes_na_fila*(lista_de_eventos[0][0] - tempo_de_simulacao)
        tempo_de_simulacao = lista_de_eventos[0][0]
        prox_chegada = random.expovariate(lamb) + tempo_de_simulacao
        prox_saida = random.expovariate(mi) + tempo_de_simulacao
        #Se o evento atual é uma chegada, trata o evento e adiciona o próximo evento de chegada na lista de eventos. Se o evento leva de 0 -> 1 cliente na fila, também adiciona o evento de saida para esse cliente.
        if lista_de_eventos[0][1] == "Chegada":
            clientes_na_fila += 1
            lista_clientes_na_fila.append(clientes_na_fila)
            lista_tempos.append(tempo_de_simulacao)
            print(str(tempo_de_simulacao) + ": chegada de cliente, total de clientes na fila é " + str(clientes_na_fila))
            if clientes_na_fila == 1:
                lista_de_eventos.append([prox_chegada,"Chegada"])
                lista_de_eventos.append([prox_saida,"Saida"])
            else:
                lista_de_eventos.append([prox_chegada,"Chegada"])
        #Se o evento atual é uma saida, trata o evento e adiciona o próximo evento de saída, exceto se não há nenhum cliente na fila após a saida.
        elif lista_de_eventos[0][1] == "Saida":
            clientes_na_fila -= 1
            lista_clientes_na_fila.append(clientes_na_fila)
            lista_tempos_de_espera.append(tempo_de_simulacao - lista_tempos[0])
            tempo_medio_espera += tempo_de_simulacao - lista_tempos.pop(0)
            clientes_atendidos += 1
            print(str(tempo_de_simulacao) + ": saida de cliente, total de clientes na fila é " + str(clientes_na_fila))
            if clientes_na_fila != 0:
                lista_de_eventos.append([prox_saida,"Saida"])
        #Remove o evento tratado da lista de eventos e organiza ela em termos de tempo.
        lista_de_eventos.pop(0)
        lista_de_eventos.sort()
    print("\n")
    return tempo_de_simulacao
    
temposzerando = []
temposate1 = []
media_tempos_zerando = []
media_tempos_ate1 = []
ICtemposzerando = []
ICtemposate1 = []
repeticoes = 10000
for i in range(10):
    for j in range(repeticoes):
        temposzerando.append(simulador2zerando(i+1, 1, 2))
        temposate1.append(simulador2ate1(i+1,1,2))
    media_tempos_zerando.append(sum(temposzerando)/len(temposzerando))
    media_tempos_ate1.append(sum(temposate1)/len(temposate1))
    ICtemposzerando.append([media_tempos_zerando[i] - 1.96*np.std(temposzerando)/math.sqrt(repeticoes), media_tempos_zerando[i] + 1.96*np.std(temposzerando)/math.sqrt(repeticoes)])
    ICtemposate1.append([media_tempos_ate1[i] - 1.96*np.std(temposate1)/math.sqrt(repeticoes), media_tempos_ate1[i] + 1.96*np.std(temposate1)/math.sqrt(repeticoes)])
    temposzerando = []
    temposate1 = []
for i in range(10):
    print("Tempo médio até chegar a zero clientes começando com " + str(i+1) + ": " + str(media_tempos_zerando[i]))
    print("Intervalo de confiança IC95: " + str(ICtemposzerando[i][0]) + " - " + str(ICtemposzerando[i][1]))
    print("Tempo médio até chegar a um clientecomeçando com " + str(i+1) + ": " + str(media_tempos_ate1[i]))
    print("Intervalo de confiança IC95: " + str(ICtemposate1[i][0]) + " - " + str(ICtemposate1[i][1]))

label_intervalos = ["C=1","C=2","C=3","C=4","C=5","C=6","C=7","C=8","C=9","C=10"]
plt.bar(label_intervalos, media_tempos_zerando)
plt.xlabel('Clientes iniciais')
plt.ylabel('Tempo medio até a fila ficar vazia')
plt.title('Tempo medio ocupado começando com C clientes')
plt.show()

plt.bar(label_intervalos, media_tempos_ate1)
plt.xlabel('Clientes iniciais')
plt.ylabel('Tempo medio até a fila chegar a 1 cliente')
plt.title('Tempo medio até chegar a 1 cliente começando com C clientes')
plt.show()

