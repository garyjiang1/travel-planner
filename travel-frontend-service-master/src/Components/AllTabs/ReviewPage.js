import React, { useState } from "react";

function ReviewPage(props) {
  //count is just a placeholder for testing. Replace with appropriate API endpoint info.
  const [count, setCount] = React.useState(0);
  const [rating, setRating] = useState();
  const [review, setReview] = useState('');
  const [city, setCity] = useState('');


  const submitHandler = async () => {
    try {
      const requestOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                "city": city,
                "user_id": 1,
                "review": review,
                "rating": rating
            })
        };
        const result = await fetch('http://127.0.0.1:5000/api/review', requestOptions)
        const reviews = await result.json()
        console.log("printing reviews", reviews)
    } catch (e){
      console.error(e)
    }
  }


  
  const textstyle = {fontSize:'20px'};
  const buttonstyle = {padding: '15px 32px',  backgroundColor: 'green', color:'white'};

    return (
        <div className="App">
          <header className="App-headerTEST">
            <div className="Review">
              <label>Review City:
                  <input
                    type="text" 
                    style={textstyle} 
                    value={city}
                    onChange={(e) => setCity(e.target.value)}
                  />
              </label>
              <br/>
              <br/>
                <label>Give a Rating:
                    <input
                      type="text" 
                      style={textstyle} 
                      value={rating}
                      onChange={(e) => setRating(e.target.value)}
                    />
                </label>
                <br/>
              <br/>
                <label>Write a Review:
                    <input
                      type="text" 
                      style={textstyle} 
                      value={review}
                      onChange={(e) => setReview(e.target.value)}
                    />
                </label>
                <br/>
              <br/>
            <button onClick={submitHandler} type="button" style={buttonstyle}> Submit </button >

              {/* <div class= "nn">
                <p>
                  Review City: <input type = "text" 
                  class= "text-box" 
                  defaultValue={props.toLocation} />
                </p>
                <div> 

                <br /> 

                <textarea 
                class= "review-box" 
                name="Text1" 
                cols="40" 
                rows="5">
                </textarea>

                <div class= "test">
                    <button type="button" onClick={handleClick}>
                        Submit Review
                    </button>
                    <p>
                    <br />
                    </p>
                </div>

                </div> 
              </div> */}
            </div>
          </header>
        </div>
    );
};
  export default ReviewPage;