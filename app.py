import os, json
from jinja2 import Environment, FileSystemLoader

templatePath = 'template/'

def main():

    with open('input/mapeamento.as') as json_file:  
        data = json.load(json_file)

        for value in data['entidades']:
            merge(value)
            editFiles(value['nome'])


def merge(entity):
    
    entityName = entity['nome']
    entityFields = entity['campos']

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
    
    cardsFachadaPath = '/Users/edmilsonneto/Downloads/autorizador/src/com/neus/cards/business/fachada/CardsFachada.java'

    linesCardsFachada = open(cardsFachadaPath).read().splitlines()
    linesCardsFachada[len(linesCardsFachada) - 1] = str('   public Colecao' + entityName + ' getColecao' + entityName + '();')
    linesCardsFachada.append(str('  public void setColecao' + entityName + '(Colecao' + entityName + ' colecao' + entityName + ');'))
    linesCardsFachada.append('}')
    open(cardsFachadaPath,'w').write('\n'.join(linesCardsFachada))

def editCardsBusiness(entityName):

    cardsBusinessPath = '/Users/edmilsonneto/Downloads/autorizador/conf/src/WEB-INF/conf/cardsBusiness.properties'
    with open(cardsBusinessPath, 'a') as the_file:
        the_file.write('\nCOLECAO_' + entityName.upper() + '=' + entityName.lower() + '/' + entityName[:1].lower() + entityName[1:] + '.xml\n')

if __name__ == '__main__':
    main()