import sys
from dataclasses import dataclass

def main():
    if len(sys.argv) < 2:
        print('Nenhum nome de arquivo informado.')
        sys.exit(1)

    if len(sys.argv) > 2:
        print('Muitos parâmetros. Informe apenas um nome de arquivo.')
        sys.exit(1)

    jogos = le_arquivo(sys.argv[1])

    # TODO: solução da pergunta 1
    print(exibicao(jogos))

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

@dataclass
class Jogo:
    '''
    Tipo de dado composto que representa as informacoes de um jogo
    '''
    anfitriao: str
    gols_anfitriao: int
    visitante: str
    gols_visitante: int

def nome_das_equipes(jogo: str) -> Jogo:
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
    anfitriao = jogo[:espacos[-3]]
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
    gols_anfitriao = int(jogo[espacos[-3] + 1:espacos[-2]])
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

@dataclass
class Estatisticas:
    '''
    Tipo de dado composto que serve para armazenar as estatisticas que
    serão exibidas
    '''
    nome: str
    pontos: int
    vitorias: int
    saldo_de_gols: int

def verificar_elemento(lista: list[str], elemento_procurado: str) -> bool:
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

def deve_trocar(a: Estatisticas, b: Estatisticas) -> bool:
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

def ordena_times(estat: list[Estatisticas]) -> None:
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

def atualiza_estatisticas(nome_time: str, gols_feitos: int, gols_sofridos: int, nomes: list[str], estat: list[Estatisticas]) -> None:
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
        estat.append(Estatisticas(nome_time, 0, 0, 0))

    for i in range(len(estat)):
        if estat[i].nome == nome_time:
            if gols_feitos > gols_sofridos:
                estat[i].pontos += 3
                estat[i].vitorias += 1
            elif gols_feitos == gols_sofridos:
                estat[i].pontos += 1
            estat[i].saldo_de_gols += (gols_feitos - gols_sofridos)

def transforma_estatistica(jogos: list[str]) -> list[Estatisticas]:
    """
    Recebe uma lista de resultados de jogos e retorna a lista de estatísticas
    dos times ordenada pelo critério de classificação.

    Exemplo:
    >>> jogos = ["Flamengo 2 Vasco 1", "Botafogo 3 Flamengo 2"]
    >>> resultado = classifica_times(jogos)
    >>> resultado[0].nome
    'Botafogo'
    """
    nomes: list[str] = []
    estat: list[Estatisticas] = []

    for i in range(len(jogos)):
        nomes_do_jogo = nome_das_equipes(jogos[i])
        placar_do_jogo_atual = placar_do_jogo(jogos[i])
        atualiza_estatisticas(
            nomes_do_jogo.anfitriao,placar_do_jogo_atual.gols_anfitriao,
            placar_do_jogo_atual.gols_visitante, nomes, estat)
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
    resultado = transforma_estatistica(tira_quebra_de_linha(jogos))
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
    # TODO: solução da pergunta 2
'''
Para a pergunta 2, você deve identificar o(s) time(s) que obtiveram o maior número de pontos em
relação à quantidade de pontos possíveis jogando como anfitrião. Por exemplo, um time que realizou
5 jogos como anfitrião (15 pontos possíveis) e conquistou três vitórias e um empate, obteve 10 pontos,
portanto, 66% de aproveitamento.
'''
    # TODO: solução da pergunta 3

def le_arquivo(nome: str) -> list[str]:
    '''
    Lê o conteúdo do arquivo *nome* e devolve uma lista onde cada elemento
    representa uma linha.
    Por exemplo, se o conteúdo do arquivo for
    Sao-Paulo 1 Atletico-MG 2
    Flamengo 2 Palmeiras 1
    a resposta produzida é
    [‘Sao-Paulo 1 Atletico-MG 2’, ‘Flamengo 2 Palmeiras 1’]
    '''
    try:
        with open(nome) as f:
            return f.readlines()
    except IOError as e:
        print(f'Erro na leitura do arquivo "{nome}": {e.errno} - {e.strerror}.')
        sys.exit(1)

if __name__ == '__main__':
    main()

