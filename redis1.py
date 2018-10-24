import redis
import random
import time

r = redis.Redis(host="localhost",port=6379,db=0)

listTenSach = ["In Search of Lost Time by Marcel Proust","Don Quixote by Miguel de Cervantes","Ulysses by James Joyce","The Great Gatsby by F. Scott Fitzgerald",
            "Moby Dick by Herman Melville","Hamlet by William Shakespeare","War and Peace by Leo Tolstoy","The Odyssey by Homer","One Hundred Years of Solitude by Gabriel Garcia Marquez",
            "The Divine Comedy by Dante Alighieri","The Brothers Karamazov by Fyodor Dostoyevsky","Madame Bovary by Gustave Flaubert"," The Adventures of Huckleberry Finn by Mark Twain",
            "The Iliad by Homer","Lolita by Vladimir Nabokov"]
listTen = ["Livinus","James","Michael","David","John","Kevin","Robert","Thomas","Emily","Mark","Matthew","Anthony","Anna",
            "Daniel","William","Jessica","Brian","Elizabeth","Christopher","Paul","Jennifer","Stephen","Emma","Alexander",
            "Sarah","Joseph","Chaima","Dennis","Maria","Rebecca","Ashley","Ryan","Patrick","Jeffrey","Charles","Richard","Andrea",
            "Heather","Michelle","Taylor","Rachel","Laura","Kimberly","Linda","Andrew"]
listEmail = ["@gmail.com","@outlook.com","@yahoomail.com","@yanindex.com","@ProtonMail.com","@Gmx.com","@Mail.com"]
# listNXB = ["Chinh tri quoc gia","Tu phap","Kim Dong","My thuat","Quan doi","Phu nu","Lao dong","Thanh nien","Tai chinh","Thong ke",
#         "Xay dung","Dai hoc Quoc gia TP HCM","Dai hoc quoc gia Ha Noi","Dai hoc su pham","Y hoc"]
def insertSACH():
    for i in range(0,10000):
        tenSach = str(listTenSach[random.randint(0,len(listTenSach)-1)])
        soTrang = str(random.randint(1,1000))
        MSNXB = "NXB" + str(random.randint(1,100))
        key = "sach" + str(i +1)
        values = tenSach +"," + soTrang + ","+ MSNXB
        r.set(key,values)

def insertTACGIA():
    for i in range(0,10000):
        tenTacGia = str(listTen[random.randint(0,len(listTen)-1)])
        soDT = "0987" + str(random.randint(10000,100000))
        eMail = tenTacGia + str(listEmail[random.randint(0,len(listEmail)-1)])
        key = "tacgia" + str(i +1)
        values = tenTacGia + "," + soDT +"," + eMail
        r.set(key,values)

def insertTACGIASACH():
    for i in range(0,50000):
        MSTG = "tacgia" + str(i+1)
        MSSACH = "sach" + str(i+1)
        key = "tgs" + str(i+1)
        values = MSTG + "," + MSSACH
        r.set(key,values)


def insertNXB():
    for i in range(0,100):
        tenNXB = "TENNXB" + str(i+1)
        eMail = tenNXB + str(listEmail[random.randint(0,len(listEmail)-1)])
        soDT = "0987" + str(random.randint(10000,100000))
        key = "NXB" + str(i + 1)
        values = tenNXB + "," + soDT + "," + eMail
        r.set(key,values)

def select_not_where():
    # tim tat ca cac nha xuat ban
    for key in r.scan_iter("NXB*"):
        values = r.get(key)
        # format thanh kieu tring
        values = key.decode("UTF8") + "," + values.decode("UTF8")
        print(values)

def select_in_pk():
    # tim thong tin cua quyen sach co ms "sach69"
    values = r.get("sach69")
    values = "sach69" + "," + values.decode("UTF8")
    print(values)

def select_notin_pk():
    # tim tac gia co email la Heather@yahoomail.com
    values = ""
    for key in r.scan_iter("*"):
        temp = r.get(key).decode("UTF8")
        if ("Heather@yahoomail.com" in temp):
            values = key.decode("UTF8") + "," + temp
            print(values)
    if(values == ""):
        print("ko tim thay tac gia co email Heather@yahoomail.com")
        

def select():
    # print("select khong co dieu kien")
    # select_not_where()
    # print("select co dieu kien tren khoa chinh")
    # select_in_pk()
    print("select co dieu kien khong tren khoa chinh")
    select_notin_pk()


def main():
#     start_time = time.time()
#     insertSACH()
#     insertTACGIA()
#     insertTACGIASACH()
#     insertNXB()
#     end_time = time.time()
#     print ('total time insert data: %f ms' % ((end_time - start_time) * 1000))
    select()
if __name__ == '__main__':
    main()
    print("finish program")