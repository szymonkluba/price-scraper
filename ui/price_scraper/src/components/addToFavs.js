import React from "react";
import Auth from "../utils/auth";
import {Redirect} from "react-router-dom";

class AddToFavs extends React.Component {
    componentDidMount() {
        const path = window.location.origin.replace('3000', '8000') + '/favourites/'
        const headers = {'Content-Type': 'application/json', 'Authorization': `Token ${Auth.getToken()}`}
        const data = {slug: this.props.location.state.slug}
        fetch(path, {
            method: "POST",
            mode: "cors",
            body: JSON.stringify(data),
            headers: headers,
        })
    }

    render() {
        return <Redirect to={this.props.location.state.previous} />
    }
}

export default AddToFavs