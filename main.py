kuyruk={"on":0,"boyut":0,"arka":-1,"dizi":[]}
kuyruk["arka"]=len(kuyruk["dizi"])-1
def bosMu():
    return (kuyruk["boyut"]==0)

def enqueue(eleman):
    kuyruk["dizi"].append(eleman)
    kuyruk["arka"]+=1
    kuyruk["boyut"]+=1
    print(f"{eleman} kuyruk eklendi!")


def dequeue():
    if bosMu():
        print("Eleman silinemedi kuyruk bos")
        return
    eleman=kuyruk["dizi"][kuyruk["on"]]
    kuyruk["dizi"].pop(kuyruk["on"])
    kuyruk["boyut"]-=1
    print(f"{eleman} kuyruktan silindi! ")



def tumKuyruk():

    for i in range(0,kuyruk["boyut"]):
        eleman=kuyruk["dizi"][i]
        print(f"|{i}.   {eleman}.|",end="\t")
    print()




enqueue(5)
enqueue(6)
tumKuyruk()
dequeue()
tumKuyruk()
enqueue(15)
enqueue(25)
enqueue(35)
tumKuyruk()
dequeue()
tumKuyruk()