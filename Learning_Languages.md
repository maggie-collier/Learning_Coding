# Notes On Learning Languages
## Types of Languages
### Procedural Programming Language: 
A procedural language follows a sequence of statements or commands in order to achieve a desired output. Each series of steps is called a procedure, and a program written in one of these languages will have one or more procedures within it. 
- Java
### Object-oriented Programming Languages (OOP):
This type of language treats a program as a group of objects composed of data and program elements, known as attributes and methods. Objects can be reused within a program or in other programs. This makes it a popular language type for complex programs, as code is easier to reuse and scale.
- Java
- Python
### Scripting Languages:
Programmers use scripting languages to automate repetitive tasks, manage dynamic web content, or support processes in larger applications.
- Python
- bash
### Back-end Languages:
Back-end languages deal with storage and manipulation of the server side of software. This includes data architecture, scripting, and communication between applications and underlying databases.
- Java
- Python
- C#
### High-level vs. Low-level Languages:
**High-level languages** are less memory efficient but  more human friendly. Easier to write, understand, maintain, and debug. Most popular programming languages in use today are considered high-level languages. 

**Low-level languages** are machine-friendly, which makes them highly efficient in terms of memory usage but difficult to understand without the help of an assembler. Machine code is an example.

### Interpreted vs. Compiled Languages:
Differ in how they convert high-level code to be readable by a computer. 

With **interpreted languages**, code goes through a program called an interpreter, which reads and executes the code line by line.
- Python

**Compiled languages** go through a build step where the entire program is converted into machine code. This makes it faster to execute, but it also means that you have to compile or "build" the program again anytime you need to make a change.
- C#

## Software Methodologies
### Waterfall
- old school, traditional methodology
- sequential, plan-driven approach
- lots of up-front planning/discussion between customers and developers to determine project requirements
- operates in stages...requirements, design, implement, test, deploy, maintain
- inflexible, if need to go back and change something, may need to restart entire method
### Agile
- response to problems with waterfall, accommodates change
- customer collaboration throughout, team oriented
- responds to change instead of strict plan
- sprints with defined deliverables
- scrum and extreme programming (XP) are agile frameworks

### Buzzwords:
- **Full-stack developer** has front- and back-end knowledge and can develop for any part of the process
- **Object-oriented programming** utilizes data/objects instead of functions/logic, increasing readability and reusability of code
- **Agile**
- **Waterfall**
- **Scrum**
- **Lean** basic principles—optimize the whole, eliminate waste, build quality in, create knowledge, defer commitment, deliver fast, and respect people
- **Product backlog** is a prioritized list of work for the development team that is derived from the roadmap and its requirements
- **Stories** informal, short descriptions of a small piece of desired functionality, or smallest unit of work 

## Concepts
### Loops:
**For Loop** execute code for a known number of times
- do this x times
**While Loop** execute code until a certain condition is no longer true
- do this as long as x = y
**For Each Loop** used to "traverse" items in a collection (ie array)
- do this to everything in this set
**Do While Loop** used to execute code at least 1 time, then either do it again or not, based on a boolean condition
- used for iteration, possibly wanting to repeat an action if warranted
- "question" or "test expression" or boolean is used to control execution of loop

`do` 

>`some statements or action`

>`some statements or action`

>`some statements or action`

>`update the flag`
  
`while expression is true`

### Variables:
**Integer** takes only integers, primitive
**Double/Float** can take integers and fractional/decimal values, up to 15 places, primitive
- double is for C# and other languages
- float is for python
**String** takes characters, like letters, numbers, and symbols
**Character** takes a singular character (letter, number, space, or symbol)
- in java and C# 'char' is its own keyword for this
**Boolean** has only true or false values, used in tandem with other control statements
**Array** group of variables of the same data type, stored under the same name, but with different index values, or positions, in a fixed length data structure
- in Java, *cannot* change the length once created, but can store primitives (int, float, double) and 'objects'
- can use for loop or for each loop to iterate through array
- has length variable which returns length of array
- can be multi-dimensional
- static
**ArrayList** single dimensional, slower, variable length data structure, that allows objects to be easily added or removed with dynamic resizing
- in Java, *can change* the length, but can only store 'objects'
- as elements are added, its capacity automatically grows
- can use iterator or for each loop to iterate through arraylist
- length provided by `size()` method
- insert elements into arraylist object using `add()` method
**Static** variable allocated for the entire run of the program, declared within a given class, but outside the objects in the class, type of variable
**Dynamic** computes its own value by executing statements, then assigns itself the result of the operation, address is determined by running the program