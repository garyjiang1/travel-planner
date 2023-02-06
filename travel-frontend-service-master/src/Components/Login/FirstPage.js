import React, { useState } from "react";
import Dashboard from "../AllTabs/Dashboard";
import UserInputs from "../UserInputs/UserInputs";
import nature1 from './nature1.png';



const FirstPage = (props) => {
  const [showDashboard, setShowDashboard] = useState(false);
  const [user, setUser] = useState(false);
  const [name, setName] = useState('');


  // function handleLoginSubmit () {
  //   setShowDashboard(true)
  //   console.log("printing_name", showDashboard)
  // };

  function handleNameInput(event){
    setName(event.target.value)
  }

  const handleNewUser = async () => {
    try{
        const resp = await fetch('http://127.0.0.1:5011/users_service/login2')
        const url = await resp.json()
        window.location.href = url.request_url;
    } catch(err){
      console.error(err)
    }

    setUser("true")

  }

  // function handleNewUser() {
  //   setUser("true")


  //   console.log("testinggg", user)
  // }
  
  const textstyle = {fontSize:'20px'};
  const buttonstyle = {padding: '10px'};

    if(user && !showDashboard){
      {console.log("test12user")}
      // return <UserInputs/>
    }

    if (!showDashboard) {
      return (
        <div className="App">
          <header className="App-header">
            <div className="Login">
              <div class= "log">
              <p style={{ fontSize: 60}}>
                EASYTRIP.AI <br/>
                </p>

            
                <br/>
                <button onClick={handleNewUser} type="button" style={buttonstyle}> Log In </button >
                <br/>
                <br/>
                <img align="left" src={nature1} className="App-login-cover"/>

              </div>
              <br />
            </div>
          </header>

        </div>
      );
    } 
    if(showDashboard) {
      {console.log("test12")}
      return  <Dashboard name={name}/>
    }
};
export default FirstPage;