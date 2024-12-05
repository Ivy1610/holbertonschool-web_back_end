# Python - Async
Coroutines and the async/await syntax in Python are used to write asynchronous code that can perform tasks concurrently without the need for threads or processes. This is particularly useful for I/O-bound tasks, like web requests or database queries, where you’d otherwise be waiting for a response and wasting CPU cycles and where traditional threading or multiprocessing might be overkill or introduce unnecessary complexity.

Basic Concepts:
Coroutine: A coroutine is a special type of function that can pause its execution and yield control back to the event loop, allowing other tasks to run. It can later resume from where it left off.

Event Loop: The event loop is the core of every asyncio application. It schedules and executes tasks and callbacks, manages I/O operations, and handles events.

async: This keyword is used to define a coroutine. For example, async def foo(): pass defines a coroutine named foo.

await: This keyword is used inside an async function to call another async function and wait for its result. It essentially yields control back to the event loop.

Basic Example:
```
import asyncio

async def say_hello():
    await asyncio.sleep(1)
    print("Hello")

async def say_world():
    await asyncio.sleep(1)
    print("World")

async def main():
    await say_hello()
    await say_world()

asyncio.run(main())
```

In this example, the main coroutine calls say_hello and then say_world. Each of these coroutines sleeps for 1 second using asyncio.sleep (an asynchronous sleep) and then prints a message. The program will take 2 seconds to complete because the coroutines are awaited one after the other.

## Resources

### Read or watch:

- Async IO in Python: A Complete Walkthrough
- asyncio - Asynchronous I/O
- random.uniform

### Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

- async and await syntax
- How to execute an async program with asyncio
- How to run concurrent coroutines
- How to create asyncio tasks
- How to use the random module

## Requirements

### General

- A README.md file, at the root of the folder of the project, is mandatory
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.9)
- All your files should end with a new line
- All your files must be executable
 The length of your files will be tested using wc
- The first line of all your files should be exactly #!/usr/bin/env python3
- Your code should use the pycodestyle style (version 2.5.x)
- All your functions and coroutines must be type-annotated.
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your functions should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)'
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
Tasks
