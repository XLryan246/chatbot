import openai

openai.api_key = "SUA API KEY" 

def main():
    def gerar_texto(prompt):
        completions = openai.Completion.create( #gera o texto
            engine = "text-davinci-002",
            prompt = prompt,
            max_tokens = 2048,
            n = 1,
            stop = None,
            temperature = 0.5 #nivel de criatividade do texto
        )
        message = completions.choices[0].text #retorna o texto gerado
        return message.strip() #remove espaços em branco

    prompt = input("Faça sua pergunta: ")
    print (gerar_texto(prompt)) 

    opcao = int(input("Deseja fazer uma nova pergunta? \n 1 - SIM \n 2 - NAO \n"))
    if opcao == 1:
        main()
    else:
        print ("saindo...")
        exit()
    
if __name__ == '__main__':
    main()