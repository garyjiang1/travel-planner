import React, { useState } from "react";
import Tabs from "../TabComponent/Tab";
// import { useHistory ,useLocation } from 'react-router-dom';
import DisplayNewTrips from "../AllTabs/DisplayNewTrips";

const NewTripInputs = (props) => {
  // get the username from URI
  let urlElements = window.location.href.split('/')
  const username = decodeURI(urlElements[urlElements.length-1])

  const [fromLocation, setFromLocation] = useState('');
  const [toLocation, setToLocation] = useState('');
  const [fromDate, setFromDate] = useState('');
  const [toDate, setToDate] = useState('');

  const [itenerary, setItenerary] = useState([]);
  const [reviews, setReviews] = useState([]);


  const [showInputs, setShowInputs] = useState(true);
  const [isLoading, setIsLoading] = useState(false);

  // let isLoading = false;

  // set username
  // setUsername(user)

  const submitHandler = async () => {
      // handle signup data via api and fetch initial flight information
    setIsLoading(true)
    const resp = await handleItenerary()
    setItenerary(resp)
    setIsLoading(false)
    setShowInputs(false);
    const getRviews = await getReviews(toLocation)
    setReviews(getRviews)
    console.log("fetched reviews", reviews)
  }

  const getReviews = async (city) => {
    const result = await fetch('http://127.0.0.1:5000/api/review?city='+city)
    const resp = await result.json()
    return resp
  }
  
  const buttonstyle = {padding: '15px 32px',  backgroundColor: 'green', color:'white'};

  const handleItenerary = async () => {
    try {
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
      const resp = await fetch('http://127.0.0.1:5005/composite_service/new_itenerary', requestOptions)
      const respJson = await resp.json()
      return respJson
    } catch(e){
      console.error("error in handleItenerary", e)
    }
}

  const textstyle = {fontSize:'20px'};

  if(showInputs) {
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
    <label>Enter your trip start date.?
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
    <button style={buttonstyle} onClick={submitHandler} type="button" > Submit </button >
  
  </form>
 )

} else if (isLoading){
  return (<h1>Fetching Itenerary.. Please Wait .. </h1>)
}
 else {
    return(
      // <h1>DisplayNewTrips</h1>
      <DisplayNewTrips itenerary={itenerary} username={props.username} reviews={reviews}/>
    )
}

};
export default NewTripInputs;