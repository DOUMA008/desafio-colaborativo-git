def calcular_porcentagem(valor, total):
    if total == 0:
        return 0
    return (valor / total) * 100

# Exemplo de uso
if __name__ == "__main__":
    resultado = calcular_porcentagem(50, 200)
    print(f"Porcentagem: {resultado}%") 
    