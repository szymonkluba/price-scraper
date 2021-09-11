import React from "react";
import {Route} from "react-router-dom";
import Auth from "../utils/auth";
import UserForm from "./userForm";

const PrivateRoute = ({ component: Component, ...rest }) => {
    return (
        <Route {...rest} render={(props) => {
            return (

            Auth.isAuthenticated() === true
                ? <Component {...props} from={props.from}
                             key={props.location.key}/>
                : <UserForm {...props} from={props.location.pathname} action={'login'}/>
        )
        }}/>
    )
}

export default PrivateRoute;