import React from "react";
import ReactDOM from "react-dom";

class Header extends React.Component {
    addTest() {
        const element = <div>Test</div>
        ReactDOM.render(element, document.getElementById('content'))
    }

    addTest2() {
        const element = <div>Test 2</div>
        ReactDOM.render(element, document.getElementById('content'))
    }

    render() {
        return (
        <nav>
            <ul>
                <li><button onClick={this.addTest}>Products</button></li>
                <li><button onClick={this.addTest2}>Categories</button></li>
                <li>Stores</li>
                <li>Login</li>
            </ul>
            <input type="search"/>
            <button>Search</button>
        </nav>
    );
    }

}

export default Header