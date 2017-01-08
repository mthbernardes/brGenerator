# brGenerator
Gera informações pessoais de um brasileiro, util para automação de cadastros.

#Install
pip install brGenerator

#Usage
<pre>
>>> from brGenerator.personGen import personGen
>>> personGen().generate('H',23)
>>> from brGenerator.personGen import personGen
>>> personGen().generate('H',23)
{'nome': '', 'bairro': '', 'cidade': '', 'cpf': '', 'rg': '', 'estado': '', 'telefone': '', 'cep': '', 'endereco': '', 'aniversario': '', 'casa_numero': '', 'email': '', 'celular': ''}
</pre>

#DISCLAIMER
<pre>
Essa biblioteca é apenas um wrapper do site http://www.4devs.com.br/gerador_de_pessoas
</pre>
