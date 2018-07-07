import os, json
from jinja2 import Environment, FileSystemLoader
from Campo import Campo

templatePath = 'template/'

def main():

    with open('input/mapeamento.as') as json_file:  
        data = json.load(json_file)

        for value in data['entidades']:
            merge(value)
            editFiles(value['nome'])


def merge(entidade):
    
    
    entityName = entidade['nome']
    entityFields = entidade['campos']

    jinja = Environment(loader=FileSystemLoader(os.path.dirname(os.path.abspath(__file__))), trim_blocks=True)

    writeFile(entityName, jinja.get_template(templatePath + 'mapeamento.tpl').render(nomeEntidade=entityName, campos=entityFields), '.xml') 

    writeFile(entityName, jinja.get_template(templatePath + 'entidade.tpl').render(nomeEntidade=entityName, campos=entityFields), '.java') 

    writeFile('Colecao' + entityName, jinja.get_template(templatePath + 'colecao.tpl').render(nomeEntidade=entityName, campos=entityFields), '.java') 

    writeFile('ComandoRepositorio' + entityName + 'JDBC', jinja.get_template(templatePath + 'comandoRepositorio.tpl').render(nomeEntidade=entityName, campos=entityFields), '.java') 

def writeFile(fileName, stringFile, fileExtension):

    outputPath = 'output/'

    fileName = fileName.lower() if fileExtension == '.xml' else fileName

    file = open(outputPath + fileName + fileExtension,'w') 
    file.write(stringFile)
    file.close

def editFiles(entityName):
    cardsBusinessPath = '/Users/edmilsonneto/Downloads/autorizador/conf/src/WEB-INF/conf/cardsBusiness.properties'
    cardsFachadaPath = '/Users/edmilsonneto/Downloads/autorizador/src/com/neus/cards/business/fachada/CardsFachada.java'

    with open(cardsBusinessPath, 'a') as the_file:
        the_file.write('\nCOLECAO_' + entityName.upper() + '=' + entityName.lower() + '/' + entityName[:1].lower() + entityName[1:] + '.xml\n')

    jinja = Environment(loader=FileSystemLoader(os.path.dirname(os.path.abspath(__file__))), trim_blocks=True)
    code = jinja.get_template(templatePath + 'cardsFachada.tpl').render(nomeEntidade=entityName)

    linesCardsFachada = open(cardsFachadaPath).read().splitlines()
    linesCardsFachada[len(linesCardsFachada) - 1] = ''
    open(cardsFachadaPath,'w').write('\n'.join(linesCardsFachada))
    print linesCardsFachada

if __name__ == '__main__':
    main()