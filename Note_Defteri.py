class Note:
    def __init__(self, note): # Not bilgileri text ve tititle olarak liste halinde alındı ve index numarası kontrol için 0 dan başlatıldı
        self.note = note
        self.index = 0

    def displayTitleNote(self):  # Notların başlıkları sıralı bir şekilde ekrana yazdırılıp hangi not üzerinde işlem yapıcaksa onun cevabı alınıp Answer fonksiyonuna gönderildi.
        noteTitle = self.note

        for title in noteTitle:
            print(title , end='  ') # Birden fazla girilen not bilgilerinin başlıklarını belirli aralıklarla aynı satırda yazdırıp kullanıcıya daha kolay seçme imkanı sunuyoruz.

        print('')
        print('Notlarınız Başarı ile Kaydedilmiştir \n')
        
        answer = input('Hangi Not Üzerinde işlem yapmak istiyorsunuz lütfen başlığını giriniz : ')
        self.noteAnswer(answer) # alınan cevap answer methoduna gönderildi

    def noteAnswer(self,answer):    # Girilen Notların Başlıklarını ekrana getirdikten sonra işlem yapmak istediği notun başlık bilgisini almak için answer değişkenini kullanıyoruz.
        self.answer = answer        # Silme işlemindede kullanabilmek için self. olarak tanımladım.
        if answer in self.note:
            print(f'\nSEÇİLEN NOTUN TEXT BİLGİSİ \n ' , self.note[self.answer]['text'])
            process = str(input('Ekleme yapmak için (E)\n Notu Silmek için (S) yazınız : '))
        self.updateProcessText(process) # Güncelleme yapılacak Nota hangi işlemin yapılacağını belirliyoruz.

    def updateProcessText(self,process):
        
        if process == 'e' or process == 'E':    # Kullanıcı ekleme yapıcak ise kontrol ediliyor
            additions = str(input('Notunuza Eklemek istediklerinizi yazınız; \n'))
            self.updateNotes(additions) # Ekleme yapılması için yazılan not methoda gönderiliyor

        elif process == 's' or process == 'S':
            del self.note[self.answer]
            self.displayTitleNote()
        else:
            print('Geçersiz seçim yaptınız tekrar deneyin')
            self.displayTitleNote()
            
    def updateNotes(self,additions):    # Ekleme  yapılması için Methoda Yukarıdan Text bilgisi geliyor.
        note = self.note[self.answer]['text']   # Notun önceden içerisinde bulunan text bilgisi değişkene aktarılıp saklanıyor
        totalText = note + ' ' + additions  # Ekleme yapılması için gelen text bilgisi ve zaten içerisinde varolan text bilgisi birleştiriliyor
        self.note[self.answer]['text'] = totalText # Belirtilen not belgesinin içeriği birleştirilen text bilgisi ile güncelleniyor
        
        self.displayTitleNote()



notesayisi = int(input('Kaç Adet Not Girmek istiyorsunuz : '))
note = {}   # liste tipi dictionary olması için küme parantezi ile oluşturuldu.
for n in range(notesayisi):
    title = str(input('Not Başlığını Giriniz : '))
    text = str(input('Notunuzu Giriniz : '))
    # Girilen not bilgisi dictionary liste tipinde ve title(key) olarak text bilgisi içerisinde tutuluyor.
    note.update({
        title : {
            'text' : text
        }
    })


notePad = Note(note)
notePad.displayTitleNote()


