; sisi: {total,kembar-dua,kembar-satu,berantakan}
; sudut: {total,kembar-dua,kembar-satu,berantakan}
; jenis-sudut: {tumpul,lancip,siku}
; titik: {3,4,5,6}


;menentukan jenis bangun apa 
(defrule segitiga
  (titik 3)
  => 
  (assert (jenis segitiga)
  )
)

(defrule segiempat
  (titik 4)
  => 
  (assert (jenis segiempat)
  )
)

(defrule segilima
  (titik 5)
  => 
  (assert (jenis segilima)
  )
)

(defrule segienam
  (titik 6)
  => 
  (assert (jenis segienam)
  )
)

;segi 6
(defrule segi-enam-sama-sisi
  (jenis segienam)
  (sisi total)
  => 
  (assert (solution bangun segienam-sama-sisi)
  )
)

(defrule segi-enam-berantakan
  (jenis segienam)
  (sisi berantakan)
  => 
  (assert (solution bangun segienam-berantakan)
  )
)


;segi 5

(defrule segi-lima-sama-sisi
  (jenis segilima)
  (sisi total)
  => 
  (assert (solution bangun segilima-sama-sisi)
  )
)

(defrule segi-lima-berantakan
  (jenis segilima)
  (sisi berantakan)
  => 
  (assert (solution bangun segilima-berantakan)
  )
)

;segi4

(defrule jajar-genjang
  (jenis segiempat)
  (sudut kembar-dua)
  (sisi kembar-dua)

  => 
  (assert (solution bangun jajar-genjang)
  )
)

(defrule layang-layang
  (jenis segiempat)
  (sudut kembar-satu)
  (sisi kembar-dua)

  => 
  (assert (solution bangun layang-layang)
  )
)

(defrule persegi
  (jenis segiempat)
  (sudut total)
  (sisi total)

  => 
  (assert (solution bangun persegi)
  )
)

;untuk trapesium belum nemu caranya
(defrule trapesium-sama-kaki
  (jenis segiempat)
  (sudut kembar-dua)
  (sisi kembar-satu)
  

  => 
  (assert (solution bangun trapesium-sama-kaki)
  )
)

;belum
(defrule trapesium-rata-kiri
  (jenis segiempat)
  (sudut berantakan)
  (sisi berantakan)
  (sudut siku)
  (siku kiri)

  => 
  (assert (solution bangun trapesium-rata-kiri)
  )
)

;belum
(defrule trapesium-rata-kanan
  (jenis segiempat)
  (sudut berantakan)
  (sisi berantakan)
  (sudut siku)
  (siku kanan)

  => 
  (assert (solution bangun trapesium-rata-kanan)
  )
)

;segitiga

(defrule segitiga-sama-sisi
  (jenis segitiga)
  (sisi total)

  => 
  (assert (solution bangun segitiga-sama-sisi)
  )
)

; setelah ini segitiga sama kaki
(defrule segitiga-sama-kaki-tumpul
  (jenis segitiga)
  (sisi kembar-satu)
  (sudut tumpul)
  => 
  (assert (solution bangun segitiga-sama-kaki-tumpul)
  )
)

(defrule segitiga-sama-kaki-lancip
  (jenis segitiga)
  (sisi kembar-satu)
  (sudut lancip)
  => 
  (assert (solution bangun segitiga-sama-kaki-lancip)
  )
)

(defrule segitiga-sama-kaki-siku
  (jenis segitiga)
  (sisi kembar-satu)
  (sudut siku)
  => 
  (assert (solution bangun segitiga-sama-kaki-siku)
  )
)
;setelah ini rules untuk segitiga gak sama kaki
(defrule segitiga-tumpul
  (jenis segitiga)
  (sisi berantakan)
  (sudut tumpul)
  => 
  (assert (solution bangun segitiga-tumpul)
  )
)

(defrule segitiga-lancip
  (jenis segitiga)
  (sisi berantakan)
  (sudut lancip)
  => 
  (assert (solution bangun segitiga-lancip)
  )
)

(defrule segitiga-siku
  (jenis segitiga)
  (sisi berantakan)
  (sudut siku)
  => 
  (assert (solution bangun segitiga-siku)
  )
)


;(printout t crlf crlf))
;untuk solution

(defrule print-solution
  (solution bangun ?h)
  => 
   (printout t
    "masuk solusi"  crlf
    )
)

(defrule startup
  =>
  (printout t
    "startup"  crlf)
  
)

(defrule coba-print
  (jenis segitiga)
  =>
  (printout t
    "nah"  crlf
    )
)