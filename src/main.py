from excel_reader import ler_excel
from analyzer import analisar_colunas

def main():
    print("Iniciando ExcelIngestor")
    caminho = input("Informe o caminho do arquivo Excel: ")

    df = ler_excel(caminho)
    info_colunas = analisar_colunas(df)
    print("\nColunas detectadas:")
    for col in info_colunas:
        print(f"-{col['nome']} ({col['tipo']})")

    
if __name__ == "__main__":
    main()