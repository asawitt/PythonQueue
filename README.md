# PythonQueue
Linked-List backed Queue Implementation for Python challenges

## Installation
-Just use the built-in Queue in python, unless you intend to edit this

-Fastest would be to copy-paste the contents of Queue.py into your code 

-Or you could download Queue.py and throw it in your project directory. Use "from DisjointSet import *" to use it in your code

-You could clone https://github.com/asawitt/PythonQueue/ , move PythonQueue.py to your project directory, then use the above import statement if you really want to. Don't. 

## Usage
### Create a new Queue
q = Queue()
### Add a value to the Queue O(1)
q.push(value)
### Peek O(1)
-Returns the value at the front of the Queue, None if empty

q.peek()
### Remove a value from the front of the queue O(1)
-Returns the value at the front of the Queue

q.pop()

### Finding a value O(n)
-Returns True if the given value is in the Queue, False otherwise

Q.find(value)

### Display the Queue:
q.display()

### Size O(1)
-Returns the number of elements in the Queue

q.size()

### Check if the Queue is empty O(1)
-Returns True if the Queue is empty, False otherwise

q.isEmpty()



## License
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
