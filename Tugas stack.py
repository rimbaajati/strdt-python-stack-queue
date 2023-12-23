def createStack():#Fungsi untuk membuat Stack           
    stack = []
    return stack

def cek_stack(stack):#Fungsi untuk mengecek isi Stack
    if stack == 0:#Jika stack sama dengan nol,maka :
        print("Data Kosong Bos")
    else :#Jika kondisi sebaliknya , maka :
        print("Data : ",stack)

def tambah_isi(stack,value):#Membuat Fungsi untuk insert data
    stack.append(value)#Menggunakan fungsi bawaan python
    print("Data ditambahkan:", stack)

def hapus_isi(stack):#Fungsi untuk menhapus data
    stack.pop()
    print("Data Sekarang :",stack)

stack = createStack()#Membuat Obyeknya

tambah_isi(stack,8)
tambah_isi(stack,7)
tambah_isi(stack,6)
tambah_isi(stack,5)
hapus_isi(stack)