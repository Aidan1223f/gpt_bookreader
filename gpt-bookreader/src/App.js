import logo from './logo.svg';
import './App.css';
import React, {useState,useEffect} from 'react'

function App() {

const [accuracy, setAccuracy] = useState(0)
useEffect(() => {

}, [])

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Output: {accuracy}
        </p>
       
      </header>
    </div>
  );
}

export default App;
