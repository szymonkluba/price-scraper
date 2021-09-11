import React from "react";
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import {faSearch} from "@fortawesome/free-solid-svg-icons";
import {Link} from "react-router-dom";


class SearchForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            value: '',
            path: '/search/?q='
        }
        this.handleChange = this.handleChange.bind(this);
    }

    handleChange(event) {
        const path = this.state.path + event.target.value;
        this.setState({path: path});
    }

    render() {
        return (
            <div className={'search'}>
                <div className={'search-border'}>
                    <form>
                        <input className={'search-input'}
                               type="search"
                               placeholder={"Search"}
                               onChange={this.handleChange}/>
                        <Link to={this.state.path} className={'search-button'}><FontAwesomeIcon icon={faSearch}/></Link>
                    </form>
                </div>
            </div>
        );
    }
}

export default SearchForm;