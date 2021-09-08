import React from "react";
import Picker from "./picker";
import {Link} from "react-router-dom";
import {faSearch} from "@fortawesome/free-solid-svg-icons";
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";

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
            const picker = document.getElementById('picker');
            if (picker) {
                console.log(picker);
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
        ;
    }

    render() {
        const picker = this.state.pickerVisible && <Picker key={this.state.picker_key}
                                                           url={this.state.url}/>;
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
                    <li><a className={"menu-item"}
                           href={"login"}>Login</a></li>

                </ul>
                <div className={'search'}>
                    <div className={'search-border'}>
                        <input className={'search-input'}
                               type="search"
                               placeholder={"Search"}/>
                        <button className={'search-button'}><FontAwesomeIcon icon={faSearch}/></button>
                    </div>
                </div>
                {picker}
            </nav>

        );
    }

}

export default Header