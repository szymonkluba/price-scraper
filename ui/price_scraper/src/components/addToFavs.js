import React from "react";
import Auth from "../utils/auth";

class AddToFavs extends React.Component {
    componentDidMount() {
        const path = window.location.origin.replace('3000', '8000') + '/favourites/'
        const headers = {'Content-Type': 'application/json', 'Authorization': `Token ${Auth.getToken()}`}
        console.log(headers)
        const data = {slug: this.props.location.state.slug}
        console.log(data)
        fetch(path, {
            method: "POST",
            mode: "cors",
            body: JSON.stringify(data),
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

export default AddToFavs