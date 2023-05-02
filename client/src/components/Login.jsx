import React, {useState} from "react";
import { useHistory, Link } from "react-router-dom";
import UserNew from "./UserNew";
import UserProfile from "./UserProfile";

function Login ({currentUser, setCurrentUser, toggle, users, onAddUser}) {
    const [username, setUsername] = useState("")
    const [password, setPassword] = useState("")
    const [isPasswordSecure, setIsPasswordSecure] = useState(true)
    const [invalidUser, setInvalidUser] = useState(false)
    const [newUser, setNewUser] = useState(false)
    
    const history = useHistory()

    function handleSubmit(e) {
        e.preventDefault();
        <Link to={`/`}></Link>
        fetch("api/login", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ username, password }),
        })
          .then((r) => {
            if (r.ok) {
              r.json()
              .then((user) => {
                setCurrentUser(user)
              })
            history.push(`/`)
            toggle()
            } else { 
              setInvalidUser(e=>setInvalidUser(!invalidUser))
          }});
    }
        
    function handleNewUser(addUser){
      onAddUser(addUser)
      setNewUser(!newUser)
    }
        
    return (
        <div>
          {newUser ? <UserNew onNewUser={handleNewUser} toggle={toggle} /> :
            <form onSubmit={handleSubmit}>
                <input type="text" id="username" placeholder="User Name" value={username} onChange={e => setUsername(e.target.value) }/>
                <input type={isPasswordSecure? "password" : "text"} id="password" placeholder="Password" value={password} onChange={e => setPassword(e.target.value)}/>
                <span><input label="show-password" type="checkbox" checked={!isPasswordSecure} onChange={(e)=>setIsPasswordSecure(!isPasswordSecure)}/> {isPasswordSecure ? "🙈" : "🙉"}</span>
                <br/>
                <button type="submit">Login</button>
                <br/>
                {invalidUser ? <small>Invalid User</small> : null}
                <button onClick={e=>setNewUser(!newUser)}>New User? Sign up here!</button> 
            </form>}
        </div>
    );
 }

export default Login