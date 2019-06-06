# Python Cheatsheet

##### Note: '~~' is used to provide a `C#` synonym (LHS is `Python`, RHS is `C#`)

* *iterable* ~~ `IEnumerable`
* *range* ~~ `IEnumerable{int}`
* Slicing
    * creates shallow copy (i.e. references are copied, not underlying objects)
    * *notation* = `object[{start index}:{end index (noninclusive)}]`
* `for` ~~ `for`
    * Behind the scenes, `for` calls `iter()` on the collection to get the iterator, which defines the `__next__` method.
* `pass` is no-op
* `raise` ~~ `throw`
* `else`
    * if this is for an `if`-block, then it's pretty standard behavior
    * on a `try`-block, it is executed if there were **no** exceptions raised.
    * on a `for`-loop, it is executed at the end condition, **iff** there was no `break`, `continue` or `return` hit.
* `with` ~~ `using`
* Default values don't have to be compile-time constants, but are bound at point of function definition!
    * e.g. 
        ```python
            i = 5
            def myFunc(arg = i):
                print(arg)
            i = 6
            myFunc() # prints 5, not 6
        ```
* `in` ~~ `IEnumerable{T}.Contains`
    * e.g.
        ```python
            x = input("Please enter the value")
            if x in ('helloworld', 'hello', 'world'):
                print("Hello World")
        ```
* `*`and `**`
    * On the call-site, 
        * `*` can be used to unpack a list/tuple to a function call's arguments. e.g.
            ```python
                def func(a = 1, b = 2):
                    pass
                
                args = [3, 4]
                func(*args)
            ```
        * `**` can be used to unpack a dictionary to a function call's arguments. e.g.
            ```python
                def func(a = 1, b = 2):
                    pass
                
                args = {'a': 3, 'b': 4}
                func(**args)
            ```
    * On the function-definition site,
        * `*` ~~ `params object[]` for variadic args. e.g.
            ```python
                def func(a, *args)
            ```
        * `**` is special variadic args: all the **named**/keyword args that aren't a formal parameter. e.g.
            ```python
                def func(a, **keywordArgs, b = 5):
                    pass
                
                func(6, b = 7, c = "Something", d = "Another thing") # keywordArgs will be a dictionary containing c and d, but not a, b
            ```
* Lambda expressions:
    * Syntactically limited to single expression (so ~~ `=>`)
    * e.g.
        ```python
            from typing import Callable
            def lambdaInput(n: int, arg: Callable[[int], int]) -> int:
                return arg(n) + 5

            lambdaRes = lambdaInput(5, lambda x: x + 5)

            def lambdaOutput(n: int) -> Callable[[str], int]:
                return lambda s: len(s) + n

            lambdaFunc = lambdaOutput(n=5)
            lambdaRes = lambdaFunc("HelloWorld")
        ```
* `deque` - data structure with efficient appendLeft and pop from both ends. 
    ```python
        from collections import deque
        queue = deque(['A', 'B', 'C'])
        queue.append('D')
        queue.popleft() # yields A
    ```
* `map(lambda, iterable)` ~~ `IEnumerable{T}.Select(lambda)`
* `import {module}` ~~ `using {namespace}`
* `dir` lists the exports of a module (e.g. `dir(sys)`)
* `__init__.py` is used to define a directory as a package
    * A package can have subpackages (recursively)
    * Can define `__all__` in the `__init__.py` to determine what to import when `from {package} import *` is used.
    * Within a package, one can use either absolute package identifier or relative paths from current module to reference other submodules or sub-packages.
* JSON serialization/deserialization can be done using the `json` module:
    ```python
        import json
        json.dumps({'Good': 23, 'bye': 42, 'NewtonSoft': 111})
        x = [1, 2, 3, 4, 5]
        json.dump(x, file)
        y = json.load(file)
    ```
* Metaclass - the class of a class. Class definitions incorporate class name, class dictionary (for methods and fields), and base classes. A class is an instance of a metaclass, just like an object is an instance of a class. The default metaclass is `type`.
* `class`:
    * Syntax is:
        ```python
            class BaseClass1:
                pass
            class BaseClass2:
                pass
            class DerivedClass(BaseClass1, BaseClass2):
                staticVar = 'static class field'
                def __init__(self):
                    self.memberVar = 'instance field'
                def method(self):
                    pass
            
            classInstance = DerivedClass()
        ```
    * All methods are effectively **virtual**
    * `isinstance(obj, type)` ~~ `obj is type`
    * `issubclass(t1, t2)` tests if `t1` is a subclass (i.e. derivative) of `t2`
    * `super` let's you avoid referring to the base class explicitly
    * Method Resolution Order (MRO) changes dynamically to support cooperative calls to `super` (*call-next-method* approach)
        * MRO [documentation](https://www.python.org/download/releases/2.3/mro/)
    * While there is **no** support for private fields in Python, prefixing methods/fields with '__' results in name mangling (to become _classname__var):
        ```python
            class C:
                __privateVar = 5 # compiler replaces this with _C__privateVar
        ```
    * Can be equivalent to `struct`:
        ```python
            class Struct:
                pass
            
            s = Struct()
            s.a = 42
            s.b = 'Another field'
        ```
        * Note that this approach can be used more generally by defining `read` and `readline` methods in the `struct`-like class, which parse strings into fields
    * Can implement `__iter__` and `__next__` methods to become an iterable collection
        * Alternatively, and sometimes more advisably, **generator** functions can be used to the same effect without needing to implement the iterator tracking (simply use `yield`). e.g.
            ```python
                def reverse(data):
                    for index in range(len(data) - 1, -1):
                        yield data[index]
                for char in reverse('golf'):
                    print(char)
            ```
* Parallelism:
    * `threading` - contains synchronization primitives (locks, semaphores, `Threading` base class).
        * It is [recommended](https://docs.python.org/3/tutorial/stdlib2.html#multi-threading) to have resources allocated by a single thread, which has a `Queue` that receives requests for those resources from the other threads. This way the concurrency can be designed in a thread-safe manner with simplicity
    * [`asyncio`](https://docs.python.org/3/library/asyncio-task.html)
* [Performance measurements](https://docs.python.org/3/tutorial/stdlib.html#quality-control):
    * `profile`
    * `pstats`
    * `timeit`
* [Logging](https://docs.python.org/3/tutorial/stdlib2.html#logging)
    * `logging`
* [Unit testing](https://docs.python.org/3/tutorial/stdlib.html#quality-control):
    * `doctest` - embeds tests/expected result in the method's docstring, and scans the module to run all such tests
    * `unittest` - more traditional unit-testing module which can be used to implement test classes
* [Garbage collection](https://docs.python.org/3/library/gc.html#module-gc):
    * `gc`
    * `weakref` - allows tracking objects without creating references to them
* [Package management](https://docs.python.org/3/installing/index.html#installing-index) ([seealso](https://code.visualstudio.com/docs/python/python-tutorial#_install-and-use-packages)):
    * In order to prevent cross-pollination of conflicting package dependencies between different Python applications, each application can have a **virtual environment**.
        ```cmd
            > py -3 -m venv <virtual environment folder>
            > <virtual environment folder>\scripts\activate
        ```
    * https://pypi.org - Python Package Index (default location where packages are installed from by `pip`)
    * To install packages:
        ```cmd
            > python -m pip install <package name>
        ```
* `PYTHON_STARTUP` environment variable can be used to point to a file that defines a set of commands to run on startup (*interactive mode only*)
    * `usercustomize` and `sitecustomize` are hooks that can be used to execute code on every invocation of Python (more information [here](https://docs.python.org/3/tutorial/appendix.html#the-customization-modules))