import { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";

import { saveInteraction, getInteractions, sendChat } from "../services/api";
import {
  setInteractions,
  addInteraction,
} from "../redux/interactionSlice";
function InteractionForm() {
  const [mode, setMode] = useState("form");

  const [hcpName, setHcpName] = useState("");
  const [chatMessage, setChatMessage] = useState("");
  const [chatReply, setChatReply] = useState("");
  const [hospital, setHospital] = useState("");
  const [specialization, setSpecialization] = useState("");
  const [notes, setNotes] = useState("");

  const dispatch = useDispatch();

const interactionList = useSelector(
  (state) => state.interactions.interactions
);

  useEffect(() => {
    loadInteractions();
  }, []);

  const loadInteractions = async () => {
    try {
      const data = await getInteractions();
      dispatch(setInteractions(data));
    } catch (error) {
      console.error(error);
    }
  };

  const handleSave = async () => {
    const data = {
      hcp_name: hcpName,
      hospital: hospital,
      specialization: specialization,
      notes: notes,
    };
    try {
      const response = await saveInteraction(data);
      alert(response.message);

      dispatch(addInteraction(data));

      setHcpName("");
      setHospital("");
      setSpecialization("");
      setNotes("");
    } catch (error) {
      console.error(error);
      alert("Failed to save interaction");
    }
  };

  const handleChat = async () => {
    try {
      const response = await sendChat(chatMessage);
      setChatReply(response.reply);
      setChatMessage("");
    } catch (error) {
      console.error(error);
      alert("Chat failed");
    }
  };

  return (
    <div style={{ padding: "20px" }}>
      <h2>Log Interaction Screen</h2>

      <button onClick={() => setMode("form")}>Form Mode</button>

      <button
        onClick={() => setMode("chat")}
        style={{ marginLeft: "10px" }}
      >
        Chat Mode
      </button>

      <br />
      <br />

      {mode === "form" ? (
        <div>
          <label>HCP Name</label>
          <br />
          <input
            type="text"
            placeholder="Enter HCP Name"
            value={hcpName}
            onChange={(e) => setHcpName(e.target.value)}
          />

          <br />
          <br />

          <label>Hospital</label>
          <br />
          <input
            type="text"
            placeholder="Enter Hospital Name"
            value={hospital}
            onChange={(e) => setHospital(e.target.value)}
          />

          <br />
          <br />

          <label>Specialization</label>
          <br />
          <input
            type="text"
            placeholder="Enter Specialization"
            value={specialization}
            onChange={(e) => setSpecialization(e.target.value)}
          />

          <br />
          <br />

          <label>Interaction Notes</label>
          <br />
          <textarea
            rows="5"
            cols="50"
            placeholder="Write interaction notes..."
            value={notes}
            onChange={(e) => setNotes(e.target.value)}
          />

          <br />
          <br />

          <button onClick={handleSave}>
            Save Interaction
          </button>

          <hr />

          <h3>Saved Interactions</h3>

          <table border="1" cellPadding="8">
            <thead>
              <tr>
                <th>HCP Name</th>
                <th>Hospital</th>
                <th>Specialization</th>
                <th>Notes</th>
              </tr>
            </thead>

            <tbody>
              {interactionList.map((item, index) => (
                <tr key={index}>
                  <td>{item.hcp_name}</td>
                  <td>{item.hospital}</td>
                  <td>{item.specialization}</td>
                  <td>{item.notes}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      ) : (
        <div>
          <label>Chat with AI</label>
          <br />
          <textarea
            rows="6"
            cols="50"
            placeholder="Type your interaction..."
            value={chatMessage}
            onChange={(e) => setChatMessage(e.target.value)}
          />

          <br />
          <br />

          <button onClick={handleChat}>Send</button>
          <br />
          <br />

          <b>AI Reply:</b>

          <p>{chatReply}</p>
        </div>
      )}
    </div>
  );
}

export default InteractionForm;