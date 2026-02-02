from excel_reader import ler_excel
from analyzer import analisar_colunas
from converter import converter_para_txt


def main():
    print("Iniciando ExcelIngestor")
    caminho = input("Informe o caminho do arquivo Excel: ")

    df = ler_excel(caminho)
    info_colunas = analisar_colunas(df)
    converter_para_txt(df, info_colunas)

    print("Arquivo TXT gerado com sucesso!!")
    

    
if __name__ == "__main__":
    main()