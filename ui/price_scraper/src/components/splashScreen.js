import React from "react";
import {faSpinner} from "@fortawesome/free-solid-svg-icons";
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";

class SplashScreen extends React.Component {
    render() {
        return (
            <div className={'splash-screen'}>
                <FontAwesomeIcon icon={faSpinner} size={"lg"} className={'loading'} />
            </div>
        )
    }
}

export default SplashScreen