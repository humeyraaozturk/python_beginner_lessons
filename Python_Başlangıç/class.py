class Player():
    def __init__(self,name,pac,dri,sho,pas,dff,phy):
        self.name = name
        self.pac = pac
        self.dri = dri
        self.sho = sho
        self.pas = pas
        self.dff = dff
        self.phy = phy
    def __str__(self):
    #__str__ fonksiyonun parametresini self olarak atadığımız sürece yukarıda self ile
    #bağladığımız değişkenleri kullanabiliriz.
        return self.name

    def overall(self):
        ovr = (self.pac*3) + (self.dri*3) + (self.sho*2) + (self.dff*0.5) + \
              (self.phy*1.5) + (self.pas*2)
        result = ovr/12
        return int(result)




player1 = Player("Christiano Ronaldo",91,91,95,85,45,90)
player2 = Player("Lionel Messi",95,95,90,100,60,85)
player_list = [player1,player2]
#print(player_list[1].overall())

x = 0
for i in player_list:
    print(player_list[x].name)
    print(i.overall())
    x += 1
"""
print("Ronaldo: ",player1.overall())
print("Messi: ",player2.overall())
#__str__ fonksiyonu olmadan player1 yazdırılmak istenirse ramdeki adresi yazdırılır.
"""