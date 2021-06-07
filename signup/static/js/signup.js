const mariadb = require("mysql");
const express = require("express");
const bodyParser = require("body-parser");
const encoder = bodyParser.urlencoded();

const app = express();

const connection = mariadb.createConnection({
    host: "localhost",
    user:"root",
    password: "database",
    database: "user",
});

connection.connect(function(error){
    if(error) throw error
    else console.log("connected to the database successfully!")
});

app.get("/", function (req,res){
    res.sendFile(__dirname + "/../../login.html")
})

app.post("/",encoder, function(req,res){
    var username = req.body.username;
    var password = req.body.password;
    connection.query("INSERT INTO `user` (`username`, `password`) VALUES ('?', '?')",[username,password], function(error,results,fields){
        if (results.length > 0) {
            res.redirect("/../../setup.html");
        } else{
            res.redirect("/");
        }
        res.end();
    })
})

app.get("/../../annotate.html", function(req,res){
    res.sendFile(__dirname + "/../../setup.html")
})

app.listen(4000);