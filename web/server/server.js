// web/server/server.js

const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');
const dotenv = require('dotenv');

// Load environment variables
dotenv.config();

const usersRoute = require('./routes/users');
const skillsRoute = require('./routes/skills');

const app = express();

// Middleware
app.use(cors());
app.use(express.json());

// Routes
app.use('/api/users', usersRoute);
app.use('/api/skills', skillsRoute);

// Connect to MongoDB
const PORT = process.env.PORT || 5000;
const MONGO_URI = process.env.MONGO_URI;

mongoose.connect(MONGO_URI, {
  useNewUrlParser: true,
  useUnifiedTopology: true
})
.then(() => {
  console.log('Connected to MongoDB');
  app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
})
.catch(err => {
  console.error('Error connecting to MongoDB:', err.message);
});
