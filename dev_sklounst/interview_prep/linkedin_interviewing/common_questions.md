# LinkedIn -- Common Questions (SRE)

Common questions asked in SRE interviews (according to certain sources such as glassdoor).

## Networking

First round was based on Networking. TCP/IP, ARP, DNS
resolution, Sharding, Scaling, caching, server management
concepts were covered.

--

You have Gigabytes of data that needs to periodically
be synced from a producer to a large number of
consumers. How do you approach it? Hint: the data set C
isn't necessarily entirely new each time it needs to be
synced, so only sync the data that has changed...

--

Describe how SSH works...

--

Describe how curl works. What happens when you call
the command? Describe the process of loading
libraries, parsing arguments, DNS resolution, etc...

## Linux / OS

Second round was scheduled only for Linux Memory
management. Entire Memory management questions
were asked. How it works, why is it required, Virtual
memory, swap memory, swappiness and all...

--

Questions on DNS, Linux nodes, Message Queues,
Processes, Fork and VFork, Kernel, Linux Boot
Process, etc.

--

How do you change the priority of a running process?

--

How do make a variable in a shell script available after
the script exits (assume the shell script was sourced)?

## Troubleshooting

Systems are bouncing after a new version is deployed and
rollback fails --what do you do, do you/how do you escalate,
what do you include in your post-mortem/future mitigation
steps?

--

There was an Apache server and we had to debug it. It
had 500 and 400 errors.

You will be asked to do live troubleshooting of an
Apache (httpd) web service. You will not be given many
details by the recruiter, so it's easy to study the wrong
thing here. It ended up that you need to be familiar
with the httpd config file and Aliases. You need to be
familiar with how to change Linux filesystem
permissions, but you can ignore that you are running
on RedHat and you won't need to touch SELinux
permissions. Be careful of one problem where they will
have two nearly-identical file names, except one has a
hyphen and the other a Unicode dash character. They
look very similar in many fonts. Make sure you know
how to do a simple GDB backtrace. You will be asked
to debug a segfault and work around it (via simple file
rename/...

**Working with different encoding:**

Some ways to reveal special or hidden characters:

- `cat -v <file>` will work for the contents of a file.

``` text
-v      Display non-printing characters so they are visible.  Control characters print as ‘^X’ for control-X; the delete
             character (octal 0177) prints as ‘^?’.  Non-ASCII characters (with the high bit set) are printed as ‘M-’ (for meta)
             followed by the character for the low 7 bits.
```

The `cat` command has other flags if you want to specialize.

- `-T`  displays `TAB` characters as `^I`.
- `-E` displays a `$` at the end of each line.
- `-A` will show all the invisible characters.

Extrapolating; if a file is named with a "bad" character, this could be one way to troubleshoot.

- To get information about a file, use `stat` command.
- Pipe the output of the `stat` command to a new file.
- Use `cat -v` on the new file, which could hopefully reveal any unusual characters

Another option is to explore your file directories using vim. (You can open a file with vim, and then type in `:edit .` to enter the file context explorer.) While you are using vim to explore files, you can again enter command mode with `:` and set `listchars` and `list` to control how things are displayed.

**About GDB:**

GDB is *GNU Debugger* and is used for debugging backtraces (aka stack traces).

A backtrace or stack trace is a summary of how your program got where it is. Basically, it is a report of the active stack frames at a certain point in time during the execution of a program.

Learn more from these references:

- <https://ftp.gnu.org/old-gnu/Manuals/gdb/html_node/gdb_42.html>
- <https://www.thegeekstuff.com/2014/01/gdb-backtrace/>
- <https://sourceware.org/gdb/current/onlinedocs/gdb/Backtrace.html>

## System Design

Scale a ride-hailing application so that it handles
~10,000 requests/minute. This was a 1.5-hour-long
discussion with follow-ups, including Consistent
Hashing. They also challenged multiple of my design
claims which I had to think about on the spot....

--

You will be shown several architecture diagrams and
asked various questions, like "what happens when
database X goes down?", or "How to speed up requests
from service Y?". Caching plays a big role in almost all
responses...

## Monitoring / Alerting

You take over a new service and discover it has no
monitoring. What monitoring would you put in place
within the first week to ensure the service is working?
Within the first month? How do you monitor failures
which are local to a region?...

--

You will be asked to role play a scenario where the
number of registrations for a service has dropped to 0
for the past 6 or so hours, setting off an alert. You will
have to go through an incident response and elevation.
You will be asked to write simple reports that are
suitable for giving high-level status to a manager....

## Other

The process started with an online coding challenge. It had
three coding questions around LeetCode medium level, one
DBMS query, and around 20 MCQs involving Networks,
DBMS, Linux, etc. Following that, there were two technical
interviews and one host manager round. The first technical
interview was a Service Architecture round where I was
asked to scale a ride-hailing application to handle about
10000 requests/min. It was a 1.5 hour round. In the second
interview, I was tested a lot on Data Structures, Networking,
Linux administration, troubleshooting. Certain questions
were very tough, like in what port do you attach your hard
drive, but I guess they asked that to check our limits, and they
weren't deciding questions. The last round was a Hiring
Manager round close to a typical HR round, but I had certain
technical questions about my projects.

--

For the on-site, there were several rounds:

- code review
- live troubleshooting
- discussion with host manager
- system design/diagramming
The code review consisted of several Python scripts with
logic errors strewn about. I felt I did "ok" here, but likely
missed some opportunities for improving the invalid logic.
The live troubleshooting module is similar to what others
described. There are four challenges and each is basically
getting to the root cause of errors or issues with the Apache
webserver on a host. I spent about 5 minutes for each of the
first three challenges but ran out of time for the final one; it
seemed to require doing some debugging with the
webserver's worker threads. Afterward, the interviewer for
this step was open to questions for the last 5 minutes, before
leaving me to meet with the next and final interview.
The last two modules, discussion with the host manager and
system design questions, were done by the same interviewer.
We had a pleasant introduction and then went on to talk
about my experience, my goals, and how I'd react to certain
scenarios. This is essentially a behavioral interview--no
technical questions whatsoever. Finally, there was the system
design module.

I stumbled a bit here, having not done any diagramming in a
while and not much time designing _actual_ production
systems myself in past roles; I could only rely on my base
understanding of systems and a week of studying system
design. The system design was definitely the most difficult
module, considering that it's up to the applicant to lead the
discussion--no hints or pushes in the right direction.
By the end of it, I'd say I fared well on at least 2 out of the 4
modules--live troubleshooting and the behavioral module.
One of the recruiters and an interviewer mentioned that
even (hypothetically) failing one round doesn't mean the end,
nor does passing all rounds result in an offer.

--

The interview questions were more like a shotgun blast
across a wide range of topics rather than focusing on
anything in particular. It went from as low level as how/when
shared libraries are loaded when starting an application to as
high-level as designing video streaming service.
