class Livro:
    
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True  # Atributo que armazena o estado do livro

    def emprestar(self):
      
        if self.disponivel:
            self.disponivel = False
            return True
        return False

    def devolver(self):
      
        self.disponivel = True

    def __str__(self):
        status = "🟢 DISPONÍVEL" if self.disponivel else "🔴 EMPRESTADO"
        return f"Título: {self.titulo:<30} | Autor: {self.autor:<20} | Status: {status}"


class Biblioteca:
    
    def __init__(self):
        self.livros = []
        print("🏛️ Biblioteca criada e pronta para o catálogo.")

    def adicionar_livro(self, livro: Livro):
        self.livros.append(livro)
        print(f"➕ Livro '{livro.titulo}' adicionado ao catálogo.")

    def listar_disponiveis(self):
        disponiveis = [livro for livro in self.livros if livro.disponivel]
        
        print("\n--- 📖 LIVROS DISPONÍVEIS ---")
      
        if not disponiveis:
            print("Nenhum livro disponível no momento.")
            return

        for livro in disponiveis:
            print(livro)
        print("------------------------------")
    
    def emprestar_livro(self, titulo_do_livro):
       
        for livro in self.livros:
            if livro.titulo.lower() == titulo_do_livro.lower():
                # Tenta emprestar usando o método interno do objeto Livro
                if livro.emprestar():
                    print(f"✅ Livro '{livro.titulo}' emprestado com sucesso!")
                    return True
                else:
                    # Regra de negócio falhou: livro já emprestado
                    print(f"⚠️ Livro '{livro.titulo}' já está emprestado.")
                    return False

        print(f"❌ Livro '{titulo_do_livro}' não encontrado no catálogo.")
        return False

    def devolver_livro(self, titulo_do_livro):
       
        for livro in self.livros:
            if livro.titulo.lower() == titulo_do_livro.lower():
                livro.devolver()
                print(f"↩️ Livro '{livro.titulo}' devolvido e agora está disponível.")
                return True
        
        print(f"❌ Livro '{titulo_do_livro}' não encontrado no catálogo para devolução.")
        return False



print("\n" + "="*50)
print("📚 TESTE - SISTEMA DE BIBLIOTECA")
print("="*50)


minha_biblioteca = Biblioteca()


livro1 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien")
livro2 = Livro("1984", "George Orwell")
livro3 = Livro("Pequeno Príncipe", "Antoine de Saint-Exupéry")

minha_biblioteca.adicionar_livro(livro1)
minha_biblioteca.adicionar_livro(livro2)
minha_biblioteca.adicionar_livro(livro3)


minha_biblioteca.listar_disponiveis()


print("\n--- Simulação de Empréstimos ---")


minha_biblioteca.emprestar_livro("1984") 


minha_biblioteca.emprestar_livro("1984")

minha_biblioteca.emprestar_livro("O Senhor dos Anéis")

minha_biblioteca.listar_disponiveis()


print("\n--- Simulação de Devolução ---")
minha_biblioteca.devolver_livro("1984")


minha_biblioteca.listar_disponiveis()