# ExcelIngestor

## Visão Geral

O **ExcelIngestor** é um sistema desenvolvido em Python capaz de ler, processar e importar dados de planilhas Excel (.xlsx), convertendo-os para arquivos de texto (.txt).

O projeto utiliza a biblioteca **pandas** para leitura e processamento dos dados provenientes das planilhas e a biblioteca **logging** para registro de informações e histórico de execução do sistema.

O objetivo principal é a conversão de formatos de arquivos, além de preparar dados para sistemas de importação, bancos de dados e outros pipelines de dados, transformando informações não estruturadas em dados estruturados e rastreáveis, preservando a linhagem dos dados.

Essas funcionalidades são especialmente úteis para automatizar tarefas repetitivas de ingestão de dados, reduzindo erros manuais e organizando dados financeiros ou operacionais armazenados em arquivos Excel.

---

## Funcionalidades

- Leitura de dados a partir de arquivos Excel (.xlsx)
- Análise dinâmica das colunas da planilha
- Conversão de arquivos Excel para texto (.txt)
- Geração de histórico do sistema por meio de logs
- Estrutura modular e extensível

---

## Estrutura do Projeto

```
ExcelIngestor/
│
├── src/
│ ├── main.py # Ponto de entrada do sistema
│ ├── excel_reader.py # Leitura do Excel
│ ├── analyzer.py # Análise dinâmica das colunas
│ ├── converter.py # Conversão para TXT
│ └── logger.py # Logs do sistema
│
├── data/
│ ├── input/ # Arquivos Excel de entrada
│ └── output/ # Arquivos TXT gerados
│
├── tests/ # (futuro) testes automatizados
│
├── README.md
├── requirements.txt
└── .gitignore

```

---

## Tecnologias Utilizadas

- Python
- Pandas
- Logging

---

## Como Executar

1. Clone o repositório:
```
```bash
git clone <url-do-repositorio>

2. Instale as dependências:
```
pip install -r requirements.txt

3. Execute o sistema:
```
python src/main.py

---

## Próximos Passos (Roadmap)

- Suporte a outros formatos de saída (JSON, CSV)
- Suporte a múltiplas abas do Excel
- Interface via linha de comando (CLI)
- Implementação de testes automatizados

---

## Autor

Projeto desenvolvido por Vinícius Gomes, com foco em automação de processos administrativos e conversão de dados utilizando Python.

Este repositório faz parte de um portfólio voltado para soluções personalizadas de automação e ingestão de dados, podendo ser adaptado conforme as necessidades de cada cliente.