import React from "react";

export default function Header() {
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