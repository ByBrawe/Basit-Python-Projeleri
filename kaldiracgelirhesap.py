
kaldiracOrani = 7
anaPara = 10
karOrani = 20
Ardardaislem = 10
risk = 1

print(f"\n Kaldirac Oranı: {kaldiracOrani}\n Anapara başlangıc: {anaPara}\n Karorani %{karOrani} \n Herzaman anaparanin yüzde kacı ile devam ediceksin: %{risk*100} \n Ardarda işlem sayısı: {Ardardaislem}\n")

for i in range (1, Ardardaislem+1):


    kazanc = ((anaPara)*karOrani/100)*kaldiracOrani
    anaPara = (kazanc+anaPara)
    print(f'{i}.ci kazanç: {round(kazanc,2)}')


print(f"\nToplam Kazanç: {round(kazanc, 2)}")
