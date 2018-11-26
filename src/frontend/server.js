var express = require('express');
var path = require('path');
var serveStatic = require('serve-static')

let app = express();

app.use(serveStatic(path.join(__dirname, 'gui_topology')))

app.set('view engine', 'html');
app.set('views', 'src');

app.use('/', express.static('dist', { index: false }));

app.get('*', (req, res, next) => {
    res.sendFile(path.join(__dirname, '/index.html'));
});
app.listen(3000, () => {
    console.log("listening on localhost:3000 (non-universal)");
});
