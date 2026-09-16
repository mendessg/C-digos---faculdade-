preco_bolodemorango = 18.00
preco_bolodechocolate = 20.00
preco_refrigerante = 6.00
preco_suco = 8.00
preco_agua = 4.00
preco_cafe = 5.00
preco_sanduiche = 12.00
preco_coxinha = 10.00
print("Bem-vindo ao Restaurante bololitos!")
print("Cardápio:")
print(f"1. Bolo de morango - R$ {preco_bolodemorango:.2f}")
print(f"2. Bolo de chocolate - R$ {preco_bolodechocolate:.2f}")
print(f"3. Refrigerante - R$ {preco_refrigerante:.2f}")
print(f"4. Suco - R$ {preco_suco:.2f}")
print(f"5. Água - R$ {preco_agua:.2f}")
print(f"6. Café - R$ {preco_cafe:.2f}")
print(f"7. Sanduíche - R$ {preco_sanduiche:.2f}")
print(f"8. Coxinha - R$ {preco_coxinha:.2f}")
print("Digite a quantidade consumida de cada item:")
quantidade_bolodemorango = int(input("Bolo de morango: "))
quantidade_bolodechocolate = int(input("Bolo de chocolate: "))
quantidade_refrigerante = int(input("Refrigerante: "))          
quantidade_suco = int(input("Suco: "))
quantidade_agua = int(input("Água: "))
quantidade_cafe = int(input("Café: "))
quantidade_sanduiche = int(input("Sanduíche: "))
quantidade_coxinha = int(input("Coxinha: "))
total_bolodemorango = preco_bolodemorango * quantidade_bolodemorango
total_bolodechocolate = preco_bolodechocolate * quantidade_bolodechocolate
total_refrigerante = preco_refrigerante * quantidade_refrigerante
total_suco = preco_suco * quantidade_suco
total_agua = preco_agua * quantidade_agua
total_cafe = preco_cafe * quantidade_cafe
total_sanduiche = preco_sanduiche * quantidade_sanduiche
total_coxinha = preco_coxinha * quantidade_coxinha
total = (total_bolodemorango + total_bolodechocolate + total_refrigerante + total_suco + total_agua + total_cafe + total_sanduiche + total_coxinha)
total += total * 0.10  # Adiciona 10% de taxa de serviço
print(f"Total a pagar: R$ {total:.2f}")
resposta_gorjeta = input("Deseja adicionar uma gorjeta? (s/n): ")
if resposta_gorjeta.lower() == 's':
    gorjeta = float(input("Digite o valor da gorjeta: R$ "))
    total += gorjeta
elif resposta_gorjeta.lower() == 'n':
    print("Sem gorjeta adicionada.")
else:
    print("Resposta inválida. Nenhuma gorjeta foi adicionada.")

print(f"Total a pagar com gorjeta: R$ {total:.2f}")
num_pessoas = int(input("Digite o número de pessoas para dividir a conta: "))
if num_pessoas > 4:
    print("Você tem direito a um desconto de 5% por dividir a conta entre mais de 4 pessoas.")
    total -= total * 0.05
elif num_pessoas <= 0:
    print("Número de pessoas inválido. A conta não será dividida.")

print("Resumo da conta:")
itens = [
    (quantidade_bolodemorango, "Bolo de morango", preco_bolodemorango, total_bolodemorango),
    (quantidade_bolodechocolate, "Bolo de chocolate", preco_bolodechocolate, total_bolodechocolate),
    (quantidade_refrigerante, "Refrigerante", preco_refrigerante, total_refrigerante),
    (quantidade_suco, "Suco", preco_suco, total_suco),
    (quantidade_agua, "Água", preco_agua, total_agua),
    (quantidade_cafe, "Café", preco_cafe, total_cafe),
    (quantidade_sanduiche, "Sanduíche", preco_sanduiche, total_sanduiche),
    (quantidade_coxinha, "Coxinha", preco_coxinha, total_coxinha),
]
for quantidade, nome, preco, subtotal in itens:
    if quantidade > 0:
        print(f"{nome}: {quantidade} x R$ {preco:.2f} = R$ {subtotal:.2f}")

print(f"Total geral a pagar: R$ {total:.2f}")
if num_pessoas > 0:
    print(f"Total a pagar por pessoa: R$ {total / num_pessoas:.2f}")
if total > 300:
    print("\nUma conta excelente! Agradecemos a preferência e esperamos vê-lo novamente em breve!")
