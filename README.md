YouTube Video İndirme Aracı
Bu Python kodu, belirttiğiniz bir YouTube kanalındaki videoları indirmenizi sağlar. İndirilen videolar "indirilenler" adlı klasöre kaydedilir. Bu rehber, kodu nasıl kullanabileceğinizi adım adım açıklar.

Gereksinimler
1. Python Yüklemesi
Sisteminizde Python 3.x sürümünün kurulu olduğundan emin olun.
2. Gerekli Python Paketlerinin Yüklenmesi
yt-dlp kütüphanesi, YouTube videolarını indirmek için kullanılır. Aşağıdaki komutla bu kütüphaneyi yükleyin:

pip install yt-dlp

3. FFmpeg Yüklemesi
FFmpeg, video ve ses dosyalarını işlemek için kullanılan bir araçtır. Aşağıdaki adımları takip ederek FFmpeg'i kurun:

FFmpeg'in resmi web sitesinden uygun sürümü indirin.
FFmpeg'i uygun bir klasöre çıkarın (örneğin, C:\ffmpeg).
ffmpeg.exe dosyasının yolunu kontrol edin ve doğru şekilde kodda belirtildiğinden emin olun (C:\ffmpeg\ffmpeg.exe).
4. İndirilecek Klasörün Oluşturulması
Kod, "indirilenler" adlı bir klasör oluşturur ve videoları bu klasöre kaydeder. Klasör otomatik olarak oluşturulacaktır, bu yüzden ek bir işlem yapmanıza gerek yoktur.

5. Kodun Çalıştırılması
Yukarıdaki adımları tamamladıktan sonra, kodu çalıştırabilirsiniz. Kod çalıştırıldığında, belirttiğiniz YouTube kanalındaki videolar indirilecek ve "indirilenler" klasörüne kaydedilecektir.

6. Kullanıcı Girdisi
Kodun şu kısmında:

python
ydl.download(["Bu kısma kanal linkini giriniz"])
Bu kısma kanal linkini giriniz kısmını indirmek istediğiniz YouTube kanalının linki ile değiştirin.

Özet
Python 3.x sürümünün kurulu olduğundan emin olun.
yt-dlp kütüphanesini yükleyin.
FFmpeg'i doğru bir şekilde yükleyip yapılandırın.
İndirilecek YouTube kanal linkini doğru bir şekilde girin.
