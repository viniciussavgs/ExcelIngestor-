from excel_reader import ler_excel

def main():
    print("Iniciando ExcelIngestor")
    caminho = input("Informe o caminho do arquivo Excel: ")
    df = ler_excel(caminho)
    print("Arquivo carregado com sucesso!")
    print(df.head())

if __name__ == "__main__":
    main()