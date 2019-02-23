# Homework 2
* ``` Due Mar 3 by 11:59pm ```
* <b>10</b> points
* ```zip, tar,tgz```

## Purpose
The main purpose of this homework is to bring together some things you've learned in class (classes, web scraping, and others) into a working program that does something useful.

## Purpose
* 1. Go to <a href="http://directory.oregonstate.edu/">http://directory.oregonstate.edu/ </a> (Links to an external site.)Links to an external site. and play around with finding people.  Use your web browser to see what the underlying HTML code looks like when you get a query result. 

* 2. Write some code that, given a name, finds that person in the directory, and returns their directory name, title, department, and phone number.

* 3. Wrap your code up in a program, called directory.py, that can be called like this:
```
directory.py Edward Feser
```
and returns
```
Name: Feser, Edward
Title: Executive 1-Provost/Exec VP
Department: Provost / Exec Vice Pres
Phone: 1-541-737-0731
```

* 4. Extra Credit: Make the system work when there are multiple hits, and print out the information for each of them.

* 5. Extra Credit: Write another program, called mime_count.py, that prints out all the job titles in MIME, and the number of people that hold each position:
```
Assistant Professor: 23
Associate Professor: 3
[and so on]
```

## Thoughts
* 1. When developing your scraper, pick a person with a single directory entry to start with.  Figure out the code for extracting and storing their information.

* 2. Storing information about people might be a great use of a class.  You might also want to wrap up your directory-scraping code in a class, just to encapsulate it.

* 3. You should have a simple interface for scraping, with a function call like search('My Name'), or something like that.

* 4. Do a few searches, and see what URLs the system generates.  You're going to want to replicate these in your code.

* 5. Think about how you're going to split up your code into different files, functions, classes, etc.  Again, we're not going to specify this for you, so you should give it some thought before you start writing code.

## Grading
- [X] 1. Command-line arguments work. [1 point]
- [X] 2. Connects to directory site, and makes a valid query.  [1 point]
- [X] 3. Extracts some information from the returned query. [1 point]
- [ ] 4. Extracts four attributes and stores them (0.5 points each for extraction). [2 points]
- [ ] 5. Encapsulates data about a person in a reasonable way.  [1 point]
- [ ] 6. Code is structured appropriately (functions, classes, etc), with suitable comments.  [1 point]
- [ ] 7. Prints out information as shown. [1 point]
- [ ] 8. Deals with errors reasonably, in the case of no hits (1 point) and many hits (1 point) [2 points]
- [ ] 9. Extra Credit: Prints out multiple names in the event of multiple hits (1 point) and deals with the case when there are too many matches, such as when searching for "Smith"(1 point).  [2 points]
- [ ] 10. Extra Credit: Correct MIME position titles (1 point) and counts (1 point). [2 points]

## What to Turn In
A single file with all of your code in it.

## Useful Link
<a href="http://directory.oregonstate.edu/">Online Directory, Oregon State University </a>
