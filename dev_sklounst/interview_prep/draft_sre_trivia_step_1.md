# SRE Trivia - Step 1

```
This is a work in progress.
```

-------------------

ToC:

1. Linux / OS
2. Computer Networking
3. Monitoring & Alerting
4. System Design
5. Behavioral or PM
6. Other

## Linux / OS

### What is umask in Linux?

umask dictates what is a user’s default permissions when creating files.  Use the umask command to set the default
mode for newly created files. It takes as argument a 3-digit code to represent the access to be inhibited (masked
out). If you want all new files to automatically have the permission mode 751, then set umask to 026 (because 777 -
751 = 026).

You can put a umask command in the system init file to set a default for all users. You can also set your own umask
in your shell setup files to override defaults.

### What is setuid?

set user id.
Some executable files can have an s instead of an x in the permission listing, which would indicate that the setuid is
set. This flag makes it so that the file is run as the owner, instead of you. A program might use this setuid bit to run as a super user system account, in order to always have special privileges. The setuid bit is aka mode 4000.
adding:
chmod u+s /home/dgibney/myscript.sh
or
chmod 4755 /home/dgibney/myscript.sh
removing:
chmod u-s /home/dgibney/myscript.sh

### What is setgid?

set group id.
AKA mode 2000. This sets the group ID. When a file is created, it normally belongs to the primary group of the user that created it; however, if the setgid bit is set on the directory in which a file is to be created, then new files created
will have their group ownership set to the same group as the directory’s owner. This allows a level of access to group members while allowing different access to non-group members.

chmod 2755 /home/share​   --  sets the SGID flag

chmod g-s /home/share​    -- removes the SGID flag

### What is Sticky Bit?

AKA mode 1000. Set the sticky bit to prevent users from deleting others’ files, even if they might have full access to the directory. The owner of a directory should set its sticky bit; this way, only the owner and superuser can
rename/remove files in that directory.
chmod o+t /home/share

### What is noatime in Linux?

If a filesystem is mounted with ‘noatime’, such as can be configured in ​/etc/fstab​ , then Linux will not record access
time or when files in that system were created/modified. Because of this, filesystemlatten performance can be improved. Use this for filesystems where files are frequently accessed and changed.
You can also set ‘noatime’ for a specific directory tree:
chattr -R +A /var/spool  

### What is the sync command in Linux?

Synchronize data on disk with memory; write out any data buffered in memory out to the disk. This is good to do before you do something that might cause the system to crash. When you issue a shutdown or reboot, part of the
subcommands that the OS will run include the sync command.

### What does the ‘count’ entry in an inode track?

How many times has the file been opened without closed (how many references still active?)
What if you try to truncate a big log file to try to reclaim disk space, but the space doesn’t reappear?  A way to debug is
to see what process might have the data part still open -- if so, then the OS won’t release the space until the process closes it.  So look at the count entry in an inode and look at lsof

### How would you troubleshoot an application that is not writing logs?

If the log files do not exist, or if nothing is being written to them, I would check...:

- Is the application running? What is its running state?
- Does the application's runas user have sufficient filesystem permissions in the directory path where it is configured to write log files?
- Does the relevant disk partition have enough free storage space and enough available free inodes?
- If this is a new problem that recently started, I would check on what are the recent code changes and deployments that might coincide with this emergent problem.
- Are there any related log messages in the kernel log? Are there any memory or RAID errors in dmesg or mce log?
- I could deep dive on the application's run state with ps aux, strace, lsof, netstat, heapdump, and by checking its current local configuration files on the hosts

### How would you debug a broken cron job?

crontab -l
crontab -e
check /var/spool/cron
run the script manually, check the crontab for any custom env settings, run the cron with output saved to a file
(instead of the default of email, which might also be broken)

### What is the difference between a process and a thread?

A thread is a lightweight process. A thread is owned by a
process. Each process has a separate stack, text, data and heap. Threads
 have their own stack, but share text, data and heap with the process.
Threads all belonging to the same process can share some information
between them.

### What is an inode?

An inode is a data structure in Unix that contains metadata about a file. The filename is present in the parent directory’s inode structure.  Some of the items contained in an inode are:

- mode (e.g., permissions, rwx)
- owner (e.g., UID, GID)
- size
- atime, ctime, mtime (access time, change time {permissions, owner}, modified time {file contents only})
- list of blocks of where the data actually is

### What is the difference between a soft link and a hard link?

Hardlink shares the same inode number as the source link.
Softlink has a different inode number. Hardlinks are only valid in the
same filesystem, softlinks can be across filesystems.

A hardlink is useful when the source file is getting moved
around, because renaming the source does not remove the hardlink
connection. If you rename the source of a softlink, the softlink is
broken -- hardlinks share the same inode, whereas softlink uses the
source filename in its data portion.

Can you solve this log parsing w/ awk question?
You have a log file, and you want to parse the log and print out only the lines that have the word "hello" as the third word, and you must also print the line number. Example log lines:

Service started in 20.1 seconds
Server sent hello to client x.x.x.x
Server sent hello to client y.y.y.y
Server got hello from client x.x.x.x
Server did not get hello in time from client y.y.y.y

What is a command that could accomplish this?

awk '$3 == "hello" { print NR, $0 }' logfile.txt

Can you describe the boot process of a linux system?
Once you power a system on, the first thing that happens is the BIOS loads and performs POST (power on self test) to ensure that the components needed for a boot are OK.  (For instance if the CPU or memory is defective, the system will give an error that POST has failed.)

After POST, the BIOS looks at the MBR (master boot record) or the GPT (GUID Partition Table) to find the installed boot loader, and executes the boot loader.

A common boot loader program is GRUB (Grand Unified BootLoader).  GRUB’s job is to give you the choice of loading a Linux kernel or other OS that you may be running.

Once you ask GRUB to load a kernel, usually an initial ramdisk kernel is loaded, which is a small kernel that understands filesystems. This will in turn mount the installed filesystem and will start the Linux kernel from the filesystem.

Traditionally--and somewhat differently from the newer systemd control/init system--the kernel will then start init, which is the very first process (PID 1).  Init will look at  /etc/inittab  and will switch to the default run-level which on Linux servers tends to be 3 (multi-user mode with networking).  (Other runlevels are available to be entered via scripts in  /etc/rc.d/rc[0-6].d/ )

Can you describe how processes are commonly executed in a Linux shell?
Whenever you run, for example,  ls  , the shell searches in its path for an executable named ls.  (It finds it at  /bin/ls )
When the shell finds it, the shell will fork a copy of itself using the fork system call.  If the fork succeeds, then in the child process, the shell will run  `exec /bin/ls`  which will replace the copy of the child shell with itself.  Any parameters that are passed to  ls  are done so by exec.

Can you describe some mechanisms in which there can be process inter-communication, whether strictly within a Linux environment or otherwise?

- POSIX mmap
- Message queues
- Semaphores
- Shared memory
- Anonymous pipes
- Named pipes
- Unix domain sockets
- RPC

-

mmap - map pages of memory

The mmap() (C-lang) function is used for mapping between a process address space and either files or devices. When a file is mapped to a process address space, the file can be accessed like an array in the program.

The mmap() function shall establish a mapping between an address space of a process and a memory object.
The mmap() function shall be supported for the following memory objects:

- Regular files
- [SHM] Shared memory objects
- [TYM] Typed memory objects

mmap is a POSIX-compliant Unix system call that maps files or devices into memory. It is a method of memory-mapped file I/O. It implements demand paging because file contents are not read from disk directly and initially do not use physical RAM at all. The actual reads from disk are performed in a "lazy" manner, after a specific location is accessed. After the memory is no longer needed, it is important to munmap (use munmap) the pointers to it. Protection information can be managed using mprotect, and special treatment can be enforced using madvise.
<https://en.wikipedia.org/wiki/Mmap>

-

Semaphores

Semaphore in Linux plays an important role in a multiprocessing
system. We need to review the semaphore status if we need to kill
unwanted entries to free up the memory allocated to the server.

Semaphores are IPCs, which means Inter-Process Communication Systems
used to allow different processes to communicate with each other. It is a
 variable or abstract data type used to control access to a common
resource by multiple processes in a concurrent system such as a
multiprogramming operating system.

Semaphores are used for communication between the active process of
some applications such as Apache. If you are facing the following error
while restarting the Apache server...:

 Apache error: No space left on device: mod_rewrite: Parent could not create Rewrite Lock.

...then your semaphores' memory location is not free.  And in most cases with this error, the parent process dies without killing its child process properly.

Related commands:

- Check/show semaphores status:
  - ipcs -s
- Kill a semaphore process:
  - ipcrm -s
- List current semaphore configuration:
  - ipcs -l

You can change semaphore and kernel configs in   /etc/sysctl.conf

-

Unix domain sockets

A Unix domain socket or IPC socket (inter-process communication socket) is a data communications endpoint for exchanging data between processes executing on the same host operating system. Valid socket types in the UNIX domain are:

    SOCK_STREAM (compare to TCP) – for a stream-oriented socket
    SOCK_DGRAM (compare to UDP) – for a datagram-oriented socket that preserves message boundaries (as on most UNIX implementations, UNIX domain datagram sockets are always reliable and don't reorder datagrams)
    SOCK_SEQPACKET (compare to SCTP) – for a sequenced-packet socket that is connection-oriented, preserves message boundaries, and delivers messages in the order that they were sent

The Unix domain socket facility is a standard component of POSIX operating systems.

The API for Unix domain sockets is similar to that of an Internet socket, but rather than using an underlying network protocol, all communication occurs entirely within the operating system kernel. Unix domain sockets may use the file system as their address name space. Processes reference Unix domain sockets as file system inodes, so two processes can communicate by opening the same socket.

In addition to sending data, processes may send file descriptors across a Unix domain socket connection using the sendmsg() and recvmsg() system calls. This allows the sending processes to grant the receiving process access to a file descriptor for which the receiving process otherwise does not have access. This can be used to implement a rudimentary form of capability-based security. For example, this allows the Clam AntiVirus scanner to run as an unprivileged daemon on Linux and BSD, yet still read any file sent to the daemon's Unix domain socket.

-

RPC

In distributed computing, a remote procedure call (RPC) is when a computer program causes a procedure (subroutine) to execute in a different address space (commonly on another computer on a shared network), which is coded as if it were a normal (local) procedure call, without the programmer explicitly coding the details for the remote interaction. That is, the programmer writes essentially the same code whether the subroutine is local to the executing program, or remote. This is a form of client–server interaction (caller is client, executor is server), typically implemented via a request–response message-passing system. In the object-oriented programming paradigm, RPCs are represented by remote method invocation (RMI). The RPC model implies a level of location transparency, namely that calling procedures are largely the same whether they are local or remote, but usually they are not identical, so local calls can be distinguished from remote calls. Remote calls are usually orders of magnitude slower and less reliable than local calls, so distinguishing them is important.

RPCs are a form of inter-process communication (IPC), in that different processes have different address spaces: if on the same host machine, they have distinct virtual address spaces, even though the physical address space is the same; while if they are on different hosts, the physical address space is different. Many different (often incompatible) technologies have been used to implement the concept.

Computer Networking
-----------------------------

What is the OSI networking model?

1. Physical
2. Data link
3. Network
4. Transport
5. Session
6. Presentation
7. Application

What is TCP?
<https://datatracker.ietf.org/doc/html/rfc793>
TRANSMISSION CONTROL PROTOCOL  -  DARPA INTERNET PROGRAM PROTOCOL SPECIFICATION

The Transmission Control Protocol (TCP) is intended for use as a highly
reliable host-to-host protocol between hosts in packet-switched computer
communication networks, and in interconnected systems of such networks.

  TCP is a connection-oriented, end-to-end reliable protocol designed to
  fit into a layered hierarchy of protocols which support multi-network
  applications.  The TCP provides for reliable inter-process
  communication between pairs of processes in host computers attached to
  distinct but interconnected computer communication networks.  Very few
  assumptions are made as to the reliability of the communication
  protocols below the TCP layer.  TCP assumes it can obtain a simple,
  potentially unreliable datagram service from the lower level
  protocols.  In principle, the TCP should be able to operate above a
  wide spectrum of communication systems ranging from hard-wired
  connections to packet-switched or circuit-switched networks.

  The TCP fits into a layered protocol architecture just above a basic
  Internet Protocol which provides a way for the TCP to send and
  receive variable-length segments of information enclosed in internet
  datagram "envelopes".  The internet datagram provides a means for
  addressing source and destination TCPs in different networks.  The
  internet protocol also deals with any fragmentation or reassembly of
  the TCP segments required to achieve transport and delivery through
  multiple networks and interconnecting gateways.  The internet protocol
  also carries information on the precedence, security classification
  and compartmentation of the TCP segments, so this information can be
  communicated end-to-end across multiple networks.

         Protocol Layering:

                  +---------------------+
                  |     higher-level    |
                  +---------------------+
                  |        TCP          |
                  +---------------------+
                  |  internet protocol  |
                  +---------------------+
                  |communication network|
                  +---------------------+

  The TCP interfaces on one side to user or application processes and on
  the other side to a lower level protocol such as Internet Protocol.

  The interface between an application process and the TCP is
  illustrated in reasonable detail.  This interface consists of a set of
  calls much like the calls an operating system provides to an
  application process for manipulating files.  For example, there are
  calls to open and close connections and to send and receive data on
  established connections.  It is also expected that the TCP can
  asynchronously communicate with application programs.

  To provide this service on top of a less reliable internet
  communication system requires facilities in the following areas:

    Basic Data Transfer
    Reliability
    Flow Control
    Multiplexing
    Connections
    Precedence and Security

...
  Multiplexing:

    To allow for many processes within a single Host to use TCP
    communication facilities simultaneously, the TCP provides a set of
    addresses or ports within each host.  Concatenated with the network
    and host addresses from the internet communication layer, this forms
    a socket.  A pair of sockets uniquely identifies each connection.
    That is, a socket may be simultaneously used in multiple
    connections.

    The binding of ports to processes is handled independently by each
    Host.  However, it proves useful to attach frequently used processes
    (e.g., a "logger" or timesharing service) to fixed sockets which are
    made known to the public.  These services can then be accessed
    through the known addresses.  Establishing and learning the port
    addresses of other processes may involve more dynamic mechanisms.
...

  Processes transmit data by calling on the TCP and passing buffers of
  data as arguments.  The TCP packages the data from these buffers into
  segments and calls on the internet module to transmit each segment to
  the destination TCP.  The receiving TCP places the data from a segment
  into the receiving user's buffer and notifies the receiving user.  The
  TCPs include control information in the segments which they use to
  ensure reliable ordered data transmission.

TCP segments are packaged inside internet datagrams.  To transmit the datagram through the local network, it is embedded in a local network packet.  The packet switches may perform further packaging, fragmentation, or other operations to achieve the delivery of the local packet to the destination internet module.

  At a gateway between networks, the internet datagram is "unwrapped"
  from its local packet and examined to determine through which network
  the internet datagram should travel next.  The internet datagram is
  then "wrapped" in a local packet suitable to the next network and
  routed to the next gateway, or to the final destination.

  A gateway is permitted to break up an internet datagram into smaller
  internet datagram fragments if this is necessary for transmission
  through the next network.

  Transmission is made reliable via the use of sequence numbers and
  acknowledgments.

  When the TCP transmits a
  segment containing data, it puts a copy on a retransmission queue and
  starts a timer; when the acknowledgment for that data is received, the
  segment is deleted from the queue.  If the acknowledgment is not
  received before the timer runs out, the segment is retransmitted.

  An acknowledgment by TCP does not guarantee that the data has been
  delivered to the end user, but only that the receiving TCP has taken
  the responsibility to do so.

  To govern the flow of data between TCPs, a flow control mechanism is
  employed.  The receiving TCP reports a "window" to the sending TCP.
  This window specifies the number of octets, starting with the
  acknowledgment number, that the receiving TCP is currently prepared to
  receive.

What are some load balancing algorithms/techniques?

- Round robin
- Least-connection
- Weighted round robin
- Weighted least connection
- Bandwidth and load based
- Random
- Least traffic
- Least latency
- Geographic

What is the arp command?
Address Resolution Protocol. Display/modify the ARP cache. An ARP cache is a mapping of IP addresses to
MAC addresses.

Where do DNS client settings for a linux host reside?

- /etc/hosts
- /etc/resolv.conf
- nsswitch.conf
- /etc/named.conf (old, redhat 5)
- Also check if the host uses any DNS caching program, or if the applications use any DNS caching libraries

What are some different kinds of ICMP packets?
(ICMP - internet control messaging protocol {ping, traceroute})

- ECHO
- REDIRECT
- DEST_UNREACH
- TIME_EXCEEDED

Those are good to know. REDIRECT is a good one to block in firewall configurations. Other ICMP packets
include router advertisements/solicitations, address mask request/reply, ...

Name some tools useful for troubleshooting when another host goes down?
Ping, traceroute, arp, nslookup, dig, ifconfig, ethtool, host, route, netstat, mtr, tcpdump, wireshark,  

What packets involved in establishing a TCP session, with “the handshake”?
SYN, SYN+ACK, ACK
There will also be TCP sequence numbers.

What packets involved with closing a TCP session?
FIN, FIN+ACK, ACK
There will also be TCP sequence numbers.

What about for UDP?
Trick question -- there are no stages for this, because it is unreliable.

How does traceroute work?
Traceroute can reveal what path a request could take from source to destination. "Path" describes routes or hops, such as routers or gateways, and the time taken between each hop. Even if the destination is ultimately unreachable, traceroute can show what is the last hop before the packets can not go any further.

Traceroute works with UDP or TCP, ICMP echo requests, and network packet TTL settings.

Regarding how it works, one must first explain what happens when routers transmit packets. Packets are sent with headers that contain information such as SRC and DST for IP and port. Whenever a router forwards a packet to the next hop, it decrements the TTL value of the packet (this prevents infinite routing loops).  Whenever a packet has its TTL field decremented to 0 and is thus dropped for good, the router that does that action also communicates back to where it received the packet from, and says “I dropped this packet” -- and of course that reply back has header information in it that describes the router.  

Traceroute leverages this logic in a clever way. Traceroute first sends a packet with TTL 1; then it sends a packet with TTL 2; then
TTL 3; and etcetera. This is how traceroute crawls through router after router to get the info of each router.
Certain networks and routers may be configured to not respond to ICMP. But when and where it works,
traceroute tells you the path to get to the final host or IP in question, the names and identities of routers and
devices along the path, and network latency between each hop.  

You need to distribute GiB or even TiB data from a single server to a couple thousand nodes, and also keep data up to
date. It takes time to copy the data to one server. How would you reduce  the time needed to update all the servers? Also, how would you make sure that the files were not corrupted during the copy?
One option is to build your own peer-to-peer (P2P) service (e.g., "Torrent").

Another option is to use the cloud.

S3 could be a good intermediary.  Copy the data to S3 with Multi-part Upload.  Hosts could "listen" (SNS, S3 events) or poll for work (SQS, S3 events) to know when to download.

An implementation approach could be to split up the list of files to be copied, and spawn separate threads or processes for each list of files to run an S3 API copy command.  S3 has managed transfer algorithms to ensure perfect file uploads (but you should add a custom header to each object that describes the md5 checksum of the object - because checksums are necessary to later verify download).  S3, being a managed service, also scales automatically for requests to the same data, so your thousand servers can download the data without slowing down each other's connections.

To potentially improve efficiency, you could edit your AWS SDK library or AWS CLI configuration to increase, for example, the S3 concurrency limit to be perhaps 20 or more (the default is less than this - but whatever you do, experiment and settle on optimal settings for your scenario).

What is an HTTP Header
HTTP Headers allow client and server to share additional
information within the request or response.  Fields within an HTTP
Header include the following:

- Accept
  - Acceptable media types
- Accept-Charset
  - Acceptable character sets
- Content-Length
  - length of the request body
- Cookie
- Content-MD5
- From
- Host
- User-Agent
- X-Forwarded-For

What's the difference between ELB and ALB, and what OSI layers are those?
Per the well-known OSI model, load balancers generally run at Layer 4 (transport) or Layer 7 (application).

A Layer 4 load balancer works at the network protocol level and does not look inside of the actual network packets, remaining
unaware of the specifics of HTTP and HTTPS. In other words, it balances the load without necessarily knowing a whole lot about it.

A Layer 7 load balancer is more sophisticated and more powerful. It inspects packets, has access to HTTP and HTTPS headers, and
 (armed with more information) can do a more intelligent job of spreading the load out to the target.

ELB - classic load balancer (not often used anymore)
NLB - network load balancer
ALB - application load balancer

ALB offers support for context-based routing, even for container-based applications.  An ALB is cheaper than an ELB, so where
possibe, use ALB.

If you need to handle requests in the highest of numbers, use NLBs.

[ Copy+paste from <https://aws.amazon.com/blogs/aws/new-aws-application-load-balancer/> ]

Name some of the TCP connections states

- LISTEN – Server is listening on a port, such as HTTP
- SYNC-SENT – Sent a SYN request, waiting for a response
- SYN-RECEIVED – (Server) Waiting for an ACK, occurs after sending an ACK from the server
- ESTABLISHED – 3 way TCP handshake has completed

What are some differences between TCP/UDP?
Reliable/Unreliable
Heavyweight/Lightweight
Ordered/Unordered
Stateful versus streaming
Header size

- UDP is typically used for video streaming, DNS, VoIP, online games
- TCP is typically used for transmitted data such as web, SSH, FTP, SMTP.  If the application needs to maintain state, TCP is typically the solution.
- TCP has more processing overhead than UDP
- TCP can stop on error for multiple reasons;  UDP lets the application software deal with lost packets, errors, and retransmission timers
- UDP can tolerate data loss (e.g., if some packets are lost in video stream, the worst outcome is that a few pixels are lost)

Related to TCP, what is TCB, and what are some important TCP variables?
=> Deep dive on a section in RFC 793, <https://datatracker.ietf.org/doc/html/rfc793>
  
The maintenance of a TCP connection requires several variables.  We conceive of these variables being stored in a connection record called a Transmission Control Block, or TCB.  Among the variables stored in the TCB are the local and remote socket numbers, the security and precedence of the connection, pointers to the user's send and receive buffers, and pointers to the retransmit queue and to the current segment.  In addition, several variables relating to the send and receive sequence numbers are stored in the TCB.

    Send Sequence Variables

      SND.UNA - send unacknowledged
      SND.NXT - send next
      SND.WND - send window
      SND.UP  - send urgent pointer
      SND.WL1 - segment sequence number used for last window update
      SND.WL2 - segment acknowledgment number used for last window
                update
      ISS     - initial send sequence number

    Receive Sequence Variables

      RCV.NXT - receive next
      RCV.WND - receive window
      RCV.UP  - receive urgent pointer
      IRS     - initial receive sequence number

The following diagrams may help to relate some of these variables to
  the sequence space.

  Send Sequence Space

                   1         2          3          4
              ----------|----------|----------|----------
                     SND.UNA    SND.NXT    SND.UNA
                                          +SND.WND

        1 - old sequence numbers which have been acknowledged
        2 - sequence numbers of unacknowledged data
        3 - sequence numbers allowed for new data transmission
        4 - future sequence numbers which are not yet allowed

  The send window is the portion of the sequence space labeled 3 in
  the diagram figure.

  Receive Sequence Space

                       1          2          3
                   ----------|----------|----------
                          RCV.NXT    RCV.NXT
                                    +RCV.WND

        1 - old sequence numbers which have been acknowledged
        2 - sequence numbers allowed for new reception
        3 - future sequence numbers which are not yet allowed

                         Receive Sequence Space

  The receive window is the portion of the sequence space labeled 2 in
  the diagram figure.

  There are also some variables used frequently in the discussion that
  take their values from the fields of the current segment.

    Current Segment Variables

      SEG.SEQ - segment sequence number
      SEG.ACK - segment acknowledgment number
      SEG.LEN - segment length
      SEG.WND - segment window
      SEG.UP  - segment urgent pointer
      SEG.PRC - segment precedence value

  A connection progresses through a series of states during its
  lifetime.  The states are:  LISTEN, SYN-SENT, SYN-RECEIVED,
  ESTABLISHED, FIN-WAIT-1, FIN-WAIT-2, CLOSE-WAIT, CLOSING, LAST-ACK,
  TIME-WAIT, and the fictional state CLOSED.  CLOSED is fictional
  because it represents the state when there is no TCB, and therefore,
  no connection.  Briefly the meanings of the states are:

    LISTEN - represents waiting for a connection request from any remote
    TCP and port.

    SYN-SENT - represents waiting for a matching connection request
    after having sent a connection request.

    SYN-RECEIVED - represents waiting for a confirming connection
    request acknowledgment after having both received and sent a
    connection request.

    ESTABLISHED - represents an open connection, data received can be
    delivered to the user.  The normal state for the data transfer phase
    of the connection.

    FIN-WAIT-1 - represents waiting for a connection termination request
    from the remote TCP, or an acknowledgment of the connection
    termination request previously sent.

    FIN-WAIT-2 - represents waiting for a connection termination request
    from the remote TCP.

    CLOSE-WAIT - represents waiting for a connection termination request
    from the local user.

    CLOSING - represents waiting for a connection termination request
    acknowledgment from the remote TCP.

    LAST-ACK - represents waiting for an acknowledgment of the
    connection termination request previously sent to the remote TCP
    (which includes an acknowledgment of its connection termination
    request).

    TIME-WAIT - represents waiting for enough time to pass to be sure
    the remote TCP received the acknowledgment of its connection
    termination request.

    CLOSED - represents no connection state at all.

  A TCP connection progresses from one state to another in response to
  events.  The events are the user calls, OPEN, SEND, RECEIVE, CLOSE,
  ABORT, and STATUS; the incoming segments, particularly those
  containing the SYN, ACK, RST and FIN flags; and timeouts.

  The state diagram in the next figure illustrates only state changes, together
  with the causing events and resulting actions, but addresses neither
  error conditions nor actions which are not connected with state
  changes.  In a later section in RFC 793, more detail is offered with respect to
  the reaction of the TCP to events.

                              +---------+ ---------\      active OPEN
                              |  CLOSED |            \    -----------
                              +---------+<---------\   \   create TCB
                                |     ^              \   \  snd SYN
                   passive OPEN |     |   CLOSE        \   \
                   ------------ |     | ----------       \   \
                    create TCB  |     | delete TCB         \   \
                                V     |                      \   \
                              +---------+            CLOSE    |    \
                              |  LISTEN |          ---------- |     |
                              +---------+          delete TCB |     |
                   rcv SYN      |     |     SEND              |     |
                  -----------   |     |    -------            |     V
 +---------+      snd SYN,ACK  /       \   snd SYN          +---------+
 |         |<-----------------           ------------------>|         |
 |   SYN   |                    rcv SYN                     |   SYN   |
 |   RCVD  |<-----------------------------------------------|   SENT  |
 |         |                    snd ACK                     |         |
 |         |------------------           -------------------|         |
 +---------+   rcv ACK of SYN  \       /  rcv SYN,ACK       +---------+
   |           --------------   |     |   -----------
   |                  x         |     |     snd ACK
   |                            V     V
   |  CLOSE                   +---------+
   | -------                  |  ESTAB  |
   | snd FIN                  +---------+
   |                   CLOSE    |     |    rcv FIN
   V                  -------   |     |    -------
 +---------+          snd FIN  /       \   snd ACK          +---------+
 |  FIN    |<-----------------           ------------------>|  CLOSE  |
 | WAIT-1  |------------------                              |   WAIT  |
 +---------+          rcv FIN  \                            +---------+
   | rcv ACK of FIN   -------   |                            CLOSE  |
   | --------------   snd ACK   |                           ------- |
   V        x                   V                           snd FIN V
 +---------+                  +---------+                   +---------+
 |FINWAIT-2|                  | CLOSING |                   | LAST-ACK|
 +---------+                  +---------+                   +---------+
   |                rcv ACK of FIN |                 rcv ACK of FIN |
   |  rcv FIN       -------------- |    Timeout=2MSL -------------- |
   |  -------              x       V    ------------        x       V
    \ snd ACK                 +---------+delete TCB         +---------+
     ------------------------>|TIME WAIT|------------------>| CLOSED  |
                              +---------+                   +---------+

                      TCP Connection State Diagram
                               Figure 6.

What are some common HTTP response codes?

- 200 OK (The request has succeeded)
- 301 Permanent Redirect
- 302 Temporary Redirect
- 403 Forbidden
- 404 File Not Found
- 500 Internal Server Error (Server Error)
- 503 Service Unavailable
- 504 Gateway Timeout

What does a SSL/TLS handshake look like? How does it work?
First, a typical TCP connection is established (handshake of SYN -> SYN/ACK -> ACK). Then,

1. Client Hello
Information that the server needs to communicate with the
client using SSL. This includes the SSL version number, cipher settings,
 session-specific data.

2. Server Hello
Information that the server needs to communicate with the
client using SSL. This includes the SSL version number, cipher settings,
 session-specific data.

3. Authentication and Pre-Master Secret
Client authenticates the server certificate. (e.g. Common
Name / Date / Issuer) Client (depending on the cipher) creates the
pre-master secret for the session, Encrypts with the server's public key
 and sends the encrypted pre-master secret to the server.

4. Decryption and Master Secret
Server uses its private key to decrypt the pre-master
secret. Both Server and Client perform steps to generate the master
secret with the agreed cipher.

5. Encryption with Session Key
Both client and server exchange messages to inform that future messages will be encrypted.

ref:  <https://www.websecurity.symantec.com/security-topics/how-does-ssl-handshake-work>

What is "TCP slow start"?
TCP slow start is a congestion control algorithm that starts by increasing the TCP congestion window each time an ACK is received, until an ACK is not received.

Terms to know:
cwnd - congestion window
rwnd - receiver's advertised window

To elaborate, TCP slow start is a TCP state variable that limits the amount of data that can be sent.  At any given time, a TCP transmission must not send data with a sequence number higher than the sum of:  the highest acknowledged sequence number, the minimum of 'cwnd', and the minimum of 'rwnd'.

The congestion window (cwnd) is a sender-side limit on the amount of data the sender can transmit into the network before receiving an acknowledgment (ACK), while the receiver’s advertised window (rwnd) is a receiver-side limit on the amount of outstanding data. The minimum of cwnd and rwnd governs data transmission.

Can you describe the TCP header format?
TCP segments are sent as internet datagrams.  The Internet Protocol header carries several information fields, including the source and destination host addresses.  A TCP header follows the internet header, supplying information specific to the TCP protocol.  This division allows for the existence of host level protocols other than TCP.

 TCP Header Format

    0                   1                   2                   3
    0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |          Source Port          |       Destination Port        |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |                        Sequence Number                        |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |                    Acknowledgment Number                      |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |  Data |           |U|A|P|R|S|F|                               |
   | Offset| Reserved  |R|C|S|S|Y|I|            Window             |
   |       |           |G|K|H|T|N|N|                               |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |           Checksum            |         Urgent Pointer        |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |                    Options                    |    Padding    |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |                             data                              |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

 Note that one tick mark represents one bit position.

Source Port:  16 bits

    The source port number.

  Destination Port:  16 bits

    The destination port number.

Sequence Number:  32 bits

    The sequence number of the first data octet in this segment (except
    when SYN is present). If SYN is present the sequence number is the
    initial sequence number (ISN) and the first data octet is ISN+1.

  Acknowledgment Number:  32 bits

    If the ACK control bit is set this field contains the value of the
    next sequence number the sender of the segment is expecting to
    receive.  Once a connection is established this is always sent.

  Data Offset:  4 bits

    The number of 32 bit words in the TCP Header.  This indicates where
    the data begins.  The TCP header (even one including options) is an
    integral number of 32 bits long.

  Reserved:  6 bits

    Reserved for future use.  Must be zero.

  Control Bits:  6 bits (from left to right):

    URG:  Urgent Pointer field significant
    ACK:  Acknowledgment field significant
    PSH:  Push Function
    RST:  Reset the connection
    SYN:  Synchronize sequence numbers
    FIN:  No more data from sender

  Window:  16 bits

    The number of data octets beginning with the one indicated in the
    acknowledgment field which the sender of this segment is willing to
    accept.

  Checksum:  16 bits

    The checksum field is the 16 bit one's complement of the one's
    complement sum of all 16 bit words in the header and text.  (The ones' complement of a binary number is the value obtained by
    inverting all the bits in the binary representation of the number (swapping 0s and 1s).)

    The checksum also covers a 96 bit pseudo header conceptually prefixed to the TCP header.  
    This pseudo header contains the Source Address, the Destination Address, 
    the Protocol, and TCP length.
    This gives the TCP protection against misrouted segments.  This
    information is carried in the Internet Protocol and is transferred
    across the TCP/Network interface in the arguments or results of
    calls by the TCP on the IP.

Monitoring & Alerting
----------------------------

What would be some good CloudWatch Metrics to alarm on?

- CPU Utilization,
- Billing (aws spend),
- CPU or EBS Credit Balance,
- StatusCheckFailed,
- EBS Idle Time,
- disk_free (w/ agent),
- mem_free (w/ agent),
- HTTPCode_ELB_5XX_Count,
- LB RejectedConnectionCount,
- TargetConnectionErrorCount,
- UnhealthyHostCount,
- LB Spillover
- Throttles (Lambda),
- ConcurrentExecutions (Lambda), ....
- RDS: connection pooling, and all the metrics for cpu, disk, network, ...
- Route53: HealthChecks
- SQS: DeadLetterQueue receive message
- AWS account service limits (service quotas)

System Design
--------------------

tk
tk

Behavioral or PM
-----------------------

How do you approach a new project?
● Outline the scope, timeline, requirements; start with a research & design document template
● Outline stakeholders and communicate with them
● Draft a plan, including implementation steps, and share it, requesting feedback

- Define how success will be measured and tracked
- Define multiple solution options and their trade-offs, and provide recommendation for one of them
● Communicate early, communicate often
● Schedule meetings (kick off, milestone, sprint planning, kaizen explorations) to set expectations and be in
the loop on progress and to find opportunities for improvement
● Prioritize documentation. Always take detailed notes about everything and share them
● Organize in JIRA -- Epics, acceptance criteria, tags, “Fixed Version”, sprint version, kanban, is related to, time spent on, story points,
priority, planned to be finished on, ...

Other
--------

- Study Google's SRE Handbook:  <https://sre.google/sre-book/table-of-contents/>
- Key chapters:
    1. <https://sre.google/sre-book/testing-reliability/>
    2. <https://sre.google/sre-book/effective-troubleshooting/>
    3. <https://sre.google/sre-book/monitoring-distributed-systems/>
    4. <https://sre.google/sre-book/release-engineering/>
    5. <https://sre.google/sre-book/software-engineering-in-sre/>
    6. <https://sre.google/sre-book/load-balancing-frontend/>
    7. <https://sre.google/sre-book/load-balancing-datacenter/>
    8. <https://sre.google/sre-book/handling-overload/>
    9. <https://sre.google/sre-book/addressing-cascading-failures/>
    10. <https://sre.google/sre-book/managing-critical-state/>
    11. <https://sre.google/sre-book/operational-overload/>
    12. <https://sre.google/sre-book/dealing-with-interrupts/>
