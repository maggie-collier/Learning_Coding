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

```
do

  some statements or action

  some statements or action

  some statements or action

  update the flag

while expression is true
```

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

**Dictionary** a set of keys, where each one has a single associated value
- aka hash, map, hashmap
- uses `{}` syntax
- dictionaries can contain other variables, arrays or other dictionaries
- typically the key is a "string", looks like `{"string" => value}` in Java

**Unsigned vs Signed** 

**Unsigned** variables can only hold positive numbers, while **Signed** variables can hold negative and positive numbers
- can be applied to numeric data types like int, char

**Snake Case** uses_underscores_instead_of_spaces_to_separate_words

**Camel Case** capitalize each word except the first with no spacing
- aka medial capitals, PascalCase, mixedCase
- can make it more difficult to parse variable names

**Global** variables that remain in memory and can be accessed throughout the whole program
- they can be changed by any function and can affect the program as a whole
- good practice to minimize use of global variables
- the **scope** of a variable refers to where in the program a variable or constant can be accessed

**Local** a variable that is only accessible within a specific part of a program
- usually defined within a function or routine, can only be used within the scope of that function
- parameters of a function
- local variables within different functions can have the same name, because they only exist within that function

**Instance/Member** a non-static variable which is defined in a class but outside of constructors, methods, or blocks
- created inside object
- value of instance variable can vary from object to object, a separate copy of the instance variable is created for each object
- can have access modifiers (class variables have these)
- in OOP, called member variable, associated with a specific object and all of its methods (member functions)

**Public Visibility** a modifier that allows a method/variable of an object to be accessed by code outside of the object
- accessible to all elements that can access the contents of the object/class
- default visibility is public

**Private Visibility** variable not visible outside of a small section of code, hidden from other classes
- only accessible within the class where it is declared

### Objects:
- abstract data type that contains value
- can be a variable, data structure, function, method, instance of a class
- has "polymorphism" and "inheritance" (feature of classes)
- concept is integrated *data* (which has state) and *code* (which has behavior)
- Object-oriented programming combines code and data, so rather than having separate functions act on doors, we design doors that have **methods** that can act on themselves. Methods represent something the object can do (behavior/procedure), and are typically defined using verbs:

```
   door.Open()
   door.Close()
   door.Lock()
   door.Unlock()
   ```


- Objects may also have **attributes** , something the object is or has, and are typically defined using nouns or adjectives:

```
   door.Height
   door.Width
   door.Color
   door.Closed
   door.Locked
   ```


### Classes:
- in OOP, a blueprint for creating objects, providing initial values for state (member variables or attributes), and implementations of behavior (member functions or methods)
- classes define the nature of future objects, and are used to create and manage new objects and support **inheritance**
- an **instance** is a specific object created from a particular class
- Example: make a new class called class *car*, which can be a template for many different kinds of cars, *objects* 
    - the *car* class will structure the *objects* to contain information about the car’s model, the color, how many passengers it can hold, its speed, etc. *Car* class can also define types of operations, or methods, that can be performed on the *objects*, like acceleration **method** and speed **attribute**

**Static Classes**
- class that cannot be instantiated, can't have instance members
- always derive from object


**Inheritance** 
- a mechanism of reusing code, and reducing the complexity of a program, key to OOP
- the idea that different classes can have similar components, so inheritance links parent classes to descendant classes
- how the attributes and methods of parent classes are inherited by the child class
- Example: To allow for classes to share some key information before getting very specific into a descendant object, inheritance allows the classes to share information relevant to multiple parts of the code.
    - in a fantasy story, there are heroes and monsters but both the heroes and the monsters are *characters* (parent class). And both dragons and orcs are *monsters* (descendant class). Though dragons and orcs are different monsters, they share some qualities that a reader might want to know: they both have a color, they both have a size, they both have enemies. Orcs might have characteristics that dragons do not; for example, what kind of weapon does the orc carry?
    - dragon is a *subclass* of monster, but character is a *superclass* of monster
- any change or update to the character class would also be an acceptable update to any other subclass
- *dragon* inherits *monster*'s "movement" method, but it is overridden because *dragon* defines its own "movement" method. this adds unique functionality to the dragon subclass


**Interfaces**
- a programming structure/syntax that allows the computer to enforce certain properties on an object (class)
- description of the actions an object can do
- allows the computer to enforce specific properties/methods and know that a specific object must have specific functions according to the interface
- Example: If there is a *car class* and a *scooter class* and a *truck class*. Each of these three classes should have a `start_engine()` action. How the "engine is started" for each vehicle is left to each particular class, but the fact that they must have a start_engine action is the *domain* of the interface.
- Syntax: Inside the {} of the interface is a list of functions that must be found in any object that purports to "follow" the interface, looks very much like a class definition
- Differences between interfaces and class
    - No VARIABLES are allowed to be declared by the interface. An interface is about actions that are allowed, not about data or implementation of those actions.
    - The keyword public is not placed in front of the function prototypes. By definition, all functions listed in an interface must be public functions.
    - There is no code after the function prototype. The normal {} are replaced with a single semi-colon.

### Functions:
**Signatures** define in put and output of functions/methods
- aka function signature, type signature, method signature
- Example: parameters and their types, return value and type

**Return Types** function returns a value after completing its task. return type tells is what type of value it is returning
- four types: `handle`, `integer`, `object` or `string`

**Naming conventions** using camel case and descriptive names
- call java files what their class name is

**Recursion** when a function calls itself directly or indirectly

### Regular Expressions:
- `/d` can be used in place of any digit from 0 to 9
- `.` (dot) metacharacter can match any single character (letter, digit, whitespace, everything)
  - this actually overrides the matching of the period character, so in order to specifically match a period, you need to escape the dot by using `\.` 
- the pattern [abc] will only match a single a, b, or c letter and nothing else
- in a string "jarod doesn't say hi sometimes", `jarod.*hi` would match "jarod doesn't say hi", and return True
  - `jarod(.*)hi` would *capture* "doesn't say", so the match would still be "jarod doesn't say hi", but there would also be a group, " doesn't say "