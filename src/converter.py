from datetime import datetime
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def converter_para_txt(df, info_colunas):
    caminho_saida = os.path.join(BASE_DIR, "data", "output", "saida.txt")

    with open(caminho_saida, "w", encoding="utf-8") as f:

        f.write("EXCELL INGESTOR - RELATÓRIO DE CONVERSÃO\n")
        f.write(f"Data de processamento: {datetime.now()}\n")
        f.write("="*50 + "\n\n")

        f.write("COLUNAS IDENTIFICADAS:\n")
        for col in info_colunas:
            f.write(f"- ({col['nome']}) / ({col['tipo']})\n")

        f.write("\n" + "="*50 + "\n")
        f.write("DADOS:\n")
        f.write(df.to_string(index=False))

    print("TXT gerado em:", caminho_saida)
