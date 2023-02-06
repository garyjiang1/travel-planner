import React, { useEffect, useState } from "react";
import DisplayTrips from "./DisplayTrips";
import DisplayNewTrips from "./DisplayNewTrips";

import axios from "axios"

const Dashboard = (props) => {
    const [userId, setUserId] = useState(0);
    const [trips, setTrips] = useState([]) 
    const [recTrips, setRecTrips] = useState([]) 
    const [lastSavedTrip, setLastSavedTrip] = useState([]) 
    // get the username from URI
    let urlElements = window.location.href.split('/')
    const username = decodeURI(urlElements[urlElements.length-1])

    let userIdNum = -1
    let recommendTrip = []
    let isRecommendLoading = false

    let inFetchingItenerary = false
    if(props.itenerary){
        inFetchingItenerary = true
    }

    if (props.itenerary && props.itenerary.dest_flights != undefined) {
        inFetchingItenerary = false
    }

    useEffect(()=> {
        const fetchUserId = async () => {
          try {
            const requestOptionsById = {
              method: 'POST',
              headers: { 'Content-Type': 'application/json' },
              body: JSON.stringify({ username: props.username})
            };
            const result = await fetch('http://127.0.0.1:5011/users_service/get_user_id', requestOptionsById)
            const data = await result.json()
            userIdNum = data.user_id.user_id
            fetchTrips(userIdNum)
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
            setLastSavedTrip(trips[trips.length-1])
            console.log("printing_trips ", trips)
          } catch(e) {
            console.error(e);
          }
        } 
    
        fetchUserId()
      },[])

    const [iteneraryResp, setIteneraryResp] = useState(0);
    // let isTripSaved = false

    const handleRecommend = async () => {
        try {
            // isRecommendLoading = true
            const resp = await fetch('http://127.0.0.1:5011/users_service/recommend')
            const data = await resp.json()
            setRecTrips(data)
            console.log("recocmmend trips", recTrips)
            isRecommendLoading = true
        } catch(e){
            console.error(e)
        }
    }

    function handleSaveFlight(flight) {
        // get userid
        const requestOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ username: props.username })
        };
        fetch('http://127.0.0.1:5011/users_service/get_user_id', requestOptions)
            .then(response => response.json())
            .then(data => {
                setUserId(data.user_id.user_id)
            });

            // set body
            const itinerary_id = Math.floor(Math.random() * 1000000000);
            const iteneraryBody = {
                itinerary_id: itinerary_id,
                review_id: 1,
                origin: props.itenerary.org,
                destination: props.itenerary.dest,
                origin_code: flight.origin_airport,
                destination_code: flight.destination_airport,
                departure_time: flight.departure,
                arrival_time: flight.arrival,
                airline_name: flight.carrier,
                flight_num: flight.flight_id,
                cost: flight.price
            }
            axios.post('http://127.0.0.1:5012/api/flight/update', iteneraryBody)
                .then(response => { console.log(response)});
        
        // store the itenerary_id and user_id in the trips table in users_service
        console.log("printing_user_id", userId)
        const requestOptionsSaveTrip = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ user_id: userId, trip_id: itinerary_id})
        };
        fetch('http://127.0.0.1:5011/users_service/create_trip', requestOptionsSaveTrip)
        .then(response => response.json())
        .then(data => {
            console.log("trip_data", data)
        });
    }
    const buttonstyle = {padding: '15px 32px',  backgroundColor: 'green', color:'white'};

    if(props.itenerary && props.itenerary.dest_flights != undefined && !inFetchingItenerary){
        return (
            <div className="App">
                <h2><b>Flights from {props.itenerary.org} to {props.itenerary.dest}</b></h2>
                <div>
                    {props.itenerary.dest_flights.map(it => {
                        return (
                            <div class="card">
                                <br></br>
                            <div class="container">
                                    {/* <h4><b>Flights from {props.itenerary.org} to {props.itenerary.dest}</b></h4> */}
                                    <p>Flight ID: {it.flight_id}</p>
                                    <p>Arrival Time: {it.arrival}</p>
                                    <p>Departure Time: {it.departure}</p>
                                    <p>Origin Airport: {it.origin_airport}</p>
                                    <p>Destination Airport: {it.destination_airport}</p>
                                    <p>Flight Duration: {it.duration} minutes</p>
                                    <p>Price: {it.price}</p>
                                    <br/>
                                    
                            </div>
                                    <button onClick={() => handleSaveFlight(it)}>Save</button>
                            <br></br>

                            </div>
                            
                        );
                    })}
                </div>

                <br></br>
                <br></br>

                <h2><b>Flights from  {props.itenerary.dest} to {props.itenerary.org} </b></h2>
                <div>
                    {props.itenerary.return_flights.map(it => {
                        return (
                            <div class="card">
                                <br></br>
                            <div class="container">
                                    {/* <h4><b>Flights from {props.itenerary.org} to {props.itenerary.dest}</b></h4> */}
                                    <p>Flight ID: {it.flight_id}</p>
                                    <p>Arrival Time: {it.arrival}</p>
                                    <p>Departure Time: {it.departure}</p>
                                    <p>Origin Airport: {it.origin_airport}</p>
                                    <p>Destination Airport: {it.destination_airport}</p>
                                    <p>Flight Duration: {it.duration} minutes</p>
                                    <p>Price: {it.price}</p>
                                  
                            </div>
                            <button onClick={() => handleSaveFlight(it)}>Save</button>

                            <br></br>
                            </div>
                            
                        );
                    })}
                </div>
    
                <br></br>
            </div>
    
        );
    } else if(inFetchingItenerary) {
        return (
            <h2>Fetching Itenerary, please wait ..</h2>
        );
    } else {
        return (
            <p> <h1>Your recent trips:</h1>
             <br/> 
                <DisplayTrips itenerary={trips.slice(-2)}/>
                <br/> <br/>
            </p>
        );
    }



  };
  export default Dashboard;