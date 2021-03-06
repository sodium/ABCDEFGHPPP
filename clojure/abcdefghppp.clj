; http://m2.hkgolden.com/view.aspx?message=6307521&type=SW&page=1
; binc
(defn make-seq []

  (map read-string

       (for [x (range 10)

             y (range 10)

             :when (and (not= x y) (not= x 0))]

         (apply str [x y]))))



(defn test-form []

  (let [mq (make-seq)]

    (->>

     (for [ab mq

           cd mq

           gh mq

           :let [ef (- ab cd)

                 ppp (+ ef gh)

                 v2s (fn [v] (reduce #(clojure.set/union %1 (set (str %2))) #{} v))]

           :when (and (= 1 (count (set (str ppp))))

                      (> ppp 99))]

       [ab cd ef gh ppp])

     (filter #(= 9 (count (v2s %)))))))




(test-form)

;; ([85 46 39 72 111] [86 54 32 79 111] [90 27 63 48 111] [90 63 27 84 111] [95 27 68 43 111])
