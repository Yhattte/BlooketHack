#Script to kick all players from Blooket
#Original Code: iCrazeiOS; Modifyed By: kgsensei
import requests, json

gamePin=str(input("Game pin: "))
r=requests.put("https://api.blooket.com/api/firebase/join",data={"id":gamePin,"name":"blooketbad"},headers={"Referer":"https://www.blooket.com/"})
joinText=r.text
r=requests.delete(f"https://api.blooket.com/api/firebase/client?id={gamePin}&name=blooketbad",headers={"Referer":"https://www.blooket.com/"})
players=json.loads(joinText)["host"]["c"].keys()
for playerName in players:
	r=requests.delete(f"https://api.blooket.com/api/firebase/client?id={gamePin}&name={playerName}",headers={"Referer":"https://www.blooket.com/"})