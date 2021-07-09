var express = require('express');
var app = express();
var bodyParser = require("body-parser");

const mySecret = process.env['serverip'] // Necessidade do Repl.it para esconder o IP

var mysql = require('mysql');

app.set("view engine", "ejs");
app.use(bodyParser.urlencoded({extended: true}));
app.use(express.static(__dirname + "/public"));

var connection = mysql.createConnection({
	host: mySecret,
  port: 9096,
	user: 'user', // Inserir usuário do Banco de dados
	password: '',  // Inserir Senha do Banco de dados
	database: 'aioti'
});

app.get("/", function(req, res) {
  var tables;
  var recon_data;
  var recon_append = [];
  var people_data;
  var printer_data;
  
	connection.query('SHOW TABLES', function (err, results, fields) {
		if (err) throw err;
		tables = results;
	});

  connection.query('SELECT * FROM recon ORDER BY id DESC LIMIT 5', function (err, results, fields) {
		if (err) throw err;
		recon_data = results;
  console.log(recon_data);
  Object.keys(fields).forEach(function(key) {
      var field = fields[key];
      recon_append.push(field.name)
      console.log(field.name)
    });
  console.log(recon_append)
  });

  connection.query('SELECT * FROM people ORDER BY id DESC LIMIT 5', function (err, results, fields) {
		if (err) throw err;
		people_data = results;
  });	

  connection.query('SELECT * FROM printer ORDER BY id DESC LIMIT 5', function (err, results, fields) {
		if (err) throw err;
		printer_data = results;
    res.render("home", {data1: tables, data2: recon_data, append2: recon_append, data3: people_data, data4: printer_data});
  });
  
});

app.listen(3000, function() {
	console.log('Server running on 3000');
});
