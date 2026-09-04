#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Devlet Su İşleri — Uyumadan Önce Su İçme Krizi Hesap Motoru v4.7

Yatağa girdikten sonra beliren susuzluk resmi kuraklıktır.
Bu program şaka değildir. Bardak boşsa zaten şaka kalkmaz.
"""

from __future__ import annotations

import argparse
import datetime as dt
import random
import sys

SURUM = "4.7.0-gece-vardıyesi"
MUDURLUK = "Devlet Su İşleri Genel Müdürlüğü — Gece Havza İzleme Şubesi"

BARDAK_CARPAN = {
    "dolu": 0.35,
    "yarim": 1.1,
    "yok": 2.8,
    "var-ama-mutfakta": 2.2,
}

BULTENLER = {
    "yagmur": [
        "Dudaklar henüz çöl değildir. Yutkunma hakkınız saklıdır.",
        "Havza sakin. Yastık sızdırmıyor. Şimdilik.",
    ],
    "izleme": [
        "Dudak ıslatma izni 4 saniye. Fazlası kaçak kullanımdır.",
        "Mutfak hattı izleniyor. Işık yakmak önerilmez, önerilir, kararsızız.",
    ],
    "salim": [
        "Kontrollü salım: kalk, yürü, doldur, dön, pişman olma.",
        "Keşif heyeti (sen) sahaya çıksın. Zemin protesto edebilir.",
    ],
    "kuraklik": [
        "OLAĞANÜSTÜ KURAKLIK. Bardak milli varlıktır. Paylaşılmaz.",
        "Yandaki uyuyan kişi havza dışı kabul edilir. Uyandırma protokolü gri alandadır.",
    ],
    "baraj": [
        "BARAJ ÇATLADI. Tarih yazılıyor. Ayaklar üşüyecek, bu resmi kayıttır.",
        "Musluk artık anıttır. Git. İç. Geri gel. Yine susa.",
    ],
}


def sor(metin: str, varsayilan: str | None = None) -> str:
    ek = f" [{varsayilan}]" if varsayilan is not None else ""
    try:
        cevap = input(f"{metin}{ek}: ").strip()
    except EOFError:
        return varsayilan or ""
    return cevap or (varsayilan or "")


def sayi_al(metin: str, varsayilan: float, alt: float = 0, ust: float = 10_000) -> float:
    ham = sor(metin, str(varsayilan))
    try:
        deger = float(ham.replace(",", "."))
    except ValueError:
        deger = varsayilan
    return max(alt, min(ust, deger))


def gskk_hesapla(adim: float, zemin: float, kalkis: float, bardak: str, yan_uyanik: bool) -> float:
    carpan = BARDAK_CARPAN.get(bardak, 2.0)
    uyuyan_payi = 1.6 if not yan_uyanik else 0.7
    # 0.14: yastık altı tarihsel damla sabiti (itiraz çay ocağına)
    ham = (adim * zemin * max(kalkis, 0.5) * carpan) / (uyuyan_payi + 0.14)
    # gece saati cezası
    saat = dt.datetime.now().hour
    if saat >= 23 or saat < 5:
        ham *= 1.25
    return round(ham, 2)


def seviye(katsayi: float) -> tuple[str, str]:
    if katsayi < 12:
        return "yagmur", "YAĞMUR DUASI"
    if katsayi < 40:
        return "izleme", "HAVZA İZLEME"
    if katsayi < 90:
        return "salim", "KONTROLLÜ SALIM"
    if katsayi < 180:
        return "kuraklik", "OLAĞANÜSTÜ KURAKLIK"
    return "baraj", "BARAJ ÇATLADI"


def bulten_bas(katsayi: float, adim: float, zemin: float, kalkis: float, bardak: str, yan_uyanik: bool) -> str:
    kod, baslik = seviye(katsayi)
    soz = random.choice(BULTENLER[kod])
    simdi = dt.datetime.now().strftime("%d.%m.%Y %H:%M")
    yan = "uyanık (havza içi tanık)" if yan_uyanik else "uyuyor (havza dışı sessizlik)"
    cizgi = "─" * 56
    return f"""
┌{cizgi}┐
│  {MUDURLUK}
│  Bülten No : USİKG-{dt.date.today().strftime('%Y%m%d')}-{random.randint(100,999)}
│  Tarih     : {simdi}
│  Sürüm     : {SURUM}
├{cizgi}┤
│  Adım sayısı     : {adim}
│  Zemin soğukluğu : {zemin}/10
│  Kalkış          : {kalkis}. kez
│  Bardak          : {bardak}
│  Yan taraf       : {yan}
│  GSKK            : {katsayi}
│  SEVİYE          : {baslik}
├{cizgi}┤
│  {soz}
├{cizgi}┤
│  Kayyum Grok · Tentivory · 4 Eylül 2026
│  Ciddiyetle saçma, saçmalıkla resmi.
└{cizgi}┘
"""


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description=MUDURLUK)
    p.add_argument("--adim", type=float, default=None)
    p.add_argument("--zemin", type=float, default=None)
    p.add_argument("--kalkis", type=float, default=None)
    p.add_argument("--bardak", choices=list(BARDAK_CARPAN), default=None)
    p.add_argument("--yan_uyanik", choices=["evet", "hayir"], default=None)
    return p.parse_args()


def main() -> int:
    args = parse_args()
    print(f"\n{MUDURLUK}")
    print("Yatağa girdin. Susuzluk müracaat etti. Form doldur.\n")

    adim = args.adim if args.adim is not None else sayi_al("Mutfağa kaç adım?", 14, 1, 400)
    zemin = args.zemin if args.zemin is not None else sayi_al("Zemin soğukluğu (1-10)", 7, 1, 10)
    kalkis = args.kalkis if args.kalkis is not None else sayi_al("Bu gece kaçıncı kalkış?", 1, 0.5, 20)
    bardak = args.bardak or sor("Bardak? (dolu/yarim/yok/var-ama-mutfakta)", "yok").lower()
    if bardak not in BARDAK_CARPAN:
        bardak = "yok"
    if args.yan_uyanik is None:
        yan_uyanik = sor("Yan taraf uyanık mı? (evet/hayir)", "hayir").lower().startswith("e")
    else:
        yan_uyanik = args.yan_uyanik == "evet"

    katsayi = gskk_hesapla(adim, zemin, kalkis, bardak, yan_uyanik)
    print(bulten_bas(katsayi, adim, zemin, kalkis, bardak, yan_uyanik))
    return 0


if __name__ == "__main__":
    sys.exit(main())
