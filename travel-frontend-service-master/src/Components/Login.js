//Login file, user enters username
import React from 'react';
import { useState } from 'react';
import ReactDOM from 'react-dom/client';
//import styles from "../Button.css";
import Signup from "./Signup"

//function MyForm() {
const LoginForm = () => {
  const [name, setName] = useState("");
  /*const newUser = () => {
        navigate(<Signup/>);
    //navigate('/signup');
    }*/
  const handleSubmit = (event) => {

   /* <form onSubmit={handleSubmit2}>
    <h3> <center> Who is taking the trip? </center> </h3>
    <center>  <label> 
       <input 
          type="text" 
          value={name}
          onChange={(e) => setName(e.target.value)}
        />
      </label>
      <div> <input type="submit" class="submitbutton" value="Continue"/> </div> </center>
    </form>*/
      
    //event.preventDefault();
    //alert(`The name you entered was: ${name}`)
  }

  /*const handleSubmit2 = (event) => {
    event.preventDefault();
    alert(`The city you entered was: ${city}`)
  }*/

  return (
    <form onSubmit={handleSubmit}>
    <div> <h2> <center> Login </center> </h2> </div>
    <h3> <center> Who is taking the trip? </center> </h3>
    <center>  <label> 
       <input 
          type="text" 
          value={name}
          onChange={(e) => setName(e.target.value)}
        />
      </label>
      <div> <input type="submit" class="submitbutton" value="Continue"/> </div> </center>
      <div><button onClick={Signup} text-align="center">  Log In </button> </div>
    </form>
  )
}

const root = ReactDOM.createRoot(document.getElementById('root'));
//root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<LoginForm />);

export default function Login() {
  return(
    <LoginForm/>
  );
}