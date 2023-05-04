import React, { useState, useEffect } from "react";
import { useParams, useHistory, Link } from "react-router-dom";
import { Datepicker, Input, Ripple, Select, initTE } from "tw-elements";
import MessageEdit from "./MessageEdit"

function Message({ users, user, message, currentUser, onDeleteMessage, onUpdateMessage }) {
  const [isEditing, setIsEditing] = useState(false)
  const { id, sender_user_id, receiver_user_id, message_text, created_at } = message
 
/////////////////////
// Setup Functions //
/////////////////////
console.log(message)
console.log(user)

  const history = useHistory()

  // This is what implements Tailwind... so DON'T delete it. 
  useEffect(() => {
    initTE({ Datepicker, Input, Select, Ripple });
  }, []);

  function handleDeleteClick() {
    fetch(`api/messages/${id}`, {
      method: "DELETE"
    })    
    onDeleteMessage(id)
  }
  
  function handleUpdateMessage(updatedMessage) {
    setIsEditing(false)
    onUpdateMessage(updatedMessage)
  }

const date = new Date(created_at);
const formattedDate = new Intl.DateTimeFormat("en-US", {
  month: "short",
  day: "2-digit",
  year: "numeric",
  hour: "numeric",
  minute: "numeric",
  hour12: true
}).format(date);

  return (
    <li>
      <span>{formattedDate}</span>
      <br/>
      {sender_user_id == currentUser.id ?
      <span>From: {currentUser.username} (ID#{sender_user_id}) | To: {user.username} (ID#{receiver_user_id})</span> 
      :
      <span>From: {user.username} (ID#{sender_user_id}) | To: {currentUser.username} (ID#{receiver_user_id})</span>
      }
      
      {isEditing ? <MessageEdit id={id} message_text={message_text} onUpdateMessage={handleUpdateMessage} /> : <p>{message_text}</p>}
      {currentUser ? 
        <div>
          <button onClick={() => setIsEditing(isEditing => !isEditing)}>
            <span>✏️</span>
          </button>
          <button onClick={handleDeleteClick}>
            <span> 🗑 </span>
          </button>
        </div>
       : null}
    </li>
  );
}

export default Message;
