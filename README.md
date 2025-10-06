# Python Concurrency e Algoritmos

Este repositório serve como uma coleção de exemplos e implementações em Python, focando em **concorrência**, **algoritmos de busca e ordenação**, e **operações utilitárias**. O objetivo é demonstrar diversas abordagens para lidar com tarefas paralelas, otimização de código e funcionalidades básicas de programação em Python.

## 🚀 Começando

Siga estas instruções para configurar e executar os projetos em sua máquina local para desenvolvimento e testes.

### Pré-requisitos

Certifique-se de ter o Python 3 e `virtualenv` instalados em seu sistema.

```bash
- python3
- virtualenv
```

### Instalação

Para sistemas operacionais baseados em Linux ou macOS, execute:

```bash
make install
```

Para usuários Windows, utilize os seguintes comandos:

```bash
virtualenv env
env\Scripts\activate.bat
pip install -r requirements.txt
```

### Executando Testes

Para executar os testes automatizados, use:

```bash
make test
```

ou diretamente com `pytest`:

```bash
pytest
```

## 📂 Estrutura do Projeto

O repositório está organizado nas seguintes categorias:

### 🔍 Algoritmos de Busca e Ordenação

Esta seção contém implementações de algoritmos fundamentais.

| Arquivo             | Descrição                                      |
| :------------------ | :--------------------------------------------- |
| `binary_search.py`  | Implementação do algoritmo de busca binária.   |
| `bubble_sort.py`    | Implementação do algoritmo Bubble Sort.        |
| `sort.py`           | Outra implementação do algoritmo Bubble Sort.  |

### ⚡ Concorrência e Paralelismo

Exemplos de como lidar com concorrência e paralelismo em Python usando `threading` e `multiprocessing`.

| Arquivo                         | Descrição                                                                                             |
| :------------------------------ | :---------------------------------------------------------------------------------------------------- |
| `multi-threading.py`            | Demonstra o uso de múltiplas threads para executar tarefas simultaneamente (cálculo de quadrado e cubo). |
| `multi_processing_example.py`   | Exemplo de uso de `multiprocessing` para paralelizar tarefas.                                         |
| `thread_example.py`             | Exemplo básico de criação e execução de uma única thread.                                             |
| `assessment_multithreading.py`  | Script de web scraping que utiliza multithreading para extrair detalhes de filmes do IMDb.             |
| `assessment_single_thread.py`   | Versão single-thread do script de web scraping para comparação de desempenho.                         |
| `movies_multithread.py`         | Outro script de web scraping de filmes do IMDb, utilizando multithreading.                            |
| `web-scraping.py`               | Exemplo de web scraping usando `multiprocessing.Pool` para raspar múltiplas URLs.                     |

### 🔄 Corrotinas, Geradores e Iteradores

Exemplos que ilustram o funcionamento e uso de corrotinas, geradores e iteradores em Python.

| Arquivo                       | Descrição                                                                                             |
| :---------------------------- | :---------------------------------------------------------------------------------------------------- |
| `coroutine-computations.py`   | Demonstra corrotinas com `yield` para pausar e retomar a execução, realizando computações.             |
| `coroutine-example.py`        | Exemplo básico de corrotina.                                                                          |
| `coroutine-send-values.py`    | Demonstra como enviar valores para uma corrotina usando `send()`.                                     |
| `coroutines-multiple-functions.py` | Exemplo de como múltiplas corrotinas podem ser executadas de forma intercalada.                       |
| `generator-example.py`        | Exemplo de função geradora que produz uma sequência de valores.                                       |
| `iterator-example.py`         | Demonstra a criação e uso de iteradores.                                                              |

### ➕ Operações Matemáticas e Utilitários

Scripts com funções matemáticas básicas e outras operações utilitárias.

| Arquivo             | Descrição                                      |
| :------------------ | :--------------------------------------------- |
| `math_operations.py`| Funções para operações de adição e subtração.  |
| `operations.py`     | Funções para adição, subtração e multiplicação.|

### 🧪 Testes

Arquivos de teste para validar as implementações.

| Arquivo                  | Descrição                                                                     |
| :----------------------- | :---------------------------------------------------------------------------- |
| `test_binary_search.py`  | Testes unitários para o algoritmo de busca binária.                           |
| `test_bubble_sort.py`    | Testes unitários para o algoritmo Bubble Sort (`bubble_sort.py`).             |
| `testBubbleSort.py`      | Testes unitários para o algoritmo Bubble Sort (`sort.py`).                    |
| `test_math_operations.py`| Testes unitários para as funções em `math_operations.py`.                     |
| `testAdditionOperation.py`| Testes unitários para as funções em `operations.py`.                          |

## 📄 Arquivos de Dados

| Arquivo      | Descrição                                                                      |
| :----------- | :----------------------------------------------------------------------------- |
| `movies.csv` | Arquivo CSV contendo dados de filmes, gerado pelos scripts de web scraping.    |

## 👤 Autor

Feito com 💙 por [Seu Nome/Usuário do GitHub](https://github.com/SeuUsuarioDoGitHub)

## 📚 Referências

Este projeto foi inspirado e construído com base em conceitos de concorrência e algoritmos em Python. As referências específicas para cada implementação podem ser encontradas nos comentários dos respectivos arquivos. Para mais informações sobre os tópicos abordados, consulte a documentação oficial do Python e recursos de algoritmos.

