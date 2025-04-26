const express = require('express');
require('dotenv').config();
const fetch = require('node-fetch');

const app = express();
app.use(express.static('public'));

app.get('/session', async (req, res) => {
  const response = await fetch('https://api.openai.com/v1/realtime/sessions', {
    method: 'POST',
    headers: {
      Authorization: `Bearer ${process.env.OPENAI_API_KEY}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      model: process.env.MODEL,
      voice: process.env.VOICE
    })
  });
  const data = await response.json();
  res.json(data);
});

app.listen(3000, () => console.log('Server running on http://localhost:3000'));
