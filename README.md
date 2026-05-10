# Analise de Alunos

Aplicação em Python com Streamlit para visualizar desempenho de alunos a partir de uma planilha Excel.

## Requisitos

- Python 3.13+
- PowerShell (Windows)

## Estrutura do projeto

- `analise_alunos.py`: aplicação Streamlit
- `alunos_notas.xlsx`: base de dados dos alunos
- `requirements.txt`: dependências do projeto

## Como executar

1. Criar ambiente virtual:

```powershell
python -m venv .venv
```

2. Ativar ambiente virtual:

```powershell
.\.venv\Scripts\Activate.ps1
```

3. Instalar dependências:

```powershell
pip install -r requirements.txt
```

4. Rodar a aplicação:

```powershell
streamlit run analise_alunos.py
```

## Dependências principais

- altair==6.1.0
- pandas==3.0.2
- streamlit==1.57.0
- openpyxl==3.1.2

## Observações

- O arquivo `alunos_notas.xlsx` deve estar na raiz do projeto.
- Caso o PowerShell bloqueie scripts, execute:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```
