class Jogador:

    def __init__(self, nome, saldo_inicial=0):
        self.nome = nome
        self.saldo = saldo_inicial
        self.itens = []  # Lista para armazenar os itens comprados
        print(f"🎮 Jogador(a) '{self.nome}' criado(a) com saldo inicial de R$ {self.saldo:.2f}.")

    def adicionar_saldo(self, valor):
        
        if valor > 0:
            self.saldo += valor
            print(f"💰 R$ {valor:.2f} adicionados ao saldo. Novo saldo: R$ {self.saldo:.2f}")
            return True
        print("❌ O valor a ser adicionado deve ser positivo.")
        return False

    def comprar_item(self, item, preco):
       
        if preco <= 0:
            print(f"❌ '{item}' não pode ser comprado por preço zero ou negativo.")
            return False

        if self.saldo >= preco:
            # 1. Subtrai o custo do saldo
            self.saldo -= preco
            
            # 2. Adiciona o item ao inventário
            self.itens.append(item)
            
            print(f"✅ Compra bem-sucedida! '{item}' adquirido por R$ {preco:.2f}.")
            print(f"   Saldo restante: R$ {self.saldo:.2f}.")
            return True
        else:
            # Regra de negócio: Saldo insuficiente
            print(f"⚠️ Saldo insuficiente para comprar '{item}' (Preço: R$ {preco:.2f}, Saldo: R$ {self.saldo:.2f}).")
            return False

    def mostrar_status(self):
       
        itens_formatados = ", ".join(self.itens) if self.itens else "Nenhum item"
        print("\n" + "-"*40)
        print(f"🌟 STATUS DO JOGADOR: {self.nome}")
        print(f"  Saldo Atual: R$ {self.saldo:.2f}")
        print(f"  Inventário: [{itens_formatados}]")
        print("-" * 40)


print("\n" + "="*50)
print("🕹️ TESTE - GESTÃO DE JOGADORES")
print("="*50)

jogador1 = Jogador("HeroiDestemido", 50.00)
jogador2 = Jogador("MagoLendario")

jogador1.mostrar_status()


print("\n--- Operações de Compra para HeroiDestemido ---")
jogador1.adicionar_saldo(100.00) 

jogador1.comprar_item("Espada Flamejante", 80.00)

jogador1.comprar_item("Poção de Cura", 45.00) 

jogador1.comprar_item("Armadura de Ouro", 50.00)

jogador1.mostrar_status()

print("\n--- Operações de Compra para MagoLendario ---")
jogador2.adicionar_saldo(10.00) 


jogador2.comprar_item("Cajado Élfico", 30.00)

jogador2.mostrar_status()