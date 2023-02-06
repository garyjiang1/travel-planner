import React, { useState } from "react";
import Tabs from "../TabComponent/Tab";
// import { useHistory ,useLocation } from 'react-router-dom';

const UserInputs = (props) => {
  // get the username from URI
  let urlElements = window.location.href.split('/')
  const username = decodeURI(urlElements[urlElements.length-1])

  // const [username, setUsername] = useState('');
  const [fromLocation, setFromLocation] = useState('');
  const [toLocation, setToLocation] = useState('');
  const [fromDate, setFromDate] = useState('');
  const [toDate, setToDate] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const [itenerary, setItenerary] = useState([]);

  const [showDashboard, setShowDashboard] = useState(false);


  // set username
  // setUsername(user)

  function submitHandler(){
      // handle signup data via api and fetch initial flight information
      setItenerary(handleItenerary())
      setShowDashboard(true);
  }
  
  
  const handleItenerary = () => {

    // email available means registration
        const requestOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                "fromLocation": fromLocation,
                "toLocation": toLocation,
                "fromDate": fromDate,
                "toDate": toDate
            })
        };
        // TODO: put URL as an env variable
        fetch('http://127.0.0.1:5005/composite_service/new_itenerary', requestOptions)
        .then(response => response.json())
        .then(data => setItenerary(data));
    return itenerary
}

  const textstyle = {fontSize:'20px'};
  const buttonstyle = {padding: '10px'};

  if(!showDashboard) {
    return (
      <form>
      <p style={{ fontSize: 40}}>
          EASYTRIP.AI <br/>
      </p>
      <br/>
    <h2>
      Hello, {username}
    </h2>
    <br/>
    <br/>

    <label>Where are you taking your trip from?
      <input
        type="text" 
        style={textstyle} 
        value={fromLocation}
        onChange={(e) => setFromLocation(e.target.value)}
      />
    </label>
    <br/>
    <br/>
    <label>Where are you taking your trip to?
      <input
        type="text" 
        style={textstyle} 
        value={toLocation}
        onChange={(e) => setToLocation(e.target.value)}
      />
    </label>
    <br/>
    <br/>
    <label>Enter your trip start date?
      <input
        type="text" 
        style={textstyle} 
        value={fromDate}
        onChange={(e) => setFromDate(e.target.value)}
      />
    </label>
    <br/>
    <br/>
    <label>Enter your trip end date?
      <input
        type="text" 
        style={textstyle} 
        value={toDate}
        onChange={(e) => setToDate(e.target.value)}
      />
    </label>
    <br/>
    <br/>
    <button onClick={submitHandler} type="button" style={buttonstyle}> Submit </button >
  
  </form>
 )


} else {
  return  <Tabs username={username} itenerary={itenerary} />
}

};
export default UserInputs;