import pandas as pd
from lxml import etree
import sys

def add_question_to_xml(question_data, root_element):
    question_xml = etree.SubElement(root_element, 'question', type="multichoice")

    name = etree.SubElement(question_xml, 'name')
    text = etree.SubElement(name, 'text')
    text.text = etree.CDATA(question_data['Pregunta'])

    questiontext = etree.SubElement(question_xml, 'questiontext', format="html")
    text = etree.SubElement(questiontext, 'text')
    text.text = etree.CDATA(f"<p>{question_data['Pregunta']}</p>")

    generalfeedback = etree.SubElement(question_xml, 'generalfeedback', format="html")
    text = etree.SubElement(generalfeedback, 'text')
    text.text = etree.CDATA(f"<p>{question_data['Explicación']}</p>")

    defaultgrade = etree.SubElement(question_xml, 'defaultgrade')
    defaultgrade.text = '1.0000000'

    penalty = etree.SubElement(question_xml, 'penalty')
    penalty.text = '0.3333333'

    hidden = etree.SubElement(question_xml, 'hidden')
    hidden.text = '0'

    single = etree.SubElement(question_xml, 'single')
    single.text = 'true'

    shuffleanswers = etree.SubElement(question_xml, 'shuffleanswers')
    shuffleanswers.text = 'true'

    answernumbering = etree.SubElement(question_xml, 'answernumbering')
    answernumbering.text = 'abc'

    for i in range(1, 5):
        answer = etree.SubElement(question_xml, 'answer', fraction=str(100 if i == question_data['Correcta'] else 0), format="html")
        text = etree.SubElement(answer, 'text')
        text.text = etree.CDATA(f"<p>{question_data[f'Opcion{i}']}</p>")

    return root_element

def create_moodle_xml(xlsx_path):
    # Leer el archivo de Excel
    excel_data = pd.read_excel(xlsx_path)

    # Definir el esqueleto base del archivo XML para Moodle
    root = etree.Element('quiz')

    # Recorrer el DataFrame y añadir cada pregunta al XML
    for index, row in excel_data.iterrows():
        root = add_question_to_xml(row, root)

    # Convertir el árbol XML en una cadena
    return etree.tostring(root, pretty_print=True, xml_declaration=True, encoding='UTF-8')

if __name__ == "__main__":
    # Tomar el archivo XLSX como parámetro desde la línea de comandos
    if len(sys.argv) != 2:
        print("Usage: python script.py <path_to_xlsx>")
        sys.exit(1)

    xlsx_path = sys.argv[1]
    xml_data = create_moodle_xml(xlsx_path)
    
    # Guardar el resultado en un archivo XML
    xml_file_path = xlsx_path.replace('.xlsx', '.xml')
    with open(xml_file_path, 'wb') as xml_file:
        xml_file.write(xml_data)

    print(f"XML file created at {xml_file_path}")
