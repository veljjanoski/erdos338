# Erdős problem #338 — partial results on restricted order

**Problem** (https://www.erdosproblems.com/338; Erdős and Graham 1980). A set A ⊆ ℕ is an (asymptotic) basis if, for
some h, every sufficiently large integer is a sum of at most h elements of A (repetitions allowed); the least such h is
the *order* of A. The *restricted order* of A is the least t, if it exists, such that every sufficiently large integer is
a sum of at most t **distinct** elements of A. Among other things, Erdős and Graham asked: if A \ F is a basis for every
finite F (call such A *robust*), must A have a restricted order? What if all the A \ F are bases of the same order?
Both questions are open. Bateman's example {1} ∪ hℕ (order h ≥ 3, no restricted order) is not robust. Patrick White
(erdosproblemaday.com/report/338) settled the eventually periodic case: there a robust set has restricted order at most
the period, and it equals h if all A \ F have order h.

This note proves two partial results. Theorem 1: a robust set of positive lower density always has a restricted order,
bounded in terms of the density alone. Theorem 2: in the block model behind the constructions of Hegyvári, Hennecart and
Plagne and of the Bitter Lemma project, the restricted order at order 3 is at most 4 for every block. Neither result
settles the questions.

## Theorem 1 (positive density)

Let A ⊆ ℕ have lower asymptotic density δ > 0, and suppose that for every modulus g the residue classes mod g that
contain infinitely many elements of A generate ℤ/gℤ. Then every sufficiently large integer is a sum of at most
3s − 2 distinct elements of A, where s = ⌈8/δ²⌉.

The residue condition holds when A is robust: if the classes containing infinitely many elements generated a proper
subgroup H, then removing the finitely many elements in the other classes would leave a set all of whose sums lie in
classes of H, which is not a basis. The density and the residue condition are unchanged when a finite set is removed,
so the same bound holds for every A \ F.

**Consequences.** Every robust set of positive lower density has a restricted order. For eventually periodic sets
this recovers the existence part of White's result, with a much weaker bound (White's bounds are sharper: at most the
period, and equal to h when all A \ F have order h). A counterexample to either question must have lower density 0.

**Proof.** For n ∈ ℕ let r(n) be the number of pairs a < b in A with a + b = n, and for R ≥ 1 let
M_R = {n : r(n) ≥ R}. Lower asymptotic densities are written d(·).

*Step 1: d(M_R) ≥ δ²/4 for every R.* Let ε > 0, let N be large and put x = N/2 (a real number), so that
A(x) := |A ∩ [1, x]| ≥ (δ − ε)x. The pairs a < b in A ∩ [1, x] have sums at most N, so Σ_{n ≤ N} r(n) ≥ binom(A(x), 2).
On the other hand r(n) ≤ n/2 ≤ x for n ≤ N, and r(n) < R for n ∉ M_R, so Σ_{n ≤ N} r(n) ≤ x·|M_R ∩ [1, N]| + NR.
Hence |M_R ∩ [1, N]| ≥ ((δ − ε)²/4)·N − O(R + 1).

*Step 2: sM_R contains all large integers of some residue class mod g, with g ≤ s − 1.* Here sM_R is the set of sums
of s elements of M_R. With s = ⌈8/δ²⌉ we have s·d(M_R) ≥ 2 > 1 ≥ d(sM_R). By Kneser's theorem on the lower asymptotic
density of sumsets (Kneser, Math. Z. 58 (1953) 459–484; in the form quoted by Hegyvári, Hennecart and Plagne,
Combin. Probab. Comput. 16 (2007), proof of Theorem 10 in the preprint), there are g ≥ 1 and a set M′ ⊇ M_R with
g + M′ ⊆ M′, sM′ \ sM_R finite and d(sM′) ≥ s·d(M′) − (s − 1)/g. Since d(M′) ≥ d(M_R), this gives 1 ≥ 2 − (s − 1)/g,
so g ≤ s − 1. Fix y₀ ∈ sM_R. Then y₀ + gℕ ⊆ sM′, so every sufficiently large n ≡ y₀ (mod g) lies in sM_R.

*Step 3: fixing the residue with distinct elements.* Let Γ be the set of classes mod g that contain infinitely many
elements of A; by hypothesis Γ generates ℤ/gℤ. The sets T_i = {0} ∪ {sums of at most i elements of Γ, repetitions
allowed} increase with i, and once T_i = T_{i+1} the set T_i is closed under adding elements of Γ, hence is the
generated subgroup ℤ/gℤ. As |T_0| = 1 and |ℤ/gℤ| = g, T_{g−1} = ℤ/gℤ. Because every class in Γ is infinite, for each
class t mod g we can fix a set E_t ⊆ A of at most g − 1 ≤ s − 2 distinct elements with Σ E_t ≡ t − y₀ (mod g).

*Step 4: assembling.* Choose R = 3s and let g, y₀ and the sets E_t be as above (they depend on R, but g ≤ s − 1 in any
case). Let n be large and t ≡ n (mod g). Then m = n − Σ E_t is large and m ≡ y₀ (mod g), so m = m_1 + ⋯ + m_s with
m_i ∈ M_R. Each m_i has at least R representations m_i = a + b with a < b in A, and these are pairwise disjoint as
2-element sets (a determines b). Choose them one at a time: when choosing {a_i, b_i}, at most |E_t| + 2(i − 1) ≤
(s − 2) + 2(s − 1) < R elements are already used, and each used element meets at most one of the R disjoint
representations of m_i, so one of them avoids all used elements. Then
n = Σ E_t + (a_1 + b_1) + ⋯ + (a_s + b_s)
is a sum of at most (g − 1) + 2s ≤ 3s − 2 distinct elements of A. ∎

The disjoint-representation step is the argument of Hegyvári, Hennecart and Plagne (cf. the proof of Theorem 9 in the
preprint of their CPC 2007 paper).

**How sharp is the bound?** It cannot be better than about 2/δ: the set A = {n : n ≡ 0 or 1 (mod m)} has density
δ = 2/m and is robust, but an integer n ≡ −1 (mod m) needs at least m − 1 summands ≡ 1 (mod m), so the restricted
order of A is at least m − 1 = 2/δ − 1. Whether the right dependence on δ is linear in 1/δ is left open.

**Literature.** We did not find Theorem 1 in the literature. We checked the papers listed by Bitter Lemma on the forum
of #338 (for Fang–Cheng 2025, Chen–Li 2026 and Chen–Fang 2014 only abstracts and reviews). The nearest results are
Kelly's (as reported on the problem page: an order-2 basis of positive lower density has restricted order at most 3),
the theorem that lower density above 1/2 gives restricted order 2 (Chen and Yu, Discrete Math. 346 (2023) 113388), and
Theorem 10 of Hegyvári, Hennecart and Plagne (CPC 2007), which uses Kneser's theorem in a similar way but is
conditional on their Conjecture 2 and concerns bounded gaps of k × A.

## Theorem 2 (block model, order 3)

The constructions of Hegyvári–Hennecart–Plagne (HHP) and of the Bitter Lemma project are unions of blocks
B(x) = [x, x + x²] ∪ {x + c·x² : c ∈ C} at rapidly growing scales x (the next scale is about ρ_h(C)·x², see below),
with C a finite set of positive reals; HHP use C = {2, 4, …, 2^{h−2}} (with 1 in some descriptions), Bitter Lemma use
other C. In units of x² and dropping lower-order terms, a sum of at most h elements of B(x) ranges over
σ(S) + [0, h − |S|], where S is a multiset of elements of C with |S| ≤ h and σ(S) is its sum. Elements c ≤ 1 add
nothing in this model (each of their intervals lies inside the interval for S without c), so we assume C ⊂ (1, ∞). Let

- U_h = ⋃ [σ(S), σ(S) + h − |S|] over multisets S with |S| ≤ h, and ρ_h(C) the right end of the component of U_h
  that contains 0 (the reach);
- V_l = ⋃ [σ(T), σ(T) + l − |T|] over sets T ⊆ C (distinct elements) with |T| ≤ l, and r_l(C) the right end of the
  component of V_l that contains 0;
- l*(C, h) = the least l with r_l(C) ≥ ρ_h(C).

We take l*(C, h) as the restricted order of a block construction in this model. The reduction to one block is HHP's
(as Bitter Lemma note); we do not treat the lower-order terms needed to pass from the model to actual sets of
integers. The model reproduces the known values: 4, 7, 12, 21 for HHP's sets at h = 3, 4, 5, 6, and Bitter Lemma's value
9 at h = 4 (C = {4, 5}); see `block338.py` and its output `block338_output.txt`.

**Theorem 2.** For every finite C ⊂ (1, ∞), l*(C, 3) ≤ 4. The bound is attained by C = {2}, HHP's set at h = 3.

Bitter Lemma report 4 as the maximum within the block family over integer C with |C| ≤ 8; Theorem 2 removes both the
size and the integrality restriction.

**Proof.** Let ρ = ρ₃(C) and W = [0, ρ], the component of U₃ containing 0. We show W ⊆ V₄; since W is connected and
contains 0, this gives r₄(C) ≥ ρ. Suppose not. V₄ is a finite union of closed intervals, so W \ V₄ is relatively open
in W and nonempty, hence infinite, and it contains a point y that is not one of the finitely many single points
σ(S), |S| = 3. So y lies in an interval [σ(S), σ(S) + 3 − |S|] with |S| ≤ 2.

If the elements of S are distinct (including S = ∅), this interval lies in [σ(S), σ(S) + 4 − |S|] ⊆ V₄, which is a
contradiction. So S = {c, c} and y ∈ [2c, 2c + 1]. Every point of [0, 2c) lies in W and hence in some interval
[σ(S′), σ(S′) + 3 − |S′|] with σ(S′) < 2c. These are finitely many closed intervals whose union contains [0, 2c), so
their union also contains 2c: there is S′ with σ(S′) < 2c ≤ σ(S′) + 3 − |S′|, and so |S′| ≤ 2.

- If the elements of S′ are distinct, then [σ(S′), σ(S′) + 4 − |S′|] ⊆ V₄ contains [σ(S′), 2c + 1], hence y.
- If S′ = {d, d}, then 2d < 2c ≤ 2d + 1, so c − 1/2 ≤ d < c. The set T = {c, d} has two distinct elements, and
  [c + d, c + d + 2] ⊆ V₄ with c + d < 2c ≤ y and c + d + 2 ≥ 2c + 3/2 > y.

In both cases y ∈ V₄, a contradiction. For C = {2}: U₃ = [0, 3] ∪ [2, 4] ∪ [4, 5] ∪ {6}, so ρ₃ = 5, while
V₃ = [0, 3] ∪ [2, 4] reaches only 4; hence l* = 4. ∎

So, within this model, a block construction of order 3 (with any C at each scale) has restricted order at most 4. A
negative answer to the second question at h = 3 cannot come from this family, since it would need l*(C_n, 3) to be
unbounded. This concerns the block family only: White's eventually periodic example {4, 6} ∪ {10q} ∪ {10q + 3} has order
3 and restricted order 6. A random check of 4000 sets C with up to six elements (`block338.py`) also gave maximum 4.

## Remark (relation to Conjecture 2 of HHP)

If A has restricted order t, then the set t × A of sums of exactly t distinct elements has bounded gaps: for large n,
write n as a sum of j ≤ t distinct elements and add t − j of the 2t smallest elements of A not already used. A basis of
order 3 satisfies 3(A ∪ {0}) ∼ ℕ, and bounded gaps for k × (A ∪ {0}) give bounded gaps for k × A (add a small unused
element). Hence a positive answer to the second question for h = 3 would give, for every robust A whose deletions all
have order 3, some k with bounded gaps in k × A: a special case of the question behind Conjecture 2 of HHP (CPC 2007),
who note that no value k(h) with h ≥ 3 is known. Chen and Fang (Eur. J. Combin. 41 (2014) 289–297) showed that the
analogue fails for sets A ⊆ ℤ.

## Files

`README.md` (this note), `block338.py` (exact rational computation of reach, restricted reach and l* in the block model;
running it reproduces the values above), `block338_output.txt` (its output).

## Credits and references

- P. Erdős and R. L. Graham, *Old and new problems and results in combinatorial number theory*, Enseign. Math. (1980) —
  the questions.
- N. Hegyvári, F. Hennecart and A. Plagne, A proof of two Erdős' conjectures on restricted addition and further
  results, J. Reine Angew. Math. 560 (2003) 199–220; Answer to a question by Burr and Erdős on restricted addition, and
  related results, Combin. Probab. Comput. 16 (2007) 747–756 (preprint numbering used above) — the disjoint-
  representation argument, the block construction and Conjecture 2.
- M. Kneser, Abschätzungen der asymptotischen Dichte von Summenmengen, Math. Z. 58 (1953) 459–484.
- P. White, erdosproblemaday.com/report/338 — the eventually periodic case and the example of order 3 with restricted
  order 6.
- The Bitter Lemma project (forum of #338, Aug 2026; github.com/bitterlemma/erdos-338) — the block computations and the
  literature list.
- J. B. Kelly, Restricted bases, Amer. J. Math. 79 (1957) 258–264; Chen and Yu, On the restricted order of two,
  Discrete Math. 346 (2023) 113388; Chen and Fang, All sums of h distinct terms of a sequence, Eur. J. Combin. 41 (2014)
  289–297.

AI-usage disclosure: Claude (Anthropic) was used as assistant.
