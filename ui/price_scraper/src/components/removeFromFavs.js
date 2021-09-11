import React from "react";
import Auth from "../utils/auth";

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
        }).then(response => {
                return new Promise((resolve) => response.json()
                    .then((json) => resolve({
                        status: response.status,
                        ok: response.ok,
                        json,
                    })));
            })
    }

    render() {
        return null
    }
}

export default RemoveFromFavs