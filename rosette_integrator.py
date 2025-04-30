import subprocess
import os
import tempfile

"""
allows for synthesising bitvector and integer programs
via Rosette. Defines several Racket grammar templates for
different bitwidths and domains, and wraps out-of-process
invocation of Racket to run the synthesis.

- run_rosette: write temporary Racket file and invoke racket.exe
- iterative_synth: repeatedly increase grammar depth until synthesis succeeds
"""

# throughout the project the bitvectors are referred to as int32 but in paractice int16s were used
rosette_int16_template = r'''#lang rosette

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
   (choose #t #f (int32 0) (int32 1) (beat-cmp x)
           (if (beat-cmp x) (term) (term)))]
  )

{sketch}

;; set maximum recursion depth for grammar
(current-grammar-depth {depth})
;; define symbolic input x with range 0..upper_bound
(define-symbolic x int32?)
(current-bitwidth 32)

;; synthesise a function satisying the assertions
(define sol
  (synthesize
   #:forall (list x)
   #:guarantee (begin
                 (assume (bvsge x (int32 0)))
                 (assume (bvsle x (int32 {upper_bound})))
                 {assertions}
   ))
  )
;;sol

(print-forms sol)

'''

rosette_int32_template = r'''#lang rosette

(require rosette/lib/synthax)

(define int32? (bitvector 32))

(define (int32 i)
  (bv i int32?))

(define (bveven? y)
  (bveq (bvand y (int32 1)) (int32 0))
  )

(define (bvodd? y)
  (bveq (bvand y (int32 1)) (int32 1))
  )

(define (bvdiv4? y)
  (bveq (bvand y (int32 3)) (int32 0))
  )

(define (bvdiv8? y)
  (bveq (bvand y (int32 7)) (int32 0))
  )

(define (bvdiv? n m)
  (if (bveven? m)
      (bveq (bvand n (bvsub m (int32 1))) (int32 0))
      (bveq (bvsmod n m) (int32 0))
      )
  )

(define (bvmodfaster n m)
  (if (bveq (bvand m (bvsub1 m)) (int32 0))
      (bvand n m)
      (bvsmod n m)
      )
  )

(define-grammar (beat-mapper2 x)
  [expr
   (choose x (?? int32?)
           ((bop) (expr) (expr))
           ((uop) (expr)))]
  [bop
   (choose bvadd bvsub bvmul
           bvshl bvashr)]
  [uop
   (choose bvneg bvadd1 bvsub1)]
  )

(define-grammar (beat-cmp x)
  [cmp
   (choose x
    #t #f (int32 0) (int32 1)
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
    bvnot bvzero? bveven? bvodd? bvdiv4? bvdiv8? false?)]
  )

(define-grammar (beat-if x)
  [term
   (choose x (beat-cmp x) (beat-mapper2 x)
           (if (beat-cmp x) (term) (term)))]
  )

  
(define (beatmapper-fun x)
  (assume (bvsge x (int32 0)))
  (assume (bvsle x (int32 47)))
  (beat-if x))

(define (beatmapper-sketch x)
  (assume (bvsge x (int32 0)))
  (assume (bvsle x (int32 47)))
  (if (beat-cmp x) (beat-if x) (beat-if x))
  )

(define (beatmapper-spec candidate)
  {assertions}
  )

(current-grammar-depth {depth})
(define-symbolic x int32?)

(define sol
  (synthesize
   #:forall (list x)
   #:guarantee (assert (beatmapper-spec {sketch}))
  )
 )

;;(assert (equal? (candidate-results beatmapper-fun) expected))
;;sol

(print-forms sol)
'''

rosette_bitvector_template = r'''#lang rosette

(require rosette/lib/synthax)

(define int32? (bitvector 32))

(define (int32 i)
  (bv i int32?))

(define-grammar (beat-mapper2 x)
  [expr
   (choose x (?? int32?)
           #t #f
           ((bop) (expr) (expr))
           ((uop) (expr)))]
  [bop
   (choose bvadd bvsub bvmul bvslt bvsle bvsgt bvsge bveq
           bvsdiv bvsmod
           bvshl bvashr)]
  [uop
   (choose bvneg bvnot bvzero? bvadd1 bvsub1)]
  )

(define-grammar (beat-cmp x)
  [cmp
   (choose
    x
    #t #f (int32 0) (int32 1)
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
    bvnot bvzero?)]
  )

(define-grammar (beat-if x)
  [term
   (choose (beat-mapper2 x)
           (if (beat-cmp x) (term) (term)))]
  )

(define (beatmapper-fun x)
  (assume (bvsge x (int32 0)))
  (assume (bvsle x (int32 {upper_bound})))
  (beat-if x))


(define (beatmapper-spec candidate)
  {assertions}
  )

(define (beat-spec candidate)
  (assert (andmap positive? '((candidate 0) (not (candidate 1)) (candidate 2) (not (candidate 3)) (candidate 4))))
  )

(define expected '(#f #t #f #t #f #f #t #f #t #f #t #f #t #f #t #f))

(define (candidate-results candidate)
  (map candidate (range (length expected))))

;;(candidate-results beatmapper-fun)

(current-grammar-depth {depth})
(define-symbolic x int32?)

;;(current-bitwidth {bitwidth})

(define sol
  (synthesize
   #:forall (list x)
   #:guarantee (assert (beatmapper-spec beatmapper-fun))
  )
 )

;;(assert (equal? (candidate-results beatmapper-fun) expected))
;;sol

(print-forms sol)

;;(generate-forms sol)
'''

rosette_template = r'''#lang rosette

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
  (assume (<= x {upper_bound}))
  (beat-if x))

(define (beatmapper-spec candidate)
  {assertions}
  )


;; set grammar depth
(current-grammar-depth {depth})
(define-symbolic x integer?)

;; set bitwidth
(current-bitwidth {bitwidth})

(define sol
  (synthesize
   #:forall (list x)
   #:guarantee (assert (beatmapper-spec beatmapper-fun))
   ))

(print-forms sol)

'''

def run_rosette(depth, bitwidth, assertions, upper_bound, sketch):
    """
    Args:
      depth (int): max grammar depth to allow
      bitwidth (int): bitvector width (unused for current template used)
      assertions (str): assertion string to embed
      upper_bound (int): maximum x value
      sketch (str): Rosette expression or sketch to fill in
    Returns:
      str: raw stdout printed by Racket
    """
    
    code = rosette_int16_template.format(depth=depth, assertions=assertions, upper_bound=upper_bound, sketch=sketch)
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.rkt') as temp_file:
        filename = temp_file.name
        temp_file.write(code)

    try:
        result = subprocess.run([r"C:\\Program Files\\Racket\\racket.exe", filename], shell=True, capture_output=True, text=True)
        print(result)
        output = result.stdout.strip()
        return output
    finally:
        os.remove(filename)

def iterative_synth(max_depth=3, bitwidth=16, assertions=None, upper_bound=16, sketch="beatmapper-fun"):
    """
    Try synthesising a mapping function by gradually increasing grammar depth
    Args:
      max_depth (int): highest gramar depth to try
      bitwidth (int): bitvector width
      assertions (str): assertion for synthesis
      upper_bound (int): maximum x value to constrain
      sketch (str): which sketch to plug in
    Returns:
      str or None: the synthesis result or None if all depths fail
    """
    if assertions is None:
        assertions = """
(assert (candidate 0))
(assert (not (candidate 1)))
(assert (candidate 2))
(assert (not (candidate 3)))
        """
    
    for depth in range(1, max_depth + 1):
        print(depth)
        output = run_rosette(depth, bitwidth, assertions, upper_bound, sketch=sketch)
        print(output)
        if "beatmapper-fun" in output:
            return output
        #output = run_rosette(depth, bitwidth, assertions, upper_bound, sketch="beatmapper-sketch")
    return None

#depth, output = iterative_synth()

"""
(define-grammar (beat-if x) ...)	; grammar
(define (beatmapper-sketch x)		; sketch with holes
  (if (bvdiv4? x)
      #t
      (beat-if x))
  )
(current-grammar-depth 3)
(define-symbolic x int32?)

(define sol
  (synthesize
   #:forall (list x)
   #:guarantee (begin
                 (assume (bvsge x (int32 0)))
                 (assume (bvsle x (int32 30)))
                 (assert (<=> (or (bveq x (int32 0)) 
                                  (bvdiv4? x)) 
                              (beatmapper-sketch x)))
   )
  )
"""

"""
(define (betmapper-sketch x)
  (if (bvdiv4? x)
      #t
      (if (bvzero? x) #t #f)
      )
  )
"""

"""
[Symbol('define'), [Symbol('betmapper-sketch'), Symbol('x')], [Symbol('if'), [Symbol('bdiv4?'), Symbol('x')], Symbol('#t'), [Symbol('if'), [Symbol('bvzero?'), Symbol('x')], Symbol('#t'), Symbol('#f')]]]
"""

"""
Function(
	name="sleep_1",
  	argument="x",
  	body=[
      If(
      	conditions=[Eq(Mod(Int("x"), Int(4)), Int(0))],
        bodies=[
          Return(Bool("true")),
          If(
          	conditions=[Eq(Int(x), Int(0))],
            bodies=[Return(Bool("true")), Return(Bool("false"))]
          )])])
"""

"""
define :sleep_1 do |x|
  if x % 4 == 0
    return true
  else
    if x == 0
    	return true
  	else
    	return false
    end
  end
end
"""