import React, { useState } from "react";
import { ChatKit, useChatKit } from "@openai/chatkit-react";
import "./style.css";

function App() {
  const [isOpen, setIsOpen] = useState(false);

  let visitorId = localStorage.getItem("reynaldo_visitor_id");

  if (!visitorId) {
    visitorId = crypto.randomUUID();
    localStorage.setItem("reynaldo_visitor_id", visitorId);
  }

 const { control } = useChatKit({
  api: {
    url: "http://127.0.0.1:8000/chatkit",
    domainKey: "local-dev",

    fetch: async (input, init) => {
      return fetch(input, {
        ...init,
        headers: {
          ...(init?.headers || {}),
          "X-Visitor-ID": visitorId,
        },
      });
    },
  },

  onReady() {
    console.log("Reynaldo ChatKit ready");
  },

  onError(error) {
    console.error("Reynaldo ChatKit error:", error);
  },
});

  return (
    <>
      {/* Floating Chat Button */}
      {!isOpen && (
        <button
          className="chat-bubble"
          onClick={() => setIsOpen(true)}
          aria-label="Open Reynaldo AI assistant"
        >
          <span className="chat-bubble-icon">✦</span>

          <span className="chat-bubble-text">
            Ask Reynaldo
          </span>
        </button>
      )}

      {/* Chat Window */}
      {isOpen && (
        <div className="chat-panel">

          <div className="chat-panel-header">
            <div>
              <div className="chat-panel-label">
                AI PORTFOLIO ASSISTANT
              </div>

              <div className="chat-panel-title">
                Ask Reynaldo
              </div>
            </div>

            <button
              className="chat-close"
              onClick={() => setIsOpen(false)}
              aria-label="Close chat"
            >
              ×
            </button>
          </div>

          <div className="chat-panel-body">
            <ChatKit control={control} />
          </div>

        </div>
      )}
    </>
  );
}

export default App;