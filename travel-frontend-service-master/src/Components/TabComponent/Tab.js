import React, { useEffect, useState } from "react";
import BeforeLastPage from "../AllTabs/BeforeLastPage";
import SavedTrips from "../AllTabs/SavedTrips";
import ReviewPage from "../AllTabs/ReviewPage";
import Dashboard from "../AllTabs/Dashboard";
import SettingsPage from "../AllTabs/SettingsPage";
import UserInputs from "../UserInputs/UserInputs";
import NewTripInputs from "../NewTripInputs/NewTripInputs";



function Tabs(props) {
    const [activeTab, setActiveTab] = useState("Dashboard");   

   let urlElements = window.location.href.split('/')
   const user = decodeURI(urlElements[urlElements.length-1])
   console.log("user from tabs", user)

    // useEffect(()=> {
    //     console.log(props.username)
    //     setUsername(props.username)
    // },[])

    const handleDashboard = () => {
        setActiveTab("Dashboard");
    };

    const handleTop = () => {
        setActiveTab("Top");
    };
    const handleSaved = () => {
        setActiveTab("Saved");
    };
    
    const handleReview = () => {
        setActiveTab("Review");
    };

    const handleSettings = () => {
        setActiveTab("Settings");
    };

    const handleNewTrip = () => {
        setActiveTab("New Trip");
    };

  return (

            <div className="">
                <ul className="nav">
                <li className={activeTab === "Dashboard" ? "active" : ""}
                                onClick={handleDashboard} 
                                >Dashboard</li>
                <li className={activeTab === "Saved" ? "active" : ""}
                                onClick={handleSaved}
                                >Saved Trips</li>
                <li className={activeTab === "New Trip" ? "active" : ""}
                                onClick={handleNewTrip}
                                >New Trip</li>
                <li className={activeTab === "Review" ? "active" : ""}
                                onClick={handleReview}
                                >Review</li>
                <li className={activeTab === "Settings" ? "active" : ""}
                                onClick={handleSettings}
                                >Settings</li>

                </ul>
                <div className="outlet">
                    {(() => {
                        if (activeTab === "Top") {
                        return (
                            <BeforeLastPage />
                        )
                        } else if (activeTab === "Saved") {
                        return (
                            <SavedTrips username={user} />
                        )
                        } else if(activeTab === "Dashboard") {
                            return (
                                <Dashboard username={props.username?props.username:user} itenerary={props.itenerary?props.itenerary: undefined}/>
                            )
                        }
                        
                        else if(activeTab === "Review"){
                            return (
                                <ReviewPage name={props.name} username={props.username} fromLocation={props.fromLocation} toLocation={props.toLocation} fromDate={props.fromDate} toDate={props.toDate}/>
                            )
                        } else if(activeTab === "New Trip"){
                            return (
                                <NewTripInputs username={props.username}/>
                            )
                        }

                        else {
                            return (
                                <SettingsPage username={props.username} />
                            )
                        }
                    })()}
                    
                </div>
            </div>
  );
};
export default Tabs;