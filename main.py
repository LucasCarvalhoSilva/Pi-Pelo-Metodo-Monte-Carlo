from src.calculator import calculatePi

def main():
  print("=> Cálculo de Pi pelo Método de Monte Carlo<=")

  try:
    numberOfPoints = int(input("Digite a quantidade de pontos que devem ser simulados: "))
    if numberOfPoints <= 0:
      raise ValueError("Digite um valor valído, precisa ser um número maior do que 0")
  except ValueError as e:
    print(f"Entrada inválida: {e}")
    return
  
  estimatedPi = calculatePi(numberOfPoints)
  print(f"Com {numberOfPoints} pontos, o valor estimado de Pi é {estimatedPi:.6f}")

if __name__ == "__main__":
  main()
