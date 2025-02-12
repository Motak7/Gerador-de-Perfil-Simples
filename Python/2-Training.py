# Cadastro com tratamento de erros
pessoas = []

while True:
    try:
        print("\n--- Novo Cadastro ---")
        nome = input("Nome: ").strip().title()
        
        idade = int(input("Idade: "))
        if not (0 < idade < 150):
            print("Idade deve ser entre 1 e 149!")
            continue
            
        altura = float(input("Altura (m): ").replace(',', '.'))
        if not (0.5 < altura < 2.5):
            print("Altura deve ser entre 0.5 e 2.5 metros!")
            continue
            
        pessoas.append({"nome": nome, "idade": idade, "altura": altura})
        
        if input("Continuar? (s/n): ").lower() != 's':
            break
            
    except ValueError:
        print("Valor inválido! Digite números corretamente.")
        continue

print("\n--- Resultados ---")
print(f"{'Nome':<15} | {'Idade':^5} | {'Altura':^6}")
for p in pessoas:
    print(f"{p['nome']:<15} | {p['idade']:^5} | {p['altura']:>5.2f}m")
  
input("\nPressione Enter para sair...")