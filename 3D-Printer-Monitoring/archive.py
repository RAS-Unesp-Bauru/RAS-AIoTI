import os

tEmails = '\nDigite os e-mails das pessoas que irão receber as mensagens \ne digite "stop" para finalizar:\n'
tMensagemS = '\nDigite a mensagem que será enviada ao iniciar a impressão e finalize digitando "stop":\n'
tMensagemF = '\nDigite a mensagem que será enviada ao finalizar a impressão e encerre digitando "stop":\n'
tAviso = '\nAVISO: Evite de pressionar a tecla "Enter" antes de digitar.\n'
tObs = 'Obs:\nA estrutura do texto será extamente como foi digitado, cuidado!\n'

aEmails = 'emails.txt'
aMi = 'mensagemI.txt'
aMf = 'mensagemF.txt'

a = os.path.isfile(aEmails)
b = os.path.isfile(aMi)
c = os.path.isfile(aMf)
pre = []

if a and b and c:
    print('Os arquivos com os e-mails e as mensagens já existem.\n')
    # while(1):
    #     edit = input('Deseja editar algum arquivo?[s/n] ').lower()

    #     if edit == 's':
    #         while (a or b or c) is False:
    #             print('\nEscolha um ou mais arquivos (separando eles com espaço) para ser editado:')
    #             print('\n1 --> E-mails\n2 --> Mensagem ao iniciar\n3 --> Mensagem ao finalizar\n')
    #             print('Exemplo: "1 3", será escolhido e-mails e mensagem ao finalizar')
    #             pergunta = input('Arquivos: ').split().sort()

    #             if len(pergunta) == 3 and '1' or '2' or '3' in pergunta:
    #                 for valor in pergunta:
    #                     if '1' in valor:
    #                         os.remove(aEmails)
                        
    #                     if '2' in valor:
    #                         os.remove(aEmails)
    #                         os.remove(aMi)

    #                     if '3' in valor:
    #                         os.remove(aMf)
    #                 break

    #             else:
    #                 print('AVISO: A resposta inserida não é inválida!')

    #     elif edit == 'n':
    #         break

    #     else:
    #         print('AVISO: Responda apenas com "s" ou "n" para sim ou não, respectivamente.')

else:
    print('Um ou todos dos arquivos necessário para que o programa funcione não existe.\nCrie-o agora:\n')
    
if a is False:
    i = ''
    aux = ''
    resposta = ''
    pre = []
    print('[Email]')
    while len(pre) == 0 or resposta == 'n':
        with open(aEmails,'w') as arq:
            print(tEmails)
    
            while(1):
                i = input()

                if i == '':
                    print(tAviso)
                
                elif i == 'stop':
                    aux += 'trash'
                    fim = aux.replace('\ntrash', '')
                    arq.write(fim)
                    arq.close()
                    break

                elif ' ' in i:
                    print('AVISO: E-mails não possuem "espaço" como caractere.\nDigite novamente e tome este cuidado!\n')
                
                elif '@' not in i:
                    print('AVISO: O último dado inserido não é um e-mail!\n')

                else:
                    aux += i + '\n'
                    pre.append(i)

            if len(pre) != 0:
                print("O(s) contato(s) salvo(s):")
                for count, listp in enumerate(pre, start=1):
                    print('{}) {}'.format(count,listp)) 
                
                while(1):
                    resposta = input('\nDeseja salvar esse(s) e-mail(s)? [s/n] ').lower()

                    if resposta == 's':
                        print('\nA mensagem foi salva com sucesso!\n')
                        break

                    elif resposta == 'n':
                        with open(aEmails,'r') as arquivo:
                            os.remove(aEmails)
                            pre = []
                        break

                    else:
                        print('AVISO: Responda apenas com "s" ou "n" para sim ou não, respectivamente.')

            else:
                print('AVISO: Nenhum email foi salvo.\n')
                i = ''
                pre = []
                aux = '' 
                os.remove(aEmails)
                continue

if b is False:
    j = ''
    aux = ''
    resposta = ''
    pre = []
    print('[Mensagem ao iniciar]')
    while len(pre) == 0 or resposta == 'n':
        with open(aMi,'w') as arq2:
            print(tMensagemS)
            print(tObs)

            while j != 'stop':
                j = input()
                
                if j == 'stop':
                    aux += 'trash'
                    fim = aux.replace('\ntrash', '')
                    arq2.write(fim)
                    arq2.close()
                    resposta = ''
                    break
                        
                else:
                    aux += j + '\n'
                    pre.append(j)

            if len(pre) != 0:
                print("\nA mensagem salva:")
                print(fim)
                
                while(1):
                    resposta = input('\nDeseja salvar essa mensagem? [s/n] ').lower()

                    if resposta == 's':
                        print('\nA mensagem foi salva com sucesso!\n')
                        break

                    elif resposta == 'n':
                        with open(aMi,'r') as arquivo:
                            os.remove(aMi)
                            pre = []
                        break
                    
                    else:
                        print('AVISO: Responda apenas com "s" ou "n" para sim ou não, respectivamente.')

            else:
                print('AVISO: Nenhuma mensagem foi salva.\n')
                j = ''
                pre = []
                aux = '' 
                os.remove(aMi)
                continue

if c is False:
    k = ''
    aux = ''
    resposta = ''
    pre = []
    print('[Mensagem ao finalizar]')
    while len(pre) == 0 or resposta == 'n':
        with open(aMf,'w') as arq3:
            print(tMensagemF)
            print(tObs)

            while k != 'stop':
                k = input()
                
                if k == 'stop':
                    aux += 'trash'
                    fim = aux.replace('\ntrash', '')
                    arq3.write(fim)
                    arq3.close()
                    resposta = ''
                    break
                        
                else:
                    aux += k + '\n'
                    pre.append(k)

            if len(pre) != 0:
                print("\nA mensagem salva:")
                print(aux)
                
                while (1):
                    resposta = input('\nDeseja salvar essa mensagem? [s/n] ').lower()

                    if resposta == 's':
                        print('\nA mensagem foi salva com sucesso!\n')
                        break

                    elif resposta == 'n':
                        with open(aMf,'r') as arquivo:
                            os.remove(aMf)
                            pre = []
                        break
                    
                    else:
                        print('AVISO: Responda apenas com "s" ou "n" para sim ou não, respectivamente.')

            else:
                print('AVISO: Nenhuma mensagem foi salva.\n')
                i = ''
                pre = []
                aux = '' 
                os.remove(aMf)
                continue