# memoize

Once carrying out, cash is done.

## Example

```python
from memoize import Mem
import time

class A(object):
    @Mem.memoize
    def foo(self):
        sum = 0
        for i in xrange(1, 100000000):
            sum += i
        return sum

a = A()

start = time.time()
print a.foo()                         # 4999999950000000
print round(time.time() - start, 2)   # 3.67

start = time.time()
print a.foo()                         # 4999999950000000 
print round(time.time() - start, 2)   # 0.0
```
