# Análise de Alunos

Aplicação desenvolvida em Python com Streamlit para visualizar e analisar o desempenho acadêmico a partir de uma planilha Excel. O projeto tem como objetivo transformar dados escolares em uma interface simples, intuitiva e útil para acompanhamento de resultados e identificação de padrões.

## Visão Geral

Este projeto foi construído como uma solução prática para explorar dados de alunos de forma visual e acessível. A ideia é demonstrar como a combinação de Python, análise de dados e dashboards interativos pode facilitar a interpretação de informações acadêmicas e apoiar a tomada de decisão.

## Por que este projeto?

Este projeto destaca habilidades relevantes para o mercado de tecnologia e dados, incluindo:

- Desenvolvimento em Python
- Manipulação e análise de dados com Pandas
- Visualização de informações em interface interativa com Streamlit
- Organização de projetos com arquivos e estrutura simples
- Documentação clara e profissional para apresentação em portfólio

## Funcionalidades

- Leitura de dados a partir de arquivo Excel
- Visualização do desempenho dos alunos em uma interface interativa
- Organização de informações para facilitar a leitura e interpretação
- Estrutura preparada para evolução com novas métricas, filtros e relatórios

## Tecnologias Utilizadas

- Python 3.13+
- Streamlit
- Pandas
- OpenPyXL
- PowerShell (Windows)

## Estrutura do Projeto

- `analise_alunos.py`: aplicação principal desenvolvida com Streamlit
- `alunos_notas.xlsx`: arquivo com os dados dos alunos
- `requirements.txt`: dependências do projeto
- `README.md`: documentação do projeto

## Pré-requisitos

Antes de executar o projeto, certifique-se de ter instalado:

- Python 3.13 ou superior
- PowerShell no Windows

## Como executar

### 1. Criar ambiente virtual

```powershell
python -m venv .venv

### 2. Ativar ambiente virtual

```powershell
.\.venv\Scripts\Activate.ps1

### 3. Instalar dependências

pip install -r requirements.txt

### 4. Rodar a aplicação

streamlit run analise_alunos.py

### Como usar

Coloque o arquivo alunos_notas.xlsx na raiz do projeto.

Execute a aplicação com o comando acima.
Acesse o endereço local fornecido pelo Streamlit no navegador.
Dependências principais
altair==6.1.0
pandas==3.0.2
streamlit==1.57.0
openpyxl==3.1.2

### Observações 

Caso o PowerShell bloqueie a execução de scripts, execute:

Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

### Objetivo do Projeto 

Este projeto demonstra uma abordagem prática para:

analisar dados com Python
construir interfaces interativas com Streamlit
transformar informações em insights visuais
mostrar capacidade técnica em projetos com foco em usabilidade e clareza

### Próximos passos

Algumas melhorias futuras podem incluir:

filtros por turma, período ou aluno
gráficos comparativos de desempenho
exportação de relatórios em PDF ou Excel
integração com banco de dados ou APIs

### Conclusão 

Este projeto representa uma aplicação objetiva de Python para análise de dados e desenvolvimento de dashboards, com potencial para crescer em complexidade e relevância técnica. É uma boa demonstração de um perfil com foco em dados, automação e soluções práticas.