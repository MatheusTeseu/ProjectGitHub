from time import sleep


class Empregado:
    numero_total_empregados = 0

    def __init__(self, nome_completo, email, matricula_funcional, salario):
        self.numero_empregado = 0
        self.nome_completo = nome_completo
        self.email = email
        self.matricula_funcional = matricula_funcional
        self.salario = salario
        self.aumento_salario = 0
        self.linguagens_programacao = ''
        self.litros_cafe = 0
        self.projeto_envolvido = ['Automação de Bot de uma empresa', 'software de uma casa']
        self.time_supervisao = ['pingadon', 'fortiton', 'herastor']

    def iniciar_jornada(self, nome_completo):
        Empregado.numero_total_empregados += 1
        self.nome_completo = nome_completo
        print(f'O {nome_completo} iniciou a Jornada')

    def finalizar_jornada(self, nome_comleto):
        self.nome_completo = nome_comleto
        print(f'O {nome_comleto} Finalizou a Jornada')

    def receber_aumento(self, anos_empresa, nivel_de_contribuicao, salario):
        raise NotImplementedError
        # Deve ser Abstrato (os usuario não precisa saber das informações desse atribuito dessa classe)


class Desenvolvedor(Empregado):
    porcentagem_aumento = 10.0

    def __init__(self, nome_completo, email, matricula_funcional, salario_desenvolvedor):
        super(Desenvolvedor, self).__init__(nome_completo, email, matricula_funcional, salario_desenvolvedor)
        print(f'O Desenvolvedor: {nome_completo} no Email: {email} '
              f'com a Matricula: {matricula_funcional} foi Contratado !')

    def receber_aumento(self, anos_empresa, nivel_de_contribuicao, salario):
        self.aumento_salario = (anos_empresa + nivel_de_contribuicao + salario) * \
                               Desenvolvedor.porcentagem_aumento / 100
        print(f'O Aumento do Salário do Desenvolvedor: {self.nome_completo} '
              f'terá um Aumento de R${self.aumento_salario:.2f}')

    def adicionar_linguagem(self, linguagens_programacao):
        self.linguagens_programacao = linguagens_programacao
        print(f'O Progrmador sabe a Linguagem de Programação: {linguagens_programacao}')

    def beber_cafe(self, litros_cafe):
        """
        -> Método para verificar se o Programdor Bebeu Muito café ou Não e ve se ele está com bornout ou não
        :param litros_cafe: Litros de Café que o Programador bebeu
        :return: Não tem Retorno
        """
        self.litros_cafe = litros_cafe
        if litros_cafe >= 1201:
            print(f'A Quantidade de Café que você tomo foi de {litros_cafe}ml\nPuts!  O Dev está com Burnout !')
        elif 500 < litros_cafe <= 1200:
            print(f'A Quantidade de Café que você tomo foi de {litros_cafe}ml')
            print('Aquele Café para ficar Acordado, mas Cuidado para não ficar com Burnout !')
        elif litros_cafe < 500:
            print(f'A Quantidade de Café que você tomo foi de {litros_cafe}ml')
            print('Você Toma Café mesmo ? vc Gosta de café mesmo ? Cuidado para não dormi em, Kkk')
        print('--' * 52)


class GerenteProjeto(Empregado):
    porcentagem_aumento = 20.0

    def __init__(self, time_supervisao, projeto_envolvidos, salario):
        super(GerenteProjeto, self).__init__(self, time_supervisao, projeto_envolvidos, salario)
        print(f'O Gerente tem um time com os integrantes: {time_supervisao}, Já Desenvolveu os seguintes projetos: '
              f'\n{projeto_envolvidos} e o Gerente está com um salario de R$5000')

    def receber_aumento(self, anos_empresa, nivel_de_contribuicao, salario):
        self.aumento_salario = (anos_empresa + nivel_de_contribuicao + salario) * \
                               GerenteProjeto.porcentagem_aumento / 100
        print(f'O Aumento do Salário do Gerente: {self.nome_completo} '
              f'terá um Aumento de R${self.aumento_salario:.2f}')
        # deve usar o atributo de classe porcentagem_aumento para calcular o aumento do dev

    def adicionar_desenvolvedor(self, time_supervisao):
        print(f'O time do Gerente está com os Seguintes Desenvolvedores: {self.time_supervisao}')
        self.time_supervisao.append(time_supervisao)
        print(f'{time_supervisao} Foi Adicionado no time')
        print(f'Agora o Time do Gerente tem os seguitens Desenvolvedores: {self.time_supervisao}')

    def remover_desenvolvedor(self, time_supervisao):
        self.time_supervisao.remove(time_supervisao)
        print(f'O Desenvolvedor {time_supervisao} foi Removido do Time do Gerente !')
        print(f'Agora o time do Gerente está com os Seguintes Desenvolvedores: {self.time_supervisao}')
        print('--' * 52)

    def participar_projeto(self, projeto_envolvidos):
        print(f'Os Projetos que o Gerente está envolvido é: {self.projeto_envolvido}')
        self.projeto_envolvido.append(projeto_envolvidos)
        print(f'{projeto_envolvidos} foi Adicionado nos Projetos que o Gerente está envolvido !')
        print(f'Agora os Projetos que o Gerente está envolvido são: {self.projeto_envolvido}')

    def sair_projeto(self, projetos_envolvidos):
        self.projeto_envolvido.remove(projetos_envolvidos)
        print(f'O Projeto {projetos_envolvidos} do Gerente foi Removido !')
        print(f'Agora os Projetos que o Gerente está envoldio são: {self.projeto_envolvido}')
# ----------------------------------------------------------------------------------------------------------------


rolf = Desenvolvedor('Rolf Borger', email='pigamonhagaba@gmail.com', matricula_funcional=45823669,
                     salario_desenvolvedor=3000)
rolf.iniciar_jornada('Rolf Borger')
rolf.finalizar_jornada('Rolf Borger')
rolf.receber_aumento(3, 4, 3000)
rolf.beber_cafe(1300)
sleep(3)
aristoteles = GerenteProjeto(time_supervisao=['pingadon', 'fortiton', 'herastor'], salario=5000,
                             projeto_envolvidos=['software de uma casa', 'Automação de Bot de uma empresa'])
aristoteles.adicionar_desenvolvedor('Rostifrut')
aristoteles.remover_desenvolvedor('pingadon')
aristoteles.participar_projeto('Automatização da empresa X')
aristoteles.sair_projeto('Automatização da empresa X')