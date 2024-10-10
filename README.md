# FASTAPI_APP

> Hosted App Swagger URL - https://voiceless-peafowl-pavanuppari-822d81b8.koyeb.app/docs

## Getting Started

1. Create a virtual environment
```shell
python -m venv env
```
2. Active virtual environment
```shell
source env/bin/activate
```
3. Install dependencies
```shell
pip install -r requirements.txt
```

## Core Entities

```
Item

id - PositiveInt
name - StrictStr
email - EmailStr
quantity - PositiveInt
expiry_date - FutureDate
```

```
ClockIn

id - PositiveInt
email - EmailStr
location - StrictStr

```

## Item supported methods

1. POST /items - Create an Item
2. GET /items/{id} - Get an Item
3. GET /items - Get items with optional filters. Supported filters are 
    1. email - return item with email exact match 
    2. expiry_date - return items expiring after provided date 
    3. created_date - return items created after provided date 
    4. quantity - return items whose quantity is greater than provided value
4. DELETE /items/{id} - Delete an Item
5. PUT /items/{id} - Update an Item
6. GET /items/group-by-email - Get items count per email

## ClockIn supported methods

1. POST /clock-in - Create a clock in record
2. GET /clock-in/{id} - Get a clock in record
3. GET /clock-in - Get clock in records with optional filters. Supported filters are 
    1. email - return clock in records with email exact match 
    2. location - return clock in records with exact location match 
    3. created_date - return clock in records created after provided date 
4. DELETE /clock-in - Delete a clock in record
5. PUT /clock-in - Update a clock in record

## Database

MongoDB