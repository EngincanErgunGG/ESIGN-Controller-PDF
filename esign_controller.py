from PyPDF2 import PdfReader
from PyPDF2.errors import PdfReadError

print("Programı sonlandırmak için CTRL+C tuşlarına basınız.")

def check_signature(pdf_path):
    try:
        reader = PdfReader(pdf_path)
        if "/AcroForm" in reader.trailer["/Root"]:
            acroform = reader.trailer["/Root"]["/AcroForm"]
            if "/SigFlags" in acroform:
                print("Bu PDF dosyasında e-imza var.")
                main()
                return
        print("Bu PDF dosyasında e-imza bulunamadı.")
        main()
    except FileNotFoundError:
        print("Dosya bulunamadı!")
        main()
    except PdfReadError:
        print("PDF dosyası okunurken bir sorun oluştu!")
        main()
    except KeyboardInterrupt:
        print("Program sonlandırıldı. Pencere kapatılıyor..")

def main():
    try:
        dosyaYol = input("Dosya yolu giriniz: ")
        if dosyaYol == "":
            print("Geçersiz dosya yolu girdiniz!")
            main()
        else:
            check_signature(dosyaYol)
    except KeyboardInterrupt:
        print("Program sonlandırıldı. Pencere kapatılıyor.")
main()