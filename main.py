import os
import xml.etree.ElementTree as ET
import pandas as pd
import openpyxl

def extract_xml_data(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Extraia as informações necessárias do XML
    num_nota = root.findtext('NumeroNota')
    emissor = root.findtext('Emissor')
    nome_cliente = root.findtext('NomeCliente')
    rua = root.findtext('Endereco/Rua')
    numero = root.findtext('Endereco/Numero')
    municipio = root.findtext('Endereco/Municipio')
    peso_bruto = root.findtext('PesoBruto')

    return {
        'Número da nota': num_nota,
        'Emissor da nota': emissor,
        'Nome do cliente': nome_cliente,
        'Endereço completo': f"{rua}, {numero}, {municipio}",
        'Peso bruto': peso_bruto
    }

def extract_batch_xmls(xml_folder):
    data_list = []
    for filename in os.listdir(xml_folder):
        if filename.endswith('.xml'):
            xml_file = os.path.join(xml_folder, filename)
            data = extract_xml_data(xml_file)
            data_list.append(data)

    return data_list

def create_excel_table(data_list, output_file):
    df = pd.DataFrame(data_list)
    df.to_excel(output_file, index=False)

if __name__ == '__main__':
    # Insira o caminho da pasta contendo os arquivos XML
    xml_folder_path = 'pasta_com_notas_fiscais'

    # Extrai os dados dos XMLs para uma lista de dicionários
    extracted_data = extract_batch_xmls(xml_folder_path)

    # Cria uma tabela Excel com as informações extraídas
    output_excel_file = 'notas_fiscais.xlsx'
    create_excel_table(extracted_data, output_excel_file)

    print("Extração e criação da tabela no Excel concluídas com sucesso.")
