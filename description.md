<p><strong>Due: Thursday, November 18th @ 8:00p ET</strong></p>
<p><em>This is not a team project. Do not copy someone else&rsquo;s work.</em></p>
<h2>Assignment Overview</h2>
<p>Hash Tables are a very powerful data structure that are best known for their ability to insert, delete, and lookup in O(1) time. This allows them to be very powerful in storing data that needs to be accessed quickly. Other data structures we have explored, such as Linked Lists (O(n) lookup and deletion) and AVL Trees (log(n) lookup, insertion, and deletion) lack that O(1) ability accross the board.&nbsp;</p>
<p><a href="https://camo.githubusercontent.com/5e35ecf4bbb89894faaff0d49f680a4727629ff2783c1dd99df70bfca52b12f2/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f6d696d6972706c6174666f726d2e70726f64756374696f6e2f66696c65732f65356233393530322d666364342d346565652d396136622d6536316361303332373131342f686173687461626c65732e504e47" target="_blank" rel="noopener noreferrer"><img src="https://camo.githubusercontent.com/5e35ecf4bbb89894faaff0d49f680a4727629ff2783c1dd99df70bfca52b12f2/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f6d696d6972706c6174666f726d2e70726f64756374696f6e2f66696c65732f65356233393530322d666364342d346565652d396136622d6536316361303332373131342f686173687461626c65732e504e47" alt="hashtables.PNG" /></a></p>
<p>A lot of you may already be familiar with the concept of hash tables, as they are implemented in Python as dictionaries and C++ as unordered maps.</p>
<p>In this project, you will be implementing a Hash Table from scratch in Python and applying it to an application problem.</p>
<h2>Assignment Notes</h2>
<ol>
<li><em><strong>The use of a Python dictionary or set results in a grade of 0 for the project!</strong></em>&nbsp;</li>
<li>In addition,<strong>the only python container/collection type you can use is the built in list class</strong>&nbsp;(no linked lists, queues, etc.)</li>
<li>We are going to have you use many of pythons built in "magic methods" in this project.&nbsp;<strong>A&nbsp;<em>magic method</em>&nbsp;is one that has the two underscores</strong>&nbsp;on the front and the back, such as __len__. In this project,&nbsp;<em><strong>these "magic methods" won't be doing much, they will call the other protected methods that you write!</strong></em>&nbsp;Seriously they should not be more than a few lines.</li>
<li>So, what are "protected methods"?&nbsp;<strong><em>Protected methods</em>&nbsp;are methods prefaced with a single underscore, such as a function called "_insert".</strong>&nbsp;Protected methods are meant to&nbsp;<strong>only be called inside other functions in the class</strong>. This is Pythons way of implementing the C++ equivilant of "public" and "private" - protected methods meant to be treated as private!</li>
<li>Building on the above point,&nbsp;<strong>all attributes/functions that are protected</strong>&nbsp;<strong>(that is, leading with an underscore)&nbsp;<em>should not be called outside of your class</em></strong>, which means they should not be accessed in your application problem!</li>
<li><em><strong>Use of _hash(), _insert(), _delete(), _get(), and _grow() is STRICTLY FORBIDDEN in the application!!! This will result in a 10 point deduction.</strong></em></li>
<li><em><strong>Calling magic methods with the syntax table.__len__() instead of len( table), or the equivalent special syntax for other magic methods, will result in a 2 point deduction each time this is done up to 10 total points.</strong></em></li>
<li>We have very small test cases for the _insert(), _get(), and _delete() functions. The purpose is to make sure you split the work between the magic and hidden methods appropriately. The majority of the testing will take place in the magic method implementations!</li>
<li>If you inspect _hash_1 and _hash_2 you will see that they depend on the size of the string. For the purposes of this assignment, treat these as taking O(1) (constant) time.</li>
<li>A few guarentees:
<ol>
<li>Capacity will not grow past ~1000</li>
<li>All keys will be of type string</li>
</ol>
</li>
</ol>
<p>Here is an table that shows how private methods and magic methods relate to each other:</p>
<p><a href="https://camo.githubusercontent.com/232e0ba5f6fb12eb66f09ee22c12baf1c45c1b5864ce4b612121240b2759b798/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f6d696d6972706c6174666f726d2e70726f64756374696f6e2f66696c65732f37323231366138642d353235652d346332372d393065302d3761376632646630366237322f6d616769632e504e47" target="_blank" rel="noopener noreferrer"><img src="https://camo.githubusercontent.com/232e0ba5f6fb12eb66f09ee22c12baf1c45c1b5864ce4b612121240b2759b798/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f6d696d6972706c6174666f726d2e70726f64756374696f6e2f66696c65732f37323231366138642d353235652d346332372d393065302d3761376632646630366237322f6d616769632e504e47" alt="magic.PNG" /></a></p>
<h2>Assignment Specifications</h2>
<h4>class HashNode:</h4>
<p><em>DO NOT MODIFY the following attributes/functions</em></p>
<ul>
<li><strong>Attributes</strong>
<ul>
<li><strong>key: str:</strong>&nbsp;The key of the hash node (this is what is used in hashing)</li>
<li><strong>value: T:</strong>&nbsp;Value being held in the node. Note that this may be any type, such as a&nbsp;<code>str</code>,&nbsp;<code>int</code>,&nbsp;<code>float</code>,&nbsp;<code>dict</code>, or a more complex object.</li>
<li><strong>deleted: bool:</strong>&nbsp;Whether or not the node has been deleted.</li>
</ul>
</li>
<li><strong>__init__(self, key: str, value: T, deleted: bool = False) -&gt; None</strong>
<ul>
<li>Constructs a hash node.</li>
<li><strong>key: str:</strong>&nbsp;The key of the hash node.</li>
<li><strong>value: T:</strong>&nbsp;Value being held in the node.</li>
<li><strong>deleted: bool:</strong>&nbsp;Whether or not the node has been deleted. Defaults to false.</li>
<li><strong>Returns:</strong>&nbsp;<code>None</code>.</li>
</ul>
</li>
<li><strong>__str__(self) -&gt; str</strong>&nbsp;and&nbsp;<strong>__repr__(self) -&gt; str</strong>
<ul>
<li>Represents the&nbsp;<code>Node</code>&nbsp;as a string.</li>
<li><strong>Returns:</strong>&nbsp;<code>str</code>&nbsp;representation of node</li>
</ul>
</li>
<li><strong>__eq__(self, other: HashNode) -&gt; bool</strong>
<ul>
<li>Compares to see if two hash nodes are equal</li>
<li><strong>other: HashNode:</strong>&nbsp;The HashNode we are comparing against</li>
<li><strong>Returns:</strong>&nbsp;<code>bool&nbsp;</code>stating whether or not they are equal</li>
</ul>
</li>
<li><strong>__iadd__(self, other: T) -&gt; bool</strong>
<ul>
<li>Adds to the value of the current HashNode</li>
<li><strong>other: T:</strong>&nbsp;The value we are adding to our current value</li>
<li><strong>Returns:</strong>&nbsp;<code>None</code></li>
</ul>
</li>
</ul>
<h4>class HashTable:</h4>
<p><em>DO NOT MODIFY the following attributes/functions</em></p>
<ul>
<li><strong>Attributes</strong>&nbsp;(you may edit the values of attributes but do not remove them)
<ul>
<li><strong>capacity: int:</strong>&nbsp;Capacity of the hash table.</li>
<li><strong>size: int:</strong>&nbsp;Current number of nodes in the hash table.</li>
<li><strong>table: List:</strong>&nbsp;This is where the actual data for our hash table is stored</li>
<li><strong>prime_index: int:</strong>&nbsp;Current index of the prime numbers we are using in _hash_2()</li>
</ul>
</li>
<li><strong>primes</strong>
<ul>
<li>This is a list of all the prime numbers, from 2 until 1000, used for _hash_2(). This is a&nbsp;<em><strong>class attribute</strong></em>, so it is&nbsp;<strong>accesed by HashTable.primes, NOT self.primes()!</strong></li>
</ul>
</li>
<li><strong>__init__(self, capacity: int = 8) -&gt; None</strong>
<ul>
<li>Construct an empty hash table, with the capacity as specified in the input</li>
<li>capacity: int:&nbsp;</li>
<li><strong>Returns:</strong>&nbsp;<code>None</code>.</li>
</ul>
</li>
<li><strong>__str__(self) -&gt; str</strong>&nbsp;and&nbsp;<strong>__repr__(self) -&gt; str</strong>
<ul>
<li>Represents the&nbsp;<code>HashTable</code>&nbsp;as a string.</li>
<li><strong>Returns:</strong>&nbsp;<code>str</code>.</li>
</ul>
</li>
<li><strong>__eq__(self, other: HashTable) -&gt; bool</strong>
<ul>
<li>Checks if two HashTables are equal</li>
<li><strong>other: HashTable:</strong>&nbsp;the hashtable we are comparing against</li>
<li><strong>Returns</strong>:&nbsp;<code>bool&nbsp;</code>stating whether or not they are equal</li>
</ul>
</li>
<li><strong>_hash_1(self, key: str) -&gt; int</strong>
<ul>
<li>The first of the two hash functions used to turn a key into a bin number</li>
<li>Assume this is O(1) time/space complexity</li>
<li><strong>key: str:</strong>&nbsp;key we are hashing</li>
<li><strong>Returns:</strong>&nbsp;int that is the bin number</li>
</ul>
</li>
<li><strong>_hash_2(self, key: str) -&gt; in</strong>t
<ul>
<li>The second of the two hash functions used to turn a key into a bin number. This hash function acts as the tie breaker.</li>
<li>Assume this is O(1) time/space complexity</li>
<li><strong>key: str</strong>: key we are hashing</li>
<li><strong>Returns:</strong>&nbsp;int that is the bin number</li>
</ul>
</li>
</ul>
<p><em>IMPLEMENT the following functions</em></p>
<ul>
<li><strong>__len__(self) -&gt; int</strong>
<ul>
<li>Getter for the size (that, is, the number of elements) in the HashTable</li>
<li><em>Time Complexity: O(1)</em></li>
<li><em>Space Complexity: O(1)</em></li>
<li><strong>Returns:</strong>&nbsp;int that is size of hash table</li>
</ul>
</li>
<li><strong>__setitem__(self, key: str, value: T) -&gt; None</strong>
<ul>
<li>Sets the value with an associated key in the HashTable
<ul>
<li><em><strong>This should be a short, ~1 line function</strong></em>- the majority of the work should be done in the _insert() method!</li>
</ul>
</li>
<li><em>Time Complexity: O(1)*</em></li>
<li><em>Space Complexity: O(1)*</em></li>
<li><strong>key: str:</strong> The key we are hashing</li>
<li><strong>value: T:</strong> The associated value we are storing</li>
<li><strong>Returns:</strong>&nbsp;None</li>
</ul>
</li>
<li><strong>__getitem__(self, key: str) -&gt; T</strong>
<ul>
<li>Looks up the value with an associated key in the HashTable
<ul>
<li>**If the key does not exist in the table, raise a&nbsp;<em>KeyError</em>&nbsp;**</li>
<li><em><strong>This should be a short, ~3 line function</strong></em>- the majority of the work should be done in the _get() method!</li>
</ul>
</li>
<li><em>Time Complexity: O(1)*</em></li>
<li><em>Space Complexity: O(1)</em></li>
<li><strong>key: str:</strong> The key we are seraching for the associated value of</li>
<li><strong>Returns:</strong>&nbsp;The value with an associated Key</li>
</ul>
</li>
<li><strong>__delitem__(self, key: str) -&gt; None</strong>
<ul>
<li>Deletes the value with an associated key in the HashTable
<ul>
<li>**If the key does not exist in the table, raise a&nbsp;<em>KeyError</em>&nbsp;**</li>
<li><em><strong>This should be a short, ~3 line function</strong></em>- the majority of the work should be done in the _get() and _delete() methods!</li>
</ul>
</li>
<li><em>Time Complexity: O(1)*</em></li>
<li><em>Space Complexity: O(1)</em></li>
<li><strong>key: str:</strong> The key we are deleting the associated value of</li>
<li><strong>Returns:</strong>&nbsp;None</li>
</ul>
</li>
<li><strong>__contains__(self, key: str) -&gt; bool</strong>
<ul>
<li>Determines if a node with the key denoted by the parameter exists in the table
<ul>
<li><em><strong>This should be a short, ~3 line function</strong></em>- the majority of the work should be done in the _get() method!</li>
</ul>
</li>
<li><em>Time Complexity: O(1)*</em></li>
<li><em>Space Complexity: O(1)</em></li>
<li><strong>key: str:</strong> The key we are checking to be a part of the hash table</li>
<li><strong>Returns:</strong>&nbsp;None</li>
</ul>
</li>
<li><strong>_hash(self, key: str, inserting: bool = False) -&gt; int</strong>\
<ul>
<li>Given a key string return an index in the hash table.</li>
<li>Should implement probing with double hashing.\
<ul>
<li>If the key exists in the hash table, return the index of the existing HashNode</li>
<li>If the key does not exist in the hash table, return the index of the next available empty position in the hash table.
<ul>
<li>Collision resolution should implement double hashing with hash1 as the initial hash and hash2 as the step size</li>
</ul>
</li>
<li>Note - There are 2 possibilities when hashing for an index:
<ul>
<li>When inserting a node into the hash table we want to insert into the next available bin. \</li>
<li>When performing a lookup/deletion in the hash table we want to continue until we either find the proper HashNode or until we reach a bin that has never held a value. This is to preserve the collison resolution methodology.</li>
<li>The inserting parameter should be used to differentiate between these two cases.</li>
</ul>
</li>
</ul>
</li>
<li><em>Time Complexity: O(1)*</em></li>
<li><em>Space Complexity: O(1)</em></li>
<li><strong>key: str:</strong>&nbsp;The key being used in our hash function</li>
<li><strong>inserting: bool:</strong>&nbsp;Whether or not we are doing an insertion. Important for the reasons described above.</li>
<li><strong>Returns:</strong>&nbsp;int that is the bin we hashed into</li>
</ul>
</li>
<li><strong>_insert(self, key: str, value: T) -&gt; None</strong>
<ul>
<li>Use the key and value parameters to add a HashNode to the hash table.\
<ul>
<li>If the key exists, overwrite the existing value</li>
<li>In the event that inserting causes the table to have a load factor of 0.5 or greater you must grow the table to double the existing capacity. This should use the _grow method.</li>
</ul>
</li>
<li><em>Time Complexity: O(1)*</em></li>
<li><em>Space Complexity: O(1)*</em></li>
<li><strong>key: str: </strong>The key associated with the value we are storing</li>
<li><strong>value: T: </strong>The associated value we are storing</li>
<li><strong>Returns:</strong>&nbsp;None</li>
</ul>
</li>
<li><strong>_get(self, key: str) -&gt; HashNode</strong>
<ul>
<li>Find the HashNode with the given key in the hash table.\
<ul>
<li>If the element does not exist, return None</li>
</ul>
</li>
<li><em>Time Complexity: O(1)*</em></li>
<li><em>Space Complexity: O(1)</em></li>
<li><strong>key: str:</strong> The key we looking up</li>
<li><strong>Returns:</strong>&nbsp;HashNode with the key we looked up</li>
</ul>
</li>
<li><strong>_delete(self, key: str) -&gt; None</strong>
<ul>
<li>Removes the HashNode with the given key from the hash table .
<ul>
<li>If the node is found assign its key and value to None, and set the deleted flag to True</li>
</ul>
</li>
<li><em>Time Complexity: O(1)*</em></li>
<li><em>Space Complexity: O(1)</em></li>
<li><strong>key: str:</strong> The key of the Node we are looking to delete</li>
<li><strong>Returns:</strong>&nbsp;None</li>
</ul>
</li>
<li><strong>_grow(self) -&gt; None</strong>
<ul>
<li>Double the capacity of the existing hash table.
<ul>
<li>Do&nbsp;<strong>NOT</strong>rehash deleted HashNodes</li>
<li>Must update self.prime_index, the value of self.prime_index should be the&nbsp;<strong>index</strong>&nbsp;of the largest prime&nbsp;<strong>smaller</strong>&nbsp;than self.capacity in the HashTable.primes tuple.\</li>
</ul>
</li>
<li><em>Time Complexity: O(N)</em></li>
<li><em>Space Complexity: O(N)</em></li>
<li><strong>Returns:</strong>&nbsp;None</li>
</ul>
</li>
<li><strong>update(self, pairs: List[Tuple[str, T]] = []) -&gt; None</strong>
<ul>
<li>Updates the hash table using an iterable of key value pairs
<ul>
<li>If the value already exists, update it, otherwise enter it into the table\</li>
</ul>
</li>
<li><em>Time Complexity: O(M)*, where M is length of pairs</em></li>
<li><em>Space Complexity: O(M)</em></li>
<li><strong>pairs:</strong> <strong>List[Tuple[str, T]]: </strong>list of tuples (key, value) being updated</li>
<li><strong>Returns:</strong>&nbsp;None</li>
</ul>
</li>
<li><strong>keys(self) -&gt; List[str]</strong>
<ul>
<li>Makes a list that contains all of the keys in the table
<ul>
<li>Order does not matter!</li>
</ul>
</li>
<li><em>Time Complexity: O(N)*</em></li>
<li><em>Space Complexity: O(N)</em></li>
<li><strong>Returns:</strong>&nbsp;List of the keys</li>
</ul>
</li>
<li><strong>values(self) -&gt; List[T]</strong>
<ul>
<li>Makes a list that contains all of the values in the table
<ul>
<li>Order does not matter!</li>
</ul>
</li>
<li><em>Time Complexity: O(N)*</em></li>
<li><em>Space Complexity: O(N)</em></li>
<li><strong>Returns:</strong>&nbsp;List of the values</li>
</ul>
</li>
<li><strong>items(self) -&gt; List[Tuple[str,T]]</strong>
<ul>
<li>Makes a list that contains all of the key value pairs in the table
<ul>
<li>Order does not matter!</li>
</ul>
</li>
<li><em>Time Complexity: O(N)*</em></li>
<li><em>Space Complexity: O(N)</em></li>
<li><strong>Returns:</strong>&nbsp;List of Tuples of the form (key, value)</li>
</ul>
</li>
<li><strong>clear(self) -&gt; None</strong>
<ul>
<li>Should clear the table of HashNodes completely, in essence a reset of the table
<ul>
<li>Should not modify capacity</li>
<li><strong>Notice the O(1) space complexity -&nbsp;<em>this must be done in place!</em></strong></li>
</ul>
</li>
<li><em>Time Complexity: O(N)</em></li>
<li><em>Space Complexity: O(1)</em></li>
<li><strong>Returns:</strong>&nbsp;None</li>
</ul>
</li>
</ul>
<p>*<em>Expected Complexity</em></p>
<h2>Application: Detecting Duplicate Network Packets</h2>
<p>You work for a unicorn startup with a subscription service which purchases gourmet meals from the finest restaurants in the world, cuts them up into portions for your pets, flies them in by private jet, and conveniently delivers them straight to your door three times a day for only $25.99 per month.</p>
<p>Specifically, you work on the service that signs customers up for recurring billing when they create an account. Each time a new customer is signed up, the signup service sends a message to your service over the network, and will resend this message periodically until a confirmation is received to make sure no one gets access to this premium service without being charged.</p>
<p>One day, you get a message from your boss. The accounting department has determined that many customers are being billed twice or more each month. With your company quickly burning through its Series J funding round, and the customers unable to notice this amongst the charges for all of their other subscription services, everyone is quite pleased about your double billing feature and you are getting a bonus stock grant. Not having taken CSE 300, and looking forward to the upcoming IPO, this whole situation seems pretty good and you're pretty happy about it.</p>
<p>To refine this feature and boost the double-billing rate, you investigate and find that the confirmation message from the signup service to your service is often getting lost, resulting in your billing service receiving several messages to sign up the same customers for recurring charges. You think back to your time in 331 and get curious about how you might efficiently prevent this situation if you actually wanted to, and decide to write up a solution just for fun.</p>
<p><strong>For your application problem, you will create a class called&nbsp;<code>ExecuteOnlyOnce</code></strong></p>
<p>Its constructor takes one parameter,&nbsp;<code>max_time</code>, whose purpose is explained below, you will need to modify this constructor to set up the class with whatever data structures you need.</p>
<p>When the method,&nbsp;<code>handle_request</code>&nbsp;is called with a timestamp, client ID and request ID, you must respond with</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 0 if the request has not been seen before from this client,</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; or otherwise respond with the number of times the request has been seen before from this client.</p>
<p>If the first time some message was seen is more than&nbsp;<code>max_time</code>&nbsp;time units in the past ( assume&nbsp;<code>max_time</code>&nbsp;and the time argument are in the same units), treat it as unseen and reset the count for the number of times it has been seen. This is because IDs might be reused eventually after enough time goes by.</p>
<p>Guarantees:</p>
<ul>
<li>Requests will be sent to your function in order of timestamp. Your&nbsp;<code>handle_request</code>&nbsp;method will never be called on the same object with an earlier timestamp than what has already been passed to that method of that object.</li>
<li>If you receive two requests from the same client with the same ID within&nbsp;<code>max_time</code>&nbsp;of each other, they will always be repeated attempts for the same request. If two requests from the same client with the same ID show up more than&nbsp;<code>max_time</code>&nbsp;apart they will always be unique requests where the ID had to be reused.</li>
<li>Both the&nbsp;<code>client_id</code>&nbsp;and&nbsp;<code>request_id</code>&nbsp;are comprised of only alphanumeric characters.</li>
</ul>
<p>&nbsp;</p>
<p><strong>Illustration</strong><br /><img src="https://s3.amazonaws.com/mimirplatform.production/files/7a120d4f-cc27-473f-9dd1-5bd0e92d9d10/image.png" alt="image.png" width="382" height="344" /></p>
<p>As the image shows, requests with a request ID and client ID are sent from the client, and these will be assigned a timestamp when received. Since the acknowledgment message may never be received by the client, in this case the signup service, the same request may be sent more than once and received by the server repeatedly. The server attempts to let the client know how many times the request was received so the client can adapt to the network conditions by retrying more or less aggressively.</p>
<p><strong>Examples</strong></p>
<p>Example 1</p>
<div class="snippet-clipboard-content position-relative overflow-auto">
<pre><code>handler = Execute_only_once(max_time=5)

handler.handle_request(0, "A", "A") # Returns 0
handler.handle_request(1, "A", "A") # Returns 1
handler.handle_request(2, "A", "A") # Returns 2

handler.handle_request(12, "A", "A") # Returns 0, because max time exceeded since first request.
</code></pre>
</div>
<p>Example 2</p>
<div class="snippet-clipboard-content position-relative overflow-auto">
<pre><code>handler = ExecuteOnlyOnce(max_time=4)

handler.handle_request(0, "A", "A") # Returns 0
handler.handle_request(1, "B", "B") # Returns 0
handler.handle_request(2, "A", "A") # Returns 1
handler.handle_request(3, "B", "B") # Returns 1

handler.handle_request(15, "B", "B") # Returns 0, due to max_time being exceeded since first request.
</code></pre>
</div>
<p>Example 3</p>
<div class="snippet-clipboard-content position-relative overflow-auto">
<pre><code>handler = ExecuteOnlyOnce(max_time=6)

handler.handle_request(0, "A", "A") # Returns  0
handler.handle_request(0, "B", "A") # Returns  0
handler.handle_request(1, "A", "B") # Returns  0
handler.handle_request(2, "A", "B") # Returns  1
handler.handle_request(2, "A", "B") # Returns  2
handler.handle_request(3, "B", "A") # Returns  1

# Returns 2, stops being the same request when *more than* max_time has gone by
handler.handle_request(6, "A", "A")
handler.handle_request(7, "A", "B") # Returns  3

handler.handle_request(13, "A", "A") # Returns 0
</code></pre>
</div>
<p><strong>class ExecuteOnlyOnce:</strong></p>
<ul>
<li><strong>__init__(self, max_time: int):</strong>
<ul>
<li><strong>Design your data structure here, and make sure to store max_time</strong></li>
</ul>
</li>
<li><strong>handle_request(time: int, id: str) -&gt; int:</strong>
<ul>
<li>Return the number of times this request has been seen already</li>
<li>If the first time the request was seen was more than&nbsp;<code>max_time</code>&nbsp;ago, treat it as unseen and treat this as the first time you have seen it.</li>
<li><em>Time complexity: O(1)</em></li>
<li>The total space complexity of the class should be O(n) where n is the number of times&nbsp;<code>handle_request</code>&nbsp;has been called.</li>
</ul>
</li>
</ul>
<p>REMEMBER THAT HASHTABLE VALUES CAN BE ANY TYPE<br /><em><strong>Use of _hash(), _insert(), _delete(), _get(), and _grow() is STRICTLY FORBIDDEN in the application!!!</strong></em></p>
<h2>Submission</h2>
<h4>Deliverables</h4>
<p>Be sure to upload the following deliverables in a .zip folder to Mimir by 8pm ET on Thursday, November 18th.</p>
<div class="snippet-clipboard-content position-relative overflow-auto">
<pre><code>Project4.zip
    |&mdash; Project4/
        |&mdash; README.xml      (for project feedback)
        |&mdash; __init__.py     (for proper Mimir testcase loading)
        |&mdash; hashtable.py    (contains your solution source code)
</code></pre>
</div>
<h4>Grading</h4>
<ul>
<li>Tests (70)
<ul>
<li>Coding Standard: __/5</li>
<li>README.xml Validity Check: __/5</li>
<li>hashtable: __/45
<ul>
<li>_hash: __/7</li>
<li>_insert: __/1</li>
<li>_get: __/1</li>
<li>_delete: __/1</li>
<li>__len__: __/1</li>
<li>__setitem__: __/4</li>
<li>__getitem__: __/4</li>
<li>__delitem__: __/4</li>
<li>__contains__: __/3</li>
<li>update: __/3</li>
<li>keys/values/items: __/6</li>
<li>clear: __/2</li>
<li>comprehensive: __/8</li>
</ul>
</li>
<li>ExecuteOnlyOnce: __/15
<ul>
<li>Application Basic: 5</li>
<li>Application Comprehensive: 10</li>
</ul>
</li>
</ul>
</li>
<li>Manual (30)
<ul>
<li>Manual (30)
<ul>
<li>Time and space complexity points are <strong>all-or-nothing</strong> for each function. If you fail to meet time <strong>or&nbsp;</strong>space complexity in a given function, you do not receive manual points for that function.</li>
<li>&nbsp;Up to 3 points deduction for missing docstrings across the full project</li>
</ul>
&nbsp;</li>
<li>hashtable time/space: __/24
<ul>
<li>_hash: __/3</li>
<li>__len__: __/1</li>
<li>__setitem__: __/3</li>
<li>__getitem__: __/3</li>
<li>__delitem__: __/3</li>
<li>__contains__: __/2</li>
<li>_grow: __/3</li>
<li>update: __/2</li>
<li>keys/values/items: __/2</li>
<li>clear: __/2</li>
</ul>
</li>
<li>ExecuteOnlyOnce time/space: __/6</li>
</ul>
</li>
</ul>
<h2>Appendix</h2>
<h4>Authors</h4>
<p>Project developed by Alex Woodring, Joseph Pallipadan, and Zach Matson.</p>
<p>Adapted from the work of Brandon Field, Yash Vesikar, Ian Barber, and Max Huang.</p>