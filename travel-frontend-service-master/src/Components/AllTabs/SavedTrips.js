import React, { useEffect, useState } from "react";
import UserInputs from "../UserInputs/UserInputs";
import DisplayTrips from "./DisplayTrips";


const SavedTrips = (props) => {
  const [trips, setTrips] = useState([]) 
  const [count, setCount] = React.useState(0);
  const [showUserInputPage, setShowUserInputPage] = useState(false)

  const user = props.username
  let userId = -1

  useEffect(()=> {
    const fetchUserId = async () => {
      try {
        const requestOptionsById = {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ username: user})
        };
        const result = await fetch('http://127.0.0.1:5011/users_service/get_user_id', requestOptionsById)
        const data = await result.json()
        userId = data.user_id.user_id
        fetchTrips(userId)
      } catch(e) {
        console.error(e);
      }
    } 

    const fetchTrips = async (userId) => {
      try {
        const requestOptions = {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ user_id: userId })
        };      
        const result = await fetch('http://127.0.0.1:5005/composite_service/get_saved_trips', requestOptions)
        const trips = await result.json()
        setTrips(trips)
      } catch(e) {
        console.error(e);
      }
    } 

    fetchUserId()
  },[])

    return (
        <DisplayTrips itenerary={trips}/>
    );
  };
  export default SavedTrips;