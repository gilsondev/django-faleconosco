Templates Usados
================

A aplicação usa templates para gerar o formulário de contato, como também a mensagem de sucesso. 

Elas devem estar instaladas na pasta ``templates/contato`` do projeto, ou dentro da aplicação. Os templates usados são:


Template contato_form.html
-----------------

Esse template é usado para definir e gerar o formulário de contato do seu site. A partir dela que vai estar os seguintes campos:

* Nome;
* E-mail;
* Assunto;
* Mensagem.

Abaixo está o exemplo do formulário::
    
    {% extends "base.html" %}

    {% block corpo %}
        <div class="sixteen columns">
            <h3>Contato</h3>
            <p>
                Diga o que deseja aqui em baixo, que iremos ler com toda a atenção necessária.
            </p>

            <div class="sixteen columns">
                <form action="" method="post">
                    {% csrf_token %}
                    <fieldset>
                        <label for="id_nome">
                            {{ form.nome.label }} {{ form.nome }}
                            <div class="erro">{{ form.nome.errors }}</div>
                        </label>
                        <label for="id_email">
                            {{ form.email.label }} {{ form.email }}
                            <div class="erro">{{ form.email.errors }}</div>
                        </label>
                        <label for="id_assunto">
                            {{ form.assunto.label }} {{ form.assunto }}
                            <div class="erro">{{ form.assunto.errors }}</div>
                        </label>
                        <label for="id_mensagem">
                            {{ form.mensagem.label }} {{ form.mensagem }}
                            <div class="erro">{{ form.mensagem.errors }}</div>
                        </label>
                    </fieldset>
                    <input type="submit" value="Enviar" class="button">
                </form>
            </div>
        </div>
    {% endblock corpo %}

Template contato_success.html
-----------------------------

Esse template nada mais é do que uma página que contém a mensagem de que o email foi enviado com sucesso::

    {% extends "base.html" %}

    {% block corpo %}
        <div class="sixteen columns">
            <h3>Contato</h3>
            <p>
                E-mail enviado com sucesso! Dentro de instantes estaremos entrando em contato.
            </p>
            <p><a href="{% url homepage %}">Voltar</a></p>
        </div>
    {% endblock corpo %}