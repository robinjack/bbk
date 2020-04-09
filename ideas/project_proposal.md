
#A DSL for Data Analysis

##Introduction
### Project Summary
The aim of this project is to create a domain-specific language (DSL) that allows programmers to perform sophisticated data analysis on data they receive, without having to code the relevant functions themselves. The idea will be to point it at some data, and then expose an API to this data that allows them to ask questions of this data easily, and analyse it.

In this introduction I will cover what DSLs are and why you should use them. I will then briefly discuss why a DSLs are appropriate for data analysis, then 

### DSLs and why to use them
DSLs (Domain-Specific Languages) are programming languages that are specific to a domain. Domain is a very broad word. A domain can be very specific, like a DSL for creating the configuration of a specific manufacturer's various Carbon Wind Turbines. Or it can be very general: a DSL for data analysis. They are differentiated from GPLs (General-Purpose Languages) in that they are generally not Turing complete, and can only be used for specific tasks.  However, this does not mean that they are lesser than GPLs, just that they have a different purpose.

DSLs are mainly useful in two different ways: increasing programmer productivity, and improving the quality of communication between domain experts and programmers.

#### Increasing Programmer Productivity

Firstly, DSLs increase programmer productivity by allowing programmers to be expressive in a limited area. For example, you would never write a piece of data analysis in regular expressions (REGEX). But REGEX is a DSL for parsing text, with a special syntax and a special use (or domain). Although Regular expressions are sometimes criticized for being cryptic, they allow programmers to do a great deal. For example:

```(?:\?|&)((?:[^=]+)=(?:[^&]*))```

This regex allows us to extract an arbitrary number of key value pairings in a url query string. Trying to implement the above logic in code would be reasonably complicated - but to a seasoned REGEX user, it would simple.

This demonstrates one of the fundamental tradeoffs you make when you decide to create a DSL: expressivity vs flexibility. Expressivity vs flexibility is a key trade-off to make at the heart of language design. The more expressive each statement is, the more things it does at one time, and the less flexible it is. 

So - generally DSLs are more expressive, and they increase programmer productivity by allowing them to achieve more with fewer lines of code. DSLs therefore work when the problem domain is well-defined, and there are relatively few, complicated functions the programmer needs access to. In building a DSL, we are generally aiming to have the language as expressive as possible, while achieving maximum coverage of the domain.

#### Improving communication with domain experts

There are two main reasons why DSLs can improve communication with domain experts.

Firstly, the existence of the semantic model of the DSL as a crucial part of its development. We will cover more on the semantic model later in this document. 

The semantic model governs how the entities involved relate to each other, the qualities of the relationships, and the things they can do. In order to design a DSL, the best approach is to work closely with a domain expert on the semantic model, to ensure that the model you create aligns with their internal model of the problem domain. If you do this, communication with domain experts about the DSL is relatively simple, as the concepts you have encoded will map onto concepts they are familiar with.

For example, perhaps you could build a DSL for engineers that allows you to code in units. You could override built-in functionality so that when you write
```15m / 3s```

this gets output as 

```
5 m/s
```

Rather than forcing the programmer to remember the units at each stage of the process, or create a new type for each combination of measurement, this allows the programmer to work fluently in the language that the domain expert (engineers) speak, and enforces the relationship in the output matches the relationships pre-determined through conversations with the domain expert.

 
 The second, and closely related reason, is that as the programmer has flexibility over how a DSL looks, the programmer who designs a DSL can feel free to obfuscate the implementation at a language level, and expose only the concepts that a domain expert might recognise. This greatly improves the likelihood that they will be able to follow what occurs in the code, even if they don't write it themselves.



### Why Data Analysis is suitable for a DSL
Data analysis is a specialised field for analysts and statisticians. There are general purpose programming languages with this topic in mind - for example R, Julia, and Matlab. However, sometimess we want to perform data analysis in other languages, without resorting to a data analysis specific language. This is why we see popular packages (Pandas, LINQ in C#, others) that allow programmers to perform data analysis simply.


## Literature Review 

There are two main books that get brought up regularly when researching language design: Domain-specific languages by Martin Fowler, and DSL Engineering by Markus Volter




### Review of DSL creation
In this section I will talk through:
1. Why to use a DSL
2. The important component parts of DSLs
3. Internal vs External DSLs
4. How to choose between an internal or an external DSL

#### Why use a DSL?
DSL's are useful in specialised contexts, and they allow for expressiveness by removing flexibility. For example - REGEX is no good for anything other than texting matching, but for text matching it is the best tool. 

#### Semantic models
The semantic model is the underlying logic of the DSL. For example - let's say you were modelling a lift system, you might model it in terms of states, transitions, and actions that could be performed on the lift.

#### DSL Syntax
The DSL syntax is how you use the DSL. It is the code you write. Generally, the syntax is a way to express the semantic model. 

#### Symbol tables
The symbol table contains the information a language/DSL needs in order to function. For example, when you set x=1, it will be set in the symbol table. But more importantly for DSLs, when you set, for example, the word _print_ as being a special value, the symbol table will contain the function or the rules for the function _print_.

#### Syntax tree
The syntax tree is built during the parsing phase of a DSL. The syntax (having been tokenized by a lexer) is put into a tree, so it is clear what to do with it. An example of this is something like the below:
```
if (1==1) {1} else {0}
```
The tokens for this will just look something like the following:

```
["if", "(", "1", "==", "1", ")", "{", "1", "}", "else", "{", "0", "}"]
```

I.e. this is just a stream of tokens. There is no information embedded within about how to understand these tokens.

The syntax tree on the other hand may have this hierarchical structure:

Here, all three statements underneath the "if" are at an equal level of hierarchy.

selection 
```
	--> ==
		--> 1
		--> 1
	--> 1
	#below is the else statement
	--> 0
```
The above is a visual representation of the abstract syntax tree. 


##### Internal DSLs
- expressiveness 
- functions - to chain, compose?
- closures?
- do we want literal expression editing?
- dynamic reception of functions

Rather than
a = new Controller()
a.setVariable(10)

you can do a = controller.setvariaable(10).setfuel(10) -- all in one expressions

These are called fluent expressions, and are a defining feature of internal DSLs

Command/Query separation -- methods should be divided into commands and queries.
A query is a method that returns a value but does not change the state. A command usually does not return a value, but does change state

Fluent interfaces break this (as each method returns an updated object), and the names might make no sense in context, but you can create sentences with them, like the CSHARP testing framework below:
hand.GetHandRank().Should().Be(HandRank.FullHouse);

You can manage this difference by creating an expression builder, which has the task of taking a series of commands from a fluent interface, and building it into a sequence of command query API calls.

The expression builder is a lot like a parser (i.e. we build a syntax tree, we use symbol tables aand we stikll populate a semantic model) but rather than parsing a stream of tokens, it parses a stream of function calls.

Have to decide which way to use functions. The methods are:
1. function sequencing
2. method chaining
3. nested functions

If you function sequence, it looks like
computer();
add(1);
remove_disk();

Whereas method chaining looks loike
computer().add(1).remove_disk?()

Nested functions look like

computer(processor(2, 0 ,cores(2))) 
	

Function sequences are more complicated regarding namespaces (as it has to act on global data) unless it is contained within an object (object scoping)

If you method chain, it's obvious which object it is acting on, but the methods can only ever be used on the object, and they have to return the object.

Nested functions allow you to indicate the hierarchy of information very clearly. However, the evaluation order can be quite confusing. I.e. the functions evaluate third(second(first()))

Whereas method chaining and function sequences, allow you to write it in the order that they occur

##### External DSLs
- syntactic analysis strategy
- how do we generate the parser?
- if we use a parser generator, which one to use?
- What to do with the result of parsing the input?
- Topdown or bottom up parsing? CFG or PEG?

If we create an external DSL, will need to decide how to generaate the parser. Do we write it, or do we generate it using a parser generator? As detailed later on, this project will involve the creation of aa semnantic model, on top of whhich I will build an internal DSL. Subsequently, I will create an external DSL on top of the internal DSL.

#### Internal vs External DSLs
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

#### Other DSL topics





### Review of DSLs for data analysis
In this section I will review several existing DSLs for data analysis
#### Pandas Dataframes 
Pandas is the standard way for data analysts to interact with data in Python. It allows you to do 
#### R / Julia - Statistical General Purpose Languages

## Project Overview
### Project Vision 
In this section I will explain exactly what I want to create (i.e. ingestion of data + create symbol table automatically, documentation of a simple and composable DSL that allows data analysis quickly and easily

### Requirements Analysis
In this section I will explain what the minimum requirements are.
1. automated ingestion + creation of a symbol table by the language
2. a usable syntax for core data analysis concepts
3. a way to output the summarised results




### Further implementation possibilities
1. Plotting the data
2. Create a REPL for the DSL



## Architecture plan
In this section I will discuss the semantic model, the DSL syntax, ingesting the data and populating the symbol table, creating the syntax tree, and how I will output the results.

### Creating the DSL

#### Underlying Semantic Model
In this section I will propose the outlines of the underlying semantic model
#### Proposed DSL Syntax and sample queries
In this section I will propose the outlines of the DSL syntax, and show some sample queries.
For example
```
define normalize(column x) as  (sum(x) + mean(x)) / sqrt(x))
input = read.csv(input_file)
for x in input.columns:
	normalize(x)
```

### Data Ingestion and Population of the Symbol table
I will use the Builder design pattern to ingest + populate the syntax table. I want to be able to call 

### Building the Abstract Syntax Tree

### Generating Code
I will probably not actually do this step, and will just evaluate the syntax tree in the host language, but I think of this as a stretch goal.

### Creating Output


## Tools and programming languages
In this section I will discuss the following:
1. The host language to choose (dynamic vs typed)
2. How to build the parser (parser generator vs not?)
3. Review of different parser generators
4. Compilers vs interpreters


## Methodology and work plan
In this section I will discuss how I will approach building this DSL.

### Test-driven development and minimum acceptance criteria

Before I start coding, I will create a series of tests for each step of the project. These tests will form the acceptance criteria for each step of the project.

### Project plan
As inspired by Martin Fowler's suggestion in his book "Domain-Specific Languages", I will be doing the following:
1. Designing a minimumally viable semantic model, with the option to extend
2. Designing an internal DSL syntax in the host language
3. Create test cases for the internal DSL
4. Develop the process to create the symbol table (i.e. automatic creation of symbols that represent each datatype)
5. Ensure the internal DSL passes all the test cases
6. Create test cases for external DSL
7. Create the lexer
8. Create the parser of the language
9. Write the evaluator of the language
10. Evaluate usability

Fowler points out that the diffiicult part of creating the DSL is actually creating the semantic model, and internal DSLs are much easier to extend in terms of functionality, as you can use the functions of the host language, and you can rely on things like type checking from your IDE and so on.

Once I have created this minimum viable DSL, I will then decide whether to extend the project with additional functionality, or recreate this functionality in an external DSL.


#### Designing a minimumally viable semantic model

My plan here is relatively simple. I will follow the standard path of data analysis, with terms particular to each step. I will do the following:




### Deadlines (((add this to the bit above - the project plan, when I put it into a word document)))
In terms of timings, I plan to do the following:

18th April : Hand in proposal and begin work on semantic model
1st May: Finalise design decisions for DSL (language choice, function design, internal vs external, closures, dynamic functions, etc) and submit for review from supervisor
9th May: Complete first draft of semantic model
16th May: Complete first draft of internal DSL syntax
30th May: Complete first draft of process to ingest data and populate symbol table. Start working on tests for the internal DSL
6th June: Submit draft of design of model, internal syntax + process to ingest data to supervisor. Complete test suite for internal DSL

beginning of June: Exams - progress will be limited over this time period

7th July: submit first draft of internal DSL
7th July: Make initial decision whether to extend the existing functionality of the internal DSL or to move to an external DSL
31st July: Submit code for review to supervisor (with either extended functionality, or the move to external DSL). Begin working on other option (i.e if we selected extend with further functionality before, make the shift to an external parser, or the other way round)
30th August: Submit code for further review to supervisor with either extended functionality 

14th September: Hand in final project


