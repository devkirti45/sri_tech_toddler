// web/server/routes/users.js

const express = require('express');
const router = express.Router();
const User = require('../models/User');

// Register a new user
router.post('/register', async (req, res) => {
  const { username, email, password } = req.body;
  
  // Simple validation (extend as needed)
  if (!username || !email || !password) {
    return res.status(400).json({ message: 'Please enter all fields.' });
  }

  try {
    // Check if user exists
    const existingUser = await User.findOne({ email });
    if (existingUser) return res.status(400).json({ message: 'User already exists.' });

    const newUser = new User({ username, email, password });
    await newUser.save();
    
    res.status(201).json({ message: 'User registered successfully.' });
  } catch (err) {
    res.status(500).json({ message: 'Server error.' });
  }
});

// Login a user
router.post('/login', async (req, res) => {
  const { email, password } = req.body;

  // Simple validation
  if (!email || !password) {
    return res.status(400).json({ message: 'Please enter all fields.' });
  }

  try {
    const user = await User.findOne({ email });
    if (!user) return res.status(400).json({ message: 'User does not exist.' });

    // Check password (in real app, compare hashed passwords)
    if (user.password !== password) {
      return res.status(400).json({ message: 'Invalid credentials.' });
    }

    res.json({ message: 'Login successful.', user: { username: user.username, email: user.email } });
  } catch (err) {
    res.status(500).json({ message: 'Server error.' });
  }
});

module.exports = router;
