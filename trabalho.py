# Pergunta 1
def tira_quebra_de_linha(jogos: list[str]) -> list[str]:
    """
    Remove o último caractere (que é '\n') de cada string da lista.

    >>> tira_quebra_de_linha(["Flamengo 2 Vasco 1\\n", "Botafogo 3 Flamengo 2\\n"])
    ['Flamengo 2 Vasco 1', 'Botafogo 3 Flamengo 2']
    """
    nova_lista = []
    for i in range(len(jogos)):
        linha = jogos[i]
        linha_sem_quebra = linha[:-1]
        nova_lista.append(linha_sem_quebra)
    return nova_lista

from dataclasses import dataclass
@dataclass
class nome_dos_times:
    anfitriao: str
    visitante: str
def nome_das_equipes(jogo:str) -> nome_dos_times:
    """
    >>> nome_das_equipes("Fluminense 1 Cuiaba 0")
    nome_dos_times(anfitriao='Fluminense', visitante='Cuiaba')
    """
    espacos = []
    for i in range(len(jogo)):
        if jogo[i] == " ":
            espacos.append(i)
    # O nome do anfitrião vai do início até o espaço antes do placar do anfitrião
    anfitriao = jogo[:espacos[-3]]
    # O nome do visitante vai do espaço depois do placar do anfitrião até o espaço antes do placar do visitante
    visitante = jogo[espacos[-2] + 1:espacos[-1]]
    jogos = nome_dos_times(anfitriao, visitante)
    return jogos

@dataclass
class placar:
    gols_anfitriao: int
    gols_visitante: int
def placar_do_jogo(jogo: str) -> placar:
    """
    >>> placar_do_jogo("Fluminense 1 Cuiaba 0")
    placar(gols_anfitriao=1, gols_visitante=0)
    """
    espacos = []
    for i in range(len(jogo)):
        if jogo[i] == " ":
            espacos.append(i)
    # O placar do anfitrião está entre o penúltimo e o antepenúltimo espaço
    gols_anfitriao = int(jogo[espacos[-3] + 1:espacos[-2]])
    # O placar do visitante está após o último espaço
    gols_visitante = int(jogo[espacos[-1] + 1:])
    return placar(gols_anfitriao, gols_visitante)

def vitorias(placar: placar) -> int:
    """
    >>> vitorias(placar(gols_anfitriao=1, gols_visitante=0))
    1
    >>> vitorias(placar(gols_anfitriao=0, gols_visitante=0))
    0
    """
    vitorias = 0
    if placar.gols_anfitriao > placar.gols_visitante:
        vitorias += 1
    elif placar.gols_anfitriao < placar.gols_visitante:
        vitorias += 0
    else:
        vitorias += 0
    return vitorias

def saldo_de_gols(placar: placar) -> int:
    """
    >>> saldo_de_gols(placar(gols_anfitriao=1, gols_visitante=0))
    1
    >>> saldo_de_gols(placar(gols_anfitriao=0, gols_visitante=0))
    0
    """
    saldo = 0
    saldo = placar.gols_anfitriao - placar.gols_visitante
    return saldo
@dataclass
class Pontos:
    pontos: int
def ganho_pontos(placar: placar) -> Pontos:
    """
    >>> ganho_pontos(placar(gols_anfitriao=1, gols_visitante=0))
    Pontos(pontos=3)
    >>> ganho_pontos(placar(gols_anfitriao=0, gols_visitante=0))
    Pontos(pontos=1)
    >>> ganho_pontos(placar(gols_anfitriao=0, gols_visitante=1))
    Pontos(pontos=3)
    """
    pontos = 0
    if placar.gols_anfitriao > placar.gols_visitante:
        pontos += 3
    elif placar.gols_visitante > placar.gols_anfitriao:
        pontos += 3
    else:
        pontos += 1
    return Pontos(pontos)

@dataclass
class estatisticas:
    nome: str
    pontos: int
    vitorias: int
    saldo_de_gols: int

def verificar_elemento(lista, elemento_procurado) -> bool:
    """
    Verifica se um elemento está em uma lista
    """
    encontrado = False
    for elemento in lista:
        if elemento == elemento_procurado:
            encontrado = True
    return encontrado

def valor_letra(letra: str) -> int:
    '''
    Retorna o numero que indica a posição de uma letra no alfabeto
    '''
    x = 0
    minusculas = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
                  "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                  "u", "v", "w", "x", "y", "z"]
    maiusculas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
                  "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                  "U", "V", "W", "X", "Y", "Z"]
    for i in range(len(minusculas)):
        if letra == minusculas[i] or letra == maiusculas[i]:
            x = i
    return x
def ordena_times(estat: list[estatisticas]):
    for i in range(len(estat)):
        for j in range(i + 1, len(estat)):
            troca = False

            if estat[j].pontos > estat[i].pontos:
                troca = True
            elif estat[j].pontos == estat[i].pontos:
                if estat[j].vitorias > estat[i].vitorias:
                    troca = True
                elif estat[j].vitorias == estat[i].vitorias:
                    if estat[j].saldo_de_gols > estat[i].saldo_de_gols:
                        troca = True
                    elif estat[j].saldo_de_gols == estat[i].saldo_de_gols:
                        # Usando valor da primeira letra com sua função valor_letra
                        if valor_letra(estat[j].nome[0]) < valor_letra(estat[i].nome[0]):
                            troca = True
            if troca:
                estat[i], estat[j] = estat[j], estat[i]

def classifica_times(jogos: list[str]) -> list[estatisticas]:
    nomes: list[str]= []
    estat: list[estatisticas] = []

    for i in range(len(jogos)):
        nomes_do_jogo = nome_das_equipes(jogos[i])
        placar_do_jogo_atual = placar_do_jogo(jogos[i])

        # ----------- ANFITRIÃO -----------
        if not verificar_elemento(nomes, nomes_do_jogo.anfitriao):
            nomes.append(nomes_do_jogo.anfitriao)
            nova_estat = estatisticas(nomes_do_jogo.anfitriao, 0, 0, 0)
            estat.append(nova_estat)

        for j in range(len(nomes)):
            if nomes[j] == nomes_do_jogo.anfitriao:
                if placar_do_jogo_atual.gols_anfitriao > placar_do_jogo_atual.gols_visitante:
                    estat[j].pontos = estat[j].pontos + 3
                    estat[j].vitorias = estat[j].vitorias + 1
                elif placar_do_jogo_atual.gols_anfitriao == placar_do_jogo_atual.gols_visitante:
                    estat[j].pontos = estat[j].pontos + 1
                # saldo de gols do anfitrião
                saldo = placar_do_jogo_atual.gols_anfitriao - placar_do_jogo_atual.gols_visitante
                estat[j].saldo_de_gols = estat[j].saldo_de_gols + saldo

        # ----------- VISITANTE -----------
        if not verificar_elemento(nomes, nomes_do_jogo.visitante):
            nomes.append(nomes_do_jogo.visitante)
            nova_estat = estatisticas(nomes_do_jogo.visitante, 0, 0, 0)
            estat.append(nova_estat)

        for j in range(len(nomes)):
            if nomes[j] == nomes_do_jogo.visitante:
                if placar_do_jogo_atual.gols_visitante > placar_do_jogo_atual.gols_anfitriao:
                    estat[j].pontos = estat[j].pontos + 3
                    estat[j].vitorias = estat[j].vitorias + 1
                elif placar_do_jogo_atual.gols_visitante == placar_do_jogo_atual.gols_anfitriao:
                    estat[j].pontos = estat[j].pontos + 1
                # saldo de gols do visitante
                saldo = placar_do_jogo_atual.gols_visitante - placar_do_jogo_atual.gols_anfitriao
                estat[j].saldo_de_gols = estat[j].saldo_de_gols + saldo
    ordena_times(estat)
    return estat

def exibicao(jogos: list[str]) -> str:
    '''
    >>> jogos = ["Flamengo 2 Vasco 1\\n", "Vasco 1 Botafogo 1\\n", "Botafogo 3 Flamengo 2\\n"]
    >>> print(exibicao(jogos))
    Botafogo 4 1 1
    Flamengo 3 1 0
    Vasco    1 0 -1
    <BLANKLINE>

    >>> jogos = ["Flamengo 1 Vasco 1\\n", "Vasco 2 Botafogo 2\\n", "Botafogo 1 Flamengo 1\\n"]
    >>> print(exibicao(jogos))
    Botafogo 2 0 0
    Flamengo 2 0 0
    Vasco    2 0 0
    <BLANKLINE>
    >>> jogos = ["Palmeiras 1 Sao-Paulo 1\\n", "Flamengo 1 Atletico-MG 1\\n", "Atletico-MG 1 Palmeiras 1\\n", "Sao-Paulo 1 Flamengo 1\\n"]
    >>> print(exibicao(jogos))
    Atletico-MG 2 0 0
    Flamengo    2 0 0
    Palmeiras   2 0 0
    Sao-Paulo   2 0 0
    <BLANKLINE>
    '''
    resultado = classifica_times(tira_quebra_de_linha(jogos))
    maior_nome = 0
    for time in resultado:
        if len(time.nome) > maior_nome:
            maior_nome = len(time.nome)
    
    resultado_str = ""  # variável para acumular a saída
    for time in resultado:
        # Formata cada linha com alinhamento dos nomes e os dados separados por espaço
        espacos_pontos = 3 - len(str(time.pontos))
        espacos_vitorias = 2 - len(str(time.vitorias))
        espacos_saldo = 3 - len(str(time.saldo_de_gols))

        linha = (time.nome + (' ' * (maior_nome - len(time.nome))) + ' ' +
                (' ' * espacos_pontos) + str(time.pontos) + ' ' +
                (' ' * espacos_vitorias) + str(time.vitorias) + ' ' +
                (' ' * espacos_saldo) + str(time.saldo_de_gols) + '\n')
        resultado_str += linha
    return resultado_str

#Pergunta 2:
#Pergunta 3:
