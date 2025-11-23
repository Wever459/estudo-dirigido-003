estoque = {}

class Produto:
    """
    Representa um produto no estoque com suas operações básicas.
    Os atributos do produto são encapsulados e as operações agem sobre si mesmos.
    """

    def __init__(self, nome, quantidade, preco):
        """Método construtor para criar um novo produto."""
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco
        print(f"✅ Produto '{self.nome}' criado com {self.quantidade} unidades a R$ {self.preco:.2f}")

    def adicionar(self, qtd):
        """Adiciona unidades ao estoque do produto."""
        if qtd > 0:
            self.quantidade += qtd
            print(f"📦 Adicionadas {qtd} unidades de '{self.nome}'. Estoque atual: {self.quantidade}")
            return True
        return False

    def remover(self, qtd):
        """Remove unidades do estoque do produto, verificando a disponibilidade."""
        if qtd > 0:
            if self.quantidade >= qtd:
                self.quantidade -= qtd
                print(f"📤 Removidas {qtd} unidades de '{self.nome}'. Estoque atual: {self.quantidade}")
                return True
            else:
                print(f"⚠ Estoque insuficiente de '{self.nome}'. Disponível: {self.quantidade}")
                return False
        return False

    def valor_total(self):
        """Calcula e retorna o valor total em reais do produto no estoque."""
        total = self.quantidade * self.preco
        return total

    def __str__(self):
        """Método especial para representação do objeto em string (usado no print)."""
        total = self.valor_total()
        return f"🏷 {self.nome:15} | {self.quantidade:3} unidades | R$ {self.preco:7.2f} | Total: R$ {total:8.2f}"


def criar_produto_no_estoque(nome, quantidade, preco):
    """Cria uma instância de Produto e a armazena no dicionário global."""
    if nome not in estoque:
        estoque[nome] = Produto(nome, quantidade, preco)
    else:
        print(f"❌ Produto '{nome}' já existe no estoque!")

def mostrar_estoque():
    """Exibe todos os produtos e o valor total geral."""
    print("\n" + "="*50)
    print("📊 ESTOQUE ATUAL")
    print("="*50)
    total_geral = 0
    
    if not estoque:
        print("Estoque vazio.")
    else:
        for produto_obj in estoque.values():
            print(produto_obj)
            total_geral += produto_obj.valor_total() # O objeto sabe calcular seu próprio valor!

    print("="*50)
    print(f"💵 VALOR TOTAL DO ESTOQUE: R$ {total_geral:.2f}")


print("=== SISTEMA DE ESTOQUE (POO) ===")


criar_produto_no_estoque("Notebook", 5, 2500.00)
criar_produto_no_estoque("Mouse", 20, 45.90)
criar_produto_no_estoque("Teclado", 10, 120.00)

mostrar_estoque()

print("\n--- Operações de Movimentação ---")
if "Notebook" in estoque:
    estoque["Notebook"].adicionar(3)

if "Mouse" in estoque:
    estoque["Mouse"].adicionar(10)

if "Teclado" in estoque:
    estoque["Teclado"].remover(5)


if "Monitor" not in estoque:
    print(f"❌ Produto 'Monitor' não encontrado!")
else:
    estoque["Monitor"].remover(2)


print("\n--- Consulta de Valores ---")
if "Notebook" in estoque:
    valor = estoque["Notebook"].valor_total()
    print(f"💰 Valor total de 'Notebook': R$ {valor:.2f}")

if "Mouse" in estoque:
    valor = estoque["Mouse"].valor_total()
    print(f"💰 Valor total de 'Mouse': R$ {valor:.2f}")

mostrar_estoque()