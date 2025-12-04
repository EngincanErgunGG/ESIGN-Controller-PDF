# ESIGN-CONTROLLER-PDF

Bu küçük Python aracı, PDF dosyalarında e-imza olup olmadığını kontrol eder.

## Kurulum

1. Repoyu klonla:
   git clone https://github.com/EngincanErgunGG/ESIGN-CONTROLLER-PDF.git

2. Bağımlılıkları yükle:
   pip install -r requirements.txt
* Bağımlılıkları yüklemeden kullanmaya çalışmanız durumunda hata alabilirsiniz.

## Kullanım

   Terminal üzerinde projeyi klonladığınız klasörde;
```
cd ESIGN-CONTROLLER-PDF
python esign_controller.py
```
Ardından dosya yolunu girmeniz istenir. Program PDF dosyasında e-imza olup olmadığını kontrol eder.

## Örnek Çıktı

Dosya yolu giriniz: test.pdf
Bu PDF dosyasında e-imza var.

Dosya yolu giriniz: bos.pdf
Bu PDF dosyasında e-imza bulunamadı.