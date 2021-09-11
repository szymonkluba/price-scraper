import React from "react";
import Auth from "../utils/auth";
import {Redirect} from "react-router-dom";

class Logout extends React.Component {

    componentDidMount() {
        const path = window.location.origin.replace('3000', '8000') + '/auth/token/logout/'
        fetch(path, {
            method: 'POST',
            mode: 'cors',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Token ${Auth.getToken()}`
            },
        }).then(() => {
            Auth.logoutUser();
            window.history.go();
        })
    }

    render() {
        return <Redirect to={'/'} />
    }
}

export default Logout