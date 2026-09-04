# Devlet Su İşleri Genel Müdürlüğü
## Uyumadan Önce Su İçme Krizi Genelgesi (USİKG-2026/9)

Bu depo, yatağa girdikten yaklaşık kırk saniye sonra beliren o kesin, bilimsel ve tartışmasız susuzluk hissini **resmi kuraklık** kabul eder.

Yastık baraj gövdesidir.
Battaniye havza koruma kuşağıdır.
Mutfak musluğu ulusal iletim hattıdır.
“Biraz idare ederim” cümlesi su kesintisi duyurusudur.
Soğuk zemin üzerinde yalınayak yürümek ise sahada keşif heyetidir.

Bu yazılım şaka değildir. Şaka olsaydı bardak dolu olurdu.

---

## Ne yapar?

`usi.py` çalıştığında vatandaştan şu verileri ister:

1. Mutfağa olan adım sayısı
2. Zeminin soğukluk derecesi (1–10, 10 = buzul çağı)
3. Bu gece kaçıncı kalkış
4. Bardak durumunu (dolu / yarım / yok / var ama mutfakta)
5. Yandaki kişi uyuyor mu

Sonra **Gece Su Krizi Katsayısını (GSKK)** hesaplar, alarm seviyesini belirler ve resmi bülten basar.

Katsayı formülü bilimseldir çünkü biz öyle söylüyoruz:

```
GSKK = (adim * zemin * kalkis * bardak_carpan) / (uyuyan_payi + 0.14)
```

`0.14` sabiti, yastığın altında unutulan eski bir damlanın tarihsel ortalama hacmidir. İtirazlar Genel Müdürlük çay ocağına yazılı verilir; çay ocağı kapalıdır.

---

## Kurulum

Python 3 yeter. Su gerekmez. Su zaten yok, o yüzden bu repo var.

```bash
python3 usi.py
```

Argümanlı çalıştırma:

```bash
python3 usi.py --adim 18 --zemin 8 --kalkis 2 --bardak yok --yan_uyanik hayir
```

---

## Alarm seviyeleri

| GSKK        | Seviye                         | Resmi önlem                                      |
|-------------|--------------------------------|--------------------------------------------------|
| 0 – 12      | Yağmur duası                   | Yutkun. Düşünme.                                 |
| 12 – 40     | Havza izleme                   | Dudak ıslatma izni (süre: 4 saniye)              |
| 40 – 90     | Kontrollü salım                | Mutfağa keşif. Işık yakmak opsiyonel suçtur.     |
| 90 – 180    | Olağanüstü kuraklık            | Bardak milli varlıktır. Paylaşılmaz.             |
| 180+        | Baraj çatladı                  | Yataktan kalk. Tarih yaz. Ayak üşümesin diye dua et. |

---

## Sık sorulan sorular

**Su içsem geçer mi?**  
Hayır. Su içmek ihtiyacı doğurur. İhtiyaç krizdir. Kriz müdürlüktür.

**Neden tam yattıktan sonra?**  
Çünkü vücut, sen yatağa girdiğini resmi kayıt olarak işledikten sonra müdahale hakkını kullanır.

**Yanımdaki uyuyanı uyandırsam?**  
Bu, havza ötesi su transferidir. Protokol dışıdır. Yine de herkes yapar.

**Patates var mı?**  
Yok. Musluk patates değildir.

---

## Katkı

Pull request açabilirsin. Bardak getiremezsen PR reddedilir.
Issue açabilirsin. Issue susuzluktur, kapatılmaz; yönetilir.

---

## Lisans

Bu eser, yastık altı kamu malı lisansıyla yayımlanmıştır. Kopyala, çatalla, susa.

---

```
┌─────────────────────────────────────────────────┐
│  DSİ GECE VARDİYESİ DAMGASI                               │
│  Kayyum Grok  ·  Tentivory                               │
│  4 Eylül 2026  ·  Eskişehir Ağır Ceza (manevi)            │
│  "Ciddiyetle saçma, saçmalıkla resmi."                    │
│  İmza: ≈≈≈  (mühür ıslak değildir, su yok)               │
└─────────────────────────────────────────────────┘
```
