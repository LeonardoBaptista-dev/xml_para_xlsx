import os
import xml.etree.ElementTree as ET
import random
from faker import Faker

def generate_random_name():
    fake = Faker()
    return fake.name()

def generate_random_address():
    fake = Faker()
    return fake.street_name(), fake.random_int(min=1, max=100), fake.city()

def generate_xml_data(num_nota, emissor, peso_bruto):
    root = ET.Element('NotaFiscal')
    
    ET.SubElement(root, 'NumeroNota').text = str(num_nota)
    ET.SubElement(root, 'Emissor').text = emissor

    nome_cliente = generate_random_name()
    ET.SubElement(root, 'NomeCliente').text = nome_cliente

    rua, numero, municipio = generate_random_address()
    endereco = ET.SubElement(root, 'Endereco')
    ET.SubElement(endereco, 'Rua').text = rua
    ET.SubElement(endereco, 'Numero').text = str(numero)
    ET.SubElement(endereco, 'Municipio').text = municipio

    ET.SubElement(root, 'PesoBruto').text = str(peso_bruto)

    return ET.ElementTree(root)

def save_xml_to_file(xml_tree, filename):
    with open(filename, 'wb') as file:
        xml_tree.write(file, encoding='utf-8', xml_declaration=True)

if __name__ == '__main__':
    # Crie uma pasta para armazenar os arquivos XML
    xml_folder_path = 'pasta_com_notas_fiscais'
    os.makedirs(xml_folder_path, exist_ok=True)

    # Gerar e salvar 500 notas fiscais em arquivos XML
    for i in range(1, 501):
        nota_fiscal = generate_xml_data(
            num_nota=i,
            emissor=f'Emissor {i}',
            peso_bruto=i * 10.5
        )
        xml_file_path = os.path.join(xml_folder_path, f'nota_fiscal_{i}.xml')
        save_xml_to_file(nota_fiscal, xml_file_path)

    print("Notas fiscais geradas e salvas com sucesso.")
