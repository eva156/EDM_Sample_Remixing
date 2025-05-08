#lang rosette

(require rosette/lib/synthax)

;; grammar definitions
(define-grammar (beat-mapper2 x)
  [expr
   (choose x (?? integer?)
           (?? boolean?)
           ((bop) (expr) (expr))
           ((uop) (expr)))]
  [bop
   (choose modulo quotient + - * = < >= && ||)]
  [uop
   (choose even? odd? add1 sub1 not zero? positive? negative?)]
  )

(define-grammar (beat-cmp x)
  [cmp
   (choose
    x
    (?? boolean?)
    ((op) (beat-mapper2 x) (beat-mapper2 x))
    ((oneop) (beat-mapper2 x))
    (and (cmp) (cmp))
    (or (cmp) (cmp))
    (not (cmp)))]
  [op
   (choose
    < <= > >= && || =)]
  [oneop
   (choose
    not even? odd? zero? positive? negative?)]
  )

(define-grammar (beat-if x)
  [term
   (choose x (?? boolean?) (beat-mapper2 x)
           (if (beat-cmp x) (term) (term)))]
  )
  
;; function definitions
(define (beatmapper-fun x)
  (assume (>= x 0))
  (assume (<= x 16))
  (beat-if x))

(define (beatmapper-spec candidate)
  (assert (candidate 0))
  )


;; set grammar depth
(current-grammar-depth 2)
(define-symbolic x integer?)

;; set bitwidth
(current-bitwidth 32)

(define sol
  (synthesize
   #:forall (list x)
   #:guarantee (assert (beatmapper-spec beatmapper-fun))
   ))

(print-forms sol)


