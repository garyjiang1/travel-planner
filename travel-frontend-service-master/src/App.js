import logo from './logo.svg';
import './App.css';
import React, { useState } from "react";
import Tabs from "./Components/TabComponent/Tab";
import FirstPage from "./Components/Login/FirstPage";
import UserInputs from "./Components/UserInputs/UserInputs";
import Tab from "./Components/TabComponent/Tab";

import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
//import Header from "./component_temp/Header";

function App() {
  return (
    <div className="App">
      <header className="App-header">
          <Routes>
            <Route path="" element={<FirstPage />}/>
            <Route path="/userInputs/:username" element={<UserInputs />}/>
            <Route path="/loggedin/:username" element={<Tab />}/>
          </Routes>
          
        </header> 
    </div>   
  );
}

/*
My inital changes
      <Router>
      <Routes>
      <Route path="/" element={<Login />} />
      <Route path="/signup" element={<Signup />} />
    </Routes>
   </Router>
*/

/*
Maryam's changes
<div className="App">
      <header className="App-header">
          <Tabs />
        </header> 
    </div>   
*/

export default App;