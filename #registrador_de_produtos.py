#registrador_de_produtos
import tkinter as tk
from tkinter import simpledialog, messagebox


products = [
    {"produto": "Arroz", "marca": "Camil", "tipo": "Integral", "preço": 20.00, "codigo": "AC01", "estoque": 100, "peso": "5kg"},
    {"produto": "Feijão", "marca": "Carioca", "tipo": "Carioca", "preço": 9.00, "codigo": "FA01", "estoque": 150, "peso": "1kg"},
    {"produto": "Linguiça", "marca": "Seara", "tipo": "Toscana", "preço": 20.00, "codigo": "LA01", "estoque": 50, "peso": "1kg"},
    {"produto": "Tomate", "marca": "GreenBull", "tipo": "Salada", "preço": 5.00, "codigo": "TA01", "estoque": 110, "peso": "1kg"},
    {"produto": "Refrigerante", "marca": "IT", "tipo": "Guaraná", "preço": 4.00, "codigo": "RB01", "estoque": 40, "peso": "2L"},
]


def register_product():
    product = simpledialog.askstring("Input", "Qual produto você deseja adicionar?")
    marca = simpledialog.askstring("Input", "Qual a marca do produto?")
    tipo = simpledialog.askstring("Input", "Qual o tipo do produto?")
    preco = simpledialog.askfloat("Input", "Qual o preço do produto?")
    peso = simpledialog.askstring("Input", "Qual peso do produto e sua medida?")
    estoque = simpledialog.askinteger("Input", "Quantos estão no estoque?")
    codigo = simpledialog.askstring("Input", "Qual o código do produto?")

    new_product = {
        "produto": product,
        "marca": marca,
        "tipo": tipo,
        "preço": preco,
        "codigo": codigo,
        "estoque": estoque,
        "peso": peso,
    }
    products.append(new_product)
    messagebox.showinfo("Info", f"Produto {product} registrado com sucesso!")


def register_output():
    codigo = simpledialog.askstring("Input", "Qual o código do produto?")
    for produto in products:
        if codigo == produto["codigo"]:
            quantidade = simpledialog.askinteger("Input", "Quantos você deseja retirar do estoque?")
            if quantidade <= produto["estoque"]:
                produto["estoque"] -= quantidade
                messagebox.showinfo("Info", f"{quantidade} unidades de {produto['produto']} foram retirados no estoque")
            else:
                messagebox.showwarning("Warning", "Não há quantidade o suficiente no estoque")
            return
    messagebox.showwarning("Warning", "Produto não encontrado")


def check_stock():
    codigo = simpledialog.askstring("Input", "Qual o código do produto que você deseja consultar a quantidade no estoque?")
    for produto in products:
        if codigo == produto["codigo"]:
            messagebox.showinfo("Info", f"O produto {produto['produto']} tem no estoque {produto['estoque']}")
            return
    messagebox.showwarning("Warning", "Produto não encontrado")


def edit_product():
    codigo = simpledialog.askstring("Input", "Insira o código do produto que deseja editar:")
    for produto in products:
        if codigo == produto["codigo"]:
            option = simpledialog.askinteger("Input", "Escolha a opção que deseja editar:\n1. Produto\n2. Marca\n3. Tipo\n4. Preço\n5. Peso\n6. Estoque\n7. Código")
            if option == 1:
                produto["produto"] = simpledialog.askstring("Input", "Fale qual será o novo nome do produto:")
            elif option == 2:
                produto["marca"] = simpledialog.askstring("Input", "Fale qual será a nova marca do produto:")
            elif option == 3:
                produto["tipo"] = simpledialog.askstring("Input", "Fale qual será o novo tipo do produto:")
            elif option == 4:
                produto["preço"] = simpledialog.askfloat("Input", "Fale qual será o novo preço do produto:")
            elif option == 5:
                produto["peso"] = simpledialog.askstring("Input", "Fale qual será o novo peso do produto:")
            elif option == 6:
                produto["estoque"] = simpledialog.askinteger("Input", "Fale qual será o novo estoque do produto:")
            elif option == 7:
                produto["codigo"] = simpledialog.askstring("Input", "Fale qual será o novo código do produto:")
            messagebox.showinfo("Info", "Informação do produto editada com sucesso!")
            return
    messagebox.showwarning("Warning", "Produto não encontrado")


def remove_product():
    codigo = simpledialog.askstring("Input", "Fale o código do produto que deseja remover:")
    for produto in products:
        if codigo == produto["codigo"]:
            products.remove(produto)
            messagebox.showinfo("Info", "Produto removido com sucesso!")
            return
    messagebox.showwarning("Warning", "Produto não encontrado")


def show_products():
    message = "Lista de produtos no estoque:\n\n"
    for produto in products:
        message += f"Produto: {produto['produto']}\n"
        message += f"Marca: {produto['marca']}\n"
        message += f"Tipo: {produto['tipo']}\n"
        message += f"Preço: R${produto['preço']:.2f}\n"
        message += f"Peso: {produto['peso']}\n"
        message += f"Estoque: {produto['estoque']} unidades\n"
        message += f"Código: {produto['codigo']}\n\n"
    messagebox.showinfo("Produtos em estoque", message)


def search_product():
    search_term = simpledialog.askstring("Buscar produto", "Digite o nome ou marca do produto:")
    results = []
    for produto in products:
        if search_term.lower() in produto['produto'].lower() or search_term.lower() in produto['marca'].lower():
            results.append(produto)
    if results:
        message = "Resultados da pesquisa:\n\n"
        for produto in results:
            message += f"Produto: {produto['produto']}\n"
            message += f"Marca: {produto['marca']}\n"
            message += f"Tipo: {produto['tipo']}\n"
            message += f"Preço: R${produto['preço']:.2f}\n"
            message += f"Peso: {produto['peso']}\n"
            message += f"Estoque: {produto['estoque']} unidades\n"
            message += f"Código: {produto['codigo']}\n\n"
        messagebox.showinfo("Resultados da Pesquisa", message)
    else:
        messagebox.showinfo("Resultados da Pesquisa", "Nenhum produto encontrado com esse termo de pesquisa.")


def exit_program():
    root.destroy()


root = tk.Tk()
root.title("Controle de Estoque")
root.geometry("400x400")
root.configure(bg="#1e3743")  


tk.Button(root, text="Registrar entrada de produto", command=register_product).pack(pady=5)
tk.Button(root, text="Registrar saída de produto", command=register_output).pack(pady=5)
tk.Button(root, text="Verificar saldo de produto", command=check_stock).pack(pady=5)
tk.Button(root, text="Editar informações do produto", command=edit_product).pack(pady=5)
tk.Button(root, text="Remover produto", command=remove_product).pack(pady=5)
tk.Button(root, text="Ver todos os produtos", command=show_products).pack(pady=5)
tk.Button(root, text="Buscar produto", command=search_product).pack(pady=5)
tk.Button(root, text="Sair do programa", command=exit_program).pack(pady=5)

root.mainloop()