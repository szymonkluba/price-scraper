import React from "react";
import Picker from "./picker";
import {Link} from "react-router-dom";

class Header extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            picker_key: null,
            pickerVisible: false,
            url: null,
        }
    }

    displayPicker(url, key) {
        if (key === this.state.picker_key) {
            this.setState({pickerVisible: !this.state.pickerVisible});
        } else {
            this.setState({
                pickerVisible: !this.state.pickerVisible ? true : this.state.pickerVisible,
                url: url,
                picker_key: key,
            })
        }
        ;
    }

    render() {
        const picker = this.state.pickerVisible && <Picker key={this.state.picker_key}
                                                           url={this.state.url}/>;
        return (
            <nav>
                <ul>
                    <li><Link to='/'>Products</Link></li>
                    <li>
                        <button onClick={() => this.displayPicker(window.location.origin.replace('3000', '8000') + '/category/', 'category')}>Categories</button>
                    </li>
                    <li>
                        <button onClick={() => this.displayPicker(window.location.origin.replace('3000', '8000') + '/stores/', 'stores')}>Stores</button>
                    </li>
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