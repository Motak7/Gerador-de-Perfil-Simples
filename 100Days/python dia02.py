perfils = []

while True:
    try:
        print("\n--- Novo Perfil ---")
        nome = input("Nome: ").strip().title()

        idade = int(input("Idade: ").strip())
        if (0 < idade > 100):
            print("Idade deve ser entre 1 a 149!")
            continue
        
        altura = float(input("Altura (m): ").replace(',', '.'))
        if not (0.5 < altura < 2.5):
            print("Altura deve ser entre 0.5 e 2.5 metros!")
            continue
            
        estudando_input = input("Está estudando programação? (s/n): ").strip().lower()
        if estudando_input == 's':
          estudando_programacao_bool = True 
        elif estudando_input == 'n':
          estudando_programacao_bool = False
        else:
          print("Resposta inválida! Digite 's' para sim ou 'n' para não.")
          continue

        perfils.append({"nome": nome, "idade": idade, "altura": altura, "estudando_programacao": estudando_programacao_bool})

        continuar = input("Deseja adicionar outro perfil? (s/n): ").strip().lower()
        if continuar != 's':
          break

    except ValueError:
        print("Valor inválido! Digite números corretamente.")
        continue
print("\n--- Resultados ---")
print(f"{'Nome':<15} | {'Idade':^5} | {'Altura':^6} | {'Estudando?':^12}")
for p in perfils:
    estudando_texto = "Sim" if p['estudando_programacao'] else "Não"
    print(f"{p['nome']:<15} | {p['idade']:^5} | {p['altura']:>6.2f}m | {estudando_texto:^12}")
input("\nPressione Enter para sair...")
        

          
