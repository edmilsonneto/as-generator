package com.neus.cards.business.{{tableName.lower()[2:]}};

@Entity
@Table(name = "{{tableName}}")
@SequenceGenerator(name = "gerador", sequenceName = "{{sequenceName}}", allocationSize = 1)
@AttributeOverride(name = "codigo", column = @Column(name = "ID{{tableName[2:]}}"))
public class MigracaoPrePago extends ObjetoCancelavelImpl {

    {% for item in campos %}
    private {{ item.tipo }} {{ item.nome }};
    {% endfor %}
	
}
