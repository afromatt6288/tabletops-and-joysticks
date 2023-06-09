import React, { useState, useEffect , useMemo} from "react";
import { useParams, useHistory, Link } from "react-router-dom";
import { Datepicker, Input, Ripple, Select, initTE } from "tw-elements";
import MessageSearch from "./MessageSearch";
import MessageList from "./MessageList";

function MessageBox({users, currentUser, messages, onSendMessage, onDeleteMessage, onEditMessage, theme}) {
  const [search, setSearch] = useState("")
  const [selectedUser, setSelectedUser] = useState(null);
  const [sortType, setSortType] = useState("name");

/////////////////////
// Setup Functions //
/////////////////////

  const history = useHistory()

  // This is what implements Tailwind... so DON'T delete it. 
  useEffect(() => {
    initTE({ Datepicker, Input, Select, Ripple });
  }, []); 

  function handleSendMessage(newMessage) {
      onSendMessage(newMessage)
  }

  function handleEditMessage(editedMessage) {
      onEditMessage(editedMessage)
  }

  function sortUsers(usersToSort) {
    return usersToSort.sort((a, b) => {
      switch (sortType) {
        case "name":
          return a.username.localeCompare(b.username);
        case "id":
          return a.id - b.id;
        case "recent":
          return (
            new Date(b.messages[0]?.created_at || 0) -
            new Date(a.messages[0]?.created_at || 0)
          );
        default:
          return 0;
      }
    });
  }

  // Takes all incoming messages and only keeps messages that have the currentUser.id
  const filteredMessages = useMemo(() => messages
    .filter(message => 
      (message.sender_user_id === currentUser.id || message.receiver_user_id === currentUser.id) &&
      message.message_text.toLowerCase().includes(search.toLowerCase())
    )
    .map(message => ({
      id: message.id,
      message_text: message.message_text,
      sender_user_id: message.sender_user_id,
      receiver_user_id: message.receiver_user_id,
      created_at: message.created_at
    })),
    [messages])

  // Takes the filtered messages, and grabs all the user ids, then removes the duplicates
  const userIds = useMemo(() => new Set(filteredMessages.flatMap(message => [message.sender_user_id, message.receiver_user_id])), [filteredMessages]);

  // goes through all the users, and pulls the info for any from the above list, who are not the current user.
  const filteredUsers = useMemo(() => users.filter(user => userIds.has(user.id) && user.id !== currentUser.id), [users, userIds, currentUser.id]);
  
  // creates the list of users that you have messages with. Is also used as the button to select specific users.
  const usersWithMessageHistory = useMemo(() => sortUsers(filteredUsers.map((user) => {
    const userMessages = filteredMessages.filter(message => message.sender_user_id === user.id || message.receiver_user_id === user.id);
    return { ...user, messages: userMessages };
  })), [filteredUsers, filteredMessages]);

  // same as above and mixed with below. To make the selected users messages update when the db changes. 
  useEffect(() => {
    if (selectedUser) {
      const userMessages = filteredMessages.filter(
        (message) => message.sender_user_id === selectedUser.id || message.receiver_user_id === selectedUser.id
      );
      setSelectedUser({ ...selectedUser, messages: userMessages });
    }
  }, [messages, filteredMessages]);
  
  // sets the initial selectedUserMessages, that will then adjust based on the above useEffect
  const selectedUserMessages = useMemo(() => selectedUser ? 
  selectedUser.messages.filter(message => message.message_text.toLowerCase().includes(search.toLowerCase()))
  : [], [selectedUser, search, messages]);
  
  return (
    <div className="text-[var(--color-theme-text)!important] hover:text-[var(--color-theme-hover-text)!important] text-shadow-[var(--color-theme-text-shadow)!important] hover:text-shadow-[var(--color-theme-hover-text-shadow)!important] border-[var(--color-theme-border)!important] hover:border-[var(--color-theme-hover-border)!important] shadow-lg dark:bg-neutral-800 w-full md:w-auto">
      {selectedUser ? 
        <div className="">
          <div className={`${theme === 'multi' ? 'text-multi bg-multi-gradient hover:bg-multi-gradient-hover active:bg-multi-gradient-active' : 'text-[var(--color-theme-text)!important] hover:text-[var(--color-theme-hover-text)!important] text-shadow-[var(--color-theme-text-shadow)!important] hover:text-shadow-[var(--color-theme-hover-text-shadow)!important] ' } border-[var(--color-theme-border)!important] hover:border-[var(--color-theme-hover-border)!important] relative h-full border-4 rounded-lg`}>
            <button type="submit" onClick={() => setSelectedUser(null)} className={`bg-theme-gradient hover:bg-theme-gradient-hover active:bg-theme-gradient-active mt-2 mb-2 px-3 py-0 rounded`} >
              <span className={`${theme === 'multi' ? 'text-multi bg-multi-gradient hover:bg-multi-gradient-hover active:bg-multi-gradient-active' : 'text-[var(--color-theme-gradient-text)!important] hover:text-[var(--color-theme-hover-text)!important] text-shadow-[var(--color-theme-text-shadow)!important] hover:text-shadow-[var(--color-theme-hover-text-shadow)!important] font-extrabold'}`}
                >Back
              </span>
            </button>
            <MessageSearch theme={theme} search={search} onSearchChange={setSearch} />
          </div> 
          <div className="overflow-y-auto">
            <MessageList theme={theme} user={selectedUser} messages={selectedUserMessages} currentUser={currentUser} onSendMessage={handleSendMessage} onDeleteMessage={onDeleteMessage} onEditMessage={handleEditMessage} />
          </div>
        </div>
      : 
        <div className="">
          <div className={`${theme === 'multi' ? 'text-multi bg-multi-gradient hover:bg-multi-gradient-hover active:bg-multi-gradient-active border-[var(--color-theme-border)!important] hover:border-[var(--color-theme-hover-border)!important]' : 'text-[var(--color-theme-text)!important] hover:text-[var(--color-theme-hover-text)!important] text-shadow-[var(--color-theme-text-shadow)!important] hover:text-shadow-[var(--color-theme-hover-text-shadow)!important] ' } border-[var(--color-theme-border)!important] hover:border-[var(--color-theme-hover-border)!important] relative h-full border-4 rounded-lg`}>
            <div className="flex justify-center mt-2">
              <div className="relative mb-3 " >
                <div className="mr-4 inline-block min-h-[1.5rem] pl-[1.5rem]">
                  <input type="radio" value="name" checked={sortType === "name"} onChange={(e) => setSortType(e.target.value)}
                    className="relative float-left -ml-[1.5rem] mr-2 mt-0.5 h-5 w-5 appearance-none rounded-full border-2 border-solid border-neutral-300 before:pointer-events-none before:absolute before:h-4 before:w-4 before:scale-0 before:rounded-full before:bg-transparent before:opacity-0 before:shadow-[0px_0px_0px_13px_transparent] before:content-[''] after:absolute after:z-[1] after:block after:h-4 after:w-4 after:rounded-full after:content-[''] checked:border-primary checked:before:opacity-[0.16] checked:after:absolute checked:after:left-1/2 checked:after:top-1/2 checked:after:h-[0.625rem] checked:after:w-[0.625rem] checked:after:rounded-full checked:after:border-primary checked:after:bg-primary checked:after:content-[''] checked:after:[transform:translate(-50%,-50%)] hover:cursor-pointer hover:before:opacity-[0.04] hover:before:shadow-[0px_0px_0px_13px_rgba(0,0,0,0.6)] focus:shadow-none focus:outline-none focus:ring-0 focus:before:scale-100 focus:before:opacity-[0.12] focus:before:shadow-[0px_0px_0px_13px_rgba(0,0,0,0.6)] focus:before:transition-[box-shadow_0.2s,transform_0.2s] checked:focus:border-primary checked:focus:before:scale-100 checked:focus:before:shadow-[0px_0px_0px_13px_#3b71ca] checked:focus:before:transition-[box-shadow_0.2s,transform_0.2s] dark:border-neutral-600 dark:checked:border-primary dark:checked:after:border-primary dark:checked:after:bg-primary dark:focus:before:shadow-[0px_0px_0px_13px_rgba(255,255,255,0.4)] dark:checked:focus:border-primary dark:checked:focus:before:shadow-[0px_0px_0px_13px_#3b71ca]"/>
                  <label className={`${theme === 'multi' ? 'text-multi bg-multi-gradient hover:bg-multi-gradient-hover active:bg-multi-gradient-active' : 'text-[var(--color-theme-text)!important] hover:text-[var(--color-theme-hover-text)!important] text-shadow-[var(--color-theme-text-shadow)!important] hover:text-shadow-[var(--color-theme-hover-text-shadow)!important]  ' } mt-px inline-block pl-[0.15rem] hover:cursor-pointer`}
                  > Name </label>
                </div>
                <div className=" mr-4 inline-block min-h-[1.5rem] pl-[1.5rem]">
                  <input type="radio" value="ID" checked={sortType === "ID"} onChange={(e) => setSortType(e.target.value)}
                    className="relative float-left -ml-[1.5rem] mr-2 mt-0.5 h-5 w-5 appearance-none rounded-full border-2 border-solid border-neutral-300 before:pointer-events-none before:absolute before:h-4 before:w-4 before:scale-0 before:rounded-full before:bg-transparent before:opacity-0 before:shadow-[0px_0px_0px_13px_transparent] before:content-[''] after:absolute after:z-[1] after:block after:h-4 after:w-4 after:rounded-full after:content-[''] checked:border-primary checked:before:opacity-[0.16] checked:after:absolute checked:after:left-1/2 checked:after:top-1/2 checked:after:h-[0.625rem] checked:after:w-[0.625rem] checked:after:rounded-full checked:after:border-primary checked:after:bg-primary checked:after:content-[''] checked:after:[transform:translate(-50%,-50%)] hover:cursor-pointer hover:before:opacity-[0.04] hover:before:shadow-[0px_0px_0px_13px_rgba(0,0,0,0.6)] focus:shadow-none focus:outline-none focus:ring-0 focus:before:scale-100 focus:before:opacity-[0.12] focus:before:shadow-[0px_0px_0px_13px_rgba(0,0,0,0.6)] focus:before:transition-[box-shadow_0.2s,transform_0.2s] checked:focus:border-primary checked:focus:before:scale-100 checked:focus:before:shadow-[0px_0px_0px_13px_#3b71ca] checked:focus:before:transition-[box-shadow_0.2s,transform_0.2s] dark:border-neutral-600 dark:checked:border-primary dark:checked:after:border-primary dark:checked:after:bg-primary dark:focus:before:shadow-[0px_0px_0px_13px_rgba(255,255,255,0.4)] dark:checked:focus:border-primary dark:checked:focus:before:shadow-[0px_0px_0px_13px_#3b71ca]"/>
                  <label className={`${theme === 'multi' ? 'text-multi bg-multi-gradient hover:bg-multi-gradient-hover active:bg-multi-gradient-active' : 'text-[var(--color-theme-text)!important] hover:text-[var(--color-theme-hover-text)!important] text-shadow-[var(--color-theme-text-shadow)!important] hover:text-shadow-[var(--color-theme-hover-text-shadow)!important]  ' } mt-px inline-block pl-[0.15rem] hover:cursor-pointer`}
                  > ID </label>
                </div>
                <div className=" mr-4 inline-block min-h-[1.5rem] pl-[1.5rem]">
                  <input type="radio" value="recent" checked={sortType === "recent"} onChange={(e) => setSortType(e.target.value)}
                    className="relative float-left -ml-[1.5rem] mr-2 mt-0.5 h-5 w-5 appearance-none rounded-full border-2 border-solid border-neutral-300 before:pointer-events-none before:absolute before:h-4 before:w-4 before:scale-0 before:rounded-full before:bg-transparent before:opacity-0 before:shadow-[0px_0px_0px_13px_transparent] before:content-[''] after:absolute after:z-[1] after:block after:h-4 after:w-4 after:rounded-full after:content-[''] checked:border-primary checked:before:opacity-[0.16] checked:after:absolute checked:after:left-1/2 checked:after:top-1/2 checked:after:h-[0.625rem] checked:after:w-[0.625rem] checked:after:rounded-full checked:after:border-primary checked:after:bg-primary checked:after:content-[''] checked:after:[transform:translate(-50%,-50%)] hover:cursor-pointer hover:before:opacity-[0.04] hover:before:shadow-[0px_0px_0px_13px_rgba(0,0,0,0.6)] focus:shadow-none focus:outline-none focus:ring-0 focus:before:scale-100 focus:before:opacity-[0.12] focus:before:shadow-[0px_0px_0px_13px_rgba(0,0,0,0.6)] focus:before:transition-[box-shadow_0.2s,transform_0.2s] checked:focus:border-primary checked:focus:before:scale-100 checked:focus:before:shadow-[0px_0px_0px_13px_#3b71ca] checked:focus:before:transition-[box-shadow_0.2s,transform_0.2s] dark:border-neutral-600 dark:checked:border-primary dark:checked:after:border-primary dark:checked:after:bg-primary dark:focus:before:shadow-[0px_0px_0px_13px_rgba(255,255,255,0.4)] dark:checked:focus:border-primary dark:checked:focus:before:shadow-[0px_0px_0px_13px_#3b71ca]"/>
                  <label className={`${theme === 'multi' ? 'text-multi bg-multi-gradient hover:bg-multi-gradient-hover active:bg-multi-gradient-active' : 'text-[var(--color-theme-text)!important] hover:text-[var(--color-theme-hover-text)!important] text-shadow-[var(--color-theme-text-shadow)!important] hover:text-shadow-[var(--color-theme-hover-text-shadow)!important]  ' } mt-px inline-block pl-[0.15rem] hover:cursor-pointer`}
                  > Most Recent Message </label>
                </div>
              </div>
            </div> 
            <MessageSearch theme={theme} search={search} onSearchChange={setSearch} />
          </div>
          <ul>
            {usersWithMessageHistory.map((user) => (
              <li key={user.id} className={`${theme === 'multi' ? 'text-multi bg-multi-gradient hover:bg-multi-gradient-hover active:bg-multi-gradient-active' : 'text-[var(--color-theme-text)!important] hover:text-[var(--color-theme-hover-text)!important] text-shadow-[var(--color-theme-text-shadow)!important] hover:text-shadow-[var(--color-theme-hover-text-shadow)!important]  ' }`}>
                <button onClick={() => setSelectedUser(user)}>
                  {user.username}
                </button>
              </li>
            ))}
          </ul>
        </div>
      }
    </div>
  );
}

export default MessageBox;