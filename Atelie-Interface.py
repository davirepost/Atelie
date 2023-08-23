
import PySimpleGUI as sg

sg.theme('LightGreen4')

layout=[
    [sg.Text('BEM VINDO(A)!', justification= 'center')],
    [sg.Column([[sg.Button ('LOGIN', size=(30,1))]],
        [sg.Button('CADASTRAR NOVO FUNCIONÁRIO', size= (30,1))],
        [sg.Button ('FECHAR', size=(30,1))],
    )],
    
]

window= sg.Window ('Atelie', layout, size=(600,400), font="Arial")

while True:

    event, values= window.read()
    if event == sg.WI_CLOSED or event == 'FECHAR':
        break 
   # if event == 'LOGIN':
    #    layout=[
     #       [sg.Text ('Login', size= (15,2), font=40)],
      #      [sg.Text('Nome', size=(15,2), font=40)], sg.InputText(Key='nome', font=16),
       #     [sg.Text('Senha', size=(15,2), font=40)], sg.InputText(Key='senha', password_char='*', font=16),
        #    [sg.Button('Entrar'), sg.Button('Cancelar')]

        #]
    if event == "CADASTRAR NOVO FUNCIONÁRIO":
        valores=[]
        campos=["Nome", "Idade", "E-mail", "Senha"]
        for i in range (4):
            preenchimento= sg.popup_get_text (f'{campos[i]} do(a) novo(a) funcionário(a)', title= 'Novo Funcionário')
            if preenchimento != None:
                valores.append(preenchimento)
            else:
                break  


        
            