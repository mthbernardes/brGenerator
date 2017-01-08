import requests
from lxml import html

class personGen():
    def findToken(self,):
        r = requests.get('http://www.4devs.com.br/gerador_de_pessoas')
        return r.content.split('<script type="text/javascript">var token_calc = "')[1].split('"')[0]

    def generate(self,sex,age):
        person = dict()
        token = self.findToken()
        headers = {'Referer':'http://www.4devs.com.br/gerador_de_pessoas'}
        data = {'token':token,'acao':'gerar_pessoa','sexo':sex,'idade':age,'pontuacao':'S','cep_estado':'','cep_cidade':''}
        url = 'http://www.4devs.com.br/ferramentas_online.php'
        r = requests.post(url,data=data,headers=headers)
        tree = html.fromstring(r.content)
        person['nome'] = tree.xpath('//*[@id="nome"]/@value')[0]
        person['cpf'] = tree.xpath('//*[@id="cpf"]/@value')[0]
        person['rg'] = tree.xpath('//*[@id="rg"]/@value')[0]
        person['aniversario'] = tree.xpath('//*[@id="data_nasc"]/@value')[0]
        person['email'] = tree.xpath('//*[@id="email"]/@value')[0]
        person['cep'] = tree.xpath('//*[@id="cep"]/@value')[0]
        person['endereco'] = tree.xpath('//*[@id="cep"]/@value')[0]
        person['casa_numero'] = tree.xpath('//*[@id="numero"]/@value')[0]
        person['bairro'] = tree.xpath('//*[@id="bairro"]/@value')[0]
        person['cidade'] = tree.xpath('//*[@id="cidade"]/@value')[0]
        person['estado'] = tree.xpath('//*[@id="estado"]/@value')[0]
        person['telefone'] = tree.xpath('//*[@id="telefone_fixo"]/@value')[0]
        person['celular'] = tree.xpath('//*[@id="celular"]/@value')[0]
        return person
