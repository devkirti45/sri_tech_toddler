// web/server/routes/skills.js

const express = require('express');
const router = express.Router();
const Skill = require('../models/Skill');

// Get all skills
router.get('/', async (req, res) => {
  try {
    const skills = await Skill.find();
    res.json(skills);
  } catch (err) {
    res.status(500).json({ message: 'Server error.' });
  }
});

// Add a new skill
router.post('/', async (req, res) => {
  const { name, command, response } = req.body;

  if (!name || !command || !response) {
    return res.status(400).json({ message: 'Please provide all skill fields.' });
  }

  try {
    const existingSkill = await Skill.findOne({ name });
    if (existingSkill) return res.status(400).json({ message: 'Skill already exists.' });

    const newSkill = new Skill({ name, command, response });
    await newSkill.save();
    
    res.status(201).json({ message: 'Skill added successfully.', skill: newSkill });
  } catch (err) {
    res.status(500).json({ message: 'Server error.' });
  }
});

// Update a skill
router.put('/:id', async (req, res) => {
  const { id } = req.params;
  const { name, command, response } = req.body;

  try {
    const updatedSkill = await Skill.findByIdAndUpdate(
      id,
      { name, command, response },
      { new: true }
    );

    if (!updatedSkill) {
      return res.status(404).json({ message: 'Skill not found.' });
    }

    res.json({ message: 'Skill updated successfully.', skill: updatedSkill });
  } catch (err) {
    res.status(500).json({ message: 'Server error.' });
  }
});

// Delete a skill
router.delete('/:id', async (req, res) => {
  const { id } = req.params;

  try {
    const deletedSkill = await Skill.findByIdAndDelete(id);
    
    if (!deletedSkill) {
      return res.status(404).json({ message: 'Skill not found.' });
    }

    res.json({ message: 'Skill deleted successfully.' });
  } catch (err) {
    res.status(500).json({ message: 'Server error.' });
  }
});

module.exports = router;
