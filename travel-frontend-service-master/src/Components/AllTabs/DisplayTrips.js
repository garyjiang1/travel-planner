import React, { useEffect, useState } from "react";

const DisplayTrips = (props) => {
    const [itenerary, setItenerary] = useState([]) 
    // setItenerary(props.itenerary)
    // console.log("printinglast", itenerary)
    useEffect(()=> {
        setItenerary(props.itenerary)
        console.log("printing useEffect", itenerary)
    })
    const handleTripDelete = async (it, idx) => {
        console.log("printing id", idx)
       try{
        const requestOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ trip_id: it.itinerary_id })
          };   
          await fetch('http://127.0.0.1:5011/users_service/delete_trip', requestOptions)
       } catch(e){
        console.error(e)
       }
       console.log("props.itenerary[1]", props.itenerary[1])

    }
    const buttonstyle = {padding: '15px 32px',  backgroundColor: 'red', color:'white'};

    return(
        <div className="App">
        <div>
            {itenerary.map((it, idx) => {
                return (
                    <div class="card">
                        <br></br>
                    <div class="container">
                            <h4><b>Flights from {it.origin} to {it.destination}</b></h4>
                            <p>Flight ID: {it.flight_num}</p>
                            <p>Airline Name: {it.airline_name}</p>
                            <p>Departure Time: {it.departure_time}</p>
                            <p>Arrival Time: {it.arrival_time}</p>
                            <p>Origin Airport: {it.origin_code}</p>
                            <p>Destination Airport: {it.destination_code}</p>
                            <p>Flight Duration: {it.travel_id} minutes</p>
                            <p>Price: {it.cost}</p>
                            <br/>
                            <button style={buttonstyle} onClick={() => handleTripDelete(it, idx)}>Delete this trip</button>

                    </div>
                    <br></br>

                    </div>
                    
                );
            })}
        </div>
    </div>
    )

};
export default DisplayTrips;