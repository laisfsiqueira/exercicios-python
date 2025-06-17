from datetime import datetime

def dias_vividos(data_nascimento):
  agora = datetime.now()
  nascimento = data_nascimento
  print(f"O vivente viveu {agora - nascimento}")

def conversao():
  print("Digite sua data de nascimento no formato dd/mm/yyyy: ")
  dt_nascimento = input()
  try:
    dt_nasc = datetime.strptime(dt_nascimento, "%d/%m/%Y")
  except ValueError:
    conversao()
  else:
    dias_vividos(dt_nasc)

def main():
  conversao()

if __name__ == "__main__":
  main()


