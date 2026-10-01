# Automação de Cadastro de Produtos com Python

## Objetivo

Automatizar o cadastro de produtos em um sistema web. O script lê uma base de dados (`produtos.csv`) e, para cada produto, preenche e envia o formulário do sistema **simulando um usuário real** (teclado e mouse), sem precisar de API.

## Tecnologias

| Biblioteca | Função |
|---|---|
| `pyautogui` | Controla mouse e teclado (cliques, digitação, atalhos, scroll) |
| `pandas` | Lê o arquivo de dados (`.csv` / `.xlsx`) e transforma em tabela |
| `openpyxl` | Permite ao pandas ler arquivos Excel |
| `time` | Faz pausas para esperar o carregamento das páginas |

### Instalação

```bash
pip install pyautogui pandas openpyxl
```

---

## Como funciona

### Passo 1 — Abrir o navegador
Aperta a tecla **Windows**, digita `edge` e pressiona **Enter** para abrir o Microsoft Edge.

### Passo 2 — Fazer login
1. Digita o link do sistema e pressiona **Enter**.
2. Espera 3 segundos (`time.sleep(3)`) para a página carregar.
3. Clica no campo de e-mail, digita o e-mail, usa **Tab** para ir ao campo de senha, digita a senha e envia com **Enter**.
4. Espera mais 3 segundos para o sistema carregar.

### Passo 3 — Ler a base de dados
```python
tabela = pd.read_csv("produtos.csv")
```
Carrega os produtos do arquivo `produtos.csv`, que tem as colunas:

`codigo`, `marca`, `tipo`, `categoria`, `preco_unitario`, `custo`, `obs`

### Passo 4 — Cadastrar um produto
Para cada linha da tabela:
1. Clica no primeiro campo do formulário (código).
2. Pega cada valor com `tabela.loc[linha, "coluna"]`, converte para texto (`str`), digita e pressiona **Tab** para ir ao próximo campo.
3. O campo `obs` só é preenchido se tiver valor — células vazias viram `"nan"` no pandas, por isso a verificação `if obs != "nan"`.
4. Pressiona **Enter** para enviar o cadastro.
5. Faz `scroll(5000)` para voltar ao topo da página e começar o próximo produto.

### Passo 5 — Repetir
O `for linha in tabela.index` percorre todas as linhas, repetindo o Passo 4 até cadastrar todos os produtos.

---

## Configurações importantes

- **`pyautogui.PAUSE = 0.3`** — pausa de 0,3 s entre cada comando, para o sistema acompanhar o ritmo do script.
- **Coordenadas de clique** (`x=-1344, y=498` e `x=-1431, y=356`) — dependem da tela de quem executa. O `x` negativo indica um **segundo monitor** posicionado à esquerda do principal. Para descobrir as suas coordenadas:
  ```python
  import pyautogui, time
  time.sleep(5)          # tempo para posicionar o mouse
  print(pyautogui.position())
  ```
- **`time.sleep(3)`** — ajuste conforme a velocidade da sua internet.

---

## Como executar

1. Coloque o `produtos.csv` na mesma pasta do script (ou use o caminho completo).
2. Ajuste as coordenadas de clique para a sua tela.
3. Execute:
   ```bash
   python codigo.py
   ```
4. **Não mexa no mouse nem no teclado** enquanto o script roda.

> ⚠️ Para interromper em emergência, mova o mouse rapidamente para um dos **cantos da tela** (recurso *fail-safe* do pyautogui).

---

## Comandos principais do pyautogui

| Comando | O que faz |
|---|---|
| `pyautogui.click(x, y)` | Clica numa posição da tela |
| `pyautogui.write("texto")` | Digita um texto |
| `pyautogui.press("tecla")` | Pressiona uma tecla |
| `pyautogui.hotkey("ctrl", "c")` | Pressiona um atalho |
| `pyautogui.scroll(valor)` | Rola a tela (positivo = para cima) |

---

## Limitações

- Depende da resolução e posição da tela — se a janela mudar de lugar, os cliques erram.
- Depende do tempo de carregamento — internet lenta pode quebrar o fluxo.
- O computador fica ocupado durante toda a execução.
