DSLs
Questions from Martin Fowler's book

1. Do I create an internal or external DSL? I.e. one in a language, or make a new language?
2. Need to consider separation of Semantic Model and DSL syntax - do I want to do this?
3. What is the grammar I want to work with?
4. Writing tests - Once I have the grammar, I can write a test suite. Tests should be broken down into testing the semantic model, testing the parser, and testing the scripts.
5. Do I put the error handling in the parser or the semantic model? (semantic model more expressive, but can't identify line numbers as easily) One option is to handle errors in the semantic model, but trigger them in the parser - this separates the concerns

INTERNAL DSLs - Qs
1. Which way of creating functions do I use in the DSL? Method chaining, function sequence, or nested functions? It might be best to use a sequence
2. Using literal maps (python dictionaries) to collect together items?
3. Choosing the functions by way of the grammar -- (see P79 in Fowler) - certain DSL rules suggest certain DSL structures: i.e. parent -> first -> second -> third -- nested functions, whereas parent --> first --> maybe second? --> maybe third? is probably better for method chaining
4. Do we use closures? (i.e. lambda expressions)
4. Parse tree manipulation - do we use this to allow translation from one language to another?
5. Literal extensions -- do we engage these? You can do things like in Ruby on Rails, where you can do 5.days.ago to get the date 5 days ago
6. Dynamic reception - do I want this? Dynamic reception in dynamic languages means you can call methods that don't exist yet, and when it encounterss it, handle it differently than just throwing an error. For example: rather than have people.find_by(firstname, "martin"), you can write people.find_by.first_name("martin"), and when this throws an error, you can create the first function


EXTERNAL DSLS - Qs
1. What's your syntactic analysis strategy? Syntactic analysis is all about recognising that an event is an event and a command a command. There are several strategies: a) delimiter directed translation (ie.. split it apart accordng to keywords/symbols B) syntax directed translation (defined by BNF)
2. If we go with syntax directed translation, how should I go about generating the parser? A) recursive descent b) parser combinator c) parser generator
3. If we go with parser generators, which one should we use?
4. What do we do with the result of parsing the input? (we will create a semantic model). We can: A) do embedded translation b) tree construction and then populate the semantic model
5. Top down or bottom up parsing? CFGs vs PEGs?




#CHOOSING BETWEEN EXTERNALL AND INTERNAL DSLS

1. Learning curve
- Internal - you're using a language you already know, whereas with external DSLs you have to learn about parsers, parser generators and grammars
- however, internal DSLs often rely on very odd tricks in order to come up with something that's fluent

2. Cost of building
- building a DSL is a little bit complicated -and you have to ensure you separate the cost of building the model from building the syntax. THe main cost for internal DSLs is in the expression builder - whereas the main cost for external DSLs is in building the parser -- these map onto each other in a reasonable way

3. Programmar familiarity
- with an internal DSL, you can rely on tools like an IDE to debug, do syntax highlighting, autocompletion, and everything else. However, as soon as you move to an external DSL, you are one layer separate from this

4. Communication with domain experts
- internal DSLs don't have as much flexibility as an external DSL. This means that you may not be able to communicate to domain experts as easily. However, 

5. Mixing in the host language
- if you use an internal DSL, you can drop back into the standard language if you want more custom functionality. 
- if you use an external DSL, you can't do this

6. External DSLs have a strong expressiveness boundary- meaning they are great for limiting the usage to specific functionality. This means that external DSLs prevent mistakes snad 

7. Risk of trying to do too much: internal DSLs can rely on the host language for functionality that does not fall within their remit, whereas sometimes the temptation is to try and recreate a GPL with a DSL

GENERAL NOTES

Distinction between AST and Semantic model
1. AST < representation of the hierarchy / relationship between things. However, it has no information about the quality of the relationship. For exaample, 5+5 could be 55 in some semantic models.




What's an external DSL? Differennt language from the languageg it compiles to. I.e. this might involve coming up with your own syntax.

This is separate from an internal DSL, which is valid in the general purpose language it is part of.

the job of the parser is to populate the semantic model



Elements of a DSL:
1. DSL Text (comprised from a DSL grammar)
2. Syntax Tree (also generated according to the rules from the grammar)
3. Symbol table (so we can store data)



Internal DSLs

Rather than
a = new Controller()
a.setVariable(10)

you can do a = controller.setvariaable(10).setfuel(10) -- all in one expressions

These are called fluent expressions, and are a definng feature of internal DSLs

Command/Query separation -- methods should be divided into commands and queries.
A query is a method that returns a value but does nopt change the state. A command usually does not return a value, but does change state

Fluent interfaces break this (as each method returns an updated object), and the names might make no sense in context, but you can create sentences with them, like the CSHARP testing framework below:
hand.GetHandRank().Should().Be(HandRank.FullHouse);

You can manage this difference by creating an expression builder, which has the task of taking a series of commands from a fluent interface, and building it into a sequence of command query API calls.

The expression builder is a lot like a parser (i.e. we build a syntax tree, we use symbol tables aand we stikll populate a semantic model) but rather than parsing a stream of tokens, it parses a stream of function calls.

Have to decide which way to use functions. The methods are:
1. method chaining
2. function sequencing. 
3. nested functions

If you function sequence, it looks like
computer();
add(1);
remove_disk();

Whereas method chaining looks loike
compuger().add(1).remove_disk?()

Nested functions look like

computer ( 
			processor(2, 0 ,
			cores(2)
			)
			) 
	

Function sequences are more complicated regarding namespaces (as it has to act on global data) unless it is contained within an object (object scoping)

If you method chain, it's obvious which object it is acting on, but the methods can only ever be used on the object, and they have to return the object.

Nested functions allow you to indicate the hierarchy of information very clearly. However, the evaluation order can be quite confusing. I.e. the functions evaluate third(second(first()))

Whereas method chaining and function sequences, allow you to write it in the order that they occur



Syntactic analysis is all about 



