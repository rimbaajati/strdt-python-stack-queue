front = 0
rear = 0
mymax = eval(input("Masukkan jumlah maksimum antrian: "))

def createQueue():
    queue = []
    return queue

def isEmpty(queue):
    return len(queue) == 0

def enqueue(queue, item):
    queue.append(item)
    print("--Memasukkan", item, "ke antrian--")

def dequeue(queue):
    if isEmpty(queue):
        return "Kosong Boss"
    item = queue[0]
    del queue[0]
    return item

queue = createQueue()

while True:
    print("1. Masuk")
    print("2. Bayar")
    print("3. Show")
    print("4. Quit")
    
    ch = int(input("Masukkan pilihan: "))
    
    if ch == 1:
        if rear < mymax:
            item = input("Masukkan No.Member: ")
            enqueue(queue, item)
            rear += 1
        else:
            print("Antrian sudah penuh")
    elif ch == 2:
        print("Segera Eksekusi :" + dequeue(queue))
    elif ch == 3:
        if queue == 0:
            print("Kosong Bos!!")
        else:
            print(queue)
    elif ch == 4:
        print("Keluar... Sampai jumpa lagi..")
        break
