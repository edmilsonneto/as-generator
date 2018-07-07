<?xml version="1.0"?>

<!DOCTYPE colecao [
	<!ELEMENT colecao (nomeClasseColecao, repositorio)>
	<!ELEMENT nomeClasseColecao (#PCDATA)>
	<!ELEMENT repositorio (comandoRepositorio*)>
	<!ELEMENT comandoRepositorio (nomeClasseComandoRepositorio, nomeSequencia, dependencia*, tabela)>
	<!ELEMENT nomeClasseComandoRepositorio (#PCDATA)>
	<!ELEMENT nomeSequencia (#PCDATA)>
	<!ELEMENT dependencia (#PCDATA)>
	<!ELEMENT tabela (nomeTabela, aliasTabela, coluna*, chavePrimaria)>
	<!ELEMENT nomeTabela (#PCDATA)>
	<!ELEMENT aliasTabela (#PCDATA)>
	<!ELEMENT coluna (nomeColuna, tipoColuna, nulo)>
	<!ELEMENT nomeColuna (#PCDATA)>
	<!ELEMENT tipoColuna (#PCDATA)>
	<!ELEMENT nulo (#PCDATA)>
	<!ELEMENT chavePrimaria (coluna*)>
]>

<colecao>
    <nomeClasseColecao>
        com.neus.cards.business.{{nomeEntidade.lower()}}.Colecao{{nomeEntidade}}
    </nomeClasseColecao>
    <repositorio>
        <comandoRepositorio>
            <nomeClasseComandoRepositorio>
                com.neus.cards.data.{{nomeEntidade.lower()}}.ComandoRepositorio{{nomeEntidade}}JDBC
            </nomeClasseComandoRepositorio>
            <nomeSequencia>SEQ_{{nomeEntidade.upper()}}</nomeSequencia>
            <tabela>
                <nomeTabela>T_{{nomeEntidade.upper()}}</nomeTabela>
                <aliasTabela>T</aliasTabela>
               
                <coluna>
                    <nomeColuna>ID{{nomeEntidade.upper()}}</nomeColuna>
                    <tipoColuna>INTEGER</tipoColuna>
                    <nulo>false</nulo>
                </coluna>

{% for item in campos %}
                <coluna>
                    <nomeColuna>{{item.nome.upper()}}</nomeColuna>
                    <tipoColuna>{{item.tipo.upper()}}</tipoColuna>
                    <nulo>{{item.nullable}}</nulo>
                </coluna>
{% endfor %}

                <chavePrimaria>
                    <coluna>
                        <nomeColuna>ID{{nomeEntidade.upper()}}</nomeColuna>
                        <tipoColuna>INTEGER</tipoColuna>
                        <nulo>false</nulo>
                    </coluna>
                </chavePrimaria>
            </tabela>
        </comandoRepositorio>
    </repositorio>
</colecao>
