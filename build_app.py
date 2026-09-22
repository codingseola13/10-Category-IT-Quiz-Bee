import json, os, textwrap

cats = [
"Basic Computer Concepts / General IT",
"Logic Formulation",
"Operating Systems",
"Software Engineering",
"Object-Oriented Programming",
"Computer Networks and Telecommunication",
"Computer Architecture and IT Security",
"Database Management System",
"Data Science and Analytics",
"E-commerce and Web Design"
]

mcq = []
def add(cat, concept, question, options, answer, explanation):
    mcq.append({"category":cat,"concept":concept,"question":question,"options":options,"answer":answer,"explanation":explanation})

C=cats

# 1 Basic Computer Concepts / General IT
add(C[0],"Bit and byte","How many bits are in one byte?",["4","8","16","32"],1,"A byte contains 8 bits.")
add(C[0],"RAM vs ROM","Which memory is normally volatile and loses its contents when power is removed?",["RAM","ROM","SSD","Flash memory"],0,"RAM is volatile working memory.")
add(C[0],"Firmware","Software stored in non-volatile memory that provides low-level control of a device is called what?",["Firmware","Middleware","Shareware","Spreadsheet software"],0,"Firmware is embedded software closely tied to hardware.")
add(C[0],"Compiler","Which translator converts source code into a target form before the resulting program is run?",["Compiler","Interpreter","Device driver","Shell"],0,"A compiler translates source code before execution of the resulting target program.")
add(C[0],"Interpreter","Which translator generally executes source instructions through an interpreter at runtime rather than producing a standalone native executable first?",["Interpreter","Assembler","Linker","Bootloader"],0,"An interpreter executes program instructions through the interpreter at runtime.")
add(C[0],"System vs application software","Which is system software?",["Operating system","Word processor","Presentation editor","Photo editor"],0,"An operating system manages hardware and provides services for applications.")
add(C[0],"Binary to decimal","What is binary 1010 in decimal?",["8","10","12","14"],1,"1010₂ = 8 + 2 = 10.")
add(C[0],"Hexadecimal","Which hexadecimal digit represents decimal 15?",["E","F","10","D"],1,"Hexadecimal uses F for decimal 15.")
add(C[0],"Virtualization","What technology allows multiple isolated operating-system environments to run on one physical machine through virtual machines?",["Virtualization","Defragmentation","Compilation","Packet switching"],0,"Virtualization abstracts physical hardware so multiple virtual machines can run on one host.")
add(C[0],"Cloud service model","Which cloud service model delivers complete applications to users over the internet, such as a browser-based email service?",["SaaS","IaaS","PaaS","LAN"],0,"Software as a Service provides complete applications to end users.")

# 2 Logic
add(C[1],"AND","When is P AND Q true?",["Only when both P and Q are true","When either one is true","Only when both are false","Whenever P is false"],0,"A conjunction is true only when both operands are true.")
add(C[1],"OR","When is inclusive P OR Q false?",["Only when both are false","Only when both are true","Whenever P is true","Whenever Q is true"],0,"Inclusive OR is false only when both operands are false.")
add(C[1],"XOR","For two Boolean inputs, when is XOR true?",["When exactly one input is true","When both are true","When both are false","Whenever at least one is false"],0,"XOR is true when the two Boolean inputs differ.")
add(C[1],"Material implication","When is P → Q false?",["P true, Q false","P false, Q true","P false, Q false","P true, Q true"],0,"Material implication is false only when the antecedent is true and the consequent is false.")
add(C[1],"Converse","What is the converse of P → Q?",["Q → P","¬P → ¬Q","¬Q → ¬P","P ↔ Q"],0,"The converse switches P and Q.")
add(C[1],"Inverse","What is the inverse of P → Q?",["¬P → ¬Q","Q → P","¬Q → ¬P","P AND Q"],0,"The inverse negates both parts without switching them.")
add(C[1],"Contrapositive","What is the contrapositive of P → Q?",["¬Q → ¬P","Q → P","¬P → ¬Q","Q ↔ P"],0,"The contrapositive switches and negates both parts.")
add(C[1],"De Morgan's law","NOT (P AND Q) is equivalent to which expression?",["NOT P OR NOT Q","NOT P AND NOT Q","P OR Q","P AND Q"],0,"De Morgan's law changes AND to OR while negating both operands.")
add(C[1],"Algorithm","Which description best defines an algorithm?",["A finite step-by-step procedure for solving a problem","A physical storage device","A network address","A database table"],0,"An algorithm is a finite sequence of well-defined steps used to solve a problem.")
add(C[1],"Loop tracing","A loop runs for i = 1, 2, 3 and adds i to a total starting at 0. What is the final total?",["3","5","6","9"],2,"0 + 1 + 2 + 3 = 6.")

# 3 OS
add(C[2],"Process vs thread","Which best describes a thread?",["An execution path inside a process","A complete physical computer","A database relationship","A network packet"],0,"A thread is an execution path within a process and typically shares process resources.")
add(C[2],"Context switch","What occurs during a context switch?",["The OS saves one task's state and loads another task's state","The disk is formatted","A router changes its IP address","A database is normalized"],0,"A context switch changes which process or thread the CPU is executing.")
add(C[2],"Preemptive scheduling","In preemptive scheduling, what can the OS do?",["Interrupt a running process and give the CPU to another","Never interrupt a running process","Delete a process automatically","Prevent context switches"],0,"Preemptive scheduling allows the OS to take CPU control from a running task.")
add(C[2],"Round Robin","Which CPU scheduling algorithm gives each ready process a fixed time quantum in rotation?",["Round Robin","FCFS","SJF","Batch scheduling"],0,"Round Robin cycles through ready processes using a time quantum.")
add(C[2],"Starvation vs deadlock","Which pairing is correct?",["Starvation: one process keeps getting skipped; Deadlock: processes wait on resources held by one another","Starvation: all processes finish; Deadlock: one process has high priority","Starvation: page is absent from RAM; Deadlock: disk is full","Starvation: CPU cache miss; Deadlock: DNS failure"],0,"Starvation means a process can wait indefinitely while others are favored; deadlock means processes are stuck waiting on resources held by each other.")
add(C[2],"Page replacement algorithms","Which pairing correctly describes FIFO, LRU, and Optimal page replacement?",["FIFO removes the oldest arrival; LRU removes the least recently used; Optimal removes the page whose next use is farthest in the future","FIFO removes the newest page; LRU removes the most recently used; Optimal removes the most important page","FIFO uses future knowledge; LRU uses arrival order; Optimal removes randomly","All three always remove the same page"],0,"FIFO looks at arrival order, LRU looks backward at recent use, and Optimal looks forward to the next future use.")
add(C[2],"Page vs frame","Which statement is correct?",["A page is a virtual-memory block; a frame is a physical-RAM block","A frame is virtual; a page is physical","Both are network terms","Both are CPU registers"],0,"Virtual memory is divided into pages, while physical RAM is divided into frames.")
add(C[2],"Virtual memory and pagefile","Which statement best describes Windows pagefile.sys in virtual-memory management?",["It is disk-based backing storage that can hold memory contents when needed; it is not physical RAM","It is the CPU's L1 cache","It is a database index","It is a router table"],0,"pagefile.sys is stored on secondary storage and can back virtual memory; it is much slower than RAM.")
add(C[2],"Page fault vs thrashing","Which pairing is correct?",["Page fault: needed page is not in RAM; Thrashing: excessive page faults/page movement leave little time for useful work","Page fault: CPU overheats; Thrashing: a process finishes normally","Page fault: a router drops traffic; Thrashing: a database rolls back","Page fault and thrashing are identical single events"],0,"A page fault is one missing-page event; thrashing is a performance condition caused by excessive paging activity.")
add(C[2],"Synchronization","Which mechanism is commonly used to allow only one thread at a time into a critical section?",["Mutex","Page table","Boot sector","Cache line"],0,"A mutex provides mutual exclusion for protected critical sections.")

# 4 Software Engineering
add(C[3],"Functional requirement","Which is a functional requirement?",["The system shall allow users to reset passwords","The system shall respond within 2 seconds","The system shall be available 99.9% of the time","The interface shall meet a contrast ratio target"],0,"Functional requirements describe what the system must do.")
add(C[3],"Non-functional requirement","Which is a non-functional requirement?",["The system shall respond within 2 seconds under normal load","The system shall generate invoices","The system shall let users log in","The system shall export reports"],0,"Performance is a quality constraint, so it is non-functional.")
add(C[3],"Verification","Verification primarily asks which question?",["Are we building the product correctly according to specification?","Are we building the product users actually need?","Is the network online?","Is the CPU fast enough?"],0,"Verification checks conformance to specifications and implementation correctness.")
add(C[3],"Validation","Validation primarily asks which question?",["Are we building the right product for the intended need?","Did we compile without syntax errors?","Did we save the file?","Did the router forward the packet?"],0,"Validation checks whether the resulting product satisfies intended needs.")
add(C[3],"Unit testing","Which testing level focuses on an individual function, method, class, or small component in isolation?",["Unit testing","Integration testing","Acceptance testing","System testing"],0,"Unit testing checks small units independently.")
add(C[3],"Integration testing","Which testing level checks whether combined modules interact correctly?",["Integration testing","Unit testing","Static typing","Deployment testing"],0,"Integration testing focuses on interfaces and interactions between combined components.")
add(C[3],"Acceptance testing","Which testing level is most directly concerned with whether the system is acceptable to users or stakeholders?",["Acceptance testing","Unit testing","Compilation","Linking"],0,"Acceptance testing evaluates whether the system satisfies acceptance criteria and user/business needs.")
add(C[3],"Agile","Which development approach emphasizes iterative delivery, feedback, and adapting to change?",["Agile","Waterfall only","Machine code","Normalization"],0,"Agile methods emphasize iterative development and feedback.")
add(C[3],"Scrum","In Scrum, what is a fixed-length iteration called?",["Sprint","Milestone","Branch","Packet"],0,"A Sprint is Scrum's fixed-length iteration.")
add(C[3],"Version control","What is the main purpose of version control?",["Track changes to files and support collaboration/history","Increase CPU clock speed","Encrypt every database field","Assign IP addresses"],0,"Version control records changes and supports collaboration, rollback, and history.")

# 5 OOP
add(C[4],"Class vs object","Which statement is correct?",["A class is a blueprint; an object is an instance of that class","An object is a blueprint; a class is a network packet","A class is a database row only","They are always identical concepts"],0,"A class defines structure/behavior; an object is a created instance.")
add(C[4],"Encapsulation","Which OOP principle bundles data with methods and controls direct access to internal state?",["Encapsulation","Inheritance","Recursion","Normalization"],0,"Encapsulation groups data and behavior and restricts access through a controlled interface.")
add(C[4],"Abstraction","Which OOP principle exposes essential behavior while hiding unnecessary implementation details?",["Abstraction","Aggregation","Compilation","Indexing"],0,"Abstraction presents essential features without requiring users to know internal implementation details.")
add(C[4],"Inheritance","Which OOP mechanism allows a child class to acquire or extend behavior from a parent class?",["Inheritance","Hashing","Routing","Paging"],0,"Inheritance lets a derived class reuse and extend a base class.")
add(C[4],"Polymorphism","What does polymorphism allow in OOP?",["The same interface or operation to behave differently for different objects","Only one class to exist","All fields to be public","No methods to be inherited"],0,"Polymorphism supports multiple implementations behind a common interface or operation.")
add(C[4],"Method overloading","Two methods share the same name but have different parameter lists. What is this?",["Method overloading","Method overriding","Encapsulation","Composition"],0,"Overloading uses the same method name with different signatures/parameter lists.")
add(C[4],"Method overriding","A child class provides its own implementation of an inherited method with the same signature. What is this?",["Method overriding","Method overloading","Aggregation","Instantiation"],0,"Overriding replaces inherited behavior while keeping the same method signature.")
add(C[4],"Method signature","For Quiz Bee-level OOP, which pair most directly identifies a method signature?",["Method name and parameter list","Return value and comment","Class color and filename","CPU register and address"],0,"Method signatures are identified by the method name and parameter types/order in common OOP languages such as Java.")
add(C[4],"Constructor","What is the special method used to initialize a new object when it is created called?",["Constructor","Destructor only","Router","Query"],0,"A constructor initializes a newly created object.")
add(C[4],"Composition","A Car strongly owns an Engine as an integral part of itself. Which relationship best fits?",["Composition","Inheritance","Overloading","Recursion"],0,"Composition is a strong whole-part relationship where the part's lifecycle is tied to the whole conceptually.")

# 6 Networks
add(C[5],"TCP vs UDP","Which pairing is correct?",["TCP: reliable and ordered with more control overhead; UDP: lower overhead without delivery/order guarantees","TCP: no connection or reliability; UDP: reliable ordered byte stream","TCP and UDP are database protocols","TCP is only for local networks; UDP is only for the internet"],0,"TCP uses reliability mechanisms such as sequencing and acknowledgments, while UDP has less overhead and no built-in delivery/order guarantee.")
add(C[5],"Segment, datagram, packet","Which pairing is correct?",["TCP → segment; UDP → datagram; IP → packet","TCP → packet; UDP → frame; IP → segment","TCP → datagram; UDP → segment; IP → thread","All three terms mean exactly the same layer-specific unit"],0,"At the transport layer TCP uses segments and UDP uses datagrams; IP carries them in packets at the network layer.")
add(C[5],"Network layers","Which pairing is correct?",["Transport: TCP/UDP; Network: IP/routing; Data link: local frames/MAC","Transport: CSS; Network: SQL; Data link: hashing","Transport: RAM; Network: CPU; Data link: SSD","All network functions belong to one layer"],0,"Layering separates responsibilities: transport handles end-to-end transport, the network layer handles IP/routing, and data link handles local-link delivery.")
add(C[5],"DNS and DHCP","Which pairing is correct?",["DNS resolves names; DHCP assigns network configuration","DNS assigns passwords; DHCP hashes them","DNS routes packets; DHCP compiles code","DNS and DHCP are CPU schedulers"],0,"DNS resolves names to addresses; DHCP supplies client network configuration.")
add(C[5],"ARP and NAT","Which pairing is correct?",["ARP maps local IPv4 addresses to MAC addresses; NAT translates between private/public addressing","ARP assigns domain names; NAT stores passwords","ARP encrypts HTTP; NAT schedules CPU time","ARP and NAT are database joins"],0,"ARP resolves local IPv4-to-MAC mappings, while NAT translates addressing between network realms.")
add(C[5],"Router vs switch","Which statement is correct?",["A router forwards IP packets between networks; a switch primarily forwards frames within a LAN using MAC information","A switch routes between the internet and every network; a router only repeats signals","Both devices only perform DNS","Neither device examines addresses"],0,"Routers connect IP networks, while Ethernet switches primarily make local frame-forwarding decisions using MAC addresses.")
add(C[5],"Routing vs forwarding","Which statement best distinguishes routing from forwarding?",["Routing determines paths/forwarding information; forwarding sends an individual packet out the chosen interface","Routing and forwarding are identical words with no distinction","Routing is password hashing; forwarding is encryption","Routing is only physical cabling; forwarding is only DNS"],0,"Routing builds or learns path information, while forwarding is the per-packet action that uses that information.")
add(C[5],"Flow vs congestion control","Which pairing is correct?",["Flow control protects the receiver from being overwhelmed; congestion control protects the network from excessive traffic","Flow control protects the network; congestion control only protects one receiver","Both are page replacement algorithms","Both only refer to database transactions"],0,"Flow control concerns sender/receiver rate mismatch, while congestion control addresses overloaded network paths.")
add(C[5],"Subnetting","How many usable host addresses are available in a conventional IPv4 /27 subnet?",["14","30","32","62"],1,"A /27 leaves 5 host bits: 2^5 = 32 total, minus network and broadcast = 30 usable.")
add(C[5],"Ports","Which statement about transport-layer ports is correct?",["Ports help identify the destination application/service on a host","Ports are physical RAM slots only","Ports replace IP addresses","Ports are SQL table columns"],0,"TCP and UDP port numbers help deliver transport data to the intended application/service endpoint on a host.")

# 7 Architecture & Security
add(C[6],"Fetch-decode-execute","Which sequence describes the simplified CPU instruction cycle?",["Fetch → Decode → Execute","Decode → Encrypt → Route","Read → Hash → Store","Input → Print → Delete"],0,"The CPU fetches an instruction, decodes it, then executes it.")
add(C[6],"ALU vs control unit","Which pairing is correct?",["ALU performs arithmetic/logic; control unit coordinates instruction execution","ALU stores webpages; control unit assigns IP addresses","ALU is secondary storage; control unit is a database key","ALU encrypts passwords; control unit is a router"],0,"The ALU performs arithmetic/logical work while the control unit coordinates processor operations.")
add(C[6],"Cache and locality","Which pairing is correct?",["Temporal locality: recently used data may be reused soon; Spatial locality: nearby memory locations may be used soon","Temporal locality: nearby addresses; Spatial locality: only old data","Both forms of locality mean data is encrypted","Locality is a database-only concept"],0,"Cache benefits from temporal reuse and spatially nearby accesses.")
add(C[6],"CIA triad","Which CIA-triad property protects data from unauthorized modification?",["Integrity","Confidentiality","Availability","Scalability"],0,"Integrity protects accuracy and guards against unauthorized alteration.")
add(C[6],"Hashing vs encryption","Which statement is correct?",["Hashing is designed as one-way verification; encryption is reversible with the correct key","Hashing and encryption are identical","Encryption cannot recover original data","Hashing always uses a secret decryption key"],0,"Hashing is designed to be one-way; encryption is designed to be reversible with a key.")
add(C[6],"Salt","Why is a unique random salt added before password hashing?",["To make identical passwords produce different stored hashes and resist precomputed attacks","To decrypt passwords later","To speed up networking","To replace authentication"],0,"A unique salt changes the hash input so identical passwords need not produce identical stored hashes.")
add(C[6],"Password verification","How does a properly designed system usually verify a password stored with a salt and hash?",["Hash the entered password with the stored salt and compare the result with the stored hash","Decrypt the stored hash into the original password","Email the original password to the user","Compare only password length"],0,"Password verification recomputes the hash using the stored salt and compares hash values; it does not decrypt the stored hash.")
add(C[6],"Password reset token","Why should a password-reset token normally expire and become invalid after successful use?",["So an old or reused link cannot keep authorizing password resets indefinitely","So the password hash becomes reversible","So TCP can retransmit it","So the CPU can cache it forever"],0,"Reset tokens are temporary authorization secrets and should be short-lived and one-time use.")
add(C[6],"Phishing","Which attack uses deceptive messages or websites to trick users into revealing credentials?",["Phishing","Defragmentation","Caching","Normalization"],0,"Phishing relies on social engineering and impersonation.")
add(C[6],"Least privilege","Which security principle says users and programs should receive only the permissions necessary for their tasks?",["Least privilege","Open access","Full trust","Unlimited delegation"],0,"Least privilege limits permissions to the minimum needed, reducing the damage from mistakes or compromise.")

# 8 DBMS
add(C[7],"Primary key","What is the main purpose of a primary key?",["Uniquely identify each row","Encrypt the table","Sort every query automatically","Duplicate values"],0,"A primary key uniquely identifies rows.")
add(C[7],"Composite key","What is a composite key?",["A key made of two or more attributes working together","A key stored only in RAM","An encrypted password","A CSS selector"],0,"A composite key uses multiple attributes together to identify a row.")
add(C[7],"Foreign key","What does a foreign key usually reference?",["A candidate/primary key in another or the same related table","A CPU register","A CSS class","A network frame"],0,"Foreign keys create referential relationships between tables.")
add(C[7],"1NF","Which condition is associated with First Normal Form?",["Each field contains atomic values and repeating groups are removed","No transitive dependencies","No partial dependencies","Every table has exactly two columns"],0,"1NF requires atomic values and eliminates repeating groups.")
add(C[7],"2NF / partial dependency","A table is in 1NF but a non-key attribute depends on only part of a composite key. Which problem prevents 2NF?",["Partial dependency","Transitive dependency","Join dependency","Deadlock"],0,"2NF removes partial dependency on part of a composite key.")
add(C[7],"3NF / transitive dependency","A non-key attribute depends on another non-key attribute, which depends on the key. What is this?",["Transitive dependency","Partial dependency","Multivalued dependency","Starvation"],0,"3NF addresses transitive dependency among non-key attributes.")
add(C[7],"INNER JOIN","Which SQL join returns only rows that match the join condition in both tables?",["INNER JOIN","LEFT JOIN","CROSS JOIN","FULL OUTER JOIN only"],0,"INNER JOIN keeps rows that match in both joined tables.")
add(C[7],"HAVING","Which SQL clause filters grouped results after GROUP BY?",["HAVING","WHERE","SELECT","VALUES"],0,"HAVING filters groups after aggregation.")
add(C[7],"Atomicity","Which ACID property means a transaction happens completely or not at all?",["Atomicity","Consistency","Isolation","Durability"],0,"Atomicity is the all-or-nothing property.")
add(C[7],"Index","What is the main purpose of a database index?",["Speed up data retrieval at the cost of extra storage/maintenance","Encrypt all records","Replace primary keys","Guarantee no duplicate values in every column"],0,"Indexes improve lookup performance but require extra storage and maintenance.")

# 9 Data Science
add(C[8],"Mean","What is the arithmetic mean of 2, 4, 6, and 8?",["4","5","6","20"],1,"(2+4+6+8)/4 = 20/4 = 5.")
add(C[8],"Median","What is the median of 1, 3, 7, 9, 20?",["3","7","8","9"],1,"The middle ordered value is 7.")
add(C[8],"Mode","What is the mode of 2, 2, 3, 4, 4, 4, 5?",["2","3","4","5"],2,"4 appears most frequently.")
add(C[8],"Standard deviation","What does standard deviation measure?",["How spread out values are around the mean","The most frequent value","The middle value only","A database relationship"],0,"Standard deviation measures dispersion around the mean.")
add(C[8],"Correlation vs causation","Which statement is correct?",["Correlation does not by itself prove causation","Correlation always proves causation","Causation never involves correlation","They are identical terms"],0,"A statistical association alone does not establish a causal relationship.")
add(C[8],"Supervised learning","Which learning approach uses labeled examples with known target outputs?",["Supervised learning","Unsupervised learning","Random sampling","Compression"],0,"Supervised learning trains on inputs paired with targets.")
add(C[8],"Classification","Predicting whether an email is spam or not spam is primarily what type of task?",["Classification","Regression","Clustering","Sorting"],0,"Classification predicts discrete categories.")
add(C[8],"Regression","Predicting a house price as a continuous number is primarily what type of task?",["Regression","Classification","Clustering","Hashing"],0,"Regression predicts continuous numerical values.")
add(C[8],"Overfitting vs underfitting","Which pairing is correct?",["Overfitting: strong training performance but weak unseen-data performance; Underfitting: weak performance even on training data","Overfitting: weak on all data; Underfitting: perfect generalization","Overfitting and underfitting are identical","Both terms describe database normalization"],0,"Overfitting generalizes poorly despite fitting training data well; underfitting fails to capture enough structure even on training data.")
add(C[8],"Precision","Which metric is TP / (TP + FP)?",["Precision","Recall","Accuracy","Specificity"],0,"Precision measures the fraction of predicted positives that are actually positive.")

# 10 E-commerce/Web
add(C[9],"B2C","A company selling products directly to individual customers is which model?",["B2C","B2B","C2C","C2B"],0,"Business-to-consumer describes business sales to individual consumers.")
add(C[9],"B2B","A software company selling enterprise licenses to another company is which model?",["B2B","B2C","C2C","C2B"],0,"Business-to-business describes transactions between businesses.")
add(C[9],"HTML","Which technology primarily defines the structure and semantic content of a webpage?",["HTML","CSS","JavaScript","SQL"],0,"HTML provides webpage structure and semantics.")
add(C[9],"CSS","Which technology primarily controls presentation and layout of webpages?",["CSS","HTML","SQL","DNS"],0,"CSS controls visual styling and layout.")
add(C[9],"JavaScript","Which technology primarily adds programming logic and interactivity in the browser?",["JavaScript","CSS","HTML only","SMTP"],0,"JavaScript provides client-side programming and interactivity.")
add(C[9],"CSS specificity","Which selector generally has higher specificity?",["#main",".main","div","*"],0,"An ID selector has higher specificity than class and element selectors.")
add(C[9],"Responsive design","Which CSS feature is commonly used to apply styles based on viewport conditions such as width?",["Media queries","Cookies","SQL joins","DHCP"],0,"Media queries enable conditional responsive styling.")
add(C[9],"HTTP GET vs POST","Which pairing is generally correct?",["GET retrieves a representation; POST submits data for processing","GET always deletes; POST only reads","GET is a database command; POST is CSS","GET encrypts; POST decrypts"],0,"GET requests a representation; POST submits data to a resource for processing.")
add(C[9],"HTTP status codes","Which HTTP status code means Not Found?",["200","301","404","500"],2,"404 indicates that the requested resource was not found.")
add(C[9],"HTTPS/TLS","What does HTTPS add to HTTP?",["TLS protection for encrypted/authenticated communication","A database primary key","A CPU cache","A page replacement algorithm"],0,"HTTPS uses TLS to protect HTTP communication.")

assert len(mcq)==100, len(mcq)

finals = {"easy":[],"average":[],"difficult":[]}
def fid(level, cat, concept, prompt, answers, explanation):
    finals[level].append({"category":cat,"concept":concept,"prompt":prompt,"answers":answers,"explanation":explanation})

# Easy: one per category, mostly direct recall, 10 unique concepts
fid("easy",C[0],"ROM","What non-volatile memory traditionally stores firmware or fixed instructions and retains data without power?",["ROM","read only memory"],"ROM is non-volatile memory traditionally used for fixed instructions or firmware.")
fid("easy",C[1],"NOT","Which Boolean operator reverses a truth value?",["NOT","negation"],"NOT, also called negation, reverses true to false and false to true.")
fid("easy",C[2],"Virtual memory","What OS concept gives processes an address space that can exceed physical RAM by using storage as backing when needed?",["virtual memory"],"Virtual memory abstracts memory and can use secondary storage as backing.")
fid("easy",C[3],"Waterfall","What software-development model is known for a more sequential phase-by-phase flow such as requirements, design, implementation, and testing?",["waterfall","waterfall model"],"Waterfall is a sequential development model.")
fid("easy",C[4],"Object","What do we call a concrete instance created from a class?",["object","instance"],"An object is an instance of a class.")
fid("easy",C[5],"MAC address","What address identifies a network interface at the data-link layer on a local network?",["mac address","mac","media access control address"],"A MAC address identifies a network interface at the data-link layer.")
fid("easy",C[6],"Confidentiality","Which CIA-triad property protects information from unauthorized disclosure?",["confidentiality"],"Confidentiality protects data from unauthorized access or disclosure.")
fid("easy",C[7],"Foreign key","What database key references a key in another related table to create a relationship?",["foreign key"],"A foreign key references a candidate/primary key in a related table.")
fid("easy",C[8],"Clustering","What unsupervised learning task groups similar data points without predefined labels?",["clustering"],"Clustering groups similar observations without labeled targets.")
fid("easy",C[9],"Cookie","What small piece of data can a website store in a user's browser and send with later requests?",["cookie","http cookie","web cookie"],"A cookie is browser-stored data associated with a site and can accompany later requests.")

# Average: one per category, scenario-based
fid("average",C[0],"PaaS","A cloud provider gives developers a managed runtime and deployment platform so they can build apps without managing the underlying servers. Identify the service model.",["paas","platform as a service"],"Platform as a Service provides a managed application platform/runtime.")
fid("average",C[1],"Logical equivalence","Two propositions always have the same truth value for every possible input. What relationship do they have?",["logical equivalence","logically equivalent"],"Logically equivalent propositions match in truth value under all interpretations.")
fid("average",C[2],"Semaphore","A synchronization primitive maintains a counter so a limited number of threads can access a resource at the same time. Identify it.",["semaphore"],"A semaphore uses a counter to control access to a limited number of resource slots.")
fid("average",C[3],"Regression testing","After a bug fix, testers rerun previously passing tests to check that existing features were not broken. Identify this testing practice.",["regression testing","regression test"],"Regression testing checks that changes have not broken existing behavior.")
fid("average",C[4],"Interface","In OOP, what construct declares a contract of operations that implementing classes agree to provide?",["interface"],"An interface defines a contract that implementing classes satisfy.")
fid("average",C[5],"Forwarding","A router receives one packet, consults its forwarding table, and sends that packet out the appropriate interface. Identify this action.",["forwarding","packet forwarding"],"Forwarding is the per-packet action of sending traffic to the next interface.")
fid("average",C[6],"Authentication","A system asks a user to prove who they are using a password or biometric. What security process is this?",["authentication"],"Authentication verifies identity.")
fid("average",C[7],"LEFT JOIN","A query must return every row from the left table even when no matching row exists in the right table. Which SQL join is needed?",["left join","left outer join"],"LEFT JOIN preserves all left-table rows and matches right-table rows when available.")
fid("average",C[8],"Recall","For a binary classifier, what metric is TP / (TP + FN)?",["recall","sensitivity","true positive rate"],"Recall measures the fraction of actual positives that were correctly identified.")
fid("average",C[9],"Session","A website needs to keep track of a logged-in user's state across multiple HTTP requests. What server-side concept is commonly used?",["session","web session","http session"],"A session maintains user state across multiple requests.")

# Difficult: one per category, reasoning/application, 30 sec
fid("difficult",C[0],"Two's complement","What binary representation method is commonly used by computers to represent signed integers so that addition circuitry can handle positive and negative values efficiently?",["two's complement","twos complement","2's complement","2s complement"],"Two's complement is the standard signed-integer representation in modern computers.")
fid("difficult",C[1],"Tautology","What do we call a propositional formula that is true under every possible assignment of truth values?",["tautology"],"A tautology is true under all truth assignments.")
fid("difficult",C[2],"Working set","What OS term refers to the set of memory pages a process is actively using during a recent time window, often used when reasoning about thrashing?",["working set","working set model"],"The working set is the collection of pages a process actively needs over a recent interval.")
fid("difficult",C[3],"Coupling","What software-design term describes the degree of interdependence between modules, where lower values are generally preferred?",["coupling"],"Coupling measures how strongly modules depend on one another.")
fid("difficult",C[4],"Dynamic dispatch","What mechanism chooses the implementation of an overridden method at runtime based on the object's actual type?",["dynamic dispatch","dynamic method dispatch","runtime dispatch"],"Dynamic dispatch selects the runtime implementation for polymorphic calls.")
fid("difficult",C[5],"Congestion control","TCP reduces its sending rate when the network path becomes overloaded. What broad networking mechanism is this?",["congestion control"],"Congestion control adjusts sending behavior to avoid overwhelming the network.")
fid("difficult",C[6],"Authorization","After a user proves their identity, the system checks whether they are allowed to access the admin panel. What security process is this?",["authorization"],"Authorization determines what an authenticated identity is permitted to do.")
fid("difficult",C[7],"Isolation","Two database transactions execute concurrently, but each should behave as though it were running alone with respect to intermediate states. Which ACID property is this?",["isolation"],"Isolation controls interaction among concurrent transactions so intermediate states do not improperly interfere.")
fid("difficult",C[8],"Confusion matrix","What table summarizes a classifier's true positives, false positives, true negatives, and false negatives?",["confusion matrix"],"A confusion matrix organizes classification outcomes into TP, FP, TN, and FN.")
fid("difficult",C[9],"CORS","What browser security mechanism controls whether a webpage from one origin may request resources from another origin based on server-provided HTTP headers?",["cors","cross origin resource sharing","cross-origin resource sharing"],"CORS is the HTTP-header-based mechanism governing permitted cross-origin browser requests.")

for level in finals:
    assert len(finals[level])==10

concepts = {}
for cat in cats:
    concepts[cat] = []
for q in mcq:
    concepts[q["category"]].append(q["concept"])
for level in finals.values():
    for q in level:
        concepts[q["category"]].append(q["concept"])

index_html = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>IT Quiz Bee Trainer</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <main class="app-shell">
    <section id="home" class="screen active">
      <div class="hero card">
        <p class="eyebrow">IT Quiz Bee Trainer</p>
        <h1>Elimination + Final Round Practice</h1>
        <p class="lead">100-item elimination simulation plus 30 identification questions: 10 Easy, 10 Average, 10 Difficult.</p>
        <div class="stats-grid">
          <div><strong>100</strong><span>MCQs</span></div>
          <div><strong>60 min</strong><span>Elimination</span></div>
          <div><strong>30</strong><span>Identification</span></div>
          <div><strong>130</strong><span>High-yield concepts</span></div>
        </div>
        <div class="actions">
          <button id="startElim" class="primary">Start 100-Item Elimination</button>
          <button id="startFinal" class="secondary">Start Final Round</button>
          <button id="showConcepts" class="ghost">View Concept Coverage</button>
        </div>
        <p class="note">This is a practice bank built around the 10 official scope categories plus standard high-yield subtopics. It is not an official UMak question set.</p>
      </div>
    </section>

    <section id="conceptScreen" class="screen">
      <div class="card">
        <div class="topbar">
          <div>
            <p class="eyebrow">Coverage Map</p>
            <h2>130 high-yield concepts</h2>
          </div>
          <button class="ghost homeBtn">Back</button>
        </div>
        <div id="conceptList" class="concept-list"></div>
      </div>
    </section>

    <section id="elim" class="screen">
      <div class="quiz-header card">
        <div>
          <p class="eyebrow">Elimination Round</p>
          <h2 id="elimProgress">Question 1 of 100</h2>
          <p id="elimCategory" class="muted"></p>
        </div>
        <div class="timer-box">
          <span>TIME LEFT</span>
          <strong id="elimTimer">60:00</strong>
        </div>
      </div>
      <div class="card question-card">
        <h3 id="elimQuestion"></h3>
        <div id="elimOptions" class="options"></div>
        <div class="quiz-nav">
          <button id="elimPrev" class="secondary">Previous</button>
          <button id="elimNext" class="primary">Next</button>
        </div>
      </div>
      <div class="card progress-card">
        <div class="bar"><div id="elimBar"></div></div>
        <p id="answeredCount" class="muted"></p>
        <button id="submitElim" class="danger">Submit Elimination</button>
      </div>
    </section>

    <section id="elimResults" class="screen">
      <div class="card">
        <p class="eyebrow">Elimination Results</p>
        <h2 id="elimScore"></h2>
        <p id="elimTimeUsed" class="muted"></p>
        <div id="categoryAnalytics" class="analytics-grid"></div>
        <div class="actions">
          <button id="reviewElim" class="secondary">Review Missed Questions</button>
          <button id="goFinal" class="primary">Go to Final Round</button>
          <button class="ghost homeBtn">Home</button>
        </div>
      </div>
      <div id="elimReview" class="review-list hidden"></div>
    </section>

    <section id="finalIntro" class="screen">
      <div class="card">
        <p class="eyebrow">Final Round</p>
        <h2>Identification Practice</h2>
        <div class="round-grid">
          <div><strong>Easy</strong><span>10 questions · 15 sec · 3 pts</span></div>
          <div><strong>Average</strong><span>10 questions · 20 sec · 5 pts</span></div>
          <div><strong>Difficult</strong><span>10 questions · 30 sec · 7 pts</span></div>
        </div>
        <p class="note">Type the answer yourself. Answers are checked case-insensitively and accept common equivalent forms.</p>
        <div class="actions">
          <button id="beginFinal" class="primary">Begin Easy Round</button>
          <button class="ghost homeBtn">Home</button>
        </div>
      </div>
    </section>

    <section id="finalQuiz" class="screen">
      <div class="quiz-header card">
        <div>
          <p id="finalLevel" class="eyebrow">Easy</p>
          <h2 id="finalProgress">Question 1 of 10</h2>
          <p id="finalCategory" class="muted"></p>
        </div>
        <div class="timer-box">
          <span>SECONDS</span>
          <strong id="finalTimer">15</strong>
        </div>
      </div>
      <div class="bar final-time"><div id="finalTimeBar"></div></div>
      <div class="card question-card">
        <h3 id="finalPrompt"></h3>
        <form id="finalForm">
          <input id="finalAnswer" type="text" autocomplete="off" placeholder="Type your answer" aria-label="Your answer">
          <button class="primary" type="submit">Submit Answer</button>
        </form>
      </div>
    </section>

    <section id="finalResults" class="screen">
      <div class="card">
        <p class="eyebrow">Final Round Results</p>
        <h2 id="finalScore"></h2>
        <div id="finalBreakdown" class="analytics-grid"></div>
        <div class="actions">
          <button id="reviewFinal" class="secondary">Review Missed Identification</button>
          <button class="ghost homeBtn">Home</button>
        </div>
      </div>
      <div id="finalReview" class="review-list hidden"></div>
    </section>
  </main>
  <script src="script.js"></script>
</body>
</html>
'''

style_css = '''*{box-sizing:border-box}body{margin:0;font-family:Arial,Helvetica,sans-serif;background:#f4f6f8;color:#1f2937}.app-shell{max-width:900px;margin:0 auto;padding:20px}.screen{display:none}.screen.active{display:block}.card{background:#fff;border:1px solid #d9dee5;border-radius:14px;padding:20px;margin-bottom:16px}.hero{padding:26px}.eyebrow{font-size:.78rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:#5b6472;margin:0 0 8px}.lead{font-size:1.05rem;line-height:1.6;color:#4b5563}.muted,.note{color:#687180;line-height:1.5}.note{font-size:.9rem}.stats-grid,.round-grid,.analytics-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px;margin:20px 0}.stats-grid div,.round-grid div,.analytics-grid>div{border:1px solid #d9dee5;border-radius:10px;padding:14px;background:#fafbfc}.stats-grid strong,.round-grid strong{display:block;font-size:1.2rem}.stats-grid span,.round-grid span{display:block;color:#687180;font-size:.9rem;margin-top:4px}.actions{display:flex;gap:10px;flex-wrap:wrap;margin-top:18px}button{border:0;border-radius:9px;padding:12px 16px;font-size:1rem;cursor:pointer;min-height:44px}button:disabled{opacity:.45;cursor:not-allowed}.primary{background:#1f6feb;color:#fff}.secondary{background:#e9eef5;color:#1f2937}.ghost{background:#fff;border:1px solid #cfd6df;color:#374151}.danger{background:#b42318;color:#fff}.topbar,.quiz-header{display:flex;justify-content:space-between;gap:16px;align-items:flex-start}.timer-box{min-width:112px;text-align:center;border:1px solid #d9dee5;border-radius:10px;padding:10px;background:#fafbfc}.timer-box span{display:block;font-size:.7rem;color:#687180}.timer-box strong{font-size:1.7rem}.question-card h3{font-size:1.25rem;line-height:1.5}.options{display:grid;gap:10px;margin-top:18px}.option{width:100%;text-align:left;background:#fff;border:1px solid #cfd6df}.option.selected{border-color:#1f6feb;background:#eef5ff}.quiz-nav{display:flex;justify-content:space-between;gap:10px;margin-top:20px}.progress-card{text-align:center}.bar{height:10px;border-radius:999px;background:#e6eaf0;overflow:hidden}.bar>div{height:100%;width:0;background:#1f6feb;transition:width .2s}.final-time{margin-bottom:16px}.final-time>div{width:100%}.concept-list{display:grid;gap:14px}.concept-group{border:1px solid #d9dee5;border-radius:10px;padding:14px}.concept-group h3{margin:0 0 8px;font-size:1rem}.concept-chips{display:flex;flex-wrap:wrap;gap:7px}.chip{background:#eef2f6;border-radius:999px;padding:6px 9px;font-size:.82rem}.analytics-grid h4{margin:0 0 6px}.analytics-grid p{margin:0;color:#687180}.review-list{display:grid;gap:12px}.review-item{background:#fff;border:1px solid #d9dee5;border-radius:12px;padding:16px}.review-item h4{margin:0 0 8px}.review-item p{margin:6px 0;line-height:1.5}.hidden{display:none!important}input{width:100%;padding:14px;border:1px solid #cfd6df;border-radius:9px;font-size:1rem;margin:16px 0}#finalForm button{width:100%}@media(max-width:640px){.app-shell{padding:12px}.card{padding:16px}.hero{padding:18px}.stats-grid,.round-grid,.analytics-grid{grid-template-columns:1fr}.topbar,.quiz-header{align-items:stretch}.quiz-header{flex-direction:column}.timer-box{align-self:flex-end}.quiz-nav{flex-direction:column}.quiz-nav button,.actions button{width:100%}.question-card h3{font-size:1.08rem}}
'''

script_template = '''const categories = __CATEGORIES__;
const concepts = __CONCEPTS__;
const eliminationQuestions = __MCQ__;
const finalQuestions = __FINALS__;

const screens = [...document.querySelectorAll('.screen')];
function show(id){screens.forEach(s=>s.classList.remove('active'));document.getElementById(id).classList.add('active');window.scrollTo({top:0,behavior:'smooth'});}
function shuffle(arr){const a=[...arr];for(let i=a.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]];}return a;}
function normalize(s){return (s||'').toLowerCase().trim().replace(/[’']/g,"'").replace(/[^a-z0-9+#' -]/g,'').replace(/\s+/g,' ');}

let elimState={questions:[],answers:[],index:0,seconds:3600,timer:null,startSeconds:3600,submitted:false};
let finalState={levels:['easy','average','difficult'],levelIndex:0,index:0,answers:{easy:[],average:[],difficult:[]},seconds:15,timer:null,locked:false};

const $=id=>document.getElementById(id);

document.querySelectorAll('.homeBtn').forEach(b=>b.addEventListener('click',()=>{clearInterval(elimState.timer);clearInterval(finalState.timer);show('home');}));
$('showConcepts').addEventListener('click',()=>{renderConcepts();show('conceptScreen');});
$('startElim').addEventListener('click',startElimination);
$('startFinal').addEventListener('click',()=>show('finalIntro'));
$('beginFinal').addEventListener('click',startFinal);
$('goFinal').addEventListener('click',()=>show('finalIntro'));
$('reviewElim').addEventListener('click',()=>$('elimReview').classList.toggle('hidden'));
$('reviewFinal').addEventListener('click',()=>$('finalReview').classList.toggle('hidden'));
$('elimPrev').addEventListener('click',()=>{if(elimState.index>0){elimState.index--;renderElimQuestion();}});
$('elimNext').addEventListener('click',()=>{if(elimState.index<elimState.questions.length-1){elimState.index++;renderElimQuestion();}});
$('submitElim').addEventListener('click',()=>submitElimination(false));
$('finalForm').addEventListener('submit',e=>{e.preventDefault();submitFinalAnswer(false);});

function renderConcepts(){
  $('conceptList').innerHTML=categories.map(cat=>`<div class="concept-group"><h3>${cat}</h3><div class="concept-chips">${concepts[cat].map(c=>`<span class="chip">${c}</span>`).join('')}</div></div>`).join('');
}

function startElimination(){
  clearInterval(elimState.timer);
  elimState={questions:shuffle(eliminationQuestions).map(q=>({...q,options:q.options.map((t,i)=>({text:t,originalIndex:i}))})),answers:Array(100).fill(null),index:0,seconds:3600,timer:null,startSeconds:3600,submitted:false};
  elimState.questions.forEach(q=>q.options=shuffle(q.options));
  show('elim');
  renderElimQuestion();
  updateElimTimer();
  elimState.timer=setInterval(()=>{elimState.seconds--;updateElimTimer();if(elimState.seconds<=0)submitElimination(true);},1000);
}

function updateElimTimer(){const m=Math.floor(elimState.seconds/60),s=elimState.seconds%60;$('elimTimer').textContent=`${String(m).padStart(2,'0')}:${String(s).padStart(2,'0')}`;}
function renderElimQuestion(){
  const q=elimState.questions[elimState.index];
  $('elimProgress').textContent=`Question ${elimState.index+1} of 100`;
  $('elimCategory').textContent=`${q.category} · ${q.concept}`;
  $('elimQuestion').textContent=q.question;
  $('elimOptions').innerHTML='';
  q.options.forEach((opt,i)=>{const b=document.createElement('button');b.type='button';b.className='option'+(elimState.answers[elimState.index]===i?' selected':'');b.textContent=`${String.fromCharCode(65+i)}. ${opt.text}`;b.addEventListener('click',()=>{elimState.answers[elimState.index]=i;renderElimQuestion();});$('elimOptions').appendChild(b);});
  $('elimPrev').disabled=elimState.index===0;$('elimNext').disabled=elimState.index===99;
  const answered=elimState.answers.filter(v=>v!==null).length;$('answeredCount').textContent=`Answered ${answered}/100`;$('elimBar').style.width=`${answered}%`;
}

function submitElimination(auto){
  if(elimState.submitted)return;
  if(!auto&&!confirm('Submit your 100-item elimination now?'))return;
  elimState.submitted=true;clearInterval(elimState.timer);
  let score=0;const stats={};categories.forEach(c=>stats[c]={correct:0,total:0});const misses=[];
  elimState.questions.forEach((q,i)=>{const chosen=elimState.answers[i];const chosenOriginal=chosen===null?null:q.options[chosen].originalIndex;const ok=chosenOriginal===q.answer;stats[q.category].total++;if(ok){score++;stats[q.category].correct++;}else misses.push({q,chosen:chosen===null?'No answer':q.options[chosen].text,correct:q.options.find(o=>o.originalIndex===q.answer).text});});
  const used=elimState.startSeconds-elimState.seconds;$('elimScore').textContent=`${score}/100 (${score}%)`;$('elimTimeUsed').textContent=`Time used: ${Math.floor(used/60)}m ${used%60}s${auto?' · Time expired':''}`;
  $('categoryAnalytics').innerHTML=categories.map(c=>{const x=stats[c],pct=Math.round(x.correct/x.total*100);return `<div><h4>${c}</h4><p>${x.correct}/${x.total} · ${pct}%</p></div>`;}).join('');
  $('elimReview').innerHTML=misses.length?misses.map((m,i)=>`<div class="review-item"><h4>${m.q.category} · ${m.q.concept}</h4><p><strong>${m.q.question}</strong></p><p>Your answer: ${m.chosen}</p><p>Correct answer: ${m.correct}</p><p>${m.q.explanation}</p></div>`).join(''):'<div class="review-item"><h4>Perfect score</h4><p>No missed questions.</p></div>';
  $('elimReview').classList.add('hidden');show('elimResults');
}

function startFinal(){
  clearInterval(finalState.timer);
  finalState={levels:['easy','average','difficult'],levelIndex:0,index:0,answers:{easy:[],average:[],difficult:[]},seconds:15,timer:null,locked:false,sets:{easy:shuffle(finalQuestions.easy),average:shuffle(finalQuestions.average),difficult:shuffle(finalQuestions.difficult)}};
  show('finalQuiz');renderFinalQuestion();
}
function levelSeconds(level){return level==='easy'?15:level==='average'?20:30;}
function levelPoints(level){return level==='easy'?3:level==='average'?5:7;}
function renderFinalQuestion(){
  clearInterval(finalState.timer);finalState.locked=false;const level=finalState.levels[finalState.levelIndex],set=finalState.sets[level],q=set[finalState.index];finalState.seconds=levelSeconds(level);
  $('finalLevel').textContent=`${level[0].toUpperCase()+level.slice(1)} · ${levelPoints(level)} points`;$('finalProgress').textContent=`Question ${finalState.index+1} of 10`;$('finalCategory').textContent=`${q.category} · ${q.concept}`;$('finalPrompt').textContent=q.prompt;$('finalAnswer').value='';$('finalAnswer').focus();updateFinalTimer();
  finalState.timer=setInterval(()=>{finalState.seconds--;updateFinalTimer();if(finalState.seconds<=0)submitFinalAnswer(true);},1000);
}
function updateFinalTimer(){const level=finalState.levels[finalState.levelIndex],max=levelSeconds(level);$('finalTimer').textContent=finalState.seconds;$('finalTimeBar').style.width=`${Math.max(0,finalState.seconds/max*100)}%`;}
function submitFinalAnswer(timeout){
  if(finalState.locked)return;finalState.locked=true;clearInterval(finalState.timer);const level=finalState.levels[finalState.levelIndex],q=finalState.sets[level][finalState.index],raw=timeout?'':$('finalAnswer').value,answer=normalize(raw);const ok=q.answers.some(a=>normalize(a)===answer);finalState.answers[level].push({q,raw:timeout?'Timed out':raw,ok});
  finalState.index++;if(finalState.index>=10){finalState.levelIndex++;finalState.index=0;if(finalState.levelIndex>=finalState.levels.length){finishFinal();return;}}
  setTimeout(renderFinalQuestion,180);
}
function finishFinal(){
  let total=0,max=0;const breakdown=[];const misses=[];finalState.levels.forEach(level=>{const pts=levelPoints(level),arr=finalState.answers[level],correct=arr.filter(x=>x.ok).length;total+=correct*pts;max+=10*pts;breakdown.push({level,correct,points:correct*pts,max:10*pts});arr.filter(x=>!x.ok).forEach(x=>misses.push({level,...x}));});
  $('finalScore').textContent=`${total}/${max} points`;$('finalBreakdown').innerHTML=breakdown.map(b=>`<div><h4>${b.level[0].toUpperCase()+b.level.slice(1)}</h4><p>${b.correct}/10 correct · ${b.points}/${b.max} pts</p></div>`).join('');
  $('finalReview').innerHTML=misses.length?misses.map(m=>`<div class="review-item"><h4>${m.level.toUpperCase()} · ${m.q.category} · ${m.q.concept}</h4><p><strong>${m.q.prompt}</strong></p><p>Your answer: ${m.raw||'No answer'}</p><p>Accepted answer: ${m.q.answers[0]}</p><p>${m.q.explanation}</p></div>`).join(''):'<div class="review-item"><h4>Perfect final</h4><p>No missed identification questions.</p></div>';$('finalReview').classList.add('hidden');show('finalResults');
}
'''

script_js = script_template.replace('__CATEGORIES__', json.dumps(cats, ensure_ascii=False)).replace('__CONCEPTS__', json.dumps(concepts, ensure_ascii=False)).replace('__MCQ__', json.dumps(mcq, ensure_ascii=False)).replace('__FINALS__', json.dumps(finals, ensure_ascii=False))

base='/mnt/data/it_quiz_bee_app'
open(base+'/index.html','w',encoding='utf-8').write(index_html)
open(base+'/style.css','w',encoding='utf-8').write(style_css)
open(base+'/script.js','w',encoding='utf-8').write(script_js)
open(base+'/README.txt','w',encoding='utf-8').write('IT Quiz Bee Trainer\n\n1. Keep index.html, style.css, and script.js in the same folder.\n2. Double-click index.html to open it in a browser.\n3. Elimination: 100 MCQs, 60 minutes.\n4. Final: 10 Easy (15 sec, 3 pts), 10 Average (20 sec, 5 pts), 10 Difficult (30 sec, 7 pts).\n5. The question bank is practice material based on the official 10 scope categories plus standard high-yield IT subtopics. It is not an official UMak question set.\n')
print('built', len(mcq), {k:len(v) for k,v in finals.items()})
