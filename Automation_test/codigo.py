#bibliotecas instaladas: pyautogui(automização),pandas(importa arquivos de dados para o código), openpyxl(trabalha com excell)
import pyautogui
import time
import pandas as pd
#pyautogui.click -> clica
#pyautogui.wite -> escreve um texto
#pyautogui.press -> aperta uma tecla
#pyautogui.hotkey -> aperta um atalho (hotkey)
pyautogui.PAUSE = 0.3
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login" 
pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")


# Passo 2: Fazer o login
pyautogui.write(link)
pyautogui.press("enter")
#Nesse momento específico é necessário que colocar uma pausa levando em consideração o tempo que a internet leva para carregar uma página
time.sleep(3)
pyautogui.click(x=-1344, y=498)
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab") #pode coloca o endereço (click(x=1115, y=736) e se for uma espaço logo depois pode usar o TAB 
pyautogui.write("SenhaDificil")
pyautogui.press("tab")
pyautogui.press("enter")
#pausa para o site carregar
time.sleep(3)

# Passo 3: Acessar a base de dados
tabela = pd.read_csv("produtos.csv") #caso o arquivo inteiro esteja no mesmo projeto, caso não tem que colocar o endereço completo
#caso queira ler apenas uma aba de uma arquivo(excel): pandas.read_excel(sheet_name="Custos")
# Passo 1: entrar no sistema 
print(tabela)


for linha in tabela.index:      #percorre de acordo com o número da linha, se for de acordo com a coluna usa o tabela.columns
    # Passo 4: Cadastrar 1 produto
    pyautogui.click(x=-1431, y=356)      #clica no campo do primeiro código
    #código
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")
    #marca
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")
    #tipo
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")
    #categoria
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")
    #peço unitário
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")
    #custo
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")
    #obs
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")
    pyautogui.press("enter")   #envia o cadastro do produto
#assim que finalizar é necessário voltar para o início na tela para iniciar novamente
    pyautogui.scroll(5000) #é necessário saber o tamanho do scroll, mas como é para o inicio pode colocar um número alto que vai deixa a tela no topo


# Passo 5 : Repetir o processo com todos os produtos da lista
