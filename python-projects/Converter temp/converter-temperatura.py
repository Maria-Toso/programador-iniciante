# --- Documentação do Programa ---
# Este script Python realiza a conversão de temperatura entre Celsius e Fahrenheit.

def celsius_para_fahrenheit(celsius):
    """Converte temperatura de Celsius para Fahrenheit."""
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

def fahrenheit_para_celsius(fahrenheit):
    """Converte temperatura de Fahrenheit para Celsius."""
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def iniciar_conversor():
    """Função principal para interagir com o usuário e executar a conversão."""
    print("--- Conversor de Temperatura ---")
    
    unidade = input("Qual unidade você quer converter? (C para Celsius / F para Fahrenheit): ").upper()
    
    if unidade not in ('C', 'F'):
        print("Unidade inválida. Por favor, digite 'C' ou 'F'.")
        return
    try:
        temperatura = float(input(f"Digite a temperatura em {unidade}: "))
    except ValueError:
        print("Entrada de temperatura inválida. Por favor, digite um número.")
        return
    if unidade == 'C':
        resultado = celsius_para_fahrenheit(temperatura)
        print(f"\nResultado:")
        print(f"{temperatura}°C é igual a {resultado:.2f}°F")
        
    elif unidade == 'F':
        resultado = fahrenheit_para_celsius(temperatura)
        print(f"\nResultado:")
        print(f"{temperatura}°F é igual a {resultado:.2f}°C")
        
    print("---------------------------------")

if __name__ == "__main__":
    iniciar_conversor()
