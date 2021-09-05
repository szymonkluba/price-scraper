import React from "react";
import Picker from "./picker";

class Header extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            pickerVisible: false,
            url: null,
        }
    }

    displayPicker(url) {
        this.setState({
            url: url,
            pickerVisible: !this.state.pickerVisible,
        })
    }

    render() {
        const picker = this.state.pickerVisible && <Picker url={this.state.url} />;
        return (
        <nav>
            <ul>
                <li><button>Products</button></li>
                <li><button onClick={() => this.displayPicker(window.location.origin.replace('3000', '8000') + '/category/')}>Categories</button></li>
                <li><button onClick={() => this.displayPicker(window.location.origin.replace('3000', '8000') + '/stores/')}>Stores</button></li>
                <li>Login</li>
                <input type="search"/>
                <button>Search</button>
            </ul>
            {picker}
        </nav>

    );
    }

}

export default Header