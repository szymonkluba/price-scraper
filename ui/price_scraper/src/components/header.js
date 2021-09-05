import React from "react";

class Header extends React.Component {
    render() {
        return (
        <nav>
            <ul>
                <li>Products</li>
                <li>Categories</li>
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