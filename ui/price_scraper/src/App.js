import './App.css';
import Header from "./components/header";
import MainContent from "./components/mainContent";
import React from "react";
import {BrowserRouter as Router} from "react-router-dom";

function App() {
    return (
        <div>
            <Router>
                <Header/>
                <MainContent/>
            </Router>
        </div>
    );
}

export default App;
