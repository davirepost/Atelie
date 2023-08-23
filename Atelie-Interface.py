
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

 def atualizar():
        if event == "ATUALIZAR INFORMAÇÃO DE FUNCIONÁRIO":
            nome= sg.popup_get_text ('Digite o nome do funcionário')
            if nome in funcionario:

                layout= [
                    [sg.Text('Atualizar informações de funcionário')],
                    [sg.Text(f'Nome: {nome}')],
                    [sg.Checkbox('Atualizar Nome', Keys='Nome')],
                    [sg.Checkbox('Atualizar E-mail', Keys='E-mail')],
                    [sg.Checkbox('Atualizar Senha', Keys='Senha')],
                    [sg.Button ('Atualizar', sg.Button('Cancelar'))]

                ]
                update_window= sg.Window('Atualizar dados do(a) funcionário(a)', layout)

                while True:
                    update_event, update_values= update_window.read()
                    if update_event== sg.WIN_CLOSED or update_event == 'Cancelar':
                        break
                    if update_event== 'Atualizar':
                        if update_values['Nome']:
                            novo_nome= sg.popup_get_text(f'Digite o novo nome {nome}')
                            funcionario[novo_nome]=funcionario.pop(nome)
                            nome= novo_nome
                        if update_values['E-mail']:
                            email= sg.popup_get_text(f'Digite o novo e-mail')
                            funcionario[nome]['E-mail']= email
                        if update_values['Senha']:
                            senha=sg.popup_get_text(f'Digite a nova senha')
                            funcionario[nome]['Senha']= senha
                        sg.popup(f'As informações do(a) funcionário(a) {nome} foram atualizados!')
                        update_window.Close()
                        break
                    else:
                        sg.popup(f'O Funcionário com o nome {nome} não foi encontrada')






        
            


        
            
