import React, { useEffect, useState } from "react";
import axios from "axios"

const DisplayNewTrips = (props) => {
    let urlElements = window.location.href.split('/')
    const username = decodeURI(urlElements[urlElements.length-1])
    const [userId, setUserId] = useState([]);

    console.log("printing review from newtrip", props.reviews)

    function handleSaveFlight(flight) {
        // get userid
        const requestOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ username: username })
        };
        fetch('http://127.0.0.1:5011/users_service/get_user_id', requestOptions)
            .then(response => response.json())
            .then(data => {
                setUserId(data.user_id.user_id)
            });

        console.log("user_id_display", userId)

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
    return(

        <div className="App">
        <h2><b>Flights from {props.itenerary.org} to {props.itenerary.dest}</b></h2>

        {props.itenerary.dest_flights.map(it => {
            return (
                <div class="card">
                    <br/>
                <div class="container">
                        <br/>
                        <p>Flight ID: {it.flight_id}</p>
                        <p>Arrival Time: {it.arrival}</p>
                        <p>Departure Time: {it.departure}</p>
                        <p>Origin Airport: {it.origin_airport}</p>
                        <p>Destination Airport: {it.destination_airport}</p>
                        <p>Flight Duration: {it.duration} minutes</p>
                        <p>Price: {it.price}</p>
                        <br/>
                        
                </div>
                        <button style={buttonstyle} onClick={() => handleSaveFlight(it)}>Save</button>
                <br></br>

                </div>
                
            );
        })}

        <br/>
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
                            <button style={buttonstyle} onClick={() => handleSaveFlight(it)}>Save</button>

                            <br></br>
                            </div>
                            
                        );
                    })}
                </div>

                <div>
                    <br/>
                    <h2>User reviews for {props.itenerary.dest} city:</h2>
                    {props.reviews.map(rv => {
                        return (
                            <div class="card">
                            <br></br>
                            <div class="container">
                                    <p>Rating: {rv.rating}</p>
                                    <p>Review: {rv.review}</p>
                            </div>
                            <br></br>
                            </div>
                        );
                    })}
  
                    {/* {JSON.stringify(props.reviews)} */}
                </div>
    </div>
        
    )

};
export default DisplayNewTrips;