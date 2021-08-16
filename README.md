# brGenerator
Gera informações pessoais de um brasileiro, util para automação de cadastros.

## Instalação
```bash
$ pip install brGenerator
```

## Uso
```python
>>> from brGenerator.personGen import personGen
>>> personGen().generate('H',23) # H para gerar homem e M para gerar mulher, o segundo valor é a idade.
{'nome': '', 'bairro': '', 'cidade': '', 'cpf': '', 'rg': '', 'estado': '', 'telefone': '', 'cep': '', 'endereco': '', 'aniversario': '', 'casa_numero': '', 'email': '', 'celular': ''}
```

## DISCLAIMER

Essa biblioteca é apenas um wrapper do site http://www.4devs.com.br/gerador_de_pessoas
