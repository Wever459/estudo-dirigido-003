class Usuario:
   
    def __init__(self, nome, email, senha, saldo_inicial=0):
        
        self.nome = nome
        self.email = email
        self.senha = senha
        self.saldo = saldo_inicial 
        print(f"👤 Usuário '{self.nome}' criado com saldo inicial de R$ {self.saldo:.2f}.")

    def autenticar(self, email, senha):
        return self.email == email and self.senha == senha

    def adicionar_saldo(self, valor):
        if valor > 0:
            self.saldo += valor
            return True
        return False
    
    def __str__(self):
        return f"Usuário: {self.nome} | Saldo: R$ {self.saldo:.2f}"


class Pagamento:
    
    def __init__(self, usuario: Usuario, valor: float):
        
        self.usuario = usuario 
        self.valor = valor
        self.status = "Pendente"
        print(f"💳 Pagamento criado: R$ {self.valor:.2f} para {self.usuario.nome}. Status: {self.status}")

    def processar(self):
     
        if self.status == "Pendente":
            print(f"\n⚙️ Processando pagamento de R$ {self.valor:.2f} para {self.usuario.nome}...")
            
            if self.usuario.adicionar_saldo(self.valor):
                self.status = "Concluído"
                print(f"✅ Transação concluída! Novo status: {self.status}.")
            else:
                self.status = "Falha"
                print("❌ Falha no processamento. Valor inválido ou erro interno.")
                       
            return True
        else:
            print(f"⚠️ Pagamento já foi processado ou falhou. Status atual: {self.status}.")
            return False



print("\n" + "="*60)
print("💰 TESTE - SISTEMA DE PAGAMENTO (INTERAÇÃO DE CLASSES)")
print("="*60)

user_compra = Usuario("Clara_Gamer", "clara@mail.com", "123pass", 50.00)
user_dev = Usuario("Dev_Master", "dev@mail.com", "456pass", 100.00)

print("\n--- Saldo Inicial ---")
print(user_compra)
print(user_dev)

pagamento1 = Pagamento(user_compra, 50.00) 


pagamento2 = Pagamento(user_dev, 200.50)


print("\n--- Processando Transações ---")
pagamento1.processar()
pagamento2.processar()


print("\n--- Saldo Final ---")
print(user_compra)
print(user_dev)

print("\n--- Tentativa de Re-processar ---")
pagamento1.processar()