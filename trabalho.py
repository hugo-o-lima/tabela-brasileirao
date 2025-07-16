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
class Jogo:
    '''
    Tipo de dado composto que representa as informacoes de um jogo
    '''
    anfitriao: str
    gols_anfitriao: int
    visitante: str
    gols_visitante: int

def nome_das_equipes(jogo:str) -> Jogo:
    """
    Extrai os nomes do time anfitrião e visitante de uma string com o resultado do jogo,
    retornando um objeto Jogo com os nomes preenchidos e os gols zerados.

    Exemplo:
    >>> nome_das_equipes("Fluminense 1 Cuiaba 0")
    Jogo(anfitriao='Fluminense', gols_anfitriao=0, visitante='Cuiaba', gols_visitante=0)
    """
    espacos = []
    for i in range(len(jogo)):
        if jogo[i] == " ":
            espacos.append(i)
    # O nome do anfitrião vai do início até o espaço antes do placar do anfitrião
    anfitriao = jogo[:espacos[-3]]
    # O nome do visitante vai do espaço depois do placar do anfitrião até o espaço antes do placar do visitante
    visitante = jogo[espacos[-2] + 1:espacos[-1]]
    jogos = Jogo(anfitriao, 0 , visitante, 0)
    return jogos

def placar_do_jogo(jogo: str) -> Jogo:
    """
    Extrai os gols do time anfitrião e visitante de uma string com o resultado do jogo,
    retornando um objeto Jogo com os gols preenchidos e os nomes vazios.

    Exemplo:
    >>> placar_do_jogo("Fluminense 1 Cuiaba 0")
    Jogo(anfitriao='', gols_anfitriao=1, visitante='', gols_visitante=0)
    """
    espacos = []
    for i in range(len(jogo)):
        if jogo[i] == " ":
            espacos.append(i)
    # O placar do anfitrião está entre o penúltimo e o antepenúltimo espaço
    gols_anfitriao = int(jogo[espacos[-3] + 1:espacos[-2]])
    # O placar do visitante está após o último espaço
    gols_visitante = int(jogo[espacos[-1] + 1:])
    return Jogo('', gols_anfitriao,'', gols_visitante)

def vitorias(placar: Jogo) -> int:
    """
    Retorna 1 se o time do anfitrião venceu, 0 caso contrário.

    Exemplo:
    >>> vitorias(Jogo('', 1, '', 0))
    1
    >>> vitorias(Jogo('', 0, '', 0))
    0
    """
    vitorias = 0
    if placar.gols_anfitriao > placar.gols_visitante:
        vitorias += 1
    if placar.gols_anfitriao < placar.gols_visitante:
        vitorias += 0
    return vitorias

def saldo_de_gols(placar: Jogo) -> int:
    """
    Calcula o saldo de gols (gols do anfitrião menos gols do visitante).

    Exemplo:
    >>> saldo_de_gols(Jogo('', 1, '', 0))
    1
    >>> saldo_de_gols(Jogo('', 0, '', 0))
    0
    """
    saldo = 0
    saldo = placar.gols_anfitriao - placar.gols_visitante
    return saldo

def ganho_pontos(x: Jogo) -> int:
    """
    Calcula os pontos ganhos pelo time, considerando 3 pontos por vitória,
    1 ponto por empate, e 0 para derrota.

    Exemplo:
    >>> ganho_pontos(Jogo('', 1, '', 0))
    3
    >>> ganho_pontos(Jogo('', 0, '', 1))
    3
    >>> ganho_pontos(Jogo('', 1, '', 1))
    1
    """
    if x.gols_anfitriao > x.gols_visitante:
        pontos = 3
    elif x.gols_visitante > x.gols_anfitriao:
        pontos = 3
    else:
        pontos = 1
    return pontos

@dataclass
class estatisticas:
    nome: str
    pontos: int
    vitorias: int
    saldo_de_gols: int

def verificar_elemento(lista, elemento_procurado) -> bool:
    """
    Verifica se um elemento está presente em uma lista.

    Exemplo:
    >>> verificar_elemento([1, 2, 3], 2)
    True
    >>> verificar_elemento(["a", "b"], "c")
    False
    """
    encontrado = False
    for elemento in lista:
        if elemento == elemento_procurado:
            encontrado = True
    return encontrado

def deve_trocar(a: estatisticas, b: estatisticas) -> bool:
    """
    Determina se o time b deve vir antes do time a na ordenação,
    com base nos critérios: pontos, vitórias, saldo de gols e nome.

    Exemplo:
    >>> a = estatisticas("Flamengo", 3, 1, 1)
    >>> b = estatisticas("Botafogo", 4, 1, 1)
    >>> deve_trocar(a, b)
    True
    """
    x = False
    if b.pontos > a.pontos:
        x = True
    if b.pontos == a.pontos:
        if b.vitorias > a.vitorias:
            x = True
        if b.vitorias == a.vitorias:
            if b.saldo_de_gols > a.saldo_de_gols:
                x =True
            if b.saldo_de_gols == a.saldo_de_gols:
                if b.nome < a.nome:
                    x = True
    return x

def ordena_times(estat: list[estatisticas]):
    """
    Ordena uma lista de estatísticas de times segundo critérios de pontos,
    vitórias, saldo de gols e ordem alfabética do nome.

    Exemplo:
    >>> estat = [estatisticas("Flamengo", 3, 1, 1), estatisticas("Botafogo", 4, 1, 1)]
    >>> ordena_times(estat)
    >>> estat[0].nome
    'Botafogo'
    """
    for i in range(len(estat)):
        for j in range(i + 1, len(estat)):
            if deve_trocar(estat[i], estat[j]):
                estat[i], estat[j] = estat[j], estat[i]

def list_str_para_jogo(lista: list[str]) -> list[Jogo]:
    """
    Converte uma lista de strings com resultados de jogos para uma lista
    de objetos Jogo com nomes e placares.

    Exemplo:
    >>> jogos_str = ["Flamengo 2 Vasco 1", "Botafogo 3 Flamengo 2"]
    >>> list_str_para_jogo(jogos_str)
    [Jogo(anfitriao='Flamengo', gols_anfitriao=2, visitante='Vasco', gols_visitante=1), Jogo(anfitriao='Botafogo', gols_anfitriao=3, visitante='Flamengo', gols_visitante=2)]
    """
    jogos = []
    for linha in lista:
        nomes = nome_das_equipes(linha)
        placar_atual = placar_do_jogo(linha)
        jogos.append(Jogo(
            anfitriao=nomes.anfitriao,
            gols_anfitriao=placar_atual.gols_anfitriao,
            visitante=nomes.visitante,
            gols_visitante=placar_atual.gols_visitante
        ))
    return jogos

def atualiza_estatisticas(nome_time: str, gols_feitos: int, gols_sofridos: int, nomes: list[str], estat: list[estatisticas]):
    """
    Atualiza as estatísticas de um time com base no resultado de um jogo,
    adicionando o time caso ainda não exista.

    Exemplo:
    >>> nomes = []
    >>> estat = []
    >>> atualiza_estatisticas("Flamengo", 2, 1, nomes, estat)
    >>> estat[0]
    estatisticas(nome='Flamengo', pontos=3, vitorias=1, saldo_de_gols=1)
    """
    if not verificar_elemento(nomes, nome_time):
        nomes.append(nome_time)
        estat.append(estatisticas(nome_time, 0, 0, 0))

    for i in range(len(estat)):
        if estat[i].nome == nome_time:
            if gols_feitos > gols_sofridos:
                estat[i].pontos += 3
                estat[i].vitorias += 1
            elif gols_feitos == gols_sofridos:
                estat[i].pontos += 1
            estat[i].saldo_de_gols += (gols_feitos - gols_sofridos)

def classifica_times(jogos: list[str]) -> list[estatisticas]:
    """
    Recebe uma lista de resultados de jogos e retorna a lista de estatísticas
    dos times ordenada pelo critério de classificação.

    Exemplo:
    >>> jogos = ["Flamengo 2 Vasco 1", "Botafogo 3 Flamengo 2"]
    >>> resultado = classifica_times(jogos)
    >>> resultado[0].nome
    'Botafogo'
    """
    nomes: list[str]= []
    estat: list[estatisticas] = []

    for i in range(len(jogos)):
        nomes_do_jogo = nome_das_equipes(jogos[i])
        placar_do_jogo_atual = placar_do_jogo(jogos[i])

        # Atualiza anfitrião
        atualiza_estatisticas(
            nomes_do_jogo.anfitriao,placar_do_jogo_atual.gols_anfitriao,
            placar_do_jogo_atual.gols_visitante, nomes, estat
        )
        # Atualiza visitante
        atualiza_estatisticas(
            nomes_do_jogo.visitante, placar_do_jogo_atual.gols_visitante,
            placar_do_jogo_atual.gols_anfitriao, nomes, estat)

    ordena_times(estat)
    return estat

def exibicao(jogos: list[str]) -> str:
    '''
    Gera uma string formatada com a classificação dos times a partir
    da lista de resultados dos jogos.

    Exemplo:
    >>> jogos = ["Flamengo 2 Vasco 1\\n", "Vasco 1 Botafogo 1\\n", "Botafogo 3 Flamengo 2\\n"]
    >>> print(exibicao(jogos))
    Botafogo 4 1 1
    Flamengo 3 1 0
    Vasco    1 0 -1
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
