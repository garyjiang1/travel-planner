//Login file, user enters username
import React from 'react';
import { useState } from 'react';
import ReactDOM from 'react-dom/client';

//function MyForm() {
const SignUpForm = () => {
  const [name, setName] = useState("");

  const handleSubmit = (event) => {
    event.preventDefault();
    alert(`The name you entered was: ${name}`)
  }

  return (
    <form onSubmit={handleSubmit}>
    <div> <h2> <center> New User Login </center> </h2> </div>
    <h3> <center> Enter Your Name </center> </h3>
    <center>  <label> 
       <input 
          type="text" 
          value={name}
          onChange={(e) => setName(e.target.value)}
        />
      </label>
      <div> <input type="submit" class="submitbutton" value="Sign Up"/> </div> </center>
    </form>
  )
}

const root = ReactDOM.createRoot(document.getElementById('root'));
//root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<SignUpForm />);

export default function Signup() {
  return(
    <SignUpForm/>
  );
}