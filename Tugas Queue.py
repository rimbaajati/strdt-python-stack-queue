import os
import datetime

class Queue:
    def __init__(self,size=10):
        self.size = size
        self.current_size = 0
        self.data= [None]*size
        self.front = None
        self.back = None

    def antrian_kosong(self): #Memeriksa apakah queue kosong
        if self.current_size == 0 :
            return True
        print("List Kosong")
        

    def isi(self) : #Memeriksa apakah queue berisi
        if self.current_size == self.size:
            return True
        else :
            return False
        
    def cek_atrian(self): #Memeriksa panjang antrian
         print("panjang Antrian :")
         return self.current_size

    def enqueue(self,data): #Menambah data
        if self.back is not None :
            self.back = (self.back +1)
            print("Data Masuk :" , self.data)
        else :
            self.front = 0
            self.back = 0

        self.data[self.back] = data
        self.current_size = self.current_size +1

    def dequeue(self): #Menghapus Data
        if self.kosong():
            print("Kosong")
        else :
            datakeluar = self.data[self.front]
            self.front+=1
            self.current_size = self.current_size -1

            return datakeluar     

myqueue=Queue()

while True:
    print("1. Customer Service")
    print("2. Teller")

    ch = int(input("Masukan Pilihan :"))

    if ch == 1 :
        while True :
            print("1.  ")  

