
# Booking system

This is a FastApi, MongoDB and Redis application




## Authors

- [@danialhedaiat](https://github.com/danialhedaiat)


## API Reference

### Seats

#### Swagger

```http
  GET /docs
```


#### Get all seats

```http
  GET /seat/all
```

#### Create seat

```http
  POST /seat/create
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `seat_id`      | `int` | **Required**. Id of seat  |
| `user_id`      | `int` | Id of user, **default** is 'None'   |
| `status`      | `string` | status of seat, **default** is 'available' |

#### Update seat

```http
  POST /seat/update
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `seat_id`      | `int` | **Required**. Id of seat  |
| `user_id`      | `int` | **Required**. Id of user,   |

#### delete seat

```http
  POST /seat/delete
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `seat_id`      | `int` | **Required**. Id of seat  |

### Booking
#### booking seat

```http
  POST /bookSeat
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `seat_id`      | `int` | **Required**. Id of seat  |
| `user_id`      | `int` | **Required**. Id of user  |
| `name`      | `string` | **Required**. name of customer |
| `date`      | `datetime` | **Required**. datetime of you want to book a seat |


#### reserve seat

```http
  POST /reserveSeat
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `seat_id`      | `int` | **Required**. Id of seat  |
| `user_id`      | `int` | **Required**. Id of user  |
| `name`      | `string` | **Required**. name of customer |
| `date`      | `datetime` | **Required**. datetime of you want to book a seat |


#### cancel seat

```http
  POST /cancelSeat
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `seat_id`      | `int` | **Required**. Id of seat  |
| `user_id`      | `int` | **Required**. Id of user  |
| `name`      | `string` | **Required**. name of customer |


### MongoDB
#### Get Mongo dbs

```http
  GET /mongo/dbs
```

#### Get Mongo collections

```http
  GET /mongo/collections
```

#### Get Mongo collection data

```http
  GET /mongo/data/<collection_name>
```






## dependencies
- python3.12+
- setuptools==75.8.2
- uvicorn==0.34.0
- pymongo==4.11.2
- redis==5.2.1
- fastapi==0.115.11
- motor==3.7.0



## Installation

Install **Booking System** with **docker**

first clone project from github

```bash
  git clone https://github.com/danialhedaiat/BookingSystem.git
```

run docker-compose

```bash
  docker-compose up --build -d
```


# future feature

- Make seat id increase automatically will create new one
- Auth service with jwt token 
- Check data for auto canceling booked seat
- Make environment variables for MONGO_HOST and REDIS_HOST
- Refactor project to clean architecture

