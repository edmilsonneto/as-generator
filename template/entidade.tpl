package com.neus.cards.business.{{nomeEntidade.lower()}}.{{nomeEntidade}};

@Entity
@Table(name = "T_{{nomeEntidade.upper()}}")
@SequenceGenerator(name = "gerador", sequenceName = "SEQ_{{nomeEntidade.upper()}}", allocationSize = 1)
@AttributeOverride(name = "codigo", column = @Column(name = "ID{{nomeEntidade.upper()}}"))
public class {{nomeEntidade}} extends ObjetoCancelavelImpl {

{% for item in campos %}
    private {{ item.tipo }} {{ item.nome }};
{% endfor %}

{% for item in campos %}
    public {{item.tipo}} get{{item.nome.title()}}() {
        return this.{{item.nome}};
    }

    public void set{{item.nome.title()}}({{item.tipo}} get{{item.nome}}) {
        this.{{item.nome}} = {{item.nome}};
    }
{% endfor %}
    
	
}
