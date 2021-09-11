import React from "react";
import Auth from "../utils/auth";
import {Redirect} from "react-router-dom";

class RemoveFromFavs extends React.Component {
    componentDidMount() {
        const path = window.location.origin.replace('3000', '8000') + '/favourites/' + this.props.location.state.slug + '/';
        const headers = {'Content-Type': 'application/json',}
        if (Auth.isAuthenticated()) {
            headers['Authorization'] = `Token ${Auth.getToken()}`
        }
        fetch(path, {
            method: "DELETE",
            mode: "cors",
            headers: headers,
        })
    }

    render() {
        return <Redirect to={this.props.location.state.previous} />
    }
}

export default RemoveFromFavs