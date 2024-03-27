#  Redis Basic

## Overview
This project was part of a curriculum focused on short specializations in back-end development. Throughout the project, I delved into Redis, a powerful in-memory data structure store often used as a database, cache, or message broker.

## Learning Objectives
During this project, I learned and accomplished the following objectives:
- Utilized Redis for basic operations.
- Implemented Redis as a simple cache.
- Gained proficiency in working with Redis commands and Python Redis client.

## Requirements
Throughout the project, I ensured to meet the following requirements:
- All code was interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7.
- Followed PEP 8 style guide for code formatting.
- Ensured proper documentation for all code components.
- Added type annotations for all functions and methods.
- Installed Redis and its Python client, and properly configured Redis server.

## Setup
To install Redis on Ubuntu 18.04, I followed these steps:
```bash
$ sudo apt-get -y install redis-server
$ pip3 install redis
$ sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf
```
For using Redis in a container, I started the Redis server explicitly:
```bash
$ service redis-server start
```

## Tasks Accomplished
### 0. Writing strings to Redis
- Created a `Cache` class to handle Redis operations.
- Implemented a `store` method to store data in Redis and return a unique key.
- Ensured correct type annotations and documentation.

### 1. Reading from Redis and recovering original type
- Developed a `get` method to retrieve data from Redis.
- Implemented optional conversion using a Callable.
- Created specific methods (`get_str` and `get_int`) for automatic conversion.

### 2. Incrementing values
- Implemented a `count_calls` decorator to count method calls.
- Decorated the `store` method to count its calls.

### 3. Storing lists
- Developed a `call_history` decorator to store input/output history.
- Decorated the `store` method to log its inputs and outputs.

### 4. Retrieving lists
- Developed a `replay` function to display the history of method calls.
- Utilized keys generated in previous tasks to generate the output.


## Conclusion
This project provided valuable hands-on experience in utilizing Redis for various tasks, from basic operations to advanced functionalities like caching and method call tracking. Through completing the tasks, I enhanced my skills in working with Redis and integrating it into Python applications.
