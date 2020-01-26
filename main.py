import kivy
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from random import randint

kvfile = Builder.load_file('style.kv')

print('hello world')

class Main(Screen):     
    
    def frase_trolage(self):
        frase_num = randint(1,4)
        if frase_num == 1:
            frase_tela = 'fingi ser homem bomba no transito'             

        if frase_num == 2:
            frase_tela = 'fingi pegar corona virus e minha mãe me bateu'  

        if frase_num == 3:
            frase_tela = 'trollei minha namorada no free fire falando que tinha acabado tudo'

        if frase_num == 4:
            frase_tela = 'trollei um policial com açúcar no bolso (fui preso?)'

        frase_tela = frase_tela.upper()
        self.manager.get_screen('frase_gerada').ids.lbl_frase.text = frase_tela
        self.manager.get_screen('frase_gerada').ids.gerar_outra.text = 'Mais Frases de Trolage'
        self.manager.current = 'frase_gerada'              

    def frase_horas(self):
        frase_num = randint(1,4)
        if frase_num == 1:
            frase_tela = '24 Horas algemado com o meu cachorro'             

        if frase_num == 2:
            frase_tela = '24 Horas assistindo VIROS'  

        if frase_num == 3:
            frase_tela = 'Passei 24 Horas tomando sopa de morcego (PEGUEI CORONA VÍRUS?)'

        if frase_num == 4:
            frase_tela = 'Sobrevivendo a um dia com R$ 28 MIL (SOBREVIVI???)'

        frase_tela = frase_tela.upper()
        self.manager.get_screen('frase_gerada').ids.lbl_frase.text = frase_tela
        self.manager.get_screen('frase_gerada').ids.gerar_outra.text = 'Mais Frases de 24 Horas'
        self.manager.current = 'frase_gerada'                

    def frase_react(self):
        frase_num = randint(1,4)          

        if frase_num == 1:
            frase_tela = 'Reagindo as minhas inscritas dançando funk (12 ANOS!!)'     

        if frase_num == 2:
            frase_tela = 'Minha mãe reagindo a funks pesados (Apanhei??)'                             

        if frase_num == 3:
            frase_tela = 'Reagindo a gostosas dançando funk (+18)'

        if frase_num == 4:
            frase_tela = 'Reagindo a entrevista do Toninho do Diabo'

        frase_tela = frase_tela.upper()
        self.manager.get_screen('frase_gerada').ids.lbl_frase.text = frase_tela
        self.manager.get_screen('frase_gerada').ids.gerar_outra.text = 'Mais Frases de React'
        self.manager.current = 'frase_gerada'  

    def frase_desafio(self):
        frase_num = randint(1,4)

        if frase_num == 1:
            frase_tela = 'Caguei na pia e olha no que deu'

        if frase_num == 2:
            frase_tela = 'Gastei R$6000 em materiais escolares'     

        if frase_num == 3:
            frase_tela = 'A cada kill uma peça de roupa a menos (FREE FIRE)'

        if frase_num == 4:
            frase_tela = 'Tentei não chorar com a tacada do Baianinho de Mauá (CHOREI??)'               

        frase_tela = frase_tela.upper()
        self.manager.get_screen('frase_gerada').ids.lbl_frase.text = frase_tela
        self.manager.get_screen('frase_gerada').ids.gerar_outra.text = 'Mais Frases de Desafio'
        self.manager.current = 'frase_gerada' 
        
class frase_gerada(Screen):
        pass     

sm = ScreenManager()
sm.add_widget(Main(name='main'))
sm.add_widget(frase_gerada(name='frase_gerada'))

class app(App):

    def build(self):
        return sm

app().run()        
