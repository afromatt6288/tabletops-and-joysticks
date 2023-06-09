import React, { useState, useEffect } from "react";
import { useParams, useHistory, Link } from "react-router-dom";
import { Datepicker, Input, Ripple, Select, initTE } from "tw-elements";
import MessageEdit from "./MessageEdit"

function Message({ users, user, message, currentUser, onDeleteMessage, onEditMessage, theme }) {
  const [isEditing, setIsEditing] = useState(false)
  const { id, sender_user_id, receiver_user_id, message_text, created_at } = message
 
/////////////////////
// Setup Functions //
/////////////////////

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
  
  function handleEditMessage(updatedMessage) {
    setIsEditing(false)
    onEditMessage(updatedMessage)
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
    <li className="border-[var(--color-theme-border)!important] hover:border-[var(--color-theme-hover-border)!important] mt-2 pb-2 rounded-lg border-2 ">
      <span>{formattedDate}</span>
      <br/>
      {sender_user_id == currentUser.id ?
      <span>From: {currentUser.username} (ID#{sender_user_id}) | To: {user.username} (ID#{receiver_user_id})</span> 
      :
      <span>From: {user.username} (ID#{sender_user_id}) | To: {currentUser.username} (ID#{receiver_user_id})</span>
      }
      
      {isEditing ? 
        <MessageEdit id={id} theme={theme} message_text={message_text} onEditMessage={handleEditMessage} /> 
      : 
        <p>{message_text}</p>
      }
      <div className="">
        {currentUser.id == sender_user_id ? 
          <div >
            <button onClick={() => setIsEditing(isEditing => !isEditing)} className="mr-2">
              <span className="border-[var(--color-theme-border)!important] hover:border-[var(--color-theme-hover-border)!important] border-2 rounded-lg "
              >Edit <span className="text-white">✏️</span></span>
            </button>
            <button onClick={handleDeleteClick} >
              <span className="border-[var(--color-theme-border)!important] hover:border-[var(--color-theme-hover-border)!important] border-2 rounded-lg"
              >Delete <span className="text-white">🗑</span> </span>
            </button>
          </div>
          : null}
      </div>
    </li>
  );
}

export default Message;
