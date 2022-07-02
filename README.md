# api_flask_mysql
In phpmyadmin, you have to create a DB named = curso with "Primary Key-codigo [char]6, nombre [varchar]30 and creditos [tinyint]1
Open your terminal
Write .\env\Scripts\activate and then python .\src\app.py
Copy the URL that shows in your terminal, open your browser and put it there
You will get 404 Error and "La página que intentas buscar no existe" message
In phpmyadmin, add 2 registers to the DB and then
You can write ["yourUrl:PORT"/cursos]
All values that you add shows here
In Visual Studio Code you need to have Thunder Client, with a collection and 4 Request:
GET, GET, POST, DELETE and PUT
GET: http://127.0.0.1:5000/cursos
GET: http://127.0.0.1:5000/cursos/325817 <<<<(creditos)
POST: http://127.0.0.1:5000/cursos in body json content: {
    "codigo": "556677",
    "nombre": "Biologia",
    "creditos": 2
}
DELETE: http://127.0.0.1:5000/cursos/235821 <<<<<<(Creditos)
PUT: http://127.0.0.1:5000/cursos/903871 in body json content: {
    "nombre": "Programacion Orientada a Objetos",
    "creditos": 6
    
}
