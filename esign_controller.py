import time

from PyPDF2 import PdfReader
from PyPDF2.errors import PdfReadError

def check_signature(pdf_path):
    try:
        reader = PdfReader(pdf_path)
        if "/AcroForm" in reader.trailer["/Root"]:
            acroform = reader.trailer["/Root"]["/AcroForm"]
            if "/SigFlags" in acroform:
                print("Bu PDF dosyasında e-imza var.")
                time.sleep(1)
                return
        print("Bu PDF dosyasında e-imza bulunamadı.")
        return
    except FileNotFoundError:
        print("Dosya bulunamadı!")
    except PdfReadError:
        print("PDF dosyası okunurken bir sorun oluştu!")

def main():
    dosyaYol = input("Dosya yolu giriniz: ")
    if dosyaYol == "":
        print("Geçersiz dosya yolu girdiniz!")
        main()
    else:
        check_signature(dosyaYol)

main()