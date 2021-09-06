import './App.css';
import Header from "./components/header";
import MainContent from "./components/mainContent";
import React from "react";
import {BrowserRouter as Router,} from "react-router-dom";

class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            url: 'http://localhost:8000/products/',
        }
    }
    render() {
        return (
            <div>
                <Router>
                    <Header />
                    <MainContent />
                </Router>
            </div>
        );
    }


}

export default App;
