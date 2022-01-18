# LinkedIn -- common code prompts

Common code challenges that LinkedIn uses for SRE interviewing (as according to user reports on glassdoor).

## My suggestions

My suggestions for study and practice based on the posts from glassdoor users.

### "Fizzbuzz"

Study <./code/fizzbuzz_linkedin.py>

### "REST API call and response parsing"

Study `import requests` and `import json`...

Study <https://betterprogramming.pub/how-to-recursively-parse-api-responses-using-python-126824426b18>

Study <https://stackoverflow.com/questions/43491287/elegant-way-to-check-if-a-nested-key-exists-in-a-dict>

Study <https://stackoverflow.com/questions/9807634/find-all-occurrences-of-a-key-in-nested-dictionaries-and-lists>

### "Parsing log files"

Study `import os` and `import strftime`...

Study <https://stackoverflow.com/questions/5419888/reading-from-a-frequently-updated-file>

## Posts from glassdoor users

1) Fizzball (but with Linkedln). Given an integer 1 to n,
print "Linked" if divisible by 4 and "In" if divisible by 6
and "LinkedIn" if divisible by 4 and 6. Print the integer
if it doesn't meet any of the above criteria.
2) Recursive API question. It's easy but tricky given the
exam conditions. You are given an employee API URL
to GET the names of an employee reporting structure.
The JSON response returns the employee some othet
key-value pair and the reports under the employee.
The key here is to recognize the need to use recursion.
At the very least mention it so they are aware you
know what to do even if you don't get it completely
correct.
3) You are given some logs with timestamp, process
ids, log statement. You need to parse the the log file
and print out in two columns the time stamp and the
number of times the same process (or thereabout)
shows up in the same time stamp (in other words
column A has the time stamp, column B has the count).
I think this needed to be outputted in CSV or
something, but interviewer mentioned it didn't really
matter.

--

Code review round -- I had to find bugs in a few code samples. One code sample was for storing backup. The 2nd was for parsing logs.

--

You will have to perform a code review of several
pieces of code. Focus on logic errors, not stylistic
issues. I don't remember all the code samples, but one
was about doing file backups, where they manually
implemented extension parsing and copied over "1"
files to "2", etc. without ensuring the order of the
copy...

--

Coding test: Parse a (syslog) file to get various fields
from the logs and message counts. Associate counts
with the processes that logged them...

--

1. Write a sort of FizzBuzz
2. Use rest api to get a JSON and traverse it
3. Parse a log file and process the data
4. Parse the same file in a more advanced way (regex,
grouping, etc.)
5. The same file but parse it continuously (the file can be
rolled-over, etc.)
Side questions: advantages and disadvantages of a recursion function,
rewrite a recursion function in a non-recursive way, etc. (depends on
what do you write)
