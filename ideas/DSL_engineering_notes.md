##Notes

Main difference between the books seems to be that this book is mostly focusing on Language Workbenches

Language workbenches store languages in their intermediary representation (i.e. the AST is stored and modified directly, rather than)


The seven design dimensions to consider when creating a DSL (aaccording to DSL Engineering) are:
1. Expressivity
2. Coverage
3. Semantics
4. Separation of concerns
5. Completeness
6. Language Modularisation
7. Syntax


#### Domains

The domain of everything (i.e. that denoted by a GPL) is denoted by d0. When we talk about a domain, we talk about a subset of related programs in d0, that we call through a new syntax, termed D1. We can use this to talk about the semantics of our new language.


##### Expressivity

Generally, given a language d0 and a language d0.1 which is a domain of d0, d0.1 is more expressive than d0 if every program in this language is shorter than the equivalent program in d0. A weaker but more realistic version of this statement is that this is generally true.

Expressivity is usually achieved through Linguistic Abstraction - i.e. no details irrelevant to the model's purpose are expressed. 

##### Coverage

Ideally, we want coverage of a domain to be high.

We can calculate the coverage of a domain to be high with the following metric:

Coverage of domain D by language L as:

CDL = (number of D programs expressable by L) / (number of programs possible in domain D)

However it is difficult to calculate the number of possible programs. But one way of telling if you can do something is by calculating this possibility.	


#### Semantics
We define the semantics of a language by comparing the language DN to the language DN-1

Using a function OB that defines the observable behaviour of a language, the semantics of a program p in LD, can be mapped to a program q in a language D-1	 is:

semantics(PLD) := qLD-1 where OB(PLD) = OB(qLD-1)