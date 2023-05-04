import React, { useState, useEffect } from "react";
import { useParams, useHistory, Link } from "react-router-dom";
import { Datepicker, Input, Ripple, Select, initTE } from "tw-elements";
import GameList from "./GameList"
import MessageNew from "./MessageNew";

function UserDetail({admin, currentUser, onSendMessage, onUserDelete}) {
    // const [message_text, setMessage_text] = useState("")
    const [user, setUser] = useState(null);
    const [message, setMessage] = useState(false)
    
/////////////////////
// Setup Functions //
/////////////////////
    
    const history = useHistory()
    const { id } = useParams()

    console.log(user, currentUser)

    // This is what implements Tailwind... so DON'T delete it. 
    useEffect(() => {
        initTE({ Datepicker, Input, Select, Ripple });
    }, []);
    
    useEffect(() => {
        fetch(`/api/users/${id}`)
        .then(r => r.json())
        .then(data => {
            console.log(data)
            setUser(data)});
        }, [])
        
        if (!user) return <h2>Loading...</h2>
        
    const {username, email, address, avatar_url, stars, travel_distance, is_active, is_admin} = user
    
    // Add the users games to each user
    const allGames = user.inventories.map((inv)=>inv.game)

    function handleUserDelete() {
        history.push(`/`)
        fetch(`api/users/${id}`, {
          method: "DELETE"
        })        
        onUserDelete(id)
        history.push(`/`)
        history.push(`/users`)
    }    

    return (
        <div>
            <header>
                <img src={avatar_url} alt={`${username} Avatar`} />
                <span> Username: {username} | ID: #{id} {is_admin ? " | Moderator" : null } 
                | <button onClick={() => setMessage(message => !message)}>Message</button>
                </span>
            </header>
            <h3>Peer Rating: {stars} Stars</h3>
            <h3>Travel Distance: {travel_distance} Miles</h3>
            <h3>Status: {is_active ? "Online":"Offline"}</h3>
            <h3>Email: {email}</h3>
            <h3>Address: {address}</h3>
            {message ?
            <MessageNew user={user} currentUser={currentUser} onSendMessage={onSendMessage}/>
            // <form onSubmit={handleSendMessage}>
            //     <div className="relative mb-3" data-te-input-wrapper-init>
            //         <textarea rows="4" id="send_messageFormControlInput1" value={message_text} onChange={e => setMessage_text(e.target.value)}
            //         className="peer block min-h-[auto] w-full rounded border-0 bg-transparent px-3 py-[0.32rem] leading-[1.6] outline-none transition-all duration-200 ease-linear focus:placeholder:opacity-100 peer-focus:text-primary data-[te-input-state-active]:placeholder:opacity-100 motion-reduce:transition-none dark:text-neutral-200 dark:placeholder:text-neutral-200 dark:peer-focus:text-primary [&:not([data-te-input-placeholder-active])]:placeholder:opacity-0"/>
            //         <label htmlFor="send_messageFormControlInput1"
            //         className="pointer-events-none absolute left-3 top-0 mb-0 max-w-[90%] origin-[0_0] truncate pt-[0.37rem] leading-[1.6] text-neutral-500 transition-all duration-200 ease-out peer-focus:-translate-y-[0.9rem] peer-focus:scale-[0.8] peer-focus:text-primary peer-data-[te-input-state-active]:-translate-y-[0.9rem] peer-data-[te-input-state-active]:scale-[0.8] motion-reduce:transition-none dark:text-neutral-200 dark:peer-focus:text-primary"
            //         >Send a Message</label>
            //     </div>
            //     <button type="submit">Send</button>   
            // </form>
            : null}
            <h2>Games:</h2>
                <div className="user-game-list">
                    <GameList games={allGames}/>
                </div>
            {admin ? 
                <div>
                    <button>
                        <span role="img" aria-label="edit"> ✏️ </span>
                    </button>
                    <button onClick={handleUserDelete}>
                        <span role="img" aria-label="delete"> 🗑 </span>
                    </button>
                </div>
            : null}
        </div>
    )
}
export default UserDetail