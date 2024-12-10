# Python - Async Comprehension

## Python - Asynchronous Programming Public

### What is Asynchronous Programming?

In traditional synchronous programming, each operation is executed one after the other. If one operation takes time (like fetching data from the internet), the entire program waits and nothing else progresses.

Asynchronous programming allows certain operations to be executed in the “background”, freeing up the main program to continue running. This is especially useful for I/O-bound operations like network requests, file operations, etc.

### The Event Loop

The heart of asynchronous programming in Python is the “event loop”. Think of it as a constantly running loop that checks if there are any tasks to run. If there are tasks, it runs them; if not, it keeps looping.

Tasks can be scheduled to run on the event loop, and the loop will execute them when it can. The event loop can handle many tasks by quickly switching between them, giving the illusion that they’re running at the same time.

### Async/Await

async and await are keywords introduced in Python to make asynchronous programming more readable and straightforward.

- async defines an asynchronous function. This function doesn’t run immediately; instead, it returns a coroutine object.
- await is used to call an asynchronous function and wait for it to complete.

###Simple Example:

Let’s say we want to simulate a function that waits for a while:
```
import asyncio

async def say_after(delay, msg):
    await asyncio.sleep(delay)
    print(msg)

# Running the asynchronous function
async def main():
    print("Started")
    await say_after(1, "Hello")
    await say_after(2, "World")
    print("Finished")

# Python 3.7+
asyncio.run(main())
```
In this example:

1. `say_after` is an asynchronous function because of the `async` keyword.
2. Inside `say_after`, we use `await` to pause the function for a specified `delay`. During this pause, the event loop can do other things.
3. In the `main` function, we call `say_after` twice. The second call won’t start until the first one is finished because of the `await` keyword.
4. `asyncio.run(main())` is used to run the main coroutine and start the event loop.

### How does this differ from synchronous code?

If this were synchronous code, the entire program would stop during the sleep calls. But with async/await, other tasks could run during those pauses.

### More Complex Example: Running Tasks Concurrently

What if we want both messages to print after waiting for 3 seconds, without waiting for the first task to complete?
```
async def main():
    task1 = asyncio.create_task(say_after(1, "Hello"))
    task2 = asyncio.create_task(say_after(2, "World"))

    print("Started")

    # Wait until both tasks are completed
    await task1
    await task2

    print("Finished")

asyncio.run(main())
```
Here, `asyncio.create_task()` schedules the coroutines to run on the event loop, but doesn’t wait for them to complete. Both `say_after` calls run “concurrently”, making the program faster.

### In Summary:

- Asynchronous programming allows multiple tasks to run seemingly in parallel, making efficient use of resources.
- The event loop is the core of this mechanism, constantly checking and running tasks as they’re scheduled.
- `async/await` provides a readable way to write asynchronous code in Python.

Remember, `async/await` is best suited for I/O-bound and high-level structured network code, not for CPU-bound tasks. For CPU-bound tasks, you might want to look into multi-threading or multi-processing in Python.


## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

- How to write an asynchronous generator
- How to use async comprehensions
- How to type-annotate generators


## Requirements
### General
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.9)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/env python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle style (version 2.5.x)
- The length of your files will be tested using wc
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your functions should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)'
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
- All your functions and coroutines must be type-annotated.


