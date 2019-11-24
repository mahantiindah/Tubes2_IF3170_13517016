(deftemplate avh (field a) (field v) (field h))

(deftemplate avh (field a) (field v) (field h))

; sisi: {total,kembar-dua,kembar-satu,berantakan}
; sudut: {total,kembar-dua,kembar-satu,berantakan}
; jenis-sudut: {tumpul,lancip,siku}
; titik: {3,4,5,6}


;menentukan jenis bangun apa 
(defrule segitiga
  (av (a titik) (v 3))
  => 
  (assert (jenis segitiga)
  )
)

(defrule segiempat
  (av (a titik) (v 4))
  => 
  (assert (jenis segiempat)
  )
)

(defrule segilima
  (av (a titik) (v 5))
  => 
  (assert (jenis segilima)
  )
)

(defrule segienam
  (av (a titik) (v 6))
  => 
  (assert (jenis segienam)
  )
)

;segi 6
(defrule segi-enam-sama-sisi
  (av (a jenis) (v segienam))
  (av (a sisi) (v total))
  => 
  (assert (solution bangun segienam-sama-sisi)
  )
)

(defrule segi-enam-berantakan
  (av (a jenis) (v segienam))
  (av (a sisi) (v berantakan))
  => 
  (assert (solution bangun segienam-berantakan)
  )
)


;segi 5

(defrule segi-lima-sama-sisi
  (av (a jenis) (v segilima))
  (av (a sisi) (v total))
  => 
  (assert (solution bangun segilima-sama-sisi)
  )
)

(defrule segi-lima-berantakan
  (av (a jenis) (v segilima))
  (av (a sisi) (v berantakan))
  => 
  (assert (solution bangun segilima-berantakan)
  )
)

;segi4

(defrule jajar-genjang
  (av (a jenis) (v segiempat))
  (av (a sudut) (v kembar-dua))
  (av (a sisi) (v kembar-dua))

  => 
  (assert (solution bangun jajar-genjang)
  )
)

(defrule layang-layang
  (av (a jenis) (v segiempat))
  (av (a sudut) (v kembar-satu))
  (av (a sisi) (v kembar-dua))

  => 
  (assert (solution bangun layang-layang)
  )
)

(defrule persegi
  (av (a jenis) (v segiempat))
  (av (a sudut) (v total))
  (av (a sisi) (v total))

  => 
  (assert (solution bangun persegi)
  )
)

;untuk trapesium belum nemu caranya
(defrule trapesium-sama-kaki
  (av (a jenis) (v segiempat))
  (av (a sudut) (v total))
  (av (a sisi) (v total))

  => 
  (assert (solution bangun trapesium-sama-kaki)
  )
)

;belum
(defrule trapesium-rata-kiri
  (av (a jenis) (v segiempat))
  (av (a sudut) (v total))
  (av (a sisi) (v total))

  => 
  (assert (solution bangun trapesium-rata-kiri)
  )
)

;belum
(defrule trapesium-rata-kanan
  (av (a jenis) (v segiempat))
  (av (a sudut) (v total))
  (av (a sisi) (v total))

  => 
  (assert (solution bangun trapesium-rata-kanan)
  )
)

;segitiga

(defrule segitiga-sama-sisi
  (av (a jenis) (v segitiga))
  (av (a sisi) (v total))

  => 
  (assert (solution bangun segitiga-sama-sisi)
  )

; setelah ini segitiga sama kaki
(defrule segitiga-sama-kaki-tumpul
  (av (a jenis) (v segitiga))
  (av (a sisi) (v kembar-satu))
  (av (a sudut) (v tumpul))
  => 
  (assert (solution bangun segitiga-sama-kaki-tumpul)
  )


(defrule segitiga-sama-kaki-lancip
  (av (a jenis) (v segitiga))
  (av (a sisi) (v kembar-satu))
  (av (a sudut) (v lancip))
  => 
  (assert (solution bangun segitiga-sama-kaki-lancip)
  )

(defrule segitiga-sama-kaki-siku
  (av (a jenis) (v segitiga))
  (av (a sisi) (v kembar-satu))
  (av (a sudut) (v siku))
  => 
  (assert (solution bangun segitiga-sama-kaki-siku)
  )

;setelah ini rules untuk segitiga gak sama kaki
(defrule segitiga-tumpul
  (av (a jenis) (v segitiga))
  (av (a sisi) (v berantakan))
  (av (a sudut) (v tumpul))
  => 
  (assert (solution bangun segitiga-tumpul)
  )

(defrule segitiga-lancip
  (av (a jenis) (v segitiga))
  (av (a sisi) (v berantakan))
  (av (a sudut) (v lancip))
  => 
  (assert (solution bangun segitiga-lancip)
  )

(defrule segitiga-siku
  (av (a jenis) (v segitiga))
  (av (a sisi) (v berantakan))
  (av (a sudut) (v siku))
  => 
  (assert (solution bangun segitiga-siku)
  )

