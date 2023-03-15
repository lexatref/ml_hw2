# Homework
Solution for homework https://stepik.org/lesson/753914/step/7?unit=755834

docker build -t hw2 .
docker run -v .:/app -p 8080:8080 hw2

Запрос с одним id
http://localhost:8080/readPlateNumbers?imageid=10022

{
  "plate_number": "\u0441181\u043c\u0432190"
}

Запрос с несколькими id
http://localhost:8080/readPlateNumbers?imageids=10022+9965

{
  "plate_numbers": [
    {
      "10022": "\u0441181\u043c\u0432190"
    }, 
    {
      "9965": "\u043e101\u043d\u043e750"
    }
  ]
}
