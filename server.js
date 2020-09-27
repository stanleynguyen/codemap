const express = require('express');
const revealRunInTerminal = require('reveal-run-in-terminal');
const fs = require('fs');

const app = express();
app.use(require('connect-livereload')({ port: 35729 }));
app.use(
  revealRunInTerminal({
    allowRemote: true,
  }),
);
app.use(express.static('./'));
app.use(express.static('./node_modules/reveal.js/'));

app.listen(process.env.PORT || 5000, (err) => {
  if (err) {
    throw err;
  }

  const livereload = require('livereload');
  const server = livereload.createServer();
  server.watch(__dirname);
  console.log('Presentation up & running on :5000');
});
