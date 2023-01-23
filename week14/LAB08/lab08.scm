;;; Lab08: Scheme

(define (over-or-under a b)
  (cond
    ((< a b) -1)
    ((> a b) 1)
    (else 0)
  )
)


(define (make-adder n)
  (lambda (m) (+ m n))
)


(define (composed f g) ; f(g(x))
  (lambda (x) (f (g x)))
)


(define (remainder a b)
  (- a (* b (quotient a b))))

(define (gcd a b)
  (if (= b 0) a (gcd b (remainder a b)))
)


(define lst
  (cons 1 2 (cons 3 (cons 4 nil) 5))
)


(define (ordered s)
  (or (null? s) (null? (cdr s)) (and (<= (car s) (car (cdr s))) (ordered (cdr s))))
)
