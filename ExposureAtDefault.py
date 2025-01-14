# Paramètres du modèle
credit_limit = 100000  # Limite de crédit (en $)
current_usage = 50000  # Montant actuellement utilisé (en $)
ccf = 0.4  # Facteur de conversion de crédit (40%)

# Fonction pour calculer l'EAD
def calculate_ead(credit_limit, current_usage, ccf):
    """
    Calcule l'Exposure at Default (EAD).

    Arguments :
    - credit_limit : Montant total de la ligne de crédit.
    - current_usage : Montant déjà utilisé par l'emprunteur.
    - ccf : Facteur de conversion de crédit (proportion de la partie non utilisée qui pourrait être tirée).

    Retourne :
    - L'EAD calculé.
    """
    unused_credit = credit_limit - current_usage  # Partie non utilisée de la ligne de crédit
    potential_drawn_amount = unused_credit * ccf  # Montant potentiel tiré avant défaut
    ead = current_usage + potential_drawn_amount  # EAD total
    return ead

# Calcul du EAD
ead = calculate_ead(credit_limit, current_usage, ccf)
print(f"Exposure at Default (EAD) : ${ead:.2f}")
