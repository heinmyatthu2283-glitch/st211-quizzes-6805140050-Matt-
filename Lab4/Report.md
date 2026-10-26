# Lab 4 Review Questions

## 1. What goes before yield vs after yield in a fixture?

I place setup logic before the `yield` statement in a fixture to prepare test dependencies, initialize resources, or establish initial state prior to test execution. The `yield` statement itself passes the fixture value to the test function, effectively pausing the fixture. Anything I write after the `yield` statement executes as teardown logic after the test completes, allowing me to safely clean up resources, close connections, or restore system state.

## 2. When would you use scope="session" instead of the default?

I use `scope="session"` instead of the default function scope when setting up an expensive resource that needs to be created only once for the entire test run, such as a database connection, a web browser driver instance, or a heavy configuration setup. Reusing a session-scoped fixture across all tests significantly reduces total execution time compared to destroying and recreating the resource for every individual test function.

## 3. Why does a factory fixture return a function instead of an object?

I use a factory fixture to return a function instead of a direct object when I need to create multiple instances of a resource, or when individual tests require customized parameters to instantiate an object. By returning a helper function, I allow each test to invoke the factory with specific arguments on demand, providing flexibility and supporting dynamic object creation while keeping fixture initialization clean and reusable.