gramatas_cena = 24.95
atlaide = 0.4
piegades_izmaksas = 3.00
piegade_par_gramatu = 0.75
gramatu_skaits = 60

iegades_izmaksas = piegades_izmaksas + ((gramatu_skaits-1)*piegade_par_gramatu) \
                   + (gramatu_skaits*gramatas_cena*(1 - atlaide))
print("Kopejās izmaksas: ", iegades_izmaksas)