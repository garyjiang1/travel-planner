import logo from './logo.svg';
import one from './one.jpeg';
import two from './two.jpeg';
import three from './three.jpeg';
import four from './four.jpeg';
import five from './five.jpeg';

import React, { useState } from "react";

const BeforeLastPage = () => {
    return (
        <div className="App">
          <header className="App-header">
            <div className="Search">
              <div class= "nn">
                <p>
                  Top 5 Sights in: <input type = "text" defaultValue={"London"} />
                  <br />
                </p>
                <p>
                  <br />
                </p>
    
                <div className="Attraction" class = "column">
                  <div class= "row">
                    Attraction 1: 
                    <a className="App-link" href=" https://reactjs.org" target="_blank"> View directions</a>
                    <img src={one} className="App-logo" alt="logo" />
    
                  </div>
                  <div class= "row">
                    Attraction 2: 
                    <a className="App-link" href=" https://reactjs.org" target="_blank"> View directions</a>
                    <img src={two} className="App-logo" alt="logo" />
                  </div>
                  <div class= "row">
                    Attraction 3: 
                    <a className="App-link" href=" https://reactjs.org" target="_blank"> View directions</a>
                    <img src={three} className="App-logo" alt="logo" />
                  </div>
                  <div class= "row">
                    Attraction 4: 
                    <a className="App-link" href=" https://reactjs.org" target="_blank"> View directions</a>
                    <img src={four} className="App-logo" alt="logo" />
                  </div>
                  <div class= "row">
                    Attraction 5: 
                    <a className="App-link" href=" https://reactjs.org" target="_blank"> View directions</a>
                    <img src={five} className="App-logo" alt="logo" />
                  </div>
                </div>
              </div>
            </div>
          </header>
        </div>
      );
};
export default BeforeLastPage;