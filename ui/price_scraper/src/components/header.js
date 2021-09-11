import React from "react";
import Picker from "./picker";
import {Link} from "react-router-dom";
import SearchForm from "./searchForm";

class Header extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            picker_key: null,
            pickerVisible: false,
            url: null,
        }
        this.onItemClick = this.onItemClick.bind(this)
    }

    onItemClick(pickerVisible) {
        const picker = document.getElementById('picker');
        if (picker) {
            if (picker.classList.contains('show')) {
                picker.classList.remove('show')
            }
            picker.classList.add('hide')
        }
        setTimeout(() => {
            this.setState({pickerVisible});
        }, 250)
    }

    displayPicker(url, key) {
        if (key === this.state.picker_key) {
            const picker = document.getElementById('picker');
            if (picker) {
                if (picker.classList.contains('show')) {
                    picker.classList.remove('show')
                }
                picker.classList.add('hide')
            }
            setTimeout(() => {
                this.setState({pickerVisible: !this.state.pickerVisible});
            }, 250)
        } else {
            this.setState({
                pickerVisible: !this.state.pickerVisible ? true : this.state.pickerVisible,
                url: url,
                picker_key: key,
            })
        }
    }

    render() {
        const picker = this.state.pickerVisible && <Picker key={this.state.picker_key}
                                                           url={this.state.url}
                                                           onItemClick={this.onItemClick}/>;
        return (
            <nav>
                <ul className={'menu'}>
                    <li><Link className={"menu-item"}
                              to='/'>Products</Link></li>
                    <li>
                        <button className={"menu-item"}
                                onClick={() => this.displayPicker(window.location.origin.replace('3000', '8000') + '/category/', 'category')}>Categories
                        </button>
                    </li>
                    <li>
                        <button className={"menu-item"}
                                onClick={() => this.displayPicker(window.location.origin.replace('3000', '8000') + '/stores/', 'stores')}>Stores
                        </button>
                    </li>
                    <li><Link className={"menu-item"}
                              to={"/login/"}
                              action={"login"}>Login</Link></li>
                </ul>
                <SearchForm/>
                {picker}
            </nav>

        );
    }

}

export default Header