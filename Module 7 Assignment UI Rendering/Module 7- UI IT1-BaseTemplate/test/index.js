const express = require('express');
const app = express();
const port = 3001;

app.get('/', (req, res) => {
	res.status(200).sendFile(__dirname + '/public/login.html');
});

app.listen(port, () => {
	console.log(`Server started at port ${port}`);
});