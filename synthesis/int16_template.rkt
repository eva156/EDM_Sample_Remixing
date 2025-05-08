#lang rosette

;; 16-bit bitvector template for mapping beat indices to Bools

(require rosette/lib/synthax)

;; define 16-bit bitvector
(define int32? (bitvector 16))

;; even/odd and small divisibility predicates
(define (int32 i)
  (bv i int32?))

(define (bveven? y)
  (bvzero? (bvand y (int32 1)))
  )

(define (bvodd? y)
  (bveq (bvand y (int32 1)) (int32 1))
  )

(define (bvdiv2? y)
  (bvzero? (bvand y (int32 1)))
)

(define (bvdiv4? y)
  (bvzero? (bvand y (int32 3)))
  )

(define (bvdiv8? y)
  (bvzero? (bvand y (int32 7)))
  )

(define (bvdiv? n m)
  (bvzero? (bvsmod m n))
  )

(define (bvmodfaster n m)
  (if (bveq (bvand m (bvsub1 m)) (int32 0))
      (bvand n m)
      (bvsmod n m)
      )
  )

(define (bvdiv3? y)
  (bvzero? (bvsmod y (int32 3))))

(define (bvdiv5? y)
  (bvzero? (bvsmod y (int32 5))))

(define (bvdiv6? y)
  (bvzero? (bvsmod y (int32 6))))

(define (bvdiv7? y)
  (bvzero? (bvsmod y (int32 7))))

(define (bvdiv9? y)
  (bvzero? (bvsmod y (int32 9))))

;; grammar for building arithmetic expressions over x
(define-grammar (beat-mapper2 x)
  [expr
   (choose x (?? int32?)
           ((bop) (expr) (expr))
           ((uop) (expr)))]
  [bop
   (choose bvadd bvsub
           bvshl bvashr)]
  [uop
   (choose bvneg bvadd1 bvsub1)]
  )

;; grammar for comparisons and Boolean ops
(define-grammar (beat-cmp x)
  [cmp
   (choose
    #t #f
    ((op) (beat-mapper2 x) (beat-mapper2 x))
    ((oneop) (beat-mapper2 x))
    (and (cmp) (cmp))
    (or (cmp) (cmp))
    (not (cmp)))]
  [op
   (choose
    bvslt bvsle bvsgt bvsge bveq)]
  [oneop
   (choose
    bvzero? bveven? bvodd? bvdiv4? bvdiv8? false?)]
  )

;; grammar for final branch structure
(define-grammar (beat-if x)
  [term
   (choose #t #f (beat-cmp x)
           (if (beat-cmp x) (term) (term)))]
  )

(define (beatmapper-sketch x)
      (beat-if x)
  )
;; set maximum recursion depth for grammar
(current-grammar-depth 2)
;; define symbolic input x with range 0..upper_bound
(define-symbolic x int32?)
(current-bitwidth 32)

;; synthesise a function satisying the assertions
(define sol
  (synthesize
   #:forall (list x)
   #:guarantee (begin
                 (assume (bvsge x (int32 0)))
                 (assume (bvsle x (int32 16)))
                 (<=> (bvzero? x) (beatmapper-sketch x))
   ))
  )
;;sol

(print-forms sol)