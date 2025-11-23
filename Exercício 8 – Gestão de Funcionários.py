class Funcionario:
    
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = float(salario) 
        print(f"👨‍💼 Funcionário '{self.nome}' ({self.cargo}) cadastrado com salário inicial de R$ {self.salario:.2f}.")

    def aumentar_salario(self, percentual):
        
        if percentual > 0:
            fator_aumento = 1 + (percentual / 100)
            novo_salario = self.salario * fator_aumento
            
            print(f"\n📈 Aumento de {percentual:.2f}% solicitado para {self.nome}.")
            print(f"Salário Anterior: R$ {self.salario:.2f}")
            
            self.salario = novo_salario
            
            print(f"✅ Novo Salário: R$ {self.salario:.2f}")
            return True
        else:
            print("❌ O percentual de aumento deve ser positivo.")
            return False

    def __str__(self):
        return f"Nome: {self.nome} | Cargo: {self.cargo} | Salário Atual: R$ {self.salario:.2f}"


print("\n" + "="*50)
print("💰 TESTE - GESTÃO DE FUNCIONÁRIOS")
print("="*50)

f1 = Funcionario("João Silva", "Desenvolvedor Júnior", 5000.00)
f2 = Funcionario("Maria Souza", "Gerente de Projetos", 12000.50)
f3 = Funcionario("Pedro Santos", "Estagiário", 1500.00)

print("\n--- Status Inicial ---")
print(f1)
print(f2)
print(f3)

f1.aumentar_salario(10.0) # João recebe 10% de aumento
f2.aumentar_salario(5.5)  # Maria recebe 5.5% de aumento
f3.aumentar_salario(0)    # Tentativa com 0% (deve falhar)

print("\n--- Status Final ---")
print(f1)
print(f2)
print(f3)