
    POST http://localhost:7020/login

request:
{
    "email":"test@gmail.com",
    "password":"password"
}

response:
{
    "id":"string"
}
error:
{
    "message":"email doesnt exist!"
}

    POST http://localhost:7020/register

request:
{
    "email":"test@gmail.com",
    "password":"password"
}
response:
{
    "message":"success",
    "email":"test@gmail.com"
}
error:
{
    "message":"failed",
    "email":"test@gmail.com"
}

    GET http://localhost:7020/list

response:
{
    "message":"success",
    "data":[
        {
            "message":"success",
            "email":"test2@gmail.com"
        },
        {
            "message":"success",
            "email":"test3@gmail.com"
        },
        {
            "message":"success",
            "email":"test@gmail.com"
        }
    ]
}
error:
{
    "message":"success",
    "data":[]
}