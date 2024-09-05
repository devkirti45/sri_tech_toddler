// web/client/src/App.js

import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [command, setCommand] = useState('');
  const [response, setResponse] = useState('');

  const sendCommand = async () => {
    try {
      const res = await axios.post('http://localhost:5000/api/voice-command', { text: command });
      setResponse(res.data.message);
    } catch (error) {
      console.error(error);
      setResponse('Error communicating with the assistant.');
    }
  };

  return (
    <div className="App">
      <h1>AI Voice Assistant</h1>
      <input
        type="text"
        value={command}
        onChange={(e) => setCommand(e.target.value)}
        placeholder="Enter your command"
      />
      <button onClick={sendCommand}>Send Command</button>
      <p>{response}</p>
    </div>
  );
}

export default App;
