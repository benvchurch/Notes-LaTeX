---
author:
- Benjamin Church
title: $\ell$-adic Galois Representations
---

# Introduction

Considering the importance of Galois groups in number theory and
geometry, it is natural to study their representation theory. However,
Galois groups have additional structure which makes the theory of their
representations remarkably rich. They are profinite topological groups
and using topological arguments is extremely fruitful in studying their
general representation theory. We will see that the topology is too
restrictive to admit interesting Galois representations over
$\mathbb{C}$. However, the profinite topology interacts much more
favorably with $\ell$-adic numbers due to their profinite-like topology.
Therefore, we will seek out vector spaces over $\mathbb{Q}_{\ell}$ on
which the Galois group naturally acts. Furthermore, Galois groups act on
algebraic fields and preserve certain polynomial equations meaning that
Galois groups act naturally on algebraic varieties built from fields and
polynomials. This action allows many Galois representations to be viewed
as automorphisms of certain geometric objects giving a powerful link
between the number theory of field extensions and the geometry of
algebraic objects.

::: trivlist
Let $G$ be a profinite group and $F$ a topological field. An
$n$-dimensional representation of $G$ is a continuous homomorphism,
$$\rho : G \to \mathrm{GL}_{n}(F)$$ If
$G = G_K = \mathrm{Gal} \small(\bar{K} / K \small)$, the absolute Galois
group of $K$, then we call such a representation a Galois representation
and if $F$ is algebraic over $\mathbb{Q}_{\ell}$ then we call it an
$\ell$-adic Galois representation.
:::

# Machinery

## Projective Limits

::: trivlist
A projective system is a family of objects indexed by a poset $(I, \le)$
with morphisms $f_{ij} : A_j \to A_i$ when $i \le j$ such that,

1.  $f_{ii} = \mathrm{id}_{A_i}$

2.  $f_{ik} = f_{ij} \circ f_{jk}$ for all $i \le j \le k$

3.  $(I, \le)$ is directed meaning that for every $i, j \in I$ there
    exists $k \in I$ such that $i \le k$ and $j \le k$. This means that
    for all $A_i$ and $A_j$ there is an object $A_k$ such that there are
    maps $f_{ik} : A_k \to A_i$ and $f_{jk} : A_k \to A_j$.

we define the projective limit $\varprojlim A_n$ to be the categorical
limit of this system. Concretely, for groups or modules, we can give the
explicit construction of such an object,
$$\varprojlim A_i = \left\{ (a_i)_{I} \in \prod_{i \in I} A_i \: \bigg| \: \forall i \le j : f_{ij}(a_j) = a_{i}  \right\}$$
Therefore, the projective limit is the set of sequences which reduce
compatibly under the maps $f$.
:::

A very important special case is that of a leftward mapping sequence
where $I = \mathbb{N}$ with the usual order.

::: trivlist
Given a diagram,

::: center
:::

we define the projective limit $\varprojlim A_n$ to be the categorical
limit of the diagram. Concretely, for groups or modules, we can give the
explicit construction of such an object,
$$\varprojlim A_n = \left\{ (a_n) \in \prod_n A_n \: \bigg| \: \forall n \in \mathbb{N}: f_n(a_n) = a_{n-1}  \right\}$$
Therefore, the projective limit is the set of sequences which reduce
compatibly under the maps $f$.
:::

::: remark
*Remark 1*. One should view the projective limit as the object which
"naturally projects" compatibly with the maps onto each of the given
objects. There are clear projection maps
$\pi_i : \varprojlim A_n \to A_i$ given by $\pi_i((a_n)) = a_i$.
Reversing all the maps, we can define the dual notion called the direct
limit which is the objective into which each of the given objects
include compatibly via maps $\iota_i : A_i \to \varinjlim A_n$. When the
given morphisms are inclusions the direct limit is simply the union.
:::

::: example
**Example 1**. Let $R$ be a ring. The ring of formal power series on $R$
is $$R[[X]] \cong \varprojlim R[X] / X^n R[X]$$ with maps
$R[X] / X^{n+1} R[X] \to R[X] / X^n R[X]$ given by reduction modulo
$X^n$. The sequences making up the projective limit give the partial
sums of a formal power series.
:::

## Infinite Galois Theory

::: proposition
**Proposition 1**. Let $F / K$ be Galois. Then there exists an
isomorphism,
$$\mathrm{Gal} \small(F / K \small) \cong \varprojlim_{L/K} \mathrm{Gal} \small(L / K \small)$$
where $L$ runs over all finite Galois extensions
$K \subset L \subset F$. The projective system is given by the
restriction maps
$\mathrm{Gal} \small(L / K \small) \to \mathrm{Gal} \small(L' / K \small)$
when $L' \subset L$.
:::

::: proof
*Proof.* Given $\sigma \in \mathrm{Gal} \small(F / K \small)$ we
consider the restriction $\sigma |_L$ to each finite Galois extension
$L / K$ which are clearly compatible with restrictions between finite
extensions. This gives a map to the projective limit. Since each
$\alpha \in F$ is algebraic over $K$ we know that $\alpha$ lies in a
finite Galois extension of $K$ so if $\sigma$ is trivial on all finite
Galois extensions then $\sigma(\alpha) = \alpha$ so
$\sigma = \mathrm{id}_F$. Thus the map is injective. Furthermore, an
element of the projective limit induces an automorphism of $F / K$ by
mapping each $\alpha \in F$ to its image under the automorphism acting
on any finite Galois extension containing $\alpha$. Thus the mapping is
surjective. ◻
:::

::: remark
*Remark 2*. The above identification gives a natural profinite topology
on $\mathrm{Gal} \small(F/ K \small)$ by making the projection maps
$\mathrm{Gal} \small(F / K \small) \to \mathrm{Gal} \small(L / K \small)$
continuous for each finite Galois extension $L / K$. In particular, the
kernels of these maps $\mathrm{Gal} \small(F / L \small)$ are open
subgroups and form a neighborhood basis of $\mathrm{id}$.
:::

::: example
**Example 2**. The absolute Galois group of $\mathbb{F}_{p}$ is equal to
the profinite completion of $\mathbb{Z}$,
$$\mathrm{Gal} \small(\overline{\mathbb{F}_{p}} / \mathbb{F}_{p} \small) \cong \hat{\mathbb{Z}} = \varprojlim \mathbb{Z}/ n \mathbb{Z}$$
:::

::: theorem
**Theorem 2** (Galois Correspondence). Let $F / K$ be a Galois extension
with $G = \mathrm{Gal} \small(F / K \small)$. There is an inclusion
reversing correspondence between *closed* subgroups $H \subset G$ and
subfields $K \subset L \subset F$ given by $H \mapsto F^H$ and
$L \mapsto \mathrm{Gal} \small(F / L \small)$. Furthermore, finite
extensions $K \subset L \subset F$ correspond to open subgroups
$\mathrm{Gal} \small(F / L \small) \subset G$ whose cosets correspond to
embeddings of $L$ into $F$ fixing $K$. Galois extensions
$K \subset L \subset F$ correspond to closed normal subgroups.
:::

## $\ell$-adic Numbers

::: trivlist
The $\ell$-adic integers are the projective limit,
$$\mathbb{Z}_{\ell} = \varprojlim \mathbb{Z}/ \ell^n \mathbb{Z}$$ under
the maps
$\mathbb{Z}/ \ell^{n+1} \mathbb{Z}\to \mathbb{Z}/ \ell^n \mathbb{Z}$
given by reduction mod $\ell$.
:::

::: remark
*Remark 3*. There is an inclusion
$\mathbb{Z}\hookrightarrow \mathbb{Z}_{\ell}$ given by reducing
$a \in \mathbb{Z}$ modulo each $\ell^n$. The sequences representing
$\mathbb{Z}\subset \mathbb{Z}_{\ell}$ are exactly those which are
eventually constant after the largest power dividing the integer in
question. Using the intuition gained from the ring of formal power
series, we can write any $\ell$-adic integer as a formal "base-$\ell$"
power series, $$z = a_0 + a_1 \ell + a_2 \ell^2 + a_3 \ell^3 + \cdots$$
which is the natural extension of how integers may be represented in
base $\ell$. Although this expression is simply convenient and
suggestive shorthand for the projective limit sequence of partial sums,
$$z = (a_0, \, a_0 + a_1 \ell, \, a_0 + a_1 \ell + a_2 \ell^2, \, a_0 + a_1 \ell + a_2 \ell^2 + a_3 \ell^3, \, \cdots)$$
we can actually give meaning to this infinite sum by changing the
standard definition of convergence. Define the $\ell$-adic valuation
$v_{\ell} : \mathbb{Z}_{\ell} \to \mathbb{N}\cup \{ \infty \}$ by
$v_{\ell}((a_i))$ equals the index of the first nonzero term $a_i$ and
$v_{\ell}(0) = \infty$. All terms in the sequence past $v_{\ell}((a_i))$
are nonzero because if $a_i = 0$ then $a_{i-1} = f_i(a_i) = 0$. We can
then define an absolute value, $|z|_{\ell} = \ell^{-v_{\ell}(z)}$ which
gives a non-archimedean metric on $Z_{\ell}$. Under this metric, the
sequence of elements in $\mathbb{Z}\subset \mathbb{Z}_{\ell}$ given by
these the partial sums actually does converge to the $\ell$-adic number,
$$z = a_0 + a_1 \ell + a_2 \ell^2 + a_3 \ell^3 + \cdots$$ because the
element,
$$z - z_{N-1} = z - \sum_{i = 0}^{N-1} a_i \ell^n = a_N \ell^N + a_{N+1} \ell^{N+1} + a_{N+2} \ell^{N+2} + \cdots$$
has valuation $v_\ell(z_n) \ge N$ because
$z_N = (0, \cdots, a_N \ell^N, a_{N+1} \ell^{N+1}, \cdots)$ where the
first $N-1$ terms are $0$. Therefore,
$$|z - z_n|_{\ell} \le \frac{1}{\ell^N} \to 0$$ so the sequence
converges $z_n \to z$.
:::

::: trivlist
The $\ell$-adic field is the field of fractions of $\mathbb{Z}_{\ell}$,
$$\mathbb{Q}_{\ell} = \mathrm{Frac}(\mathbb{Z}_{\ell})$$ on which we
extend the $\ell$-adic valuation to
$v_{\ell} : \mathbb{Q}_{\ell} \to \mathbb{Z}$ by
$v_{\ell}(a/b) = v_{\ell}(a) - v_{\ell}(b)$.
:::

::: proposition
**Proposition 3**.
$\mathbb{Z}_{\ell}^\times = \{ z \in \mathbb{Z}_{\ell} \mid |z|_{\ell} = 1 \}$
:::

::: proof
*Proof.* Let $z = (a_i) \in \mathbb{Z}_\ell$. If $v_{\ell}(z) > 0$ then
$a_0 = 0$ so for any $(b_i) \in \mathbb{Z}_{\ell}$ we have $a_0 b_0 = 0$
so $z \notin \mathbb{Z}_{\ell}$. However, if $v_{\ell}(z) = 0$ then
choose $b_n = a_n^{-1} \in \mathbb{Z}/ \ell^n \mathbb{Z}$ which exists
because $a_n$ is coprime to $\ell$ since it projects down to
$a_0 \neq 0$ in $\mathbb{Z}/ \ell \mathbb{Z}$. Then we have,
$$(a_i) \cdot (b_i) = (a_i b_i) = (1)$$ so
$z \in \mathbb{Z}_{\ell}^\times$. ◻
:::

::: proposition
**Proposition 4**. Every element $z \in \mathbb{Q}_{\ell}$ can be
written uniquely as $z = \ell^n u$ where
$u \in \mathbb{Z}_{\ell}^\times$ and $n = v_{\ell}(z)$.
:::

::: proof
*Proof.* First we will prove this for $z = (a_i) \in \mathbb{Z}_{\ell}$.
Take $n = v_{\ell}(z)$ so we know that $f_{n-1, k}(a_{k}) = 0$ so
$\ell^n \mid a_k$ but $\ell^{n+1}$ does not. Thus we can write
$a_k = \ell^n u_k$ with
$u_k \in (\mathbb{Z}/ \ell^k \mathbb{Z})^\times$. Take $u = (u_k)$ with
$u_k = f_{k n}(u_n) \neq 0$ since $\ell \centernot \mid u_n$ for $k < n$
so clearly $z = \ell^n u$ and $v_{\ell}(u) = 0$. Furthermore, if
$z \in \mathbb{Q}_{\ell}$ then $z = \frac{a}{b}$ for
$a,b \in \mathbb{Z}_{\ell}$ so we can write $a = \ell^n u$ and
$b = \ell^m v$ with $u,v \in \mathbb{Z}^\times$. Thus,
$$z = \frac{\ell^n u}{\ell^m v} = \ell^{n-m} u v^{-1}$$ with
$v_{\ell}(z) = v_{\ell}(a) - v_{\ell}(b) = n - m$ an
$u v^{-1} \in \mathbb{Z}_{\ell}^\times$. ◻
:::

::: proposition
**Proposition 5**.
$$\mathbb{Q}_{\ell} = \mathbb{Z}_{\ell}\left[ \frac{1}{\ell} \right] = \bigcup_n \frac{1}{\ell^n} \mathbb{Z}_{\ell}$$
Therefore we may represent an element of $\mathbb{Q}_{\ell}$ as a power
series,
$$a_{-N} \ell^{-N} + a_{-N + 1} \ell^{-N + 1} + \cdots + a_0 + a_1 \ell + a_2 \ell^2 + \cdots$$
with only finitely many negative exponent terms.
:::

::: proof
*Proof.* By the previous proposition we can write any element
$z \in \mathbb{Q}_{\ell}$ as $\ell^{n} u$ for
$u \in \mathbb{Z}_{\ell}^\times$ and $n \in \mathbb{Z}$. Therefore, we
simply need to invert $\ell$ to get negative powers of $\ell$ to
represent all of $\mathbb{Q}_{\ell}$ from $\mathbb{Z}_{\ell}$. ◻
:::

::: proposition
**Proposition 6**. $\mathbb{Z}_{\ell}$ is a local PID (and thus a
discrete valuation ring) with unique maximal ideal
$\ell \mathbb{Z}_{\ell}$ and residue field $\mathbb{F}_{\ell}$.
:::

::: proof
*Proof.* Let $I \subset \mathbb{Z}_{\ell}$ be an ideal. Consider
$n = v_{\ell}(I) = \min \{ v_{\ell}(z) \in \mathbb{N}\mid z \in I \}$
where the minimum value exists by well ordering. Thus, there exists
$z_0 \in I$ with $v_{\ell}(z_0) = n$. I claim that $I = (\ell)^n$. We
can write $z_0 = \ell^n u$ for some $u \in \mathbb{Z}_{\ell}^\times$.
Therefore, $I \subset (z_0) = (\ell^n u) = (\ell)^n$. Furthermore for
any $z \in I$ we have $v_{\ell}(z) = m \ge n$ so $\ell^n \mid z$ since
$z = \ell^m v$ for $v \in \mathbb{Z}_{\ell}^\times$ so
$z = \ell^{m - n} v \ell^n$ with $\ell^{m - n} v \in \mathbb{Z}_{\ell}$
and thus $z \in (\ell)^n$. Therefore, $I = (\ell)^n$.\
Thus, all proper ideals are contained in $(\ell)$ so
$\mathfrak{m} = (\ell)$ is the unique maximal ideal. Consider the map,
$$\phi : \mathbb{Z}\to \mathbb{Z}_{\ell} / \ell \mathbb{Z}$$ given by
inclusion and then projection. Given $z = (a_i) \in \mathbb{Z}_{\ell}$
take $a \in \mathbb{Z}$ such that
$a \equiv a_i \; \mathrm{mod} \; {\ell}$. Then $v_{\ell}(z - a) \ge 1$
so $\ell \mid z - a$. Therefore, $[a] = [z]$ in
$\mathbb{Z}_{\ell} / \ell \mathbb{Z}_{\ell}$ so $\phi$ is surjective.
Furthermore, $\ker{\phi} = \ell \mathbb{Z}$ since $[a] = 0$ exactly when
$a = (0, a, \cdots)$ i.e. $a \equiv 0 \; \mathrm{mod} \; \ell$.
Therefore,
$$\mathbb{Z}/ \ell \mathbb{Z}\cong \mathbb{Z}_{\ell} / \ell \mathbb{Z}$$
so the residue field is given by
$\mathbb{Z}_{\ell} / \mathfrak{m} \cong \mathbb{F}_{\ell}$. ◻
:::

::: proposition
**Proposition 7**.
$\mathbb{Q}_{\ell} / \mathbb{Z}_{\ell} \cong \mathbb{Q}/ \mathbb{Z}$ and
$\mathbb{Z}_{\ell} / \ell^n \mathbb{Z}_{\ell} \cong \mathbb{Z}/ \ell^n \mathbb{Z}$
:::

::: proof
*Proof.* Quotienting by $\ell^n \mathbb{Z}_{\ell}$ is equivalent to
ignoring all elements of the sequence with index greater than or equal
to $n$. Therefore, we can choose a rational number (or integer) which
reduces modulo $\ell^{n} \mathbb{Z}$ to the required value which is
consistently reduced by the reduction maps. ◻
:::

::: trivlist
A complete non-archimedean field $K$ is a topological field which is
complete with respect to an absolute value satisfying the
non-archimedean property or ultrametric inequality,
$$|\alpha + \beta| \le \max\{|\alpha|, |\beta|\}$$ For example
$\mathbb{Q}_{\ell}$ with the $\ell$-adic absolute value
$| \cdot | : \mathbb{Q}_{\ell} \to \mathbb{Z}$.
:::

::: proposition
**Proposition 8**. Let $K$ be a complete non-archimedean field and
$L / K$ a separable extension. The absolute value on $K$ extends
uniquely to a non-archimedean absolute value on $L$. Furthermore, if
$L / K$ is finite then $L$ is complete with respect to the extended
absolute value.
:::

::: lemma
**Lemma 9** (Krasner). Let $K$ be a complete non-archimedean field and
$\alpha, \beta \in \bar{K}$. If $\alpha$ is strictly closer to $\beta$
than to any conjugate of $\alpha$ then $K(\alpha) \subset K(\beta)$.
:::

::: proof
*Proof.* Consider an automorphism
$\sigma \in \mathrm{Gal} \small(\bar{K} / K \small)$. By assumption,
$|\alpha - \beta | < |\alpha - \sigma(\alpha)|$ whenever
$\sigma(\alpha) \neq \alpha$. Suppose that $\sigma(\beta) = \beta$ and
consider the value,
$$|\alpha - \sigma(\alpha)| = |\alpha - \beta + \beta - \sigma(\alpha) | \le \max \left\{ | \alpha - \beta |, | \beta - \sigma(\alpha)| \right\}$$
We know that
$|\beta - \sigma(\alpha)| = |\sigma(\beta - \alpha)| = |\alpha - \beta|$
by uniqueness of the absolute value. Therefore, unless
$\sigma(\alpha) = \alpha$,
$$|\alpha - \sigma(\alpha)| \le |\alpha - \beta| < |\alpha - \sigma(\alpha)|$$
which is a contradiction so $\sigma(\alpha) = \alpha$. Therefore,
$\mathrm{Gal} \small(\bar{K} / K(\beta) \small) \subset \mathrm{Gal} \small(\bar{K} / K(\alpha) \small)$
and thus $K(\alpha) \subset K(\beta)$. ◻
:::

::: {#thm:algebraic_extensions_adics .theorem}
**Theorem 10**. Let $K / \mathbb{Q}_{\ell}$ be finite. There exists
$\alpha \in \overline{\mathbb{Q}}$ such that
$K = \mathbb{Q}_{\ell}(\alpha)$.
:::

::: proof
*Proof.* By the primitive element theorem,
$K = \mathbb{Q}_{\ell}(\alpha')$ for some $\alpha'$ algebraic over
$\mathbb{Q}_{\ell}$ with minimal polynomial
$f \in \mathbb{Q}_{\ell}[X]$. Take $g \in \mathbb{Q}[X]$ which is monic
of the same degree. Write, $$g(X) = \prod_{i = 0}^n (X - \alpha_i)$$ for
roots $\alpha_i \in \overline{\mathbb{Q}}$. Consider,
$$|(f - g)(\alpha')|_{\ell} = |g(\alpha')|_{\ell} = \prod_{i = 0}^n |\alpha' - \alpha_i|_{\ell}$$
by choosing $g$ such that $f - g$ is sufficiently small we can ensure
that for any $\epsilon > 0$ there is some root $\alpha$ of $g$ such that
$|\alpha' - \alpha| < \epsilon$. In particular, for sufficiently small
$\epsilon$ the root $\alpha$ will be strictly closer to $\alpha'$ than
any conjugate of $\alpha'$. Therefore, by Krasner's Lemma,
$$\mathbb{Q}_{\ell}(\alpha') \subset \mathbb{Q}_{\ell}(\alpha)$$ However
because $f$ is irreducible,
$$[\mathbb{Q}_{\ell}(\alpha) : \mathbb{Q}_{\ell}] \le \deg{g} = \deg{f} = [\mathbb{Q}_{\ell}(\alpha') : \mathbb{Q}_{\ell}] \le [\mathbb{Q}_{\ell}(\alpha) : \mathbb{Q}_{\ell}]$$
forcing an equality. Therefore
$\mathbb{Q}_{\ell}(\alpha) = \mathbb{Q}_{\ell}(\alpha') = K$ and
furthermore $g$ is irreducible in $\mathbb{Q}_{\ell}[X]$ thus in
$\mathbb{Q}[X]$ so,
$$[\mathbb{Q}(\alpha) : \mathbb{Q}] = \deg{g} = [\mathbb{Q}_{\ell}(\alpha) : \mathbb{Q}_{\ell} ]$$ ◻
:::

# Galois Representations over $\mathbb{C}$

::: {#lem:no_subgroups_of_nbd .lemma}
**Lemma 11**. There exists a neighborhood $V$ of $I$ in
$\mathrm{GL}_{n}(\mathbb{C})$ that contains no nontrivial subgroup.
:::

::: proof
*Proof.* Recall that $M_n(\mathbb{C})$ is a metric space under the
absolute value $|A| = \max |A_{ij}|$.\
Let
$U_r = \{A \in M_n(\mathbb{C}) : |A - I| < r \text{ and } \mathrm{Tr} \! \left(A\right) = 0 \}$
and take $V_r = \exp(U_r)$ an open neighborhood of
$I \in \mathrm{GL}_{n}(\mathbb{C})$ since
$\det{\exp{A}} = \exp{\mathrm{Tr} \! \left(A\right)} = 1$. Suppose that
$H \subset V_r$ is a subgroup. For $B \in H$ we have $B = \exp{A}$ and
thus $B^k = (\exp{A})^k = \exp{(kA)}$ so $kA \in U_r$. However,
$|k A| = |k| \cdot |A|$ which, by the archimedean property, can be taken
arbitrarily large if $|A| > 0$. Since all $A \in U_r$ have $|A| < r$
this contradicts the fact that $k A \in U_r$ unless
$|A| = 0 \implies A = 0 \implies B = I$. Thus, $H = \{ I \}$. ◻
:::

::: remark
*Remark 4*. The above proof depends crucially on the archimedean
property.
:::

::: proposition
**Proposition 12**. Any continuous homomorphism
$\rho: G_{K} \to \mathrm{GL}_{n}(\mathbb{C})$ factors through
$\mathrm{Gal} \small(F/K \small)$ for some finite Galois extension
$F / K$. Hence its image is finite.
:::

::: proof
*Proof.* By Lemma [11](#lem:no_subgroups_of_nbd){reference-type="ref"
reference="lem:no_subgroups_of_nbd"}, let $V$ be an neighborhood of $I$
in $\mathrm{GL}_{n}(\mathbb{C})$ which contains no non-trivial
subgroups. Then $U = \rho^{-1}(V)$ is an open neighborhood of
$\mathrm{id}\in G_K$ and thus contains a normal subgroup of the form
$\mathrm{Gal} \small(\bar{K} / F \small)$ for some galois extension
$F / K$. Since $\rho$ is a homomorphism, the image of
$\mathrm{Gal} \small(\bar{K} / F \small)$ is subgroup contained in $V$.
But $V$ does not have any nontrivial subgroup so
$\mathrm{Gal} \small(\bar{K} / F  \small) \subset \ker{\rho}$ is
actually in the kernel of $\rho$. Thus, $\rho$ factors through the
quotient,
$$\mathrm{Gal} \small(\bar{K} / K \small) / \mathrm{Gal} \small(\bar{K} / F \small) \cong \mathrm{Gal} \small(F / K \small)$$
which is finite. Hence $\rho$ has finite image. ◻
:::

::: corollary
**Corollary 13**. Every $1$-dimensional Galois representation of
$G_{\mathbb{Q}}$ over $\mathbb{C}$ is a Dirichlet character.
:::

::: proof
*Proof.* Any Galois representation
$\rho : G_{\mathbb{Q}} \to \mathrm{GL}_{1}(\mathbb{C}) \cong \mathbb{C}^\times$
factors through the quotient,
$$\rho : \mathrm{Gal} \small(F / \mathbb{Q} \small) \to \mathbb{C}^\times$$
where $F$ is a Galois number field. However, $\mathbb{C}^\times$ is
abelian so $\rho$ descends to the abelianization. Let
$C \triangleleft \mathrm{Gal} \small(F / \mathbb{Q} \small)$ be the
commutator subgroup. By the Galois correspondence,
$F^{\mathrm{ab}} = F^C$ is a Galois extension of $\mathbb{Q}$ with
Galois group,
$$\mathrm{Gal} \small(F^{\mathrm{ab}} / \mathbb{Q} \small) \cong \mathrm{Gal} \small(F / \mathbb{Q} \small) / C = \mathrm{Gal} \small(F / \mathbb{Q} \small)^{\mathrm{ab}}$$
By the Kronecker-Weber theorem, every abelian extension of $\mathbb{Q}$
lies inside some cyclotomic field. So
$F^{\mathrm{ab}} \subset \mathbb{Q}(\zeta_N)$ giving a restriction map
on the Galois groups. This gives a commutative diagram,

::: center
:::

Thus $\rho$ factors through a Dirichlet character,
$$\chi : \mathrm{Gal} \small( \mathbb{Q}(\zeta_n) / \mathbb{Q} \small) \cong (\mathbb{Z}/ N \mathbb{Z})^\times \to \mathbb{C}^\times$$ ◻
:::

# $\ell$-adic Galois Representations

The archimedean nature of $\mathbb{C}$ leading to Lemma
[11](#lem:no_subgroups_of_nbd){reference-type="ref"
reference="lem:no_subgroups_of_nbd"} made the theory of complex Galois
representations fairly uninteresting. However, if we consider a
non-archimedean field such as $\mathbb{Q}_{\ell}$, this restriction is
lifted. In fact,

::: proposition
**Proposition 14**. Every neighborhood of
$1 \in \mathbb{Q}_{\ell}^\times$ contains a nontrivial subgroup.
:::

::: proof
*Proof.* Let $U$ be an open neighborhood of
$1 \in \mathbb{Q}_{\ell}^\times$, then there exists $n \in \mathbb{Z}^+$
such that $$V(n) = 1 + \ell^n \mathbb{Z}_{\ell} \subset U$$ However,
$V(n)$ is a nontrivial subgroup of $\mathbb{Q}_{\ell}^\times$ because
$$(1 + \ell^n z)^{-1} - 1 = \frac{ \ell^n z }{1 + \ell^n z} = \ell^n \frac{z}{1 + \ell^n z} \in \ell^n \mathbb{Z}_{\ell}$$
since $1 + \ell^n z \in \mathbb{Z}_{\ell}^\times$. ◻
:::

## One-Dimensional Galois Representations

::: trivlist
Let $F/\mathbb{Q}$ be Galois, $p \in \mathbb{Z}$ be a prime, and
$\mathfrak{p}$ is a prime in $\mathcal{O}_{F}$ lying above $p$. Then
$\mathrm{Frob}_{\mathfrak{p}}\in \mathrm{Gal} \small(F/\mathbb{Q} \small)$
is defined by
$$\mathrm{Frob}_{\mathfrak{p}}(x) \equiv x^p  \: \: \mathrm{mod} \:  \mathfrak{p}$$
for $x \in \mathcal{O}_{F}$.
:::

::: lemma
**Lemma 15**. Let $F = \mathbb{Q}(\zeta_N)$. Let $p$ be a prime in
$\mathbb{Z}$ such that $p \centernot \mid N$. Let $\mathfrak{p}$ be a
prime in $F$ lying above $p$. Then
$\mathfrak{f}_{\mathfrak{p}} = \mathcal{O}_{F} / \mathfrak{p} = \mathbb{F}_{p}[\zeta_N]$.
Let $x \in \mathcal{O}_{F}$, then we can describe the action of
$\mathrm{Frob}_{\mathfrak{p}}$ by
$$\mathrm{Frob}_{\mathfrak{p}}\left( \sum_{i = 0}^{N-1} a_i \zeta_N^i \right) \equiv \left( \sum_{i = 0}^{N-1} a_i \zeta_N^i \right)^p \equiv \sum_{i = 0}^{N-1} a_i \zeta_N^{ip} \: \: \mathrm{mod} \: \mathfrak{p}$$
That is to say, the action of $\mathrm{Frob}_{\mathfrak{p}}$ takes
$\zeta_N$ to $\zeta_N^p$.
:::

::: trivlist
The $\ell$-adic cyclotomic character
$\chi_{\ell} : G_\mathbb{Q}\to \mathbb{Q}_{\ell}^\times$ of
$G_\mathbb{Q}$ is defined by,
$$\sigma \mapsto (m_1, m_2, m_3, \dots ) \text{ where } \sigma(\zeta_{\ell^n}) = \zeta_{\ell^n}^{m_n}$$
is a $1$-dimensional Galois representation since $m_n$ is defined up to
multiples of $\ell^n$.
:::

::: remark
*Remark 5*. Notice that when $p \neq \ell$ we have,
$$\chi_{\ell}(\mathrm{Frob}_{\mathfrak{p}}) = p$$ In particular, the
image of $\chi_{\ell}$ is infinite. Therefore, $\ell$-adic Galois
representations allow for richer structure than those over $\mathbb{C}$.
:::

::: trivlist
We write $\mathbb{Q}_\ell(1)$ for the vectorspace $\mathbb{Q}_\ell$ with
the cyclotomic character Galois rep
$\chi_\ell : G_\mathbb{Q}\to \mathbb{Q}_\ell^\times = \mathrm{GL}_{1}(\mathbb{Q}_\ell)$
acting on it. For any $\mathbb{Q}_\ell$-rep of $G$ we define the
$m^{\text{th}}$-Tate twist via,
$$V(m) = V \otimes_{\mathbb{Q}_\ell} \mathbb{Q}_\ell(1)^{\otimes m} = V \otimes_{\mathbb{Q}_\ell} \mathbb{Q}_\ell(m)$$
and we define,
$$\mathbb{Q}_\ell(-1) = \mathbb{Q}_\ell(1)^{\otimes -1} = \mathbb{Q}_{\ell}(1)^\vee$$
the dual representation.
:::

::: remark
*Remark 6*. Note that there is a more natural way to see the cyclotomic
character arrise. The torsions points
$\mu_{\ell^n}(\overline{\mathbb{Q}}) = \overline{\mathbb{Q}}[\ell^n]$
have a natural action of $G_{\mathbb{Q}}$ which is compatible with
restriction maps. Then we define,
$$\mathbb{Z}_\ell(1) = \varprojlim_{n} \mu_{\ell^n}(\overline{\mathbb{Q}})$$
How does $G_\mathbb{Q}$ act on $\mathbb{Z}_\ell(1)$. Well, we take a
sequence
$(\zeta_\ell^{a_1}, \zeta_{\ell^2}^{a_2}, \zeta_{\ell^3}^{a_3}, \dots )$
and map it to,
$$\sigma(\zeta_\ell^{a_1}, \zeta_{\ell^2}^{a_2}, \zeta_{\ell^3}^{a_3}, \dots ) = (\sigma(\zeta_\ell^{a_1}), \sigma(\zeta_{\ell^2}^{a_2}), \sigma(\zeta_{\ell^3}^{a_3}), \dots ) = (\zeta_\ell^{m_1 a_1}), \zeta_{\ell^2}^{m_2 a_2}, \zeta_{\ell^3}^{m_3 a_3},  \dots )$$
so representing the sequence by its exponents, $\sigma \in G_\mathbb{Q}$
acts via multiplication by the sequence $(m_1, m_2, m_3, \dots)$. Then
we can define the Galois-rep $\mathbb{Q}_\ell(1)$ as,
$$\mathbb{Q}_\ell(1) = \mathbb{Z}_\ell(1) \otimes_{\mathbb{Z}_\ell} \mathbb{Q}_\ell$$
where $\mathbb{Q}_\ell$ is the trivial $\ell$-adic $G$-rep and we take
the tensor product as $G$-modules. We can do the same construction for
all primes simultaneously to get,
$$\hat{\mathbb{Z}}(1) = \varprojlim_n \mu_n(\overline{\mathbb{Q}})$$
which has an analogous $G_\mathbb{Q}$-action. In fact, by the Chinese
Remainder Theorem, there is a canonical decomposition of
$G_\mathbb{Q}$-modules,
$$\hat{\mathbb{Z}}(1) = \prod_{\ell} \mathbb{Z}_\ell(1)$$ However, by
the above product decomposition, $\hat{\mathbb{Z}}(1)$ is not a domain
so we cannot make it into a field and discuss its corresponding
representations which is why we content ourselves to work
$\ell$-adically in each prime.
:::

## Higher-Dimensional Galois Representations

::: theorem
**Theorem 16**. Let $G$ be profinite. Any continuous homomorphism
$\rho : G \to \mathrm{GL}_{n}(\overline{\mathbb{Q}_{\ell}})$ has image
$\rho(G) \subset \mathrm{GL}_{n}(K)$ where $K$ is a finite extension of
$\mathbb{Q}_{\ell}$.
:::

::: proof
*Proof.* By Theorem
[10](#thm:algebraic_extensions_adics){reference-type="ref"
reference="thm:algebraic_extensions_adics"}, the finite extensions of
$\mathbb{Q}_{\ell}$ are indexed by elements
$\alpha \in \overline{\mathbb{Q}}$ and are thus countable. Write,
$$\overline{\mathbb{Q}_{\ell}} = \bigcup_{i \in I} E_i$$ where $E_i$ are
finite extensions of $\mathbb{Q}_{\ell}$ and $I$ is countable. A
topological space $X$ is a *Baire space* if and only if given any
countable collection of closed sets $F_i$ in $X$, each with empty
interior in $X$, their union also has empty interior. The image
$\rho(G)$ is compact because $G$ is compact and $\rho$ is continuous.
Therefore $\rho(G)$ is a complete metric space and thus Baire space by
the Baire category theorem.\
Let $F_i$ be the closure of $\mathrm{GL}_{n}(E_i) \cap \rho(G)$ in
$\rho(G)$. Then $$\rho(G) = \bigcup_{i \in I} F_i$$ has nonempty
interior in $\rho(G)$. Therefore, there exists $i \in I$ such that $F_i$
contains a non-empty open subset $U \subset \rho(G)$. After translating
and shrinking $U$, we may assume it is an open subgroup of $\rho(G)$.
The quotient $\rho(G) / U$ is covered by the sets
$\mathrm{GL}_{n}(E_j) \cap \rho(G)$ for each $E_j \supset E_i$. Since
$\rho(G)$ is compact, the cover by open cosets must be finite because
there do not exist any proper subcovers. Thus the quotient $\rho(G) / U$
is finite so we need only a finite number of such $j$. The compositum
$K$ of the fields $E_j$ is then a finite extension of
$\mathbb{Q}_{\ell}$. Furthermore, $\rho(G) \subset \mathrm{GL}_{n}(K)$
because it covers $\rho(G) / U$ and $U \subset \mathrm{GL}_{n}(K)$ so
each coset $g U \subset \mathrm{GL}_{n}(K)$. ◻
:::

::: corollary
**Corollary 17**. All $\ell$-adic Galois representations
$\rho : \mathrm{Gal} \small(F / K \small) \to \mathrm{GL}_{n}(\overline{\mathbb{Q}_{\ell}})$
are of the form,
$$\rho : \mathrm{Gal} \small(F / K \small) \to \mathrm{GL}_{n}(\mathbb{Q}_{\ell}(\alpha))$$
where $\alpha \in \overline{\mathbb{Q}}$.
:::

# Galois Representations Attached to Elliptic Curves

::: trivlist
An elliptic curve is a smooth, projective curve of genus one with a
distinguished point $O$. More concretely, an elliptic curve $E$ defined
over a field $K$ is a planar algebraic curve given by,
$$\left\{ (x,y) \in \bar{K}^2 \mid y^2 = x^3 + ax^2 + bx + c \right\} \cup \left\{ O \right\} \subset \bar{K}^2$$
for constants $a,b,c \in K$ such that the equation is non-singular. The
distinguished point $O$ is viewed as the "point at infinity." For any
$L / K$, the set of $L$-rational points of $E$ is,
$$E(L) = \left\{ (x,y) \in L^2 \mid y^2 = x^3 + ax^2 + bx + c \right\} \cup \left\{ O \right\} \subset L^2$$
When $L/K$ is algebraic, that is, $K \subset L \subset \bar{K}$, then
$E(L) = E \cap L$ which is exactly the set of fixed points of $E$ under
the action of $\mathrm{Gal} \small(\bar{K}/L \small)$.
:::

::: remark
*Remark 7*. Elliptic curves are, remarkably, abelian varieties meaning
there exists a map $+ : E \times E \to E$ expressed by rational
functions which gives $E$ the structure of an abelian group with
identity $O$.
:::

::: trivlist
Let $E$ be an elliptic curve defined over $K$. For $n \in \mathbb{Z}$,
define the $n$-torsion of $E$, denoted by $E[n]$, to be the kernel of
the map $x \mapsto n x$.
:::

::: proposition
**Proposition 18**. Let $E$ be an elliptic curve defined over a number
field $K$ (in particular $\mathbb{Q}$) then
$E[n] \cong (\mathbb{Z}/ n \mathbb{Z}) \oplus (\mathbb{Z}/ n \mathbb{Z})$
:::

::: proof
*Proof.* I will give a sketch of the proof assuming some knowledge of
Weierstrass elliptic functions. Associated to any elliptic curve $E$
over $\mathbb{C}$ is a complex lattice $\Lambda \subset \mathbb{C}$ and
a doubly periodic meromorphic function $\wp(z ; \Lambda)$ defined on
$\mathbb{C}$ which is constant on translates by $\Lambda$. Therefore
$\wp$ descends to a function of quotient
$\mathbb{C}/ \Lambda \to \mathbb{C}$. It turns out that, magically,
$\wp : \mathbb{C}/ \Lambda \to E$ given by $z \mapsto (\wp(z), \wp'(z))$
is an isomorphism of groups. In particular, $E$ is topologically a
torus. Let $\Lambda$ be generated by two complex numbers
$\omega_1, \omega_2$ called the fundamental periods of the lattice. Then
the $n$-torsion points in $\mathbb{C}/ \Lambda$ are exactly the points,
$$z = \frac{a}{n} \omega_1 + \frac{b}{n} \omega_2 \text{ for } a,b \in \mathbb{Z}/ n \mathbb{Z}$$
such that $n z = a \omega_1 + b \omega_2 \in \Lambda$ is trivial in
$\mathbb{C}/ \Lambda$. Therefore,
$E[n] \cong (\mathbb{Z}/ n \mathbb{Z}) \oplus (\mathbb{Z}/ n \mathbb{Z})$
as abstract groups. ◻
:::

## The Tate Module

::: proposition
**Proposition 19**. Let $E$ be an elliptic curve defined over $K$ then
there is a natural action of the absolute Galois group,
$$\mathrm{Gal} \small(\bar{K} / K \small) \to \mathrm{Aut} \small(E \small)$$
which, because automorphism preserve $n$-torsion, reduces to an action,
$$\mathrm{Gal} \small(\bar{K} / K \small) \to \mathrm{Aut} \small(E[n] \small) \cong \mathrm{GL}_{2}(\mathbb{Z}/ n \mathbb{Z})$$
:::

::: proof
*Proof.* Let $\sigma \in \mathrm{Gal} \small(\bar{K} / K \small)$ act
component-wise on $E$ (and fix $O$). Because $\sigma$ is a field
automorphism fixing $K$, the action of $\sigma$ preserves the defining
equations of $E$ so it gives a map $E \to E$. Furthermore, since
addition in $E$ is given by rational functions with coefficients in $K$,
the action of $\sigma$ also preserves addition, that is,
$$\sigma(P + Q) = \sigma(P) + \sigma(Q)$$ and thus $\sigma$, being
inevitable point-wise, is an automorphism of $E$. Finally, let
$P_1, P_2$ be a $\mathbb{Z}/ n \mathbb{Z}$-basis of $E[n]$ as a free
$\mathbb{Z}/ n \mathbb{Z}$-module. Then there exist unique elements
$a, b, c, d \in \mathbb{Z}/ n \mathbb{Z}$ such that,
$$\sigma(P_1) = a P_1 + c P_2 \text{  and  } \sigma(P_2) = b P_1 + d P_2$$
Then the action of $\sigma$ on any element $n_1 P_1 + n_2 P_2$ is given
by,
$$\sigma(n_1 P_1 + n_2 P_2) = n_1 \sigma(P_1) + n_2 \sigma(P_2) = (a n_1 + b n_2) P_1 + (c n_1 + d n_2) P_2 = n_1' P_1 + n_2' P_2$$
Which we may write suggestively as, $$\begin{pmatrix}
n_1'
\\
n_2'
\end{pmatrix}
=
\begin{pmatrix}
a & b
\\
c & d
\end{pmatrix}
\begin{pmatrix}
n_1
\\
n_2
\end{pmatrix}$$ explicitly showing the representation of
$\mathrm{Gal} \small(\bar{K} / K \small)$ as matrices in
$\mathrm{GL}_{2}(\mathbb{Z}/ n \mathbb{Z})$. ◻
:::

::: trivlist
The Tate module of an elliptic curve $E$ is the group,
$$T_{\ell}(E) = \varprojlim E[\ell^n]$$ under the multiplication by
$\ell$ maps,

::: center
:::

The Tate module $T_{\ell}(E)$ can be given the structure of a
$\mathbb{Z}_{\ell}$ module via the action, $(a_n) \in \mathbb{Z}_{\ell}$
acts on $(P_n) \in T_{\ell}(E)$ via
$(a_n) \cdot (P_n) = (a_n \cdot P_n)$. This action is well defined
because $P_n$ has $\ell^n$ torsion so $a_n$ need only be defined up to
multiples of $\ell^n$.
:::

::: {#thm:galois_rep_tate_module .theorem}
**Theorem 20**. Let $E$ be an elliptic curve over $K / \mathbb{Q}$.
There exists an $\ell$-adic Galois representation
$V_{\ell} E = T_{\ell}(E) \otimes_{\mathbb{Z}_{\ell}} \mathbb{Q}_{\ell}$
with action,
$$\rho_{E,\ell} : \mathrm{Gal} \small(\bar{K}/K \small) \to \mathrm{Aut} \small(V_{\ell}E \small) \cong \mathrm{GL}_{2}(\mathbb{Q}_{\ell})$$
called the Galois representation attached to $E$ at $\ell$.
:::

::: proof
*Proof.* For each $n \in \mathbb{Z}^{+}$ we have an action of
$\sigma \in \mathrm{Gal} \small(\bar{K} / K \small)$ on
$P \in E[\ell^n]$ component-wise. However,
$\ell \cdot \sigma(P) = \sigma(\ell \cdot P)$ because $\sigma$ is a
group homomorphism of $E$ so $\sigma$ is compatible with the restriction
maps. Therefore, $\sigma$ lifts to $\tilde{\sigma}$ a unique
automorphism of the Tate module $T_{\ell}(E)$. By choosing bases
compatible with the multiplication by $\ell$ maps gives an isomorphism,
$$T_{\ell}(E) \cong \varprojlim{(\mathbb{Z}/ \ell^n \mathbb{Z}) \oplus (\mathbb{Z}/ \ell^n \mathbb{Z})} \cong \mathbb{Z}_{\ell} \oplus \mathbb{Z}_{\ell}$$
The action on the Tate module induces a map,
$$\rho_T : \mathrm{Gal} \small(\bar{K}/K \small) \to \mathrm{Aut} \small(T_{\ell}(E) \small) \cong  \mathrm{Aut} \small(\mathbb{Z}_{\ell} \oplus \mathbb{Z}_{\ell} \small) = \mathrm{GL}_{2}(\mathbb{Z}_{\ell}) \subset \mathrm{GL}_{2}(\mathbb{Q}_{\ell})$$
The desired map is given by taking the tensor product with the trivial
$\ell$-adic representation $(\mathbb{Q}_{\ell}, \rho_0)$,
$$\rho_{E, \ell} = \rho_T \otimes \rho_0  : \mathrm{Gal} \small(\bar{K}/K \small) \to \mathrm{Aut} \small(T_{\ell} \otimes_{\mathbb{Z}_{\ell}} \mathbb{Q}_{\ell} \small) \cong \mathrm{Aut} \small(\mathbb{Q}_{\ell} \otimes \mathbb{Q}_{\ell} \small) = \mathrm{GL}_{2}(\mathbb{Q}_{\ell})$$
and we take the $\mathbb{Q}_{\ell}$ vector space,
$$V_{\ell} E = T_{\ell} \otimes_{\mathbb{Z}_{\ell}} \mathbb{Q}_{\ell} \cong (\mathbb{Z}_{\ell} \oplus \mathbb{Z}_{\ell}) \otimes_{\mathbb{Z}_{\ell}} \mathbb{Q}_{\ell} = \mathbb{Q}_{\ell} \oplus \mathbb{Q}_{\ell}$$ ◻
:::

::: remark
*Remark 8*. We have seen here an interesting $\ell$-adic representation
arising naturally from algebraic geometry. It is a truly remarkable fact
that a very large class of all $\ell$-adic Galois representations arise
from geometric objects.
:::

## Complex Multiplication

We have discussed how $\ell$-adic representations can give information
about the underlying geometry. Galois representations can also be used
to determine algebraic properties of Galois groups from geometric
structures.

::: trivlist
An elliptic curve $E$ has complex multiplication, is CM for short, if
there exists an endomorphism of $E$ which is not a multiplication by $n$
map.
:::

::: remark
*Remark 9*. From the complex analytic viewpoint, such a map is
multiplication by $c \in \mathbb{C}$ hence the name. Note, an
endomorphism of an elliptic curve is required to be an isogeny i.e.
given by rational functions over $\bar{K}$.
:::

::: lemma
**Lemma 21**. Let $E$ be an elliptic defined over $K$ with complex
multiplication and denote the exceptional endomorphism by
$\phi : E \to E$. There exists a finite extension $K^{\mathrm{CM}} / K$
such that
$\forall \sigma \in \mathrm{Gal} \small(\bar{K} / K^{\mathrm{CM}} \small) : \phi \circ \sigma = \sigma \circ \phi$
:::

::: proof
*Proof.* Because $\phi$ is an isogeny, it is given by rational functions
with coefficients in $\bar{K}$. Let $K^{\mathrm{CM}} = K(S)$ where $S$
is the set of coefficients of $\phi$. Then for any automorphism
$\sigma \in \mathrm{Gal} \small(\bar{K} / K^{\mathrm{CM}} \small)$ we
know that $\sigma$ preserves the coefficients of $\phi$ and thus,
because $\sigma$ is a field homomorphism and $\phi$ is a rational
function, $\sigma \circ \phi(P) = \phi \circ \sigma(P)$ for any point
$P \in E$. ◻
:::

::: trivlist
The field $K^{\mathrm{CM}}(E[n])$ is the field extension of
$K^{\mathrm{CM}}$ generated by the coordinates of all points in $E[n]$.
Furthermore define the $\ell^\infty$-torsion,
$$E[\ell^\infty] = \bigcup_{n} E[\ell^n]$$ and the field,
$$K^{\mathrm{CM}}(E[\ell^\infty]) = \bigcup_{n} K^{\mathrm{CM}} (E[\ell^n]) = \varinjlim K^{\mathrm{CM}}(E[\ell^n])$$
:::

::: lemma
**Lemma 22**. For each $n \in \mathbb{Z}^{+}$ the extension
$K^{\mathrm{CM}} (E[\ell^n]) / K^{\mathrm{CM}}$ is finite Galois and
therefore $K^{\mathrm{CM}} (E[\ell^\infty]) / K^{\mathrm{CM}}$ is
Galois.
:::

::: proof
*Proof.* Take
$\sigma \in \mathrm{Gal} \small(\bar{K} / K^{\mathrm{CM}} \small)$ and
consider $\sigma(K^{\mathrm{CM}} (E[\ell^n]))$. Since $\sigma$ fixes
$K^{\mathrm{CM}}$ the image of $K^{\mathrm{CM}} (E[\ell^n])$ is entirely
determined by where $\sigma$ maps the generators which are coordinates
of $E[\ell^n]$. However, we have shown that $\sigma$ is an automorphism
of $E$ and thus must take $\ell^n$-torsion to $\ell^n$-torsion.
Therefore, for each $P \in E[\ell^n]$ we have $\sigma(P) \in E[\ell^n]$
so $\sigma$ must map coordinates of $E[\ell^n]$ to coordinates of
$E[\ell^n]$. Therefore,
$\sigma(K^{\mathrm{CM}} (E[\ell^n])) = K^{\mathrm{CM}} (E[\ell^n])$
proving that $K^{\mathrm{CM}} (E[\ell^n])$ is Galois over
$K^{\mathrm{CM}}$. Furthermore, since $E[\ell^n]$ is finite, there are
only finitely many possible permutations and thus finitely map
automorphisms of $K^{\mathrm{CM}} (E[\ell^n])$ proving the extension is
finite. ◻
:::

::: theorem
**Theorem 23**. Let $E$ be an elliptic curve defined over $K$ with
complex multiplication $\phi : E \to E$ such that $\phi$ restricted to
$E[\ell]$ is not the multiplication by $n$ map for any
$n \in \mathbb{Z}$. Then the extension
$K^{\mathrm{CM}}(E[\ell^\infty]) / K^{\mathrm{CM}}$ is abelian.
:::

::: proof
*Proof.* Restricting the map given in Theorem
[20](#thm:galois_rep_tate_module){reference-type="ref"
reference="thm:galois_rep_tate_module"} gives a representation,
$$\rho^{\mathrm{CM}}_{E, \ell} : \mathrm{Gal} \small(\bar{K} / K^{\mathrm{CM}} \small) \to \mathrm{Aut} \small(V_{\ell}E \small) \cong \mathrm{GL}_{2}(\mathbb{Q}_{\ell})$$
We have that
$\rho^{\mathrm{CM}}_{E, \ell}(\sigma) = I \iff \sigma \cdot (P_n) = (\sigma(P_n)) = (P_n)$
for every $(P_n) \in T_{\ell}(E)$. Therefore,
$\sigma \in \ker{\rho^{\mathrm{CM}}_{E, \ell}}$ if and only if $\sigma$
acts trivially on $E[\ell^n]$ for each $n \in \mathbb{Z}^{+}$ or
equivalently, since $\sigma$ acts coordinate-wise on $E[\ell^n]$, acting
trivially on the coordinates of $E[\ell^n]$. However, acting trivially
on the generators is equivalent to fixing the field
$K^{\mathrm{CM}}(E[\ell^n])$ for all $n$ or, equivalently, fixing the
compositum $K^{\mathrm{CM}}(E[\ell^\infty])$. Therefore,
$$\ker{\rho^{\mathrm{CM}}_{E,\ell}} = \mathrm{Gal} \small(\bar{K} / K^{\mathrm{CM}}(E[\ell^\infty]) \small)$$
Furthermore, the kernel is closed (because the action is continuous) and
normal so the quotient,
$$\mathrm{Gal} \small(\bar{K} / K^{\mathrm{CM}} \small) / \mathrm{Gal} \small(\bar{K} / K^{\mathrm{CM}}(E[\ell^\infty]) \small) \cong \mathrm{Gal} \small(K^{\mathrm{CM}}(E[\ell^\infty]) / K^{\mathrm{CM}} \small)$$
corresponds to the Galois extension
$K^{\mathrm{CM}}(E[\ell^\infty]) / K^{\mathrm{CM}}$. The action then
injectivly factors through the quotient as,

::: center
:::

so the group
$\mathrm{Gal} \small(K^{\mathrm{CM}}(E[\ell^\infty]) / K^{\mathrm{CM}} \small)$
is embedded in $\mathrm{GL}_{2}(\mathbb{Q}_{\ell})$. However,
$\sigma \circ \phi = \phi \circ \sigma$ for all
$\sigma \in \mathrm{Gal} \small(\bar{K} / K \small)$ and $\phi$ is not
multiplication by $n$ on $E[\ell]$ so
$\phi \in \mathrm{Aut} \small(V_{\ell}E \small) \cong \mathrm{GL}_{2}(\mathbb{Q}_{\ell})$
corresponds to a non-scalar matrix. However, all matrices in
$\mathrm{GL}_{2}(\mathbb{Q}_{\ell})$ which commute with a fixed
non-scalar matrix (which remains non-scalar in the reduction modulo
$\ell$) commute with each other (technical exercise). Therefore, the
image of
$\mathrm{Gal} \small(K^{\mathrm{CM}}(E[\ell^\infty]) / K^{\mathrm{CM}} \small)$
in $\mathrm{GL}_{2}(\mathbb{Q}_{\ell})$ is abelian so by the embedding
$\mathrm{Gal} \small(K^{\mathrm{CM}}(E[\ell^\infty]) / K^{\mathrm{CM}} \small)$
is abelian itself. ◻
:::

::: example
**Example 3**. Consider the elliptic curve over $\mathbb{Q}$ defined by,
$$E : y^2 = x^3 + x$$ which has an exceptional automorphism
$\phi : E \to E$ given by, $$\phi(x, y) = (-x, iy)$$ which preserves the
defining equation and the group law. Clearly,
$K^{\mathrm{CM}} = \mathbb{Q}(i)$ since $i$ is the only non-rational
coefficient defining $\phi$. One can easily check that $\phi$ is not
multiplication by $n$ on any torsion subgroup. Therefore, the extensions
$$\mathbb{Q}(i)(E[\ell^\infty]) / \mathbb{Q}(i)$$ given by adjoining
$\ell^n$-torsion points of $E$ are abelian for each $\ell$.
:::

::: remark
*Remark 10*. This is an example of Kronecker's Jugendtraum or "Dream of
Youth" which was to generate all abelian extensions of a number field
$K$ by adjoining special values of certain interesting functions. For
example, the Kronecker-Weber theorem does this for $K = \mathbb{Q}$
saying that the abelian extensions of $\mathbb{Q}$ are exactly the
subfields of $\mathbb{Q}(f(\tfrac{1}{n}))$ where $f(x) = e^{2 \pi i x}$
is a very special analytic function. It turns out that, astonishingly,
our above construction generated *all* the abelian extensions of
$\mathbb{Q}(i)$. That is, the compositum over all primes $\ell$ of
$\mathbb{Q}(i)(E[\ell^\infty])$ gives the maximal abelian extension of
$\mathbb{Q}(i)$. Equivalently, every finite abelian extension of
$\mathbb{Q}(i)$ is contained in $\mathbb{Q}(i)$ adjoined some finite set
of torsion points on the curve $E$. The theory of elliptic curves using
Galois representations has now realized Kronecker's dream for all
imaginary quadratic fields. However, the general case remains a mystery.
:::
