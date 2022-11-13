
def Func_Questoes(q2,q3,q4,q5,q6,q7,q8,q9,q10,q1):

    global questoes
    questoes = [q2,q3,q4,q5,q6,q7,q8,q9,q10,q1]

def Func_Alternativas(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10):
    global alternativas
    alternativas = [a2, a3, a4, a5, a6, a7, a8, a9, a10, a1]

def Func_Explicacao(e1,e2,e3,e4,e5,e6,e7,e8,e9,e10):
    global explicacao

    explicacao = [e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,]

def Func_Gabarito(g1,g2,g3,g4,g5,g6,g7,g8,g9,g10):

    global gabarito
    gabarito = [g1,g2,g3,g4,g5,g6,g7,g8,g9,g10]

def Func_Quiz():
    global cont
    cont = -1
    global respostas
    respostas = []
    global pontos
    pontos = 0
     
    for r in questoes:
        print (questoes[cont])
        print (alternativas[cont])
        
        r = (input("Digite sua resposta: ")) 
        
#-----------------------------------------Validador------------------------------------------------------------------------#
        if r == "A" or r == "a":
                        r = "A"
        elif r == "B" or r == "b":
                        r = "B"
        elif r == "C" or r == "c":
                        r = "C"
        elif r == "D" or r == "d":
                        r = "D"
        elif r == "E" or r == "e":
                        r = "E"               
        else:
            while (r!="A") or (r!="a") or (r!="B") or (r!="b") or (r!="C") or (r!="c") or (r!="D") or (r!="d") or (r!="E") or (r!="e"):
                r = (input("Mensagem inválida, digite sua resposta novamente: "))
                if (r=="A") or (r=="a") or (r=="B") or (r=="b") or (r=="C") or (r=="c") or (r=="D") or (r=="d") or (r=="E") or (r=="e"):
                                       
                    if r == "A" or r == "a":
                        r = "A"
                    elif r == "B" or r == "b":
                        r = "B"
                    elif r == "C" or r == "c":
                        r = "C"
                    elif r == "D" or r == "d":
                        r = "D"
                    elif r == "E" or r == "e":
                        r = "E" 
                
                    break          
#-----------------------------------------Acaba Validador---------------------------------------------------#
        
        
        cont = cont + 1
        respostas.append(r)
        
        if respostas[cont] == gabarito[cont]:
            print("\n Parabéns, resposta Correta \n")
            pontos = pontos + 1
            
        else:
            
            print(explicacao[cont])
            
          
def Func_Msg_Final(final1,final2,final3,mensagem1,mensagem2,mensagem3,mensagem4,mensagem5):
    print (final1, gabarito)
    print (final2, respostas)
    print (final3, pontos)
    
    if pontos >= 0 and pontos <= 3:
        print (mensagem1)
    if pontos >= 4 and pontos <= 5:
        print (mensagem2)
    if pontos >= 6 and pontos <= 8:
        print (mensagem3)
    if pontos == 9:
        print (mensagem4) 
    if pontos == 10:
        print (mensagem5)   


def main():

    Func_Questoes(
        "2. Em que ano aconteceu a primeira Copa do Mundo?",
        "3. Quem foi o primeiro vencedor da copa do mundo?",
        "4. Quem é o maior artilheiro das copas?",
        "5. Quantas vezes o Brasil foi campeão?",
        "6. Em quais anos o Brasil foi o país sede?",
        "7. Quantas vezes o Brasil foi finalista da Copa do Mundo?",
        "8. Quem é o jogador com mais partidas pela Seleção Brasileira?",
        "9. Qual país será a Copa do Mundo de 2022?",
        "10. Quais países serão sede da Copa de 2026?",
        "1. Qual foi o primeiro país sede da Copa?"
    )
    
    Func_Alternativas(
        " A - Brasil \n B - Estados Unidos \n C - Uruguai \n D - Inglaterra \n E - França",
        " A - 1922 \n B - 1938 \n C - 1926 \n D - 1930 \n E - 1934",
        " A - Uruguai \n B - Brasil \n C - França \n D - Itália \n E - Inglaterra",
        " A - Pelé - Brasil \n B - Gerd Müller - Alemanha  \n C - Ronaldo Fenômeno - Brasil \n D - Just Fontaine - França \n E - Miroslav Klose - Alemanha.",
        " A - 4 \n B - 3 \n C - 5 \n D - 2 \n E - 6",
        " A - 1950 e 2014 \n B - 1962 e 2010 \n C - 1954 e 2002 \n D - 1958 e 2006 \n E - 1946 e 2018",
        " A - 5 \n B - 3 \n C - 7 \n D - 4 \n E - 6",
        " A - Ronaldo Fenômeno \n B - Cafu \n C - Neymar \n D - Pelé \n E - Roberto Carlos",
        " A - Abu Dhabi \n B - França \n C - Estados Unidos \n D - Catar \n E - Dubai",
        " A - Catar, Dubai e Abu Dhabi \n B - Canadá, Estados Unidos e México \n C - Inglaterra, Escócia e Suíça \n D - Brasil, Argentina e Uruguai \n E - Japão, China e Coréia do Sul"

        )
    
    Func_Explicacao(
        " \n A resposta correta é C - Uruguai. A primeira Copa do Mundo foi no Uruguai. Até a definição da data e local, encontros foram realizados para que uma competição mundial de futebol fosse concretizada. \n",
        "\n A resposta correta é D - 1930. Aconteceu no dia 13 de julho de 1930. \n",
        "\n A resposta correta é A - Uruguai. A seleção uruguaia foi a primeira campeã da Copa do Mundo, após a vitória contra a Argentina.  \n",
        "\n A resposta correta é E - Miroslav Klose - Alemanha, com incríveis 16 gols na competição. Ronaldo com 15, Muller com 14, Fontaine com 13 e Pelé com 12 gols. \n",
        "\n A resposta correta é C - 5. Presente em todas as edições do Mundial desde a sua criação (1930), a Seleção Brasileira levantou o troféu mais cobiçado do futebol em 1958, 1962, 1970 e 2002. \n",
        "\n A resposta correta é A - 1950 e 2014. Sede de duas Copas do Mundo (1950 e 2014), o Brasil é a única seleção a participar de todas as edições do evento e a maior vencedora da competição, com cinco títulos, todos fora de casa. \n",
        "\n A resposta correta é C - 7. O Brasil conqusitou a taça nos anos 1958, 1962, 1970 e 2002. Porém, o Brasil também registrou dois vice-campeonatos (em 1950, perdendo para o Uruguai e, em 1998, perdendo para a França). \n",
        "\n A resposta correta é B - Cafu. Bicampeão da Copa do Mundo, Cafu é o jogador que mais vezes atuou pela seleção brasileira, com 150 jogos. Além das duas copas, Cafu conquistou duas vezes a Copa América e uma vez a Copa das Confederações. Logo atrás, Roberto Carlos com 132, Daniel Alves com 124, Neymar com 121 e Pelé com 113 jogos. \n",
        "\n A resposta correta é D - Catar. A Copa do Mundo de 2022 tem início em 20 de novembro e será sediada no Catar. É a primeira vez que um país do Oriente Médio recebe a competição mais importante do futebol. \n",
        "\n A resposta correta é B - Canadá, Estados Unidos e México. Será a primeira vez que a sede não será em só um país, apesar da distância entre os países, a Copa de 2026 terá seleções fixas em sedes para evitar longos deslocamentos. \n"
    )
    
    Func_Gabarito("C","D","A","E","C","A","C","B","D","B")

    Func_Quiz()

    Func_Msg_Final(
        "Gabarito: ", "Respostas: ", "Pontos: ", "Pontuação baixa, tente novamente" ,
        "Quase lá, tente novamente", "Isso aí, quase gabaritando", "Excelente!!" , "Gabaritou!!!!!!!!"
     )
    
main()





