import React, { useState } from "react";
import { ChatKit, useChatKit } from "@openai/chatkit-react";
import "./style.css";

export default function App() {
  const [isOpen, setIsOpen] = useState(false);

  let visitorId = localStorage.getItem("reynaldo_visitor_id");

  if (!visitorId) {
    visitorId = crypto.randomUUID();
    localStorage.setItem("reynaldo_visitor_id", visitorId);
  }

  const { control } = useChatKit({
    api: {
      url: "https://reynaldo-chatkit.onrender.com/chatkit",
      domainKey: "domain_pk_6a77d2f060988196ba6dd4ba9af06d8c0f888c9452fa380f",

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
      {!isOpen && (
        <button
          className="chat-bubble"
          onClick={() => setIsOpen(true)}
          aria-label="Open Reynaldo AI assistant"
        >
          ✦

          <span className="chat-bubble-text">
            Ask Reynaldo
          </span>
        </button>
      )}

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