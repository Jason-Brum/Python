agenda_telefonica = {}
 
def inserir(nome, agenda, telefone = "Sem telefone"):
    if nome in agenda:
        if input("Contato já cadastrado. Deseja alterar o telefone? (s/n) ") == "n":
            return False
    agenda[nome] = telefone
    return True
 
inserir("Fulano", agenda_telefonica)
inserir("Beltrano", agenda_telefonica, 1232231413)
 
print(agenda_telefonica)