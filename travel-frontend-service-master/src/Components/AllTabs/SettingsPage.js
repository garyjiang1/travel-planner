import React, { useState } from "react";
import FirstPage from "../Login/FirstPage";
import Tabs from "../TabComponent/Tab";


function SettingsPage(props) {
  const [showFirstPage, setShowFirstPage] = useState(false)
  const [showTabs, setShowTabs] = useState(true)

  const handleClick = async () => {
     try {  
      const resp = await fetch('http://127.0.0.1:5011/users_service/logout')
      const url = await resp.json()
      window.location.href = url.request_url;
     } catch(e){
      console.error(e)
     }
  };

  if(showFirstPage && !showTabs){
      return (
        <div className="Logout">
            <FirstPage/>
        </div>
      )

    }

    return (
        <div className="App">
          <header className="App-headerTEST">
            <div className="Settings">
                <div class= "test2">
                    <button type="button" onClick={handleClick}>
                        Logout
                    </button>
              </div>
            </div>
          </header>
        </div>
    );
};
  export default SettingsPage;