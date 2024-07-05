import React, { useState } from "react";
import ResultFeedback from "./ResultFeedback";

const CodeInput = () => {
  const [code, setCode] = useState("");
  const [feedback, setFeedback] = useState(null);

  const handleSubmit = (e) => {
    e.preventDefault();

    // Mock feedback data
    const feedbackData = {
      strengths: "Efficient use of algorithms and clean code structure.",
      weaknesses: "Lacks proper error handling and documentation.",
      overall:
        "Good overall structure but needs improvements in error handling.",
    };

    setFeedback(feedbackData);
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100">
      <div className="flex w-full max-w-4xl p-8 bg-white rounded-lg shadow-lg space-x-8">
        <form className="flex-1 space-y-4" onSubmit={handleSubmit}>
          <div className="text-3xl text-center text-gray-700">
            Enter your Code Below
          </div>
          <div>
            <textarea
              className="w-full h-96 p-4 border-2 border-gray-300 rounded-lg focus:outline-none focus:border-blue-500 overflow-y-scroll"
              placeholder="Paste your code here..."
              value={code}
              onChange={(e) => setCode(e.target.value)}
              name="code_snippet"
            ></textarea>
          </div>
          <div className="flex justify-center">
            <button
              type="submit"
              className="px-6 py-2 text-white bg-blue-500 rounded-lg hover:bg-blue-600 focus:outline-none"
            >
              Submit Code for Analysis
            </button>
          </div>
        </form>
        {feedback && <ResultFeedback feedback={feedback} />}
      </div>
    </div>
  );
};

export default CodeInput;
