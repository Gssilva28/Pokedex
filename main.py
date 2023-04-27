from tkinter import *
from tkinter import ttk

# Importando Pillow

from PIL import Image, ImageTk

# Importando dados

from dados import *
############################################ Cores #####################################
co0 = "#444466" # Preto
co1 = "#feffff" # Branco
co2 = "#6f9fbd" # Azul
co3 = "#38576b" # Valor
co4 = "#403d3d" # Letra
co5 = "#ef5350" # Vermelho
co6 = "#FFFF00" # Amarelo

# Criação de janela
janela = Tk()
janela.title('')
janela.geometry('550x510')
janela.configure(bg=co1)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=272)

style = ttk.Style(janela)
style.theme_use("clam")

# Criação do frame
frame_pokemon = Frame(janela, bg=co1, width=550, height=290, relief='flat')
frame_pokemon.grid(row=1, column=0)

def trocar_pokemon(i):
    global imagem_poke, pok_imagem

    # Trocando cor do fundo do frame
    frame_pokemon['bg'] = pokemon[i]['Categoria'][3]

    # Pokemon tipo

    pok_nome['text'] = i
    pok_nome['bg'] = pokemon[i]['Categoria'][3]
    pok_cate['text'] = pokemon[i]['Categoria'][1]
    pok_cate['bg'] = pokemon[i]['Categoria'][3]
    pok_id['text'] = pokemon[i]['Categoria'][0]
    pok_id['bg'] = pokemon[i]['Categoria'][3]

    # Pokemon imagem
    imagem_poke = Image.open(pokemon[i]['Categoria'][2])
    imagem_poke = imagem_poke.resize((238, 238))
    imagem_poke = ImageTk.PhotoImage(imagem_poke)

    pok_imagem = Label(frame_pokemon, image=imagem_poke, relief='flat', bg=pokemon[i]['Categoria'][3], fg=co1)
    pok_imagem.place(x=60, y=50)


    # Pokemon status
    pok_hp['text'] = pokemon[i]['Status'][0]
    pok_ataq['text'] = pokemon[i]['Status'][1]
    pok_def['text'] = pokemon[i]['Status'][2]
    pok_vel['text'] = pokemon[i]['Status'][3]
    pok_tot['text'] = pokemon[i]['Status'][4]

    # Pokemon habilidades
    pok_hab_1['text'] = pokemon[i]['Habilidades'][0]
    pok_hab_2['text'] = pokemon[i]['Habilidades'][1]



# Nome
pok_nome = Label(frame_pokemon, text='', relief='flat', anchor=CENTER, font=('Fixedsys 20'), fg=co1)
pok_nome.place(x=12, y=15)

# Categoria
pok_cate = Label(frame_pokemon, text='', relief='flat', anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co1)
pok_cate.place(x=12, y=50)

# Identificação
pok_id = Label(frame_pokemon, text='', relief='flat', anchor=CENTER, font=('Fixedsys 10'), bg=co1, fg=co1)
pok_id.place(x=12, y=75)


# Status
pok_status = Label(janela, text='Status', relief='flat', anchor=CENTER, font=('Vernana 20'), bg=co1, fg=co0)
pok_status.place(x=15, y=310)

# HP
pok_hp = Label(janela, text='HP: 300', relief='flat', anchor=CENTER, font=('Vernana 10'), bg=co1, fg=co4)
pok_hp.place(x=15, y=360)

# Ataque
pok_ataq = Label(janela, text='Ataque: 600', relief='flat', anchor=CENTER, font=('Vernana 10'), bg=co1, fg=co4)
pok_ataq.place(x=15, y=385)

# Defesa
pok_def = Label(janela, text='Defesa: 500', relief='flat', anchor=CENTER, font=('Vernana 10'), bg=co1, fg=co4)
pok_def.place(x=15, y=410)

# Velocidade
pok_vel = Label(janela, text='Velocidade: 300', relief='flat', anchor=CENTER, font=('Vernana 10'), bg=co1, fg=co4)
pok_vel.place(x=15, y=435)

# Total
pok_tot = Label(janela, text='Total: 1.700', relief='flat', anchor=CENTER, font=('Vernana 10'), bg=co1, fg=co4)
pok_tot.place(x=15, y=460)

# Habilidades
pok_hab = Label(janela, text='Habilidades', relief='flat', anchor=CENTER, font=('Vernana 20'), bg=co1, fg=co4)
pok_hab.place(x=180, y=310)

# Choque do trovao
pok_hab_1 = Label(janela, text='Choque do trovão', relief='flat', anchor=CENTER, font=('Vernana 10'), bg=co1, fg=co4)
pok_hab_1.place(x=195, y=360)

# Cabeçada
pok_hab_2 = Label(janela, text='Cabeçada', relief='flat', anchor=CENTER, font=('Vernana 10'), bg=co1, fg=co4)
pok_hab_2.place(x=195, y=385)

# Criação de botões

# Imagem do pokemon 1
imagem_poke_1 = Image.open('img\cabeca-pikachu.png')
imagem_poke_1 = imagem_poke_1.resize((40, 40))
imagem_poke_1 = ImageTk.PhotoImage(imagem_poke_1)

botao_1= Button(janela, command=lambda:trocar_pokemon('Pikatchu'), image=imagem_poke_1, text='Pikatchu', width=150,  relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=co1, fg=co0)
botao_1.place(x=375, y=10)

# Imagem do pokemon 2
imagem_poke_2 = Image.open('img\cabeca-bulbasaur.png')
imagem_poke_2 = imagem_poke_2.resize((40, 40))
imagem_poke_2 = ImageTk.PhotoImage(imagem_poke_2)

botao_2= Button(janela, command=lambda:trocar_pokemon('Bulbasaur'), image=imagem_poke_2, text='Bulbasaur', width=150,  relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=co1, fg=co0)
botao_2.place(x=375, y=65)

# Imagem do pokemon 3
imagem_poke_3 = Image.open('img\cabeca-charmander.png')
imagem_poke_3 = imagem_poke_3.resize((40, 40))
imagem_poke_3 = ImageTk.PhotoImage(imagem_poke_3)

botao_3= Button(janela, command=lambda:trocar_pokemon('Charmander'), image=imagem_poke_3, text='Charmander', width=150,  relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=co1, fg=co0)
botao_3.place(x=375, y=120)

# Imagem do pokemon 4
imagem_poke_4 = Image.open('img\cabeca-gyarados.png')
imagem_poke_4 = imagem_poke_4.resize((40, 40))
imagem_poke_4 = ImageTk.PhotoImage(imagem_poke_4)

botao_4= Button(janela, command=lambda:trocar_pokemon('Gyarados'), image=imagem_poke_4, text='Gyarados', width=150,  relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=co1, fg=co0)
botao_4.place(x=375, y=175)

# Imagem do pokemon 5
imagem_poke_5 = Image.open('img\cabeca-gengar.png')
imagem_poke_5 = imagem_poke_5.resize((40, 40))
imagem_poke_5 = ImageTk.PhotoImage(imagem_poke_5)

botao_5= Button(janela, command=lambda:trocar_pokemon('Gengar'), image=imagem_poke_5, text='Gengar', width=150,  relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=co1, fg=co0)
botao_5.place(x=375, y=230)

# Imagem do pokemon 6
imagem_poke_6 = Image.open('img\cabeca-dragonite.png')
imagem_poke_6 = imagem_poke_6.resize((40, 40))
imagem_poke_6 = ImageTk.PhotoImage(imagem_poke_6)

botao_6= Button(janela, command=lambda:trocar_pokemon('Dragonite'), image=imagem_poke_6, text='Dragonite', width=150,  relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=co1, fg=co0)
botao_6.place(x=375, y=285)


trocar_pokemon('Pikatchu')


janela.mainloop()