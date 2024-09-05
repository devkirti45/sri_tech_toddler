// web/client/src/components/SkillList.js

import React, { useEffect, useState } from 'react';
import axios from 'axios';

function SkillList() {
  const [skills, setSkills] = useState([]);

  useEffect(() => {
    const fetchSkills = async () => {
      try {
        const res = await axios.get('http://localhost:5000/api/skills');
        setSkills(res.data.skills);
      } catch (error) {
        console.error(error);
      }
    };

    fetchSkills();
  }, []);

  return (
    <div>
      <h2>Available Skills</h2>
      <ul>
        {skills.map((skill, index) => (
          <li key={index}>{skill}</li>
        ))}
      </ul>
    </div>
  );
}

export default SkillList;
