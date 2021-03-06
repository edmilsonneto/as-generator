import os
import json
from jinja2 import Environment, FileSystemLoader

PROJECT_PATH = '/Users/edmilsonneto/Developer/git/autorizador/'

CARDS_BUSINESS_PATH = 'conf/src/WEB-INF/conf/cardsBusiness.properties'
CARDS_FACHADA_PATH = 'src/com/neus/cards/business/fachada/CardsFachada.java'
CARDS_FACHADA_HTTP = 'src/com/neus/cards/business/fachada/http/CardsFachadaHttp.java'
CARDS_FACHADA_IMPL = 'src/com/neus/cards/business/fachada/CardsFachadaImpl.java'
REPOSITORIO_COLECOES_PATH = 'src/com/neus/cards/business/fachada/RepositorioColecoes.java'

TEMPLATE_MAPEAMENTO_XML = 'template/mapeamento.jinja2'
TEMPLATE_ENTIDADE = 'template/entidade.jinja2'
TEMPLATE_COLECAO = 'template/colecao.jinja2'
TEMPLATE_COMANDO_REPOSITORIO = 'template/comandoRepositorio.jinja2'
TEMPLATE_CARDS_FACHADA_HTTP = 'template/cardsFachadaHttp.jinja2'
TEMPLATE_CARDS_FACHADA_IMPL = 'template/cardsFachadaImpl.jinja2'
TEMPLATE_REPOSITORIO_COLECOES = 'template/repositorioColecoes.jinja2'

TEMPLATE_PATH = 'template/'
PROJECT_ENCODE = 'cp1252'
J2 = Environment(loader=FileSystemLoader(os.path.dirname(os.path.abspath(__file__))), trim_blocks=True)


def main():
    with open('input/entitys.json') as json_file:
        data = json.load(json_file)

        for value in data['entitys']:
            merge(value)
           # edit_repositorio_colecoes(value['name'])



def merge(entity):
    entity_name = entity['name']
    entity_fields = entity['fields']

    entidade_path = PROJECT_PATH + 'src/com/neus/cards/business/'

   # write_file(entity_name, J2.get_template(TEMPLATE_MAPEAMENTO_XML).render(entityName=entity_name, fields=entity_fields), '.xml')
    write_file(entity_name, J2.get_template(TEMPLATE_ENTIDADE).render(entityName=entity_name, fields=entity_fields), '.java', entidade_path)
   # write_file('Colecao' + entity_name, J2.get_template(TEMPLATE_COLECAO).render(entityName=entity_name, fields=entity_fields), '.java')
   # write_file('ComandoRepositorio' + entity_name + 'JDBC', J2.get_template(TEMPLATE_COMANDO_REPOSITORIO).render(entityName=entity_name, fields=entity_fields), '.java')


def write_file(file_name, string_file, file_extension, output_path):

    file_name = file_name.lower() if file_extension == '.xml' else file_name

    output_path = output_path + file_name.lower() + '/'+ file_name + file_extension

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        f.write(string_file)


def edit_file(entity_name):
    edit_cards_business(entity_name)
    edit_cards_fachada(entity_name)
    edit_cards_fachada_http(entity_name)
    edit_cards_fachada_impl(entity_name)
    edit_repositorio_colecoes(entity_name)


def edit_cards_business(entity_name):
    cards_business_path = PROJECT_PATH + CARDS_BUSINESS_PATH

    with open(cards_business_path, mode='a', encoding='cp1252') as the_file:
        the_file.write('\nCOLECAO_' + entity_name.upper() + '=' + entity_name.lower() + '/' + entity_name[:1].lower() + entity_name[1:] + '.xml\n')


def edit_cards_fachada(entity_name):
    path = PROJECT_PATH + CARDS_FACHADA_PATH

    file_lines = open(path, encoding=PROJECT_ENCODE).read().splitlines()

    file_lines.insert(38, 'import com.neus.cards.business.' + entity_name.lower() + '.Colecao' + entity_name + ';')
    file_lines[len(file_lines) - 1] = str('\tpublic Colecao' + entity_name + ' getColecao' + entity_name + '(); \n')
    file_lines.append(str('\tpublic void setColecao' + entity_name + '(Colecao' + entity_name + ' colecao' + entity_name + '); \n'))
    file_lines.append('}')

    open(path, 'w').write('\n'.join(file_lines))


def edit_cards_fachada_http(entity_name):

    new_content = J2.get_template(TEMPLATE_CARDS_FACHADA_HTTP).render(entityName=entity_name)

    path = PROJECT_PATH + CARDS_FACHADA_HTTP

    lines = open(path, encoding=PROJECT_ENCODE).read().splitlines()

    lines.insert(39, 'import com.neus.cards.business.' + entity_name.lower() + '.Colecao' + entity_name + ';')

    lines[len(lines) - 1] = new_content + ' \n'

    lines.append('}')

    open(path, 'w').write('\n'.join(lines))


def edit_cards_fachada_impl(entity_name):

    new_content = J2.get_template(TEMPLATE_CARDS_FACHADA_IMPL).render(entityName=entity_name)

    path = PROJECT_PATH + CARDS_FACHADA_IMPL

    lines = open(path, encoding=PROJECT_ENCODE).read().splitlines()

    lines.insert(26, 'import com.neus.cards.business.' + entity_name.lower() + '.Colecao' + entity_name + ';')

    lines[len(lines) - 1] = new_content + ' \n'

    lines.append('}')

    open(path, 'w').write('\n'.join(lines))


def edit_repositorio_colecoes(entity_name):

    new_content = J2.get_template(TEMPLATE_REPOSITORIO_COLECOES).render(entityName=entity_name)

    path = PROJECT_PATH + REPOSITORIO_COLECOES_PATH

    lines = open(path, encoding=PROJECT_ENCODE).read().splitlines()

    lines.insert(25, 'import com.neus.cards.business.' + entity_name.lower() + '.Colecao' + entity_name + ';')

    lines[len(lines) - 1] = new_content + ' \n'

    lines.append('}')

    open(path, 'w').write('\n'.join(lines))


if __name__ == '__main__':
    main()
