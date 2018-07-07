package com.neus.cards.data.{{nomeEntidade.lower()}}.{{nomeEntidade}};

import java.sql.ResultSet;
import java.sql.SQLException;

import com.neus.cards.business.{{nomeEntidade.lower()}}.{{nomeEntidade}};
import com.neus.cards.data.util.ComandoRepositorioAbstratoCardsJDBC;
import com.neus.cards.data.util.SetPreparedStatement;
import com.neus.util.chave.ObjetoChave;

public class ComandoRepositorio{{nomeEntidade}}JDBC extends ComandoRepositorioAbstratoCardsJDBC<{{nomeEntidade}}>{
	

	@Override
	protected void preencherPreparedStatement(SetPreparedStatement ps, {{nomeEntidade}} {{nomeEntidade[:1].lower() + nomeEntidade[1:]}}) throws SQLException {

{% for item in campos %}
        ps.set({{nomeEntidade[:1].lower() + nomeEntidade[1:]}}.get{{item.nome.title()}}());
{% endfor %}
	}


	@Override
	public void setObjeto(ObjetoChave obj, ResultSet rs) throws SQLException {
		
		{{nomeEntidade}} {{nomeEntidade[:1].lower() + nomeEntidade[1:]}} = ({{nomeEntidade}}) obj;

		{{nomeEntidade[:1].lower() + nomeEntidade[1:]}}.setCodigo(rs.getInt("ID{{nomeEntidade.upper()}}"));
{% for item in campos %}
		{{nomeEntidade[:1].lower() + nomeEntidade[1:]}}.set{{item.nome.title()}}(rs.get{{'Int' if item.tipo == 'Integer' else item.tipo}}("{{item.nome.upper()}}"));
{% endfor %}

	}

	@Override
	public ObjetoChave criarObjeto() {
		return new {{nomeEntidade}}();
	}

}