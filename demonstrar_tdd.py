import os
import time
import subprocess

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(title, color_code):
    print(f"\n\033[{color_code}m" + "="*50)
    print(f"  {title}")
    print("="*50 + "\033[0m\n")

def run_pytest(verbose=False):
    command = ["pytest", "-v", "test_calculadora.py"] if verbose else ["pytest", "test_calculadora.py"]
    subprocess.run(command)

def step_red():
    clear()
    print_header("PASSO 1: CICLO RED (FALHA)", "31") # Vermelho
    print("Nesta fase, temos os testes mas NÃO temos a implementação.")
    print("O terminal deve exibir erros (FAILED).\n")
    
    # Salva o estado RED (classe vazia)
    with open("calculadora.py", "w") as f:
        f.write("class CalculadoraService:\n    pass\n")
    
    input("Pressione ENTER para rodar os testes e ver a FALHA (RED)...")
    run_pytest(verbose=True)
    print("\n" + "-"*50)
    input("\nObserve os erros acima. Pressione ENTER para ir para a fase GREEN...")

def step_green():
    clear()
    print_header("PASSO 2: CICLO GREEN (PASSOU)", "32") # Verde
    print("Agora adicionamos o código mínimo para os testes passarem.")
    print("O terminal deve exibir pontos verdes ou 'PASSED'.\n")
    
    # Salva o estado GREEN (implementação básica)
    with open("calculadora.py", "w") as f:
        f.write("""class CalculadoraService:
    def somar(self, a, b): return a + b
    def subtrair(self, a, b): return a - b
    def multiplicar(self, a, b): return a * b
    def dividir(self, a, b):
        if b == 0: raise ValueError("Divisão por zero não permitida")
        return a / b
    def isPar(self, n): return n % 2 == 0
    def validarNumeroPositivo(self, n): return n > 0
""")
    
    input("Pressione ENTER para rodar os testes e ver o SUCESSO (GREEN)...")
    run_pytest(verbose=True)
    print("\n" + "-"*50)
    input("\nTodos os testes passaram! Pressione ENTER para ir para a fase REFACTOR...")

def step_refactor():
    clear()
    print_header("PASSO 3: CICLO REFACTOR (MELHORIA)", "34") # Azul
    print("Agora melhoramos o código (tipagem, documentação) sem quebrar nada.")
    print("Os testes devem CONTINUAR passando.\n")
    
    # Salva o estado REFACTOR (código final limpo)
    with open("calculadora.py", "w") as f:
        f.write("""class CalculadoraService:
    \"\"\"Serviço de calculadora com TDD.\"\"\"
    def somar(self, a: float, b: float) -> float:
        return a + b

    def subtrair(self, a: float, b: float) -> float:
        return a - b

    def multiplicar(self, a: float, b: float) -> float:
        return a * b

    def dividir(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Divisão por zero não permitida")
        return a / b

    def isPar(self, numero: int) -> bool:
        return numero % 2 == 0

    def validarNumeroPositivo(self, numero: float) -> bool:
        return numero > 0
""")
    
    input("Pressione ENTER para rodar os testes após a REFATORAÇÃO...")
    run_pytest(verbose=True)
    print("\n" + "-"*50)
    print("\nSucesso! O código foi melhorado e os testes continuam garantindo a qualidade.")
    input("\nFim da demonstração. Pressione ENTER para sair.")

if __name__ == "__main__":
    try:
        step_red()
        step_green()
        step_refactor()
    except KeyboardInterrupt:
        print("\nDemonstração interrompida.")
