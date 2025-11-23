estoque = {}

def criar_produto(nome, quantidade, preco):
    estoque[nome] = {'quantidade': quantidade, 'preco': preco}
    print(f"✅ Produto '{nome}' adicionado ao estoque")

def adicionar_estoque(produto, qtd):
    if produto in estoque:
        estoque[produto]['quantidade'] += qtd
        print(f"📦 Adicionadas {qtd} unidades de '{produto}'")
    else:
        print(f"❌ Produto '{produto}' não encontrado!")

def remover_estoque(produto, qtd):
    if produto in estoque:
        if estoque[produto]['quantidade'] >= qtd:
            estoque[produto]['quantidade'] -= qtd
            print(f"📤 Removidas {qtd} unidades de '{produto}'")
        else:
            print(f"⚠ Estoque insuficiente de '{produto}'")
    else:
        print(f"❌ Produto '{produto}' não encontrado!")

def valor_total(produto):
    if produto in estoque:
        qtd = estoque[produto]['quantidade']
        preco = estoque[produto]['preco']
        total = qtd * preco
        print(f"💰 Valor total de '{produto}': {qtd} x R$ {preco:.2f} = R$ {total:.2f}")
        return total
    else:
        print(f"❌ Produto '{produto}' não encontrado!")
        return 0

def mostrar_estoque():
    print("\n" + "="*50)
    print("📊 ESTOQUE ATUAL")
    print("="*50)
    for produto, dados in estoque.items():
        total = dados['quantidade'] * dados['preco']
        print(f"🏷  {produto:15} | {dados['quantidade']:3} unidades | R$ {dados['preco']:7.2f} | Total: R$ {total:8.2f}")
    print("="*50)

print("=== SISTEMA DE ESTOQUE ===")

# Criando produtos
criar_produto("Notebook", 5, 2500.00)
criar_produto("Mouse", 20, 45.90)
criar_produto("Teclado", 10, 120.00)


mostrar_estoque()

adicionar_estoque("Notebook", 3)
adicionar_estoque("Mouse", 10)
remover_estoque("Teclado", 5)
remover_estoque("Monitor", 2)  # Produto inexistente

valor_total("Notebook")
valor_total("Mouse")

mostrar_estoque()

total_geral = sum(estoque[produto]['quantidade'] * estoque[produto]['preco'] for produto in estoque)
print(f"💵 VALOR TOTAL DO ESTOQUE: R$ {total_geral:.2f}")