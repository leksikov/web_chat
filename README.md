
# REST Web chat with aiohttp and aioredis

Web chat application with aiohttp which utilises co-routines.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites
- Docker


### Installing


1. clone repository
2. At redis-container/:
	1. docker build 	-t redis .
	2. docker run -it --rm  -p 6379:6379 redis
3. At project root directory:
	1. docker build -t webchat .
	2. docker run --rm -it -p 8080:8080 -t webchat


## Usage

1. Open browser
2. enter: http://localhost:8080
3. Enter user name

## File descriptions:
1. server.py: Contans server logic and routes. Insert and retrieves data
2. static/index.html: Contains login input form for the chatroom
3. chatroom.html: Displays current user, all users in chatroom, sending and display all messages.

## Built With

* [Docker](http://www.docker.com/) - Contrainer engine
## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.


## Authors

* **Sergey Leksikov** - *author* 
See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

