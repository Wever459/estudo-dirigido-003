estoque = {}

class Produto:
    """Representa um produto no estoque com suas operações básicas."""

    def __init__(self, nome, quantidade, preco):
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

    def adicionar(self, qtd):
        """Adiciona unidades ao estoque do produto."""
        if qtd > 0:
            self.quantidade += qtd
            return True
        return False

    def remover(self, qtd):
        """Remove unidades do estoque do produto, verificando a disponibilidade."""
        if qtd > 0 and self.quantidade >= qtd:
            self.quantidade -= qtd
            return True
        return False

    def valor_total(self):
        """Calcula e retorna o valor total em reais do produto no estoque."""
        return self.quantidade * self.preco

    def __str__(self):
        """Representação formatada do objeto para impressão."""
        total = self.valor_total()
        return f"🏷 {self.nome:15} | {self.quantidade:3} unidades | R$ {self.preco:7.2f} | Total: R$ {total:8.2f}"


class Usuario:
    """
    Representa um usuário do sistema com credenciais de login.
    Cada instância armazena seu próprio nome, email e senha.
    """

    def __init__(self, nome, email, senha):
        """Método construtor para criar um novo usuário."""
        self.nome = nome
        self.email = email
        self.senha = senha 
        print(f"👤 Usuário '{self.nome}' criado com email: {self.email}")

    def autenticar(self, email, senha):
        """
        Verifica se as credenciais fornecidas (email e senha) correspondem
        aos atributos desta instância específica de usuário.
        """
      
        if self.email == email and self.senha == senha:
            print(f"✅ Autenticação bem-sucedida para {self.nome}!")
            return True
        else:
            print(f"❌ Falha na autenticação. Email ou senha incorretos para a conta de {self.nome}.")
            return False
        

print("="*50)
print("💻 TESTE - CADASTRO DE USUÁRIOS")
print("="*50)


user1 = Usuario("Alice", "alice@corp.com", "senha123")
user2 = Usuario("Bob", "bob@corp.com", "bobafe789")

print("\n--- Teste de Logins ---")


print("\n--- Tentativa 1: Login de Alice (Correto) ---")
user1.autenticar("alice@corp.com", "senha123")


print("\n--- Tentativa 2: Login de Bob (Incorreto - Senha) ---")
user2.autenticar("bob@corp.com", "senhaerrada")


print("\n--- Tentativa 3: Login de Alice (Incorreto - Email) ---")
user1.autenticar("alice.errado@corp.com", "senha123")


print("\n--- Tentativa 4: Login de Bob (Correto) ---")
user2.autenticar("bob@corp.com", "bobafe789")

print("\n")

