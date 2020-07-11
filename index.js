
var express = require('express'); 
var cors = require('cors')
var app = express(); 

app.use(cors())

app.listen(process.env.PORT || 3000, function() { 
	console.log('server running on port 3000'); 
} ) 
app.get('/',function(req,res) {
  res.sendFile('index.html',{root: __dirname});
});

app.get('/prediction', callName); 

function callName(req, res) { 
	
	 
	var spawn = require("child_process").spawn; 
	
	
	var process = spawn('python',["./fake_news_detection.py",req.query.news] );

	
	process.stdout.on('data', function(data) { 
		res.send(data.toString()); 
	} ) 
} 