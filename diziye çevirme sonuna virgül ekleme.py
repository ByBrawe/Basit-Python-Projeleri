mailler = """1@email.com
2@email.com
3@email.com
4@email.com
5@email.com"""
liste = mailler.split("\n")
say=0
count = len(liste)
maillistesi = ""
for i in liste:
  say+=1
  maillistesi += i
  if say<count:
    maillistesi+=","
  maillistesi += "\n"  
print(maillistesi)
