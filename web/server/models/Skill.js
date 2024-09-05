// web/server/models/Skill.js

const mongoose = require('mongoose');

const SkillSchema = new mongoose.Schema({
  name: {
    type: String,
    required: true,
    unique: true
  },
  command: {
    type: String,
    required: true
  },
  response: {
    type: String,
    required: true
  }
}, { timestamps: true });

module.exports = mongoose.model('Skill', SkillSchema);
